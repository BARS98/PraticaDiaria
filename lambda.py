soma = lambda x,y: x + y
sub = lambda x,y: x - y
multi = lambda x,y: x * y
div = lambda x,y: x / y

print("Escolha uma operação")
op = int(input(" 1 - Soma\n 2 - Subtração\n" 
               " 3 - Multiplicação\n 4 - Divisão"))
if op < 1 or op > 4:
    print("Valor invalido")
    exit()

num1 = int(input("Digite o primeiro número\n>>> "))
num2 = int(input("Digite o segundo número\n>>> "))

if op == 1:
    print("Soma: {} + {} = {} " .format(num1,num2,soma(num1,num2)))

elif op == 2:
    print("Subtração: {} - {} = {} " .format(num1,num2,sub(num1,num2)))

elif op == 3:
    print("Multiplicação: {} x {} = {} " .format(num1,num2,multi(num1,num2)))

else:
    print("Divisão: {} / {} = {:.2f} " .format(num1,num2,div(num1,num2)))
