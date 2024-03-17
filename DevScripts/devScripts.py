import os
import platform
from scripts import *

def clear_screen():
    # Clear screen based on OS
    if platform.system() == 'Windows':
        os.system('cls')
    else:
        os.system('clear')

def display_menu():
    clear_screen()
    print("DevScripts Tool Main Menu")
    print("=========================")
    print("1. File Backup")
    print("2. System Monitoring")
    print("3. User Account Management")
    print("4. Log Analyzer")
    print("5. Password Generator")
    print("6. File Encryption/Decryption")
    print("7. Automated Software Installation")
    print("8. Network Connectivity Checker")
    print("9. Website Uptime Checker")
    print("10. Data Cleanup")
    print("11. CPU Usage Tracker")
    print("12. System Information")
    print("13. Task Scheduler")
    print("14. Disk Space Monitoring")
    print("15. Remote Server Backup")
    print("16. Environment Setup")
    print("17. File Compression/Decompression")
    print("18. Database Backup")
    print("19. Git Repository Updater")
    print("20. Directory Synchronization")
    print("21. Web Server Log Analyzer")
    print("22. System Health Check")
    print("23. Automated Database Cleanup")
    print("24. User Password Expiry Checker")
    print("25. Service Restart")
    print("26. Folder Size Checker")
    print("27. Backup Rotation")
    print("28. Remote Script Execution")
    print("29. Network Interface Information")
    print("30. Random Quotes Generator")
    print("q. Quit")

def execute_script(script_name):
    function_name = script_name.split('.')[0]  # Extract function name from file name
    function = getattr(globals()[function_name], function_name)  # Get the function from the corresponding module
    function()  # Call the function

def main():
    while True:
        display_menu()
        choice = input("Enter your choice: ")
        if choice.lower() == 'q':
            break
        elif choice.isdigit() and 1 <= int(choice) <= 30:
            script_name = f"script_{choice}.py"
            execute_script(script_name)
        else:
            print("Invalid choice. Please enter a number between 1 and 30, or 'q' to quit.")

if __name__ == "__main__":
    main()
