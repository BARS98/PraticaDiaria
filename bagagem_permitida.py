#ESCREVA UM PROGRAMA QUE INFORME SE O USUARIO VAI TER QUE 
# PAGAR TAVA DE SERVIÇO POR EXCESSO DE BAGAGEM

print("Obrigado por escolher a Becks Airlines! Por favor, escolha seu pacote.")
print("1 - Premier Silver\n2 - Premier Gold")
print("3 - Premier Platinum\n4 - Premier 1k")
status = int(input(">>> "))

#
# PACOTE PREMIER SILVER
#
if (status == 1):
    print("Você optou pelo pacote Premier Silver!")
    num_mala = int(input("Insira a quantidade de malas"))
    if (num_mala == 0):
        print("Tudo ok! Tenha uma boa viagem")

    elif (num_mala == 1):
        comp = int(input("Insira o comprimento da mala"))
        larg= int(input("Insira a largura da mala"))
        alt = int(input("Insira a altura da mala"))
        peso = int(input("Insira o peso da mala"))
        tam_max = comp + larg + alt
        if (tam_max <= 158 and peso <= 32):
            print("Tudo ok com as bagagens, tenha uma boa viagem")
        
        else:
            print("Você terá que pagar uma ataxa de serviço por excesso de bagagem")
    
    else:
        print("Você terá que pagar uma taxa de serviço por excesso de bagagem")
#
# PACOTE PREMIER GOLD
#
elif (status == 2):
    print("Você optou pelo pacote Premier Gold!")
    num_mala = int(input("Insira a quantidade de malas"))
    if (num_mala == 0):
        print("Tudo ok! Tenha uma boa viagem")

    elif (num_mala == 1):
        comp = int(input("Insira o comprimento da mala"))
        larg= int(input("Insira a largura da mala"))
        alt = int(input("Insira a altura da mala"))
        peso = int(input("Insira o peso da mala"))
        tam_max = comp + larg + alt
        if (tam_max <= 158 and peso <= 32):
            print("Tudo ok com as bagagens, tenha uma boa viagem")
            
        else:
            print("Você terá que pagar uma taxa de serviço por excesso de bagagem")

    elif (num_mala == 2):
        comp1 = int(input("Insira o comprimento da primeira mala"))
        larg1= int(input("Insira a largura da primeira mala"))
        alt1 = int(input("Insira a altura da primeira mala"))
        peso1 = int(input("Insira o peso da primeira mala"))
        tam_max1 = comp1 + larg1 + alt1
        if (tam_max1 <= 158 and peso1 <= 32):
            print("Tudo ok com esta bagagem")
            
        else:
            print("Você terá que pagar uma taxa de serviço por excesso de bagagem")

        comp2 = int(input("Insira o comprimento da segunda mala"))
        larg2= int(input("Insira a largura da segunda mala"))
        alt2 = int(input("Insira a altura da segunda mala"))
        peso2 = int(input("Insira o peso da segunda mala"))
        tam_max2 = comp2 + larg2 + alt2
        if (tam_max2 <= 158 and peso2 <= 32):
            print("Tudo ok com as bagagens, tenha uma boa viagem")
            
        else:
            print("Você terá que pagar uma taxa de serviço por excesso de bagagem")

    else:
        print("Você terá que pagar uma taxa de serviço por excesso de bagagem")
#
# PACOTE PREMIER PLATINUM
#
elif (status == 3):
    print("Você optou pelo pacote Premier Platinum!")
    num_mala = int(input("Insira a quantidade de malas"))
    if (num_mala == 0):
        print("Tudo ok! Tenha uma boa viagem")

    elif (num_mala == 1):
        comp = int(input("Insira o comprimento da mala"))
        larg= int(input("Insira a largura da mala"))
        alt = int(input("Insira a altura da mala"))
        peso = int(input("Insira o peso da mala"))
        tam_max = comp + larg + alt
        if (tam_max <= 158 and peso <= 32):
            print("Tudo ok com as bagagens, tenha uma boa viagem")
            
        else:
            print("Você terá que pagar uma taxa de serviço por excesso de bagagem")

    elif (num_mala == 2):
        comp1 = int(input("Insira o comprimento da primeira mala"))
        larg1= int(input("Insira a largura da primeira mala"))
        alt1 = int(input("Insira a altura da primeira mala"))
        peso1 = int(input("Insira o peso da primeira mala"))
        tam_max1 = comp1 + larg1 + alt1
        if (tam_max1 <= 158 and peso1 <= 32):
            print("Tudo ok com esta bagagem")
            
        else:
            print("Você terá que pagar uma taxa de serviço por excesso de bagagem")

        comp2 = int(input("Insira o comprimento da segunda mala"))
        larg2= int(input("Insira a largura da segunda mala"))
        alt2 = int(input("Insira a altura da segunda mala"))
        peso2 = int(input("Insira o peso da segunda mala"))
        tam_max2 = comp2 + larg2 + alt2
        if (tam_max2 <= 158 and peso2 <= 32):
            print("Tudo ok com as bagagens, tenha uma boa viagem")
            
        else:
            print("Você terá que pagar uma taxa de serviço por excesso de bagagem")

    elif (num_mala == 3):
        comp1 = int(input("Insira o comprimento da primeira mala"))
        larg1= int(input("Insira a largura da primeira mala"))
        alt1 = int(input("Insira a altura da primeira mala"))
        peso1 = int(input("Insira o peso da primeira mala"))
        tam_max1 = comp1 + larg1 + alt1
        if (tam_max1 <= 158 and peso1 <= 32):
            print("Tudo ok com esta bagagem")
            
        else:
            print("Você terá que pagar uma taxa de serviço por excesso de bagagem")

        comp2 = int(input("Insira o comprimento da segunda mala"))
        larg2= int(input("Insira a largura da segunda mala"))
        alt2 = int(input("Insira a altura da segunda mala"))
        peso2 = int(input("Insira o peso da segunda mala"))
        tam_max2 = comp2 + larg2 + alt2
        if (tam_max2 <= 158 and peso2 <= 32):
            print("Tudo ok com esta bagagem")
            
        else:
            print("Você terá que pagar uma taxa de serviço por excesso de bagagem")

        comp3 = int(input("Insira o comprimento da terceira mala"))
        larg3= int(input("Insira a largura da terceira mala"))
        alt3 = int(input("Insira a altura da terceira mala"))
        peso3 = int(input("Insira o peso da terceira mala"))
        tam_max3 = comp3 + larg3 + alt3
        if (tam_max3 <= 158 and peso3 <= 32):
            print("Tudo ok com as bagagens, tenha uma boa viagem")
            
        else:
            print("Você terá que pagar uma taxa de serviço por excesso de bagagem")

    else:
        print("Você terá que pagar uma taxa de serviço por excesso de bagagem")
#
# PACOTE PREMIER 1K
#
elif (status == 4):
    print("Você optou pelo pacote Premier 1K!")
    num_mala = int(input("Insira a quantidade de malas"))
    if (num_mala == 0):
        print("Tudo ok! Tenha uma boa viagem")

    elif (num_mala == 1):
        comp = int(input("Insira o comprimento da mala"))
        larg= int(input("Insira a largura da mala"))
        alt = int(input("Insira a altura da mala"))
        peso = int(input("Insira o peso da mala"))
        tam_max = comp + larg + alt
        if (tam_max <= 158 and peso <= 32):
            print("Tudo ok com as bagagens, tenha uma boa viagem")
            
        else:
            print("Você terá que pagar uma taxa de serviço por excesso de bagagem")

    elif (num_mala == 2):
        comp1 = int(input("Insira o comprimento da primeira mala"))
        larg1= int(input("Insira a largura da primeira mala"))
        alt1 = int(input("Insira a altura da primeira mala"))
        peso1 = int(input("Insira o peso da primeira mala"))
        tam_max1 = comp1 + larg1 + alt1
        if (tam_max1 <= 158 and peso1 <= 32):
            print("Tudo ok com esta bagagem")
            
        else:
            print("Você terá que pagar uma taxa de serviço por excesso de bagagem")

        comp2 = int(input("Insira o comprimento da segunda mala"))
        larg2= int(input("Insira a largura da segunda mala"))
        alt2 = int(input("Insira a altura da segunda mala"))
        peso2 = int(input("Insira o peso da segunda mala"))
        tam_max2 = comp2 + larg2 + alt2
        if (tam_max2 <= 158 and peso2 <= 32):
            print("Tudo ok com as bagagens, tenha uma boa viagem")
            
        else:
            print("Você terá que pagar uma taxa de serviço por excesso de bagagem")

    elif (num_mala == 3):
        comp1 = int(input("Insira o comprimento da primeira mala"))
        larg1= int(input("Insira a largura da primeira mala"))
        alt1 = int(input("Insira a altura da primeira mala"))
        peso1 = int(input("Insira o peso da primeira mala"))
        tam_max1 = comp1 + larg1 + alt1
        if (tam_max1 <= 158 and peso1 <= 32):
            print("Tudo ok com esta bagagem")
            
        else:
            print("Você terá que pagar uma taxa de serviço por excesso de bagagem")

        comp2 = int(input("Insira o comprimento da segunda mala"))
        larg2= int(input("Insira a largura da segunda mala"))
        alt2 = int(input("Insira a altura da segunda mala"))
        peso2 = int(input("Insira o peso da segunda mala"))
        tam_max2 = comp2 + larg2 + alt2
        if (tam_max2 <= 158 and peso2 <= 32):
            print("Tudo ok com esta bagagem")
            
        else:
            print("Você terá que pagar uma taxa de serviço por excesso de bagagem")

        comp3 = int(input("Insira o comprimento da terceira mala"))
        larg3= int(input("Insira a largura da terceira mala"))
        alt3 = int(input("Insira a altura da terceira mala"))
        peso3 = int(input("Insira o peso da terceira mala"))
        tam_max3 = comp3 + larg3 + alt3
        if (tam_max3 <= 158 and peso3 <= 32):
            print("Tudo ok com as bagagens, tenha uma boa viagem")
            
        else:
            print("Você terá que pagar uma taxa de serviço por excesso de bagagem")

    else:
        print("Você terá que pagar uma taxa de serviço por excesso de bagagem")