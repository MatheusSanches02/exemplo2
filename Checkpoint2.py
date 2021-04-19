descontoTotal = 0

# Validando quantidade de pratos
quantidadePratos = int(input("Quantos pratos foram consumidos? "))
while quantidadePratos <= 0:
    print("Quantidade de pratos principais inválido. Digite novamente.")
    quantidadePratos = int(input("-->"))
if quantidadePratos > 3:
    descontoTotal = descontoTotal + 4

# Validando o valor da nota
valorNota = float(input("Qual o valor a pagar? R$"))
while valorNota <= 0:
    print("Valor invalido. Digite novamente.")
    valorNota = float(input("-->"))
if valorNota > 500.0:
    descontoTotal = descontoTotal + 6

# Validando o cupom
cupomQuestion = False
while cupomQuestion == False:
    cupom = input("Você tem cupom de desconto? Responda com 'S' para SIM e com 'N' para NÃO: ").upper()
    while cupom != 'S' and cupom != 'N':
        print("Resposta inválida, digite novamente.")
        cupom = input("-->")
    if cupom == 'S':
        cupomName = input("Digite o nome do cupom: ").upper()
        if cupomName == 'BORALA10':
            descontoTotal = descontoTotal + 10
            cupomQuestion = True
        elif cupomName == 'BORALA5':
            descontoTotal += 10
            cupomQuestion = True
        else:
            print("Cupom inválido!")
    else:
        cupomQuestion = True

# Validção de cliente 
clienteNovo = input("É a primeira vez que visita o restaurante? Responda com 'S' para SIM e com 'N' para NÃO: ").upper()
while clienteNovo != 'S' and clienteNovo != 'N':
    print("Resposta inválida, digite novamente.")
    clienteNovo = input("-->")
if clienteNovo == 'S':
    descontoTotal += 5

# Pergunta o numero de pessoas que vão pagar a conta 
quantidadePessoas = int(input("Quantas pessoas vão pagar a conta? "))
if quantidadePessoas > 1:
    dividirConta = input("Gostaria de dividir a conta? Responda com 'S' para SIM e com 'N' para NÃO: ").upper()
    while dividirConta != 'S' and dividirConta != 'N':
        print("Resposta inválida, digite novamente.")
        dividirConta = input("-->")

# Desenvolvendo calculo final
valorDesconto = valorNota * (descontoTotal / 100)
valorFinal = valorNota - valorDesconto
valorDividido = valorFinal / quantidadePessoas
print("-"*50)
print("Valor total da nota fiscal: R$", valorNota)
print("Valor da nota com desconto: R$", valorFinal)
print("")
print("Numero de pessoas: ", quantidadePessoas)
print("Total por pessoa: R$", valorDividido)
print("-"*50)

# Trabalho finalizado

