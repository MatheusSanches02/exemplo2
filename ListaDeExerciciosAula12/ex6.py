print("-"*30)
print("Sequencia Fibonacci")
print("-"*30)

unknowTerm = int(input("Qual termo você quer descobrir? "))
firstTerm = 0
secondTerm = 1
cont = 2
if unknowTerm == 1:
    print(0)
elif unknowTerm == 2:
    print(1)
elif unknowTerm > 2:
    while cont <= unknowTerm:
        thirdTerm = firstTerm + secondTerm
        firstTerm = secondTerm
        secondTerm = thirdTerm
        cont += 1
    print(thirdTerm)
  


