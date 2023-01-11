# Faça um programa que solicite várias palavras 
# ao usuário. Armazene cada palavra informada 
# em uma lista. Em seguida use o set (conjunto) 
# para imprimir as palavras informadas sem 
# repetições.


lista_palavras = []
while True:
    palavras = input("Digite uma palavra ou digite 0 para sair(repita algumas palavras)\n>>>")
    if (palavras == "0"):
        break
    else:
        lista_palavras.append(palavras)
conj_palavras = set(lista_palavras)
print(conj_palavras)
