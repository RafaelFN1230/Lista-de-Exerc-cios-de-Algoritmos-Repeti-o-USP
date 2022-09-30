'''
Uma loja tem 15 clientes cadastrados e deseja enviar uma carta para cada um dele anuncioando um bonus especial.
Faça um programa que leia o nome do cliente e o valor de suas compras no ano passado.
Calcule e mostre um bonus de 10% se o valor de compras for menor que 1000, caso contrario 15%.
'''

val_comp=0
for x in range (15):
    nome=input("Insira o nome do cliente: ")
    val_comp=float(input("Insira o valor de compras do ano passado: "))
    if val_comp<=1000:
        print("Parabens",nome,"por comprar,",val_comp,"no ano passado, estamos lhe oferecendo um desconto de 10% na sua proxima compra")
    else:
        print("Parabens",nome,"por comprar,",val_comp,"no ano passado, estamos lhe oferecendo um desconto de 20% na sua proxima compra")