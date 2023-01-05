#VALIDAR CALCULO
#FAÇA UM PROGRAMA QUE SOLICITE DOIS NUMEROS AO USUARIO (COM DECIMAIS)
#EM SEGUIDA SOLICITE QUE O USUARIO INFORME O RESULTADO DAS QUATRO OPERAÇÕES
#MATEMATICAS E VALIDE A RESPOSTA.



x = float(input("Digite o numero desejado\n>>>"))
y = float(input("Digite outro numero\n>>>"))

som = float(input("informe o resultado da soma\n>>> "))
sub = float(input("informe o resultado da subtração\n>>> "))
mul = float(input("informe o resultado da multiplicação\n>>> "))
div = float(input("informe o resultado da divisão\n>>> "))

if (som == (x + y)):
    print("Você acertou!")
else:
    print("Você errou! A soma de {} e {} é {}" .format(x, y, x + y))

if (sub == (x - y)):
    print("Você acertou!")
else:
    print("Você errou! A subtração de {} e {} é: {}" .format(x, y, x / y))

if (mul == (x * y)):
    print("Você acertou!")
else:
    print("Você errou! A multiplicação de {} e {} é: {}" .format(x, y, x / y))

if (div == (x / y)):
    print("Você acertou!")
else:
    print("Você errou! A divisão de {} e {} é: {}" .format(x, y, x / y))  
