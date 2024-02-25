# pip install cryptography

from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import rsa
import os

def generate_a_key():
    # Gerar uma chave privada RSA
    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048,  # Ajuste o tamanho da chave conforme necessário
        backend=default_backend()
    )

    # Exportar a chave privada RSA no formato PEM
    pem = private_key.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.PKCS8,
        encryption_algorithm=serialization.NoEncryption()
    )

    # Converter para string e imprimir
    return pem.decode('utf-8')

def save_keys_to_files(num_keys=1000, directory="keys"):
    os.makedirs(directory, exist_ok=True)  # Criar o diretório se não existir
    for i in range(1, num_keys + 1):
        key_content = generate_a_key()
        file_name = f"key_{i:04}.pem"
        file_path = os.path.join(directory, file_name)
        with open(file_path, 'w') as key_file:
            key_file.write(key_content)
        print(f"Chave {i} salva em: {file_path}")

if __name__ == "__main__":
    save_keys_to_files()