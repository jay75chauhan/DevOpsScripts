import string
import secrets

def password_generator(length):
    alphabet = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(secrets.choice(alphabet) for i in range(length))
    print(f"Generated password: {password}")
