'''
Faça um programa que verifique e mostre os numeros entre 1000 e 2000 (inclusive) que, quando divididos 11, produzam resto igual a 5.
'''

n=5
r=0
for x in range (1000,2001):
    r=x//11
    if (x==(r*11)+5):
        print(x)