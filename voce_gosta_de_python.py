#VOCE GOSTA DE PYTHON?
#FAÇA UM PROGRAMA CRIANDO UM LOOP INFINITO ONDE O USUARIO
#TERA QUE RESPONDER SE GOSTA DE PYTHON. CASO ELE RESPONDA "SIM"
#MOSTRE A MENSAGEM "RESPOSTA CORRETA", CASO CONTRARIO, MOSTRE 
#A MENSAGEM "OPA, ESTA NAO E A RESPOSTA CORRETA, TENTE NOVAMENTE".+
#UTILIZE STRING.UPPER()

while True:
    x = input("Você gosta de Python?\n>>>").upper()
    if (x == "SIM"):
        print("Resposta correta") 
        break
    else:
        print("Opa, esta não é a resposta correta, tente novamente")
        continue
