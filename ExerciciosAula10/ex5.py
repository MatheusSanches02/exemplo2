num1 = int(input("Digite um numero inteiro: "))
num2 = int(input("Digite outro numero inteiro: "))

soma = 0
for n in range(num1 + 1, num2):
    soma = n + soma
print("O valor da soma entre os numeros digitados eh: ", soma)
   