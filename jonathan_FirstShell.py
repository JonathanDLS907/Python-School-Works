import os
import platform
import subprocess
import datetime

# Color definitions using ANSI escape codes
CYAN = "\033[96m"
YELLOW = "\033[93m"
RESET = "\033[0m"

def run_shell():
    history = []

    print(f"{CYAN}Welcome to JonathanShell! Type 'help' for a list of commands.{RESET}")

    while True:
        current_dir = os.getcwd()
        prompt = f"{CYAN}{current_dir} JonathanShell> {RESET}"
        command = input(prompt).strip()

        if not command:
            continue

        # Built-in commands
        if command.lower() in ["exit", "quit"]:
            print(f"{CYAN}Goodbye!{RESET}")
            break

        if command == "history":
            print(f"{YELLOW}Command History:{RESET}")
            for cmd in history:
                print(f"{CYAN}{cmd}{RESET}")
            continue

        if command == "help":
            print(f"{YELLOW}Built-in commands:{RESET}")
            print(f"{CYAN}  cd <path>{RESET}     - Change directory")
            print(f"{CYAN}  history{RESET}       - Show command history")
            print(f"{CYAN}  help{RESET}          - Show this help message")
            print(f"{CYAN}  exit / quit{RESET}   - Exit the shell")
            continue

        if command.startswith("cd "):
            try:
                os.chdir(command[3:])
            except Exception as e:
                print(f"{YELLOW}Error changing directory: {e}{RESET}")
            continue

        if command == "clear":
            os.system("cls" if platform.system() == "Windows" else "clear")
            continue

        if command == "time":
            now = datetime.datetime.now()
            print(f"{YELLOW}Current time: {now.strftime('%Y-%m-%d %H:%M:%S')}{RESET}")
            continue



        history.append(command)

        # Platform-specific command adjustments
        system = platform.system()
        if system == "Windows":
            if command == "ls":
                command = "dir"
            elif command.startswith("cat "):
                command = command.replace("cat", "type", 1)
        elif system in ["Linux", "Darwin"]:  # Darwin = macOS
            if command == "dir":
                command = "ls"
            elif command.startswith("type "):
                command = command.replace("type", "cat", 1)

        # Execute external command
        try:
            subprocess.run(command, shell=True)
        except FileNotFoundError:
            print(f"{YELLOW}Command not found.{RESET}")
        except Exception as e:
            print(f"{YELLOW}Error executing command: {e}{RESET}")

# Run the shell
run_shell()
