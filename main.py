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

def write():
    global line_count , no_of_lines , lines
    key_thread = threading.Thread(target=check_key, daemon=True)
    key_thread.start()
    print("Welcome to Scripter\nVersion: 0.0\nAuthor:samip regmi")
    print(f"Default line count {no_of_lines}")
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
        elif event == 'v':
            print(lines)
        elif event == 'q':
            break
        elif event == "n":
            lines = ""
            write()
        else:
            print(f"Current Buffer length: {len(lines)} must be > than 1")
    
if __name__=="__main__":
    main()
