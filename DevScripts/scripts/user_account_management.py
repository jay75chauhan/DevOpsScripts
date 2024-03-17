import os

def user_account_management(username):
    if os.system(f"id {username} &>/dev/null") == 0:
        print(f"User {username} already exists.")
    else:
        os.system(f"useradd -m {username}")
        print(f"User {username} created.")
