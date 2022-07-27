conta100 = conta50 = conta20 = conta10 = conta5 = conta1 = 0
valor = 333
lstvalores = []
if valor != None:
    saque = valor

while True:
    if valor == 0:
        break
    if valor >= 100:
        valor -= 100
        lstvalores.append(100)

    if 50 <= valor <= 99:
        valor -= 50
        lstvalores.append(50)

    if 20 <= valor <= 49:
        valor -= 20
        lstvalores.append(20)

    if 10 <= valor <= 19:
        valor -= 10
        lstvalores.append(10)

    if 5 <= valor <= 9:
        valor -= 5
        lstvalores.append(5)

    if 1 <= valor <= 4:
        valor -= 1
        lstvalores.append(1)

for e in lstvalores:
    if e == 100:
        conta100 += 1
    if e == 50:
        conta50 += 1
    if e == 20:
        conta20 += 1
    if e == 10:
        conta10 += 1
    if e == 5:
        conta5 += 1
    if e == 1:
        conta1 += 1
print(
    f"Notas de 100 {conta100}\nNotas 50 {conta50}\nNotas de 20 {conta20}\nNotas 10 {conta10}\nNotas de 5 {conta5}\nNotas 1 {conta1}"
)
