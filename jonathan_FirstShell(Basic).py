import os
import platform
import subprocess

# COLORS
CYAN = "\033[96m"
YELLOW = "\033[93m"
RESET = "\033[0m"

def run_shell():
    os.system("cls" if platform.system() == "Windows" else "clear")  # Clear terminal on shell startup
    history = []

    print(f"{CYAN}Welcome to JDLS Shell! Type 'help' for a list of commands.{RESET}")

    while True:
        current_dir = os.getcwd()
        prompt = f"{CYAN}{current_dir} JDLS_Shell> {RESET}"
        raw_input = input(prompt).strip()
        command = raw_input.lower()

        if not command:
            continue

        history.append(raw_input)

        # BUILT-IN COMMANDS
        if command in ["exit", "quit"]:
            print(f"{CYAN}Shell closed. Thank you for using JDLS Shell.{RESET}")
            break

        if command == "history":
            print(f"{YELLOW}Command History:{RESET}")
            for cmd in history:
                print(f"{CYAN}{cmd}{RESET}")
            continue

        if command == "help":
            print(f"{YELLOW}Built-in commands:{RESET}")
            print(f"{CYAN}  cd <path>{RESET}     - Change directory")
            print(f"{CYAN}  pwd{RESET}           - Show current directory")
            print(f"{CYAN}  history{RESET}       - Show command history")
            print(f"{CYAN}  help{RESET}          - Show this help message")
            print(f"{CYAN}  clear{RESET}         - Clear the screen")
            print(f"{CYAN}  exit / quit{RESET}   - Exit the shell")
            continue

        if command.startswith("cd "):
            try:
                os.chdir(raw_input[3:])
            except Exception as e:
                print(f"{YELLOW}Error changing directory: {e}{RESET}")
            continue

        if command == "clear":
            os.system("cls" if platform.system() == "Windows" else "clear")
            continue

        if command == "pwd":
            print(f"{YELLOW}{os.getcwd()}{RESET}")
            continue

        # PLATFORM-SPECIFIC COMMAND ADJUSTMENTS
        system = platform.system()
        if system == "Windows":
            if command == "ls":
                raw_input = "dir"
            elif command.startswith("cat "):
                raw_input = raw_input.replace("cat", "type", 1)
        elif system in ["Linux", "Darwin"]:
            if command == "dir":
                raw_input = "ls"
            elif command.startswith("type "):
                raw_input = raw_input.replace("type", "cat", 1)

        # EXECUTE EXTERNAL COMMANDS
        try:
            subprocess.run(raw_input, shell=True)
        except FileNotFoundError:
            print(f"{YELLOW}Command not found.{RESET}")
        except Exception as e:
            print(f"{YELLOW}Error executing command: {e}{RESET}")

# RUN SHELL
run_shell()
