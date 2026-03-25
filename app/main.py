import sys

def main():
    while True:
        sys.stdout.write("$ ")
        # user input
        command = input()
        if command == "exit":
            break
        elif command.startswith("echo "):
            # this is the text after echo
            # echo [text]
            print(command[5:])
        elif command.startswith("type "):
            # if input is within the shell builtin commands
            if command[5:] in ["echo", "exit", "type"]:
                print(f"{command[5:]} is a shell builtin")
            else:
                print(f"{command[5:]} is not found")
        else:
            print(f"{command}: command not found")

if __name__ == "__main__":
    main()