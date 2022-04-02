# esse arquivo foi necessario para criar a conta no site, nao possui relacao direta com a tag.

def encrypt(chave, mensagem):
    mensagem = mensagem.upper()
    alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    result = ""

    for letra in mensagem:
        if letra in alpha: # verifica se a letra eh realmente uma letra
            # acha a letra da cifra correspondendo ao nosso alfabeto
            letra_index = (alpha.find(letra) + chave) % len(alpha)

            result = result + alpha[letra_index]
        else:
            result = result + letra

    return result

def decrypt(chave, mensagem):
    mensagem = mensagem.upper()
    alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    result = ""

    for letra in mensagem:
        if letra in alpha: # verifica se a letra eh realmente uma letra
            # acha a letra da cifra correspondendo ao nosso alfabeto 
            letra_index = (alpha.find(letra) - chave) % len(alpha)

            result = result + alpha[letra_index]
        else:
            result = result + letra

    return result

frase = "VAUZ XMPPQD MYMLUZS OTQR"

"""
 o loop precisa comecar com a chave 1, indo ate 26(inclusive) para varremos todas as possibilidades de chave. 
No alfabeto temos um ciclo, onde 1 = 27, a chave 2 = 28, a chave 3 = 29. Por isso basta procurarmos ate a chave 26
"""
for c in range(1,27):
    print(print(decrypt(c,frase)))


print("\n\n")
print(f"chave correta --> {12}")
print(f"mensagem da chave correta --> {decrypt(12,frase)}")
