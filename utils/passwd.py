from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import base64

# 这个是密钥
KEY = b"11193qX16h3G933g"

def encrypt(password: str) -> str:
    """加密"""
    key = KEY
    cipher = AES.new(key, AES.MODE_ECB)
    encrypted = cipher.encrypt(pad(password.encode('utf-8'), AES.block_size))
    return base64.b64encode(encrypted).decode('utf-8')
def decrypt(cipher_text: str) -> str:
    """解密"""
    key = KEY
    cipher = AES.new(key, AES.MODE_ECB)
    decrypted = unpad(cipher.decrypt(base64.b64decode(cipher_text)), AES.block_size)
    return decrypted.decode('utf-8')