import sys
import ctypes
import os

def check_admin():
    try:
        is_admin = ctypes.windll.shell32.IsUserAnAdmin() != 0
    except Exception as e:
        print(f"Error checking admin status: {e}")
        is_admin = False
    return is_admin

def runasadmin():
    executable = sys.executable  # Lấy đường dẫn của Python hiện tại
    result = ctypes.windll.shell32.ShellExecuteW(
        None, "runas", executable, " ".join(sys.argv), None, 1
    )
    if result <= 32:
        print("You need admin privileges to run this script.")
        getout()


def getout():
    if not check_admin():
        print("You need admin privileges to run this script.")
        runasadmin()
        sys.exit(1)
    else:
        print("Running with admin privileges.")


import ctypes, sys, os, requests, time, hashlib, subprocess
from colorama import init, Fore, Style

init(autoreset=True)


def clear():
    os.system("cls" if os.name == "nt" else "clear")


def banner():
    print(
        Fore.MAGENTA
        + Style.BRIGHT
        + requests.get(
            "https://raw.githubusercontent.com/toitenlavortex/HDT-TOOL/refs/heads/main/banner.txt"
        ).text
        + "\n"
        + Fore.YELLOW
        + "             ⚡ HDT TOOL by toitenlavortex ⚡\n"
    )


def menu():
    print(Fore.CYAN + Style.BRIGHT + "[2] " + Fore.GREEN + "Proxy Checker")
    print(Fore.CYAN + Style.BRIGHT + "[1] " + Fore.GREEN + "SMS SPAM")
    print(Fore.CYAN + Style.BRIGHT + "[0] " + Fore.RED + "Exit")


def download_and_run_sms_script():
    A = "scripts"
    print(Fore.YELLOW + "Downloading SMS SPAM script from GitHub...")
    try:
        if not os.path.exists(A):
            os.makedirs(A)
        url = "https://raw.githubusercontent.com/toitenlavortex/HDT-TOOL/refs/heads/main/script/4360208648079376.py"
        response = requests.get(url)
        hash_object = hashlib.sha256(response.text.encode())
        file_hash = hash_object.hexdigest()
        filename = f"scripts/{file_hash}.py"
        with open(filename, "w") as f:
            f.write(response.text)
        subprocess.run(["python", filename])
    except Exception as e:
        print(Fore.RED + f"Error downloading or running script: {e}")

def download_and_run_proxycheck_script():
    A = "scripts"
    print(Fore.YELLOW + "Downloading ProxyChecker script from GitHub...")
    try:
        if not os.path.exists(A):
            os.makedirs(A)
        url = "https://raw.githubusercontent.com/toitenlavortex/HDT-TOOL/refs/heads/main/script/54210108624275221.py"
        response = requests.get(url)
        hash_object = hashlib.sha256(response.text.encode())
        file_hash = hash_object.hexdigest()
        filename = f"scripts/{file_hash}.py"
        with open(filename, "w") as f:
            f.write(response.text)
        subprocess.run(["python", filename])
    except Exception as e:
        print(Fore.RED + f"Error downloading or running script: {e}")


def main():
    getout()
    clear()
    banner()
    menu()
    choice = input(Fore.LIGHTBLUE_EX + "\n➤ Enter your choice: ")
    if choice == "1":
        download_and_run_sms_script()
    elif choice == "2":
        download_and_run_proxycheck_script()
    elif choice == "0":
        print(Fore.GREEN + "Goodbye! Thanks for using HDT TOOL.")
        time.sleep(1)
        exit(0)
    else:
        print(Fore.RED + "❌ Invalid choice!")
        time.sleep(1)
        main()


if __name__ == "__main__":
    main()
    input(Fore.YELLOW + "Enter To Exit")
