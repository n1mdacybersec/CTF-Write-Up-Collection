from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.backends import default_backend
import base64

def decrypt(ciphertext, password, salt):
    # Decode the Base64-encoded ciphertext
    ciphertext = base64.b64decode(ciphertext)
    
    # Derive the encryption key using PBKDF2 with HMAC-SHA256
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=10000,
        backend=default_backend()
    )
    key = kdf.derive(password.encode())
    
    # Decrypt the ciphertext using AES
    cipher = Cipher(algorithms.AES(key), modes.ECB(), backend=default_backend())
    decryptor = cipher.decryptor()
    decrypted_bytes = decryptor.update(ciphertext) + decryptor.finalize()
    
    # Convert the decrypted bytes to a string
    decrypted_text = decrypted_bytes.decode('utf-8')
    
    return decrypted_text

if __name__ == "__main__":
    ciphertext = "FOqxc90aMQZydCQb2MUm5tj4kRIxxVeCDWzAANfOrr8JItHYneUHhSV0awvQIo/8E1LtfYm/+VVWz0PDK6MXp38BWHoFDorhdS44DzYj9CQ="  # Replace with the encrypted flag from Java
    password = "aesiseasy"
    salt = b"saltval"

    decrypted_flag = decrypt(ciphertext, password, salt)
    print("Decrypted Flag:", decrypted_flag)
