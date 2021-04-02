trabalhoLab = float(input("Qual a nota do seu trabalho de laboratorio? "))
avaliacaoSem = float(input("Qual a nota da sua avaliação semestral? "))
exFinal = float(input("Qual a nota do seu exame final? "))

mediaPonderada = ((trabalhoLab * 2)+ (avaliacaoSem * 3) + (exFinal * 5)) / 10

if(mediaPonderada >= 8.0) and (mediaPonderada <=10):
    print("Conceito A, sua média foi ", mediaPonderada)
elif(mediaPonderada >=7.0 ) and (mediaPonderada <= 7.9):
    print("Conceito B, sua média foi ", mediaPonderada)
elif(mediaPonderada >=6.0 ) and (mediaPonderada <=6.9):
    print("Conceito C, sua média foi ", mediaPonderada)
elif(mediaPonderada >=5.0 ) and (mediaPonderada <= 5.9):
    print("Conceito D, sua média foi ", mediaPonderada)
else:
    print("Conceito E, sua média foi ", mediaPonderada)



