'''
Faça um programa que receba a idade, a altura e o peso de 25 pessoas.
Calcule e mostre:
* A quantidade de pessoas com idade superior a 50 anos
* A media das alturas das pessoas com idade entre 10 e 20 anos:
* A percentagem de pessoas cm peso inferior a 40 quilos entre todas as pessoas analisadas
'''
pessoas_50=0
alturas=0
n_alturas=0
peso_40=0

for x in range (25):
    peso=float(input("Insira o seu pesso: "))
    altura=int(input("Insira a sua altua em cm: "))
    idade=int(input("Insira a sua idade: "))

    if (idade>50):
        pessoas_50+=1
    elif (idade>=10 and idade<=20):
        alturas+=altura
        n_alturas+=1
    elif (peso< 40):
        peso_40+=peso
tot_alt=alturas/n_alturas
tot_peso=(peso_40/25)*100
print("A quantidade de pessoas com idade superior a 50 anos: ",pessoas_50)
print("A media das alturas das pessoas com idade entre 10 e 20 anos: ", tot_alt)
print("A percentagem de pessoas cm peso inferior a 40 quilos entre todas as pessoas analisadas: ", tot_peso)