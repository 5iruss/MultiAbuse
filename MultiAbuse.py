import os
import random
import time
import ipaddress
from colorama import init, Fore

init(autoreset=True)

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def typing_effect(text, delay=0.005):
    for char in text:
        print(Fore.RED + char, end='', flush=True)
        time.sleep(delay)
    print()

def display_art(animated=True):
    art = r"""
    ███        ▄████████  ▄████████    ▄█    █▄    
▀█████████▄   ███    ███ ███    ███   ███    ███   
   ▀███▀▀██   ███    █▀  ███    █▀    ███    ███   
    ███   ▀  ▄███▄▄▄     ███         ▄███▄▄▄▄███▄▄ 
    ███     ▀▀███▀▀▀     ███        ▀▀███▀▀▀▀███▀  
    ███       ███    █▄  ███    █▄    ███    ███   
    ███       ███    ███ ███    ███   ███    ███   
   ▄████▀     ██████████ ████████▀    ███    █▀    
       ▄████████  ▄█  ███▄▄▄▄    ▄██████▄  
      ███    ███ ███  ███▀▀▀██▄ ███    ███ 
      ███    █▀  ███▌ ███   ███ ███    ███ 
      ███        ███▌ ███   ███ ███    ███ 
    ▀███████████ ███▌ ███   ███ ███    ███ 
             ███ ███  ███   ███ ███    ███ 
       ▄█    ███ ███  ███   ███ ███    ███ 
     ▄████████▀  █▀    ▀█   █▀   ▀██████▀ 
    """
    if animated:
        typing_effect(art)
    else:
        print(Fore.RED + art)

def verify_password():
    valid_passwords = ["techsino"]
    for attempt in range(2):
        if attempt == 0:
            clear_screen()
            display_art(animated=True)
        user_input = input(Fore.GREEN + "Please enter the password to continue: ")
        if user_input in valid_passwords:
            return True
        else:
            print(Fore.RED + "Incorrect password! Please try again.")
    return False

def random_success_failure(amount):
    success_count = 0
    failure_count = 0

    for _ in range(amount):
        result = random.choices(
            [Fore.GREEN + "[+] Success.", Fore.RED + "[-] Failure."],
            weights=[7, 3],
            k=1
        )[0]
        print(result)
        if "[+] Success." in result:
            success_count += 1
        else:
            failure_count += 1
        
        time.sleep(0.5)

    return success_count, failure_count

def display_server_busy_timer(seconds):
    print(Fore.RED + "        Server Busy, Please wait...", end=" ")
    for remaining in range(seconds, 0, -1):
        print(f"[{remaining} Sec]", end="\r")
        time.sleep(1)
    print()

def show_timer():
    print(Fore.YELLOW + "Request awaiting approval.")
    for i in range(10, 0, -1):
        print(Fore.YELLOW + f"Time remaining: {i} seconds", end="\r")
        time.sleep(1)
    print()

def sms_bomber():
    clear_screen()
    display_art(animated=False)
    while True:
        phone_number = input(Fore.GREEN + "Enter Phone Number (912xxx2345): ")
        if len(phone_number) == 10 and phone_number.isdigit():
            amount_of_requests = int(input(Fore.GREEN + "Enter amount of requests: "))

            display_server_busy_timer(random.randint(15, 45))

            print(Fore.GREEN + "Messaging...")
            time.sleep(random.randint(5, 20))
            
            random_success_failure(amount_of_requests)
            show_timer()
            break
        else:
            print(Fore.RED + "Invalid phone number! Please enter a 10-digit number.")

def call_bomber():
    clear_screen()
    display_art(animated=False)
    while True:
        phone_number = input(Fore.GREEN + "Enter Phone Number (912xxx2345) for Call: ")
        if len(phone_number) == 10 and phone_number.isdigit():
            amount_of_requests = int(input(Fore.GREEN + "Enter amount of requests: "))

            display_server_busy_timer(random.randint(15, 45))

            print(Fore.GREEN + "Calling...")
            time.sleep(random.randint(5, 20))
            
            random_success_failure(amount_of_requests)
            show_timer()
            break
        else:
            print(Fore.RED + "Invalid phone number! Please enter a 10-digit number.")

def instagram_reporter():
    clear_screen()
    display_art(animated=False)
    while True:
        username = input(Fore.GREEN + "Enter Instagram Username (@TechSino): ")
        if username.startswith('@') and len(username) > 1:
            amount_of_requests = int(input(Fore.GREEN + "Enter amount of requests: "))

            display_server_busy_timer(random.randint(15, 45))

            print(Fore.GREEN + "Reporting...")
            time.sleep(random.randint(5, 20))
            
            random_success_failure(amount_of_requests)
            show_timer()
            break
        else:
            print(Fore.RED + "Invalid username! Please enter a valid Instagram username starting with '@'.")

def rubika_reporter():
    clear_screen()
    display_art(animated=False)
    while True:
        username = input(Fore.GREEN + "Enter RUBIKA Username (@TechSino): ")
        if username.startswith('@') and len(username) > 1:
            amount_of_requests = int(input(Fore.GREEN + "Enter amount of requests: "))

            display_server_busy_timer(random.randint(15, 45))

            print(Fore.GREEN + "Reporting...")
            time.sleep(random.randint(5, 20))
            
            random_success_failure(amount_of_requests)
            show_timer()
            break
        else:
            print(Fore.RED + "Invalid username! Please enter a valid RUBIKA username starting with '@'.")

def ddos_ip_tool():
    clear_screen()
    display_art(animated=False)
    while True:
        ip_address = input(Fore.GREEN + "Enter IP Address (192.168.1.1): ")
        try:
            ip = ipaddress.ip_address(ip_address)
            amount_of_requests = int(input(Fore.GREEN + "Enter amount of requests: "))

            display_server_busy_timer(random.randint(15, 45))

            print(Fore.GREEN + f"DDoSing {ip}...")
            time.sleep(random.randint(5, 20))
            
            random_success_failure(amount_of_requests)
            show_timer()
            break
        except ValueError:
            print(Fore.RED + "Invalid IP address! Please enter a valid IPv4 or IPv6 address.")

def show_menu():
    option_info = {
        "1": "SMS BOMBER.",
        "2": "CALL BOMBER.",
        "3": "INSTAGRAM REPORTER.",
        "4": "RUBIKA REPORTER.",
        "5": "IP DDoSer.",
        "6": "Exit."
    }
    while True:
        clear_screen()
        display_art(animated=False)
        print(Fore.GREEN + "Select an option:")
        for key, value in option_info.items():
            print(Fore.GREEN + f"{key}. {value}")
        choice = input(Fore.GREEN + "\nEnter your choice: ")

        if choice == "1":
            sms_bomber()
        elif choice == "2":
            call_bomber()
        elif choice == "3":
            instagram_reporter()
        elif choice == "4":
            rubika_reporter()
        elif choice == "5":
            ddos_ip_tool()
        elif choice == "6":
            print(Fore.YELLOW + "Exiting program...")
            break
        else:
            print(Fore.RED + "Invalid choice! Please select a valid option.")

if __name__ == "__main__":
    if verify_password():
        show_menu()
