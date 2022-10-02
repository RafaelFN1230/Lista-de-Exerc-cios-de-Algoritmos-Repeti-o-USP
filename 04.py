'''
Faça um progema que que leia cinco grupos de quatro valores (A, B, C e D) e mostr-os na ordem linda
em seguida na ordem crescente e decrescente
'''
valores={"g1":[],"g2":[],"g3":[],"g4":[],"g5":[]}

for x in range (5):
    for y in range (4):
        if (x==0):
            a=int(input("Insira o valor: "))
            valores["g1"].append(a)
        elif (x==1):
            a=int(input("Insira o valor: "))
            valores["g2"].append(a)
        elif (x==2):
            a=int(input("Insira o valor: "))
            valores["g3"].append(a)
        elif (x==3):
            a=int(input("Insira o valor: "))
            valores["g4"].append(a)
        elif (x==4):
            a=int(input("Insira o valor: "))
            valores["g5"].append(a)

print(valores)

valores["g1"].sort()
valores["g2"].sort()
valores["g3"].sort()
valores["g4"].sort()
valores["g5"].sort()
print(valores)

valores["g1"].reverse()
valores["g2"].reverse()
valores["g3"].reverse()
valores["g4"].reverse()
valores["g5"].reverse()
print(valores)
