dados_departamento = {
    1: "RH",
    2: "FINANÇAS",
    3: "SAC",
    4: "VENDAS",
    5: "TI",
}

dados_funcionario = {
    100: dict(nome="José", admissao="01/05/2016", departamento= 3),
    101: dict(nome="Maria", admissao="10/08/2018", departamento= 1),
    102: dict(nome="Mariana", admissao="01/01/2019", departamento= 4),
    103: dict(nome="Ana", admissao="18/05/2001", departamento= 5),
    104: dict(nome="João", admissao="19/09/2014", departamento= 1),
    105: dict(nome="Juca", admissao="25/07/2008", departamento= 2)
}

def get_funcionario(cod_funcionario):
    if cod_funcionario in (dados_funcionario):
        return(dados_funcionario[cod_funcionario])
    else:
        print("Funcionario de código {} não localizado" .format(cod_funcionario))
        return

def imprimir_funcionario(funcionario):
    for chave, valor in funcionario.items():
        if chave == "departamento":
            print(chave + ":",  dados_departamento[valor])
        else:
            print(chave+ ":", valor)

cod_funcionario = int(input("Digite aqui o código do funcionario"))
funcionario = get_funcionario(cod_funcionario)
if funcionario:
    imprimir_funcionario(funcionario)


