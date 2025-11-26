from cryptography.fernet import Fernet

key = Fernet.generate_key()

with open("key.fernet", "wb") as f:
    f.write(key)

print("Key gerated and saved")