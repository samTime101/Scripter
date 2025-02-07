import keyboard
import threading

lines = ""


def write(line_count , no_of_lines):
    # TODO
    #listen constantly to keyboard keystroke and when user press CTRL set the current line to 1
    global lines 
    print(line_count,no_of_lines)
    print(f"Default line count {no_of_lines}")
    print(f"Buffer Length {len(lines)}")
    print("press CTRL key to set line to 1")
    print("start typing")
    print("--------------------------------------")
    while line_count > 0:
        if keyboard.is_pressed('ctrl'):
            line_count = 1
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
    global lines

    while True:
        event = input("'n' to write ,'s' to save ,  'v' to view buffer , 'q' to exit: ")
        if event == 's' and (len(lines)>1):
            filename = input("filename>")
            path = input("path>")
            try:
                with open(f"{path}{filename}", "w") as file:
                    file.write(lines)
                    print("Saved the content\nBuffer is cleared")
            except Exception as e:
                print(e)
        elif event == 'v' and len(lines) > 1:
            print(lines)
        elif event == 'q':
            break
        elif event == "n":
            lines = ""
            write(5,5)
        else:
            print(f"Current Buffer length: {len(lines)} must be > than 1")
    
if __name__=="__main__":
    main()
