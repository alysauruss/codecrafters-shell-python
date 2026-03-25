import sys
import os

def main():
    print("PATH ENVIRONMENT VARIABLE:")
    PATH = os.environ["PATH"].split(os.pathsep)

    while True:
        sys.stdout.write("$ ")
        # Wait for user input
        command = input()
        # os.environ["PATH"] is a big plain string, 
        # os.pathsep is used to separate the diff paths and 
        # gives you a list of directory strings
        for directory in PATH:
            full_path = os.path.join(directory, command)
            if os.path.exists(full_path):
                if not os.access(full_path, os.X_OK):
                    continue
                else:
                    print(f"{command} is {directory}")
                    break
        else:
            print(f"{command} is not found in PATH")

if __name__ == "__main__":
    main()