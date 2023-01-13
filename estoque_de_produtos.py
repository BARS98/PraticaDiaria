# FAÇA UM DICIONARIO COM OS SEGUINTES PRODUTOS
# AO INICIAR O PROGRAMA, IMPRIMIR O ESTOQUE
# SOLICITE AO USUARIO QUE ESCOLHA ENTRE 3 OPÇOES
# REGISTRAR ENTRADA E SAIDA DE PRODUTOS, E SAIR DO SISTEMA
# DEIXANDO O USUARIO SELECIONAR O CODIGO DO PRODUTO,
# A QUANTIDADE QUE DESEJA ADICIONAR OU RETIRAR
# E QUANDO SAIR DO SITEMA, IMPRIMIR O ESTOQUE ATUALIZADO



estoque = {
            "1": ["Teclado", 300, 166.71],
            "2": ["Mouse", 125, 80.57],
            "3": ["Processador", 25, 875.64],
            "4": ["Cooler", 70, 35.14]
}
print("Estoque atual: ")
print("Código - Descrição - Qtd. - Valor Unitário")
for codigo in estoque:
    print(codigo, "-", estoque[codigo][0], "-", estoque[codigo][1], "-", estoque[codigo][2])
while True:
    print("Escolha uma das seguintes opções")
    print("--------------------------------")
    print("1: Registrar entrada de produtos")
    print("2: Registrar saida de produtos")
    print("3: sair do sistema")

    opcao = int(input(">>>"))
    if opcao == 1:
        codigo = (input("Informe o codigo do produto\n >>>"))
        qtd = int(input("Informe a quantidade de entrada do produto\n >>>"))
        for produto in estoque:
            if produto == codigo:
                estoque[codigo][1] += qtd
                print(codigo, "-", estoque[codigo][0], "-", estoque[codigo][1], "-", estoque[codigo][2])


    elif opcao == 2:
        codigo = (input("Informe o codigo do produto\n >>>"))
        qtd = int(input("Informe a quantidade de saida do produto\n >>>"))
        for produto in estoque:
            if produto == codigo:
                if qtd <= estoque[produto][1]:
                    estoque[codigo][1] -= qtd
                    print(codigo, "-", estoque[codigo][0], "-", estoque[codigo][1], "-", estoque[codigo][2])
                else:
                    print("Quantidade insuficiente no estoque!!!")


    elif opcao ==3:
        print("Estoque atual: ")
        print("Código - Descrição - Qtd. - Valor Unitário")
        for codigo in estoque:
            print(codigo, "-", estoque[codigo][0], "-", estoque[codigo][1], "-", estoque[codigo][2])
        break
    else:
        print("Opção Invalida! Escolha uma da 3 opções")
        break

