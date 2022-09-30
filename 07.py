'''
Faça um progrma que receba a idade de 10 pessoas e informe quantas são maiores, menores ou igual a 18
'''

idade_maior=0
idade_menor=0
idade_igual=0

for x in range (10):
    idade=int(input("Insira aqui a idade:"))
    if(idade<18):
        idade_menor+=1
    elif(idade==18):
        idade_igual+=1
    elif(idade>18):
        idade_maior+=1

print("Idades menores de 18: ",idade_menor)
print("Idades iguais a 18: ",idade_igual)
print("Idades maiores de 18: ",idade_maior)