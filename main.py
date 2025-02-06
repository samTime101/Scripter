import keyboard
import threading

no_of_lines = 5
line_count = no_of_lines
lines = ""
stop_input = False

def check_key():
    global stop_input, line_count
    while True:
        if keyboard.is_pressed('ctrl'):
            print("\nline count = 1")
            stop_input = True
            line_count = 1
            break

key_thread = threading.Thread(target=check_key, daemon=True)
key_thread.start()
print("Welcome to Scripter\nVersion: 0.0\nAuthor:samip regmi")
print("Default line count 5")
print("press CTRL key to set line to 1")
print("start typing")
print("--------------------------------------")
while line_count > 0:
    if stop_input:
        break
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

while True:
    event = input("'s' to save ,  'v' to view buffer , 'q' to exit: ")
    if event == 's':
        filename = input("filename>")
        path = input("path>")
        try:
            with open(f"{path}{filename}", "w") as file:
                file.write(lines)
                print("Saved the content")
        except Exception as e:
            print(f"Error: {e}")
    elif event == 'v':
        print(lines)
    elif event == 'q':
        break


