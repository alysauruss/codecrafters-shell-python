import sys
import os
import subprocess

builtin_commands = ["echo", "exit", "type"]
PATH = os.environ["PATH"].split(os.pathsep)

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
            if command[5:] in builtin_commands:
                print(f"{command[5:]} is a shell builtin")
            else:
                # os.environ["PATH"] is a big plain string, 
                # os.pathsep is used to separate the diff paths and 
                # gives you a list of directory strings
                for directory in PATH:
                    full_path = os.path.join(directory, command[5:])
                    if os.path.exists(full_path):
                        if not os.access(full_path, os.X_OK):
                            continue
                        else:
                            print(f"{command[5:]} is {full_path}")
                            break
                else:
                    print(f"{command[5:]}: not found")
        else:
            for directory in PATH:
                full_path = os.path.join(directory, command)
                if os.path.exists(full_path):
                    if not os.access(full_path, os.X_OK):
                        continue
                    else:
                        # print(f"{command} is {full_path}")
                        subprocess.run(full_path)
                        break
                else:
                    print(f"{command}: command not found")

if __name__ == "__main__":
    main()