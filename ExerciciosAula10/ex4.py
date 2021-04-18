num1 = int(input("Digite um numero: "))
num2 = int(input("Digite outo numero: "))

c = 0

for n in range(num1, num2 + 1):
    if n % 2 != 0:
        c +=1
print("A quantidade de impares entre ", num1 ,"e", num2, "eh: ", c)

#- Inicio uma contador, representando a quantidade de ímpares, inicialmente com o valor 0
#- Para cada número de n1 a n2, testo se ele não é par
#- Se ele não for par, logo, é impar, então o contador é incrementado em 1
#- No final, retorno o contador







