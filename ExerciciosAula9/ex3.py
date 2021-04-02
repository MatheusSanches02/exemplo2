n1 = float(input("Digite um numero real: "))
n2 = float(input("Digite outro numero real: "))
n3 = float(input("Escreva mais um numero real: "))

if(n1>n2) and (n2>n3):
    print(n3,n2,n1)
elif(n2>n1) and (n1>n3):
    print(n3, n1, n2)
elif(n3>n1) and (n1>n2):
    print(n2,n1,n3)
elif(n1>n3) and (n3>n2):
    print(n2,n3,n1)
elif(n2>n3) and (n3>n1):
    print(n1,n3,n2)
elif(n3>n2) and (n2>n1):
    print(n1,n2,n3)

    
