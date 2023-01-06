#TABUADA
#FAÇA UM PROGRAMA QUE SOLICITE UM NUMERO AO USUARIO
#E EXIBA A TABUADA DE MULTIPLICAÇÃO PARA O NUMERO INFORMADO


num = int(input("Qual tabuada deseja ver? Informe o número\n>>>"))

for tabuada in range(1, 11):
    print("{} x {} = {}".format (tabuada, num, tabuada * num))
