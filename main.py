'''
imports: keyboard for listening to CTRL
readline for navigating cursor in a line
'''
import readline
# import keyboard
from pynput import keyboard
import sys

# thanks to : https://stackoverflow.com/questions/79419925/move-cursor-accross-multiple-lines-in-python

listener = None


def move_cursor_up():
    sys.stdout.write("\033[1A")
    sys.stdout.flush()


def move_cursor_down():
    sys.stdout.write("\033[1B")
    sys.stdout.flush()


lines = ""


def write(line_count, no_of_lines):
    '''
    function:write
    parameters:line_count,no_of_lines
    returns:none
    '''
    global lines, listener
    # global listener
    if listener:
        listener.stop()
    print(line_count, no_of_lines, lines)
    print(f"Default line count {no_of_lines}")
    print(f"Buffer Length {len(lines)}")
    print("press CTRL key to set line to 1")
    print("start typing")
    print("--------------------------------------")

    def on_release(key):
        nonlocal line_count
        if key == keyboard.Key.ctrl:
            line_count = 1

    def on_press(key):
        if key == keyboard.Key.up:
            move_cursor_up()
        if key == keyboard.Key.down:
            move_cursor_down()

    listener = keyboard.Listener(on_release=on_release, on_press=on_press)
    listener.start()
    while line_count > 0:
        lines += input() + "\n"
        line_count -= 1
        if line_count == 0:
            print("last line")
            try:
                inc_line = int(input("<line> or 0: "))
            except ValueError:
                inc_line = 0
            if inc_line > 0:
                no_of_lines += inc_line
                line_count += inc_line


def open_in_buffer(line_count, no_of_lines, file_content):
    '''
    function: open_in_buffer
    parameters: line_count , no_of_lines, file_content
    '''
    global lines

    def on_release(key):
        nonlocal line_count
        if key == keyboard.Key.ctrl:
            line_count = 1

    def on_press(key):
        if key == keyboard.Key.up:

            move_cursor_up()
        if key == keyboard.Key.down:
            move_cursor_down()

    listener1 = keyboard.Listener(on_release=on_release, on_press=on_press)
    listener1.start()
    for i in file_content:
        lines += i
    print(lines)
    while line_count > 0:
        lines += input() + "\n"
        line_count -= 1
        if line_count == 0:
            print("last line")
            try:
                inc_line = int(input("<line> or 0: "))
            except ValueError:
                inc_line = 0
            if inc_line > 0:
                no_of_lines += inc_line
                line_count += inc_line


def main():
    '''
    function:main
    returns:none
    main entry point
    '''
    global lines, listener
    while True:
        event = input(
            "'n' to write ,'o' to open file,'s' to save ,  'v' to view buffer , 'q' to exit: ")
        if event == 's' and (len(lines) > 1):
            filename = input("filename>")
            path = input("path>")
            try:
                with open(f"{path}{filename}", "w", encoding='utf-8') as file:
                    file.write(lines)
                    print("Saved the content\nBuffer is cleared")
            except (OSError, FileExistsError) as error:
                print(error)
        elif event == 'v' and len(lines) > 1:
            print(lines)
        elif event == 'q':
            if listener:
                listener.stop()
            break
        elif event == "n":
            lines = ""
            write(5, 5)
        elif event == "o":
            lines = ""
            filename = input("filename>")
            path = input("path>")
            try:
                with open(f"{path}{filename}", "r", encoding='utf-8') as file:
                    file_content = file.readlines()
                    open_in_buffer(len(file_content), len(
                        file_content), file_content)
            except (OSError, FileExistsError) as error:
                print(error)

        else:
            print(f"Current Buffer length: {len(lines)} must be > than 1")


if __name__ == "__main__":
    main()
