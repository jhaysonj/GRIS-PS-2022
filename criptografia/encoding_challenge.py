from pwn import * # pip install pwntools
import json
from Crypto.Util.number import bytes_to_long, long_to_bytes
import base64
import codecs
import random
from binascii import unhexlify


r = remote('socket.cryptohack.org', 13377, level = 'debug')

def json_recv():
    line = r.recvline()
    return json.loads(line.decode())

def json_send(hsh):
    request = json.dumps(hsh).encode()
    r.sendline(request)

def list_to_string(s):
    output = ""
    return(output.join(s))


# no enunciado, eh dito que temos 100 levels para passar, necessitamos decodificar 100 mensagens
for i in range(0,101):
    received = json_recv()
    # FLAG = "crypto{????????????????????}"
    # a resposta que queremos esta escrita como "FLAG": crypto{<coisas aleatorias}>
    if "flag" in received:
        print(f"\n[*] FLAG: {received['flag']}")
        break

    print(f"\n[-] Cycle: {i}")
    print(f"[-] Received type: {received['type']}")
    print(f"[-] Received encoded value: {received['encoded']}")

    palavra_codificada = received["encoded"]
    encoding = received["type"]


    """
    ENCODINGS = [
        "base64",
        "hex",
        "rot13",
        "bigint",
        "utf-8",
    ]
    """
    # {"type": "bigint", "encoded": "0x77726974696e675f646570656e64735f6c6974"}
    # para cada encoding retorno, fazemos a o decode para cada uma das possibilidades de encodings
    if encoding == "base64":
        decoded = base64.b64decode(palavra_codificada).decode('utf8')
    elif encoding == "hex":
        decoded = (unhexlify(palavra_codificada)).decode('utf8')    
    elif encoding == "rot13":
        decoded = codecs.decode(palavra_codificada, 'rot_13')
    elif encoding == "bigint":
        decoded = unhexlify(palavra_codificada.replace("0x", "")).decode('utf8')
    elif encoding == "utf-8":
        decoded = list_to_string([chr(b) for b in palavra_codificada])

    print(f"[-] Decoded: {decoded}")
    print(f"[-] Decoded Type: {decoded}")

    to_send = {
        "decoded": decoded
    }

    # printa a tag
    json_send(to_send)


