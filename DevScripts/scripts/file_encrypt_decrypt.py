import cryptography
from cryptography.fernet import Fernet

def file_encrypt_decrypt(file):
    key = Fernet.generate_key()
    cipher = Fernet(key)
    
    with open(file, 'rb') as f:
        data = f.read()
    
    encrypted_data = cipher.encrypt(data)
    encrypted_file = file + '.enc'
    
    with open(encrypted_file, 'wb') as f:
        f.write(encrypted_data)
    
    print(f"File encrypted: {encrypted_file}")
