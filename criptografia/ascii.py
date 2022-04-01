# array onde cada posicao significa uma letra
letras = [99, 114, 121, 112, 116, 111, 123, 65, 83, 67, 73, 73, 95, 112, 114, 49, 110, 116, 52, 98, 108, 51, 125]


# loop que vai de 0 ate a (quantidade_do_array-1) traduzindo letra a letra atraves da funcao chr()
for c in range(len(letras)):
    print(chr(letras[c]),end='')  
print()