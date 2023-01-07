# TREINAR TABUADA
# FAÇA UM PROGRAMA QUE SOLICITE AO USUARIO UM NUMERO QUE ELE
# QUEIRA TREINAR A TABUADA. SERA SOLICITADO AO MESMO A RESPOSTA
# DO CALCULO DO NUMERO INFORMADO MULTIPLICADO POR 1 ATE 10.

num = int(input("Qual numero da tabuada deseja treinar?\n>>>"))
acertos = 0
erros = 0
for tabuada in range (1,11):
    pergunta = int(input("Qual é o resultado de {} x {}?\n>>>" .format(tabuada, num)))
    if (pergunta == (tabuada * num)):
        print("Correto!")
        acertos += 1
    else:
        print("Que pena, você errou, o valor correto é: {}" .format(tabuada*num))
        erros += 1
print("Total de acertos: {}" .format(acertos))
print("Total de erros: {}" .format(erros))