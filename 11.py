'''
Uma loja utiliza o codigo V para transações a vista e pe para transações a prazo.
Faça um programa que receba o codigo e o valor de 15 transações.
Calcule e mostre:
* O Valor total das compras a vista: 
* O valor total das compras a prazo:
* O valor total das compras efetuadas:
* O valor da primeira prestação das compras a prazo, sabendo que seram divididas em tres vezes:
'''
vista=0
prazo=0
for x in range (15):
    tipo=input("Insira V para transação a vista e P para transação a prazo: ")
    if (tipo=="V"):
        com_vis=float(input("Insira o valor da compra a vista: "))
        vista+=com_vis
    elif (tipo=="P"):
        com_pra=float(input("insira o valor da compra a prazo: "))
        prazo+=com_pra
    else:
        print("ERRO")
        quit()
tot=prazo+vista
par=prazo/3
print("O valor total das compras a vista: %.2f" %vista)
print("O valor total das compras a prazo: %.2f" %prazo)
print("O valor total das compras efetuadas: %.2f" %tot)
print("O valor da primeira prestação das compras a prazo: %.2f" %par)