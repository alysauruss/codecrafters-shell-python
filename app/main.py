import sys


def main():

    while True:
        sys.stdout.write("$ ")
        # Captures the user's command in the "command" variable
        command = input()
        if (command == "exit"):
            break
        else:
            print(f"{command}: command not found")


if __name__ == "__main__":
    main()