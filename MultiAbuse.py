import os
import random
import time
from colorama import init, Fore

init(autoreset=True)

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def display_art():
    art = r"""
████████╗███████╗ ██████╗██╗  ██╗███████╗██╗███╗   ██╗ ██████╗ 
╚══██╔══╝██╔════╝██╔════╝██║  ██║██╔════╝██║████╗  ██║██╔═══██╗
   ██║   █████╗  ██║     ███████║███████╗██║██╔██╗ ██║██║   ██║
   ██║   ██╔══╝  ██║     ██╔══██║╚════██║██║██║╚██╗██║██║   ██║
   ██║   ███████╗╚██████╗██║  ██║███████║██║██║ ╚████║╚██████╔╝
   ╚═╝   ╚══════╝ ╚═════╝╚═╝  ╚═╝╚══════╝╚═╝╚═╝  ╚═══╝ ╚═════╝ 
    """
    print(Fore.RED + art)

def verify_password():
    valid_passwords = ["techsino"]
    for attempt in range(2):
        if attempt == 0:
            print(Fore.RED + "Server Busy, Please wait ...")
            time.sleep(random.randint(0, 5))
        user_input = input(Fore.GREEN + "Please enter the password to continue: ")
        if user_input in valid_passwords:
            return True
        else:
            print(Fore.RED + "Incorrect password! Please try again.")
    return False

def random_success_failure():
    duration = random.randint(30, 90)
    success_count = 0
    failure_count = 0
    start_time = time.time()
    while time.time() - start_time < duration:
        results = random.choices(
            [Fore.GREEN + "Success", Fore.RED + "Failure"],
            weights=[7, 3],
            k=1
        )
        print(results[0])
        if "Success" in results:
            success_count += 1
        else:
            failure_count += 1
        
        time.sleep(0.5)

    return success_count, failure_count

def continue_prompt():
    while True:
        continue_choice = input(Fore.GREEN + "Do you want to continue? (y/n): ").strip().lower()
        if continue_choice in ['y', 'yes']:
            return True
        elif continue_choice in ['n', 'no']:
            return False
        else:
            print(Fore.RED + "Invalid input! Please enter 'y' or 'n'.")

def sms_bomber():
    while True:
        phone_number = input(Fore.GREEN + "Enter Phone Number (912xxx2345): ")
        if len(phone_number) == 10 and phone_number.isdigit():
            print(Fore.GREEN + "Messaging...")
            time.sleep(random.randint(5, 20))
            
            random_success_failure()
            
            if not continue_prompt():
                break
        else:
            print(Fore.RED + "Invalid phone number! Please enter a 10-digit number.")

def call_bomber():
    while True:
        phone_number = input(Fore.GREEN + "Enter Phone Number (912xxx2345) for Call: ")
        if len(phone_number) == 10 and phone_number.isdigit():
            print(Fore.GREEN + "Calling...")
            time.sleep(random.randint(5, 20))
            
            random_success_failure()
            
            if not continue_prompt():
                break
        else:
            print(Fore.RED + "Invalid phone number! Please enter a 10-digit number.")

def instagram_reporter():
    while True:
        username = input(Fore.GREEN + "Enter Instagram Username (@TechSino): ")
        if username.startswith('@') and len(username) > 1:
            print(Fore.GREEN + "Reporting...")
            time.sleep(random.randint(5, 20))
            
            random_success_failure()
            
            if not continue_prompt():
                break
        else:
            print(Fore.RED + "Invalid username! Please enter a valid Instagram username starting with '@'.")

def rubika_reporter():
    while True:
        username = input(Fore.GREEN + "Enter RUBIKA Username (@TechSino): ")
        if username.startswith('@') and len(username) > 1:
            print(Fore.GREEN + "Reporting...")
            time.sleep(random.randint(5, 20))
            
            random_success_failure()
            
            if not continue_prompt():
                break
        else:
            print(Fore.RED + "Invalid username! Please enter a valid RUBIKA username starting with '@'.")

def show_menu():
    option_info = {
        "1": "You have accessed SMS BOMBER.",
        "2": "You have accessed CALL BOMBER.",
        "3": "You have accessed INSTAGRAM REPORTER.",
        "4": "You have accessed RUBIKA REPORTER."
    }

    while True:
        clear_screen()
        display_art()
        print(Fore.RED + "Welcome to the Program!")  
        print(Fore.GREEN + "\n--- Main Menu ---")
        print(Fore.GREEN + "1. SMS BOMBER")
        print(Fore.GREEN + "2. CALL BOMBER")
        print(Fore.GREEN + "3. INSTAGRAM REPORTER")
        print(Fore.GREEN + "4. RUBIKA REPORTER")
        print(Fore.GREEN + "5. Exit")

        choice = input(Fore.GREEN + "Please select an option: ")

        if choice in option_info:
            print(Fore.RED + "Server Busy, Please wait ...")
            time.sleep(random.randint(0, 5))
            
            clear_screen()
            display_art()
            print(Fore.GREEN + option_info[choice])
            if choice == "1":
                sms_bomber()
            elif choice == "2":
                call_bomber()
            elif choice == "3":
                instagram_reporter()
            elif choice == "4":
                rubika_reporter()
        elif choice == "5":
            print(Fore.GREEN + "Exiting the program.")
            break
        else:
            print(Fore.GREEN + "Invalid option! Please try again.")

clear_screen()  
display_art()  
if verify_password():  
    show_menu()  
else:
    print(Fore.RED + "Exiting the program due to incorrect password.")
