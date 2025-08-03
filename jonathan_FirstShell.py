import os
import platform
import subprocess
import datetime

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
        command = input(prompt).strip()

        history.append(command)

        if not command:
            continue

        # BUILT-IN COMMANDS
        if command.lower() in ["exit", "quit"]:
            print(f"{CYAN}Shell closed. Thank you for using JDLS Shell.{RESET}")
            break

        if command == "history":
            print(f"{YELLOW}Command History:{RESET}")
            for cmd in history:
                print(f"{CYAN}{cmd}{RESET}")
            continue

        if command.lower() == "help":
            print(f"{YELLOW}Built-in commands:{RESET}")
            print(f"{CYAN}  cd <path>{RESET}     - Change directory")
            print(f"{CYAN}  pwd{RESET}           - Show current directory")
            print(f"{CYAN}  history{RESET}       - Show command history")
            print(f"{CYAN}  help{RESET}          - Show this help message")
            print(f"{CYAN}  clear{RESET}         - Clear the screen")
            print(f"{CYAN}  time{RESET}          - Show current time")
            print(f"{CYAN}  touch <file>{RESET}  - Create a file")
            print(f"{CYAN}  rm <file>{RESET}     - Delete a file")
            print(f"{CYAN}  mkdir <dir>{RESET}   - Create a directory")
            print(f"{CYAN}  echo <text>{RESET}   - Print text")
            print(f"{CYAN}  exit / quit{RESET}   - Exit the shell")
            continue

        if command.startswith("cd "):
            try:
                os.chdir(command[3:])
            except Exception as e:
                print(f"{YELLOW}Error changing directory: {e}{RESET}")
            continue

        if command.lower() == "clear":
            os.system("cls" if platform.system() == "Windows" else "clear")
            continue

        if command.lower() == "time":
            now = datetime.datetime.now()
            print(f"{YELLOW}Current time: {now.strftime('%Y-%m-%d %H:%M:%S')}{RESET}")
            continue
        
        if command.startswith("touch "):
            filename = command[6:]
            open(filename, 'a').close()
            print(f"{YELLOW}Created file: {filename}{RESET}")
            continue

        if command.startswith("rm "):
            filename = command[3:]
            try:
                os.remove(filename)
                print(f"{YELLOW}Deleted file: {filename}{RESET}")
            except Exception as e:
                print(f"{YELLOW}Error deleting file: {e}{RESET}")
            continue

        if command.lower() == "pwd":
            print(f"{YELLOW}{os.getcwd()}{RESET}")
            continue

        if command.startswith("echo "):
            print(f"{YELLOW}{command[5:]}{RESET}")
            continue

        if command.startswith("mkdir "):
            dirname = command[6:]
            try:
                os.mkdir(dirname)
                print(f"{YELLOW}Created directory: {dirname}{RESET}")
            except Exception as e:
                print(f"{YELLOW}Error creating directory: {e}{RESET}")
            continue


        # PLATFORM-SPECIFIC COMMANDS ADJUSTMENTS
        system = platform.system()
        if system == "Windows":
            if command == "ls":
                command = "dir"
            elif command.startswith("cat "):
                command = command.replace("cat", "type", 1)
        elif system in ["Linux", "Darwin"]: 
            if command == "dir":
                command = "ls"
            elif command.startswith("type "):
                command = command.replace("type", "cat", 1)

        # EXECUTE EXTERNAL COMMANDS
        try:
            subprocess.run(command, shell=True)
        except FileNotFoundError:
            print(f"{YELLOW}Command not found.{RESET}")
        except Exception as e:
            print(f"{YELLOW}Error executing command: {e}{RESET}")

# RUN SHELL
run_shell()
