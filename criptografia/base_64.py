
from base64 import b64encode

hex_string = "72bca9b68fc16ac7beeb8f849dca1d8a783e8acf9679bf9269f7bf"
base = b64encode(bytes.fromhex(hex_string))

print(base)  
"""
saida --> b'crypto/Base+64+Encoding+is+Web+Safe/'
na resposta correta devemos enviar apenas o que esta entre aspas --> crypto/Base+64+Encoding+is+Web+Safe/
"""