'''
Uma companhia de teatro deseja dar uma serie de espetaculos.
A direção calcula que R$ 5,00 o ingresso, serão vendidos 120 ingressos,
e que as despesas serão R$ 200,00.
Diminuindo-se R$ 0,50 o preço dos ingressos espera-se que as vendas aumentem em 26 ingressos.
Faça um programa que escreva uma tabela de valores de lucros esperados em função do preço do ingresso,
fazendo-se variar esse preço de R$ 5,00 a R$ 1,00 de R$ 0,50 em R$ 0,50.
Escreva, ainda, o lucro maximo esperado, o preço do ingresso e a quantidade de ingressos vendidos para a obtenção desse lucro. 
'''
despesas=200
n_ingressos=120
for x in range (500,50,-50):
    n_ingressos=120+((500-x)//50)*26
    val_ing=x/100
    val_tot_bruto=n_ingressos*val_ing
    val_tot_liq=(n_ingressos*val_ing)-despesas
    print("Valor do ingresso: R$ %.2f"%val_ing," ","Numero de ingressos: ",n_ingressos," ","Lucro maximo bruto: R$ %.2f"%val_tot_bruto," ","Lucro maximo liquido: R$ %.2f"%val_tot_liq)
