import os

def user_password_expiry_checker():
    users = [line.split(':')[0] for line in open('/etc/passwd') if '/bin/bash' in line]
    for user in users:
        password_expires = os.popen(f"chage -l {user} | grep 'Password expires' | awk '{{print $4}}'").read().strip()
        print(f"User: {user}, Password Expires: {password_expires}")
