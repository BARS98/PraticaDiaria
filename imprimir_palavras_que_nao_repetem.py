# FAÇA UM PROGRAMA QUE SOLICITE AO USUARIO QUE DIGITE
# VARIAS PALAVRAS REPETINDO ALGUMAS E IMPRIMA NO FINAL
# AS PALAVRAS QUE FORAM INFORMADAS APENAS UMA VEZ



lista = []
nao_repitidas = []
while True:
    palavra = input("Digite uma palavra(digite 0 para sair)\n>>>")
    if (palavra == "0"):
        break
    else:
        lista.append(palavra)
for i in lista:
    if lista.count(i) == 1:
        nao_repitidas.append(i)

print("As palavras que não se repetem são: {}" .format(nao_repitidas))
