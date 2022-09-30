'''
Faça um progra que leia 15 idades e motres a quantidade de pessoas em cada faixa etaria 
e a porcentagem de pessoas na primeira e na ultima em relação com as outras
1 - ate 15 anos
2 - de 16 a 30 anos
3 - de 31 a 46 anos
4 - de 46 a 60 anos
5 - acima de 61 anos

'''

g1=0
g2=0
g3=0
g4=0
g5=0

for x in range (15):
    idade=int(input("Insira a idade: "))
    if (idade<=15):
        g1+=1
    elif (idade>=16 and idade<=30):
        g2+=1
    elif (idade>=31 and idade<=46):
        g3+=1
    elif (idade>=46 and idade<=60):
        g4+=1
    elif (idade>=61):
        g5+=1

print("Grupo 1: ",g1)
print("Grupo 1: ",g2)
print("Grupo 1: ",g3)
print("Grupo 1: ",g4)
print("Grupo 1: ",g5)

pg1=(g1/15)*100
pg5=(g5/15)*100

print("Porcentagem do Grupo 1: %.2f" %pg1)
print("Porcentagem do grupo 5: %.2f" %pg5)