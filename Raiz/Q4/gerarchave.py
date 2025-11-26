from cryptography.fernet import Fernet

# 1. Gerar uma nova chave
key = Fernet.generate_key()

# 2. Mostrar no ecrã (opcional, só para veres)
# print("Nova chave gerada:", key)

# 3. Guardar a chave num ficheiro
with open("key.fernet", "wb") as key_file:
    key_file.write(key)

print("Chave guardada no ficheiro key.fernet")
