
# FAÇA UM PROGRAMA QUE SOLICITE NÚMEROS AO USUÁRIO,
# INTERROMPENDO O PROGRAMA QUANDO O MESMO INFORMAR
# O NÚMERO ZERO. ARMAZENE CADA NÚMERO INFORMADO
# EM UMA LISTA E IMPRIMIR O PRIMEIRO E O ULTIMO 
# NÚMERO INFORMADO, A SOMA, A MEDIA, O NÚMERO QUE
# MAIS APARECEU, NÚMEROS PARES E IMPARES, A LISTA 
# COMPLETA, A LISTA EM ORDEM INVERSA E CRESCENTE


numeros = []
par = []
impar = []
soma = 0
num_mais = 0
qtd_mais = 1
tem_mais = False


while True:
    num = int(input("Informe um número (digite 0 para sair)\n>>> "))
    if num == 0:
        break
    else:
        numeros.append(num)

print("O primeiro número informado foi: {}" .format(numeros[0]))
print("O último número informado foi: {}" .format(numeros[-1]))

for i in numeros:
    soma += i
    if (i % 2 == 0):
        par.append(i)
    else:
        impar.append(i)
    qtd = numeros.count(i)
    if qtd > qtd_mais:
        tem_mais = True
        qtd_mais = qtd
        num_mais = i

media = soma / (len(numeros)+1)
print("A soma dos números informados é: {}" .format(soma))
print("A média dos números informados é: {}" .format(media))

if tem_mais:
    print("O número que mais pareceu foi: {}" .format(num_mais))

print("Números pares: {}" .format(par))
print("Números impares: {}" .format(impar))
print("Lista completa: {}" .format(numeros))
numeros.reverse()
print("Lista em ordem inversa: {}" .format(numeros))
numeros.sort()
print("Lista em ordem crescente: {}" .format(numeros))
