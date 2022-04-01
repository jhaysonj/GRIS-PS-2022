from Crypto.Util.number import bytes_to_long
from Crypto.Util.number import long_to_bytes

"""
para os imports funcionarem foram necessarios instalar alguns pacotes extras, por meio dos comandos abaixo:
$ sudo apt-get install build-essential python-dev
$ pip install pycryptodomex
$ pip install pycryptodome-test-vectors
$ python -m Cryptodome.SelfTest
"""

inteiro_grande = 11515195063862318899931685488813747395775516287289682636499965282714637259206269
bytes = long_to_bytes(inteiro_grande)
print(bytes)

""""
 a saida foi : b'crypto{3nc0d1n6_4ll_7h3_w4y_d0wn}'
na resposta correta devemos enviar apenas o que esta entre aspas --> crypto{3nc0d1n6_4ll_7h3_w4y_d0wn}
"""

