from matematica import operacoes
while True:
    print("Informe a operação desejada: ")
    op = int(input(" 1 - Soma\n 2 - Subtração\n" 
                " 3 - Multiplicação\n 4 - Divisão\n"
                " 5 - Quadrado\n 6 - Cubo\n 7 - Tabuada\n 8 - Sair\n>>> "))
    if op < 1 or op > 8:
        print("Opção Invalida!")
        exit()
    if op in [1,2,3,4]:
        num1 = float(input("Informe o primeiro numero\n>>> "))
        num2 = float(input("Informe o segundo numero\n>>> "))

        if op == 1:
            print(operacoes.soma(num1,num2))

        elif op == 2:
            print(operacoes.subtracao(num1,num2))

        elif op == 3:
            print(operacoes.multiplicacao(num1,num2))
        
        else:
            if num1 <= 0 or num2 <= 0:
                print("Não é possivel dividir por 0")
                break
            print(operacoes.divisao(num1,num2))

    elif op in [5,6,7,8]:
        num = int(input("Informe o um numero\n>>> "))
        if op == 5:
            print(operacoes.quadrado(num))

        elif op == 6:
            print(operacoes.cubo(num))

        elif op == 7:
            for tab in operacoes.tabuada:
                print(tab(num))

        elif op == 8:
            print("Até a proxima.")
            exit()
