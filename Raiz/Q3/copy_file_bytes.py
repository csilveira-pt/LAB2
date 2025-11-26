from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from Crypto.Random import get_random_bytes


def copy_binary_file(input_file, output_file, start_byte, end_byte=None):
    with open(input_file, 'rb') as f1, open(output_file, 'wb') as f2:
        if end_byte is None:
            f1.seek(start_byte)
            f2.write(f1.read())
        else:
            length = end_byte - start_byte
            f1.seek(start_byte)
            f2.write(f1.read(length))

def join_binary_files(file1, file2, output_file):
    with open(file1, 'rb') as f1, open(file2, 'rb') as f2, open(output_file, 'wb') as out:
        out.write(f1.read())
        out.write(f2.read())

# Example usage:
# copy_binary_file('input.bin', 'output.bin', 0, 30) # Copy bytes 0-30 to output.bin
# copy_binary_file('input.bin', 'output.bin', 54) # Copy bytes 54 to the end to output.bin

copy_binary_file('c-academy.bmp', 'head', 0, 54)
copy_binary_file('c-academy.bmp', 'body', 54)
join_binary_files('head', 'body', 'c-academy-original.bmp')

# Cifrar em ECB

key = b'0123456789abcdef'   # chave AES de 16 bytes

with open('body', 'rb') as f:
    data = f.read()

padded = pad(data, AES.block_size)

cipher = AES.new(key, AES.MODE_ECB)
ciphertext = cipher.encrypt(padded)

with open('body_ecb', 'wb') as f:
    f.write(ciphertext)

join_binary_files('head', 'body_ecb', 'c-academy-ECB.bmp')

# Cifrar em CBC

rb = get_random_bytes(16)

cipher = AES.new(key, AES.MODE_CBC, rb)
ciphertext_cbc = cipher.encrypt(padded)


with open('body_cbc', 'wb') as f:
    f.write(rb + ciphertext_cbc)


join_binary_files('head', 'body_cbc', 'c-academy-CBC.bmp')