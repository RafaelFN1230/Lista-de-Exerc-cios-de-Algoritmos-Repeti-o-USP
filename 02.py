'''
Faça um programa que leia um valor n, inteiro e positivo, calcule e mostre a seguinte soma: s=1+1/2+1/3+1/4+...+1/n
'''

n=int(input("Insira aqui o valor n: "))
tot=0
for x in range (0,n,1):
    tot=tot+(1/(1+x))

print(tot)
