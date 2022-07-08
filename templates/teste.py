lata = 18
litros = 3
metros = 325


listrosnecessarios = metros / litros
print(listrosnecessarios)

contlatas = 0
while True:
    if listrosnecessarios > 1:
        contlatas += 1
        listrosnecessarios =  listrosnecessarios - 18
    else:
        break
print(contlatas)
