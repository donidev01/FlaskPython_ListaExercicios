from ast import Return
from mmap import mmap

from flask import request


# funcionalidade01
def ex001():
    n1 = request.form.get("n1")
    n2 = request.form.get("n2")
    if n1 and n2 != None:
        n1 = int(n1)
        n2 = int(n2)

        if n1 > n2:
            return f"Maior é {n1} e menor é {n2}"
        else:
            return f"Maior é {n2} e menor é {n1}"


# funcionalidade02
def lst02ex02():
    n1 = request.form.get("n1")
    if n1 != None:
        n1 = int(n1)
        if n1 < 0:
            return "Numero é NEGATIVO"
        else:
            return "Numero é POSITIVO"


# funcionalidade03
def lst02ex03():
    letra = request.form.get("letra")
    if letra != None:
        letra = letra.upper()
        if letra == "F":
            return "FEMININO"
        else:
            return "MASCULINO"


# funcionalidade04
def lst02ex04():
    lst_vogais = ["A", "E", "I", "O", "U"]
    letra = request.form.get("letra")
    if letra != None:
        letra = letra.upper()

        if letra in lst_vogais:
            return "É Vogal"
        else:
            return "Não é vogal"


# funcionalidade05
def lst02ex05():
    n1 = request.form.get("n1")
    n2 = request.form.get("n2")
    if n1 and n2 != None:
        n1 = float(n1)
        n2 = float(n2)
        media = (n1 + n2) / 2
        if media == 10:
            return f"Media obtida {media} Aluno aprovado com distinção"
        elif media >= 7:
            return f"Media obtida {media} Aluno aprovado"
        elif media < 7:
            return f"Media obtida {media} Aluno reprovado"


# funcionalidade06
def lst02ex06():
    n1 = request.form.get("n1")
    n2 = request.form.get("n2")
    n3 = request.form.get("n3")
    if n1 and n2 and n3 != None:
        n1 = int(n1)
        n2 = int(n2)
        n3 = int(n3)
        # teste = max(n1,n2,n3) é uma possibilidade
        if n1 > n2 and n1 > n3:
            return f"Numero maior é {n1}"

        elif n2 > n3 and n2 > n1:
            return f"Numero maior é {n2}"

        elif n3 > n2 and n3 > n1:
            return f"Numero maior é {n3}"


# funcionalidade07


def lst02ex07():
    lst = []
    n1 = request.form.get("n1")
    n2 = request.form.get("n2")
    n3 = request.form.get("n3")
    if n1 and n2 and n3 != None:

        if n1 > n2 and n1 > n3:
            if n2 > n3:
                return f"Numero maior111 é {n1} numero menor {n3}"
            else:
                return f"Numero222 maior é {n1} numero menor {n2}"

        elif n2 > n3 and n2 > n1:
            if n3 > n1:
                return f"Numero maior é {n2} numero menor {n1}"
            else:
                return f"Numero maior é {n2} numero menor {n3}"

        elif n3 > n2 and n3 > n1:
            if n1 > n2:
                return f"Numero maior é {n3} numero menor {n2}"
            else:
                return f"Numero maior é {n3} numero menor {n1}"


# funcionalidade08
def lst02ex08():
    lst_valores = []
    preco1 = request.form.get("preco1")
    preco2 = request.form.get("preco2")
    preco3 = request.form.get("preco3")

    if preco1 and preco2 and preco3 != None:
        preco1 = float(preco1)
        preco2 = float(preco2)
        preco3 = float(preco3)

        lst_valores.append(preco1)
        lst_valores.append(preco2)
        lst_valores.append(preco3)

        menorValor = min(lst_valores)
        return menorValor


# funcionalidade09
def lst02ex09():
    lst_ordenada = []
    n1 = request.form.get("n1")
    n2 = request.form.get("n2")
    n3 = request.form.get("n3")
    if n1 and n2 and n3 != None:
        n1 = int(n1)
        lst_ordenada.append(n1)
        n2 = int(n2)
        lst_ordenada.append(n2)
        n3 = int(n3)
        lst_ordenada.append(n3)
        lst_ordenada.sort(reverse=True)
        return lst_ordenada


# funcionalidade10
def lst02ex10():
    msg = request.form.get("periodo")
    if msg != None:
        msg = msg.upper()
        if msg.startswith("M"):
            return "Bom dia!!!!"

        if msg.startswith("V"):
            return "Boa tarde!!!"

        if msg.startswith("N"):
            return "Boa noite!!!"


# funcionalidade11
def lst2ex11():
    msg = ""
    salarioantigo = 0
    salario = request.form.get("salario")
    if salario != None:
        salarioantigo = salario
        salario = float(salario)
        if salario < 280:
            salario += (salario * 20) / 100
            msg = "Salario menor que R$ 280 aumento concedido de 20%"

        if salario > 280 and salario < 700:
            salario += (salario * 15) / 100
            msg = "Salario entre R$280 e R$ 700 aumento concedido de 15%"

        if salario > 700 and salario < 1500:
            salario += (salario * 10) / 100
            msg = "Salario entre R$700 e R$ 1500 aumento concedido de 10%"

        if salario > 1500:
            salario += (salario * 5) / 100
            msg = "Salario superior a R$ 1500 aumento concedido de 5%"

    return (
        f"{msg}. Salario antigo R${salarioantigo}. Novo salario com aumento R${salario}"
    )


# funcionalidade12
def ex012lst2():
    lst_dados = []
    IR = INSS = FGTS = TOTAL_DESCONTOS = SAL_LIQUI = salarioBruto = 0

    salario = request.form.get("salario")
    if salario != None:
        salario = float(salario)

        if salario <= 900:
            salarioBruto = salario
            msg1 = "Salario Bruto: "
            lst_dados.append(f"{msg1} R${salarioBruto}")
            IR = (salario * 0) / 100
            msg2 = "IR (Isento)...................."
            lst_dados.append(f"{msg2} R${IR}")
            INSS = (salario * 10) / 100
            msg3 = "INSS (10%)..............."
            lst_dados.append(f"{msg3} R${INSS}")
            FGTS = (salario * 11) / 100
            msg4 = "FGTS (11%).............."
            lst_dados.append(f"{msg4} R${FGTS}")
            TOTAL_DESCONTOS = IR + INSS
            msg5 = "Total de descontos...."
            lst_dados.append(f"{msg5} R${TOTAL_DESCONTOS}")
            SAL_LIQUI = salarioBruto - TOTAL_DESCONTOS
            msg6 = "Salario liquido..........."
            lst_dados.append(f"{msg6} R${SAL_LIQUI}")

        if salario >= 901 and salario <= 1500:
            salarioBruto = salario
            msg1 = "Salario Bruto: "
            lst_dados.append(f"{msg1} R${salarioBruto}")
            IR = (salario * 5) / 100
            msg2 = "IR (5%)......................"
            lst_dados.append(f"{msg2} R${IR}")
            INSS = (salario * 10) / 100
            msg3 = "INSS (10%)..............."
            lst_dados.append(f"{msg3} R${INSS}")
            FGTS = (salario * 11) / 100
            msg4 = "FGTS (11%).............."
            lst_dados.append(f"{msg4} R${FGTS}")
            TOTAL_DESCONTOS = IR + INSS
            msg5 = "Total de descontos...."
            lst_dados.append(f"{msg5} R${TOTAL_DESCONTOS}")

            SAL_LIQUI = salarioBruto - TOTAL_DESCONTOS
            msg6 = "Salario liquido..........."
            lst_dados.append(f"{msg6} R${SAL_LIQUI}")

        if salario >= 1500 and salario <= 2500:
            salarioBruto = salario
            msg1 = "Salario Bruto: "
            lst_dados.append(f"{msg1} R${salarioBruto}")
            IR = (salario * 10) / 100
            msg2 = "IR (10%)......................"
            lst_dados.append(f"{msg2} R${IR}")
            INSS = (salario * 10) / 100
            msg3 = "INSS (10%)..............."
            lst_dados.append(f"{msg3} R${INSS}")
            FGTS = (salario * 11) / 100
            msg4 = "FGTS (11%).............."
            lst_dados.append(f"{msg4} R${FGTS}")
            TOTAL_DESCONTOS = IR + INSS
            msg5 = "Total de descontos...."
            lst_dados.append(f"{msg5} R${TOTAL_DESCONTOS}")

            SAL_LIQUI = salarioBruto - TOTAL_DESCONTOS
            msg6 = "Salario liquido..........."
            lst_dados.append(f"{msg6} R${SAL_LIQUI}")

        if salario >= 2500:
            salarioBruto = salario
            msg1 = "Salario Bruto: "
            lst_dados.append(f"{msg1} R${salarioBruto}")
            IR = (salario * 20) / 100
            msg2 = "IR (20%)......................"
            lst_dados.append(f"{msg2} R${IR}")
            INSS = (salario * 10) / 100
            msg3 = "INSS (10%)..............."
            lst_dados.append(f"{msg3} R${INSS}")
            FGTS = (salario * 11) / 100
            msg4 = "FGTS (11%).............."
            lst_dados.append(f"{msg4} R${FGTS}")
            TOTAL_DESCONTOS = IR + INSS
            msg5 = "Total de descontos...."
            lst_dados.append(f"{msg5} R${TOTAL_DESCONTOS}")

            SAL_LIQUI = salarioBruto - TOTAL_DESCONTOS
            msg6 = "Salario liquido..........."
            lst_dados.append(f"{msg6} R${SAL_LIQUI}")

    return lst_dados


# funcionalidade13
def ex13lst2():
    diaSel = request.form.get("diaSel")
    if diaSel != None:
        diaSel = int(diaSel)
        if diaSel < 1 or diaSel > 7:
            return "Valor precisa estre 0 e 7"

        if diaSel == 1:
            return "1 - Domingo"

        if diaSel == 2:
            return "2 - Segunda"

        if diaSel == 3:
            return "3 - Terça"

        if diaSel == 4:
            return "4 - Quarta"

        if diaSel == 5:
            return "5 - Quinta"

        if diaSel == 6:
            return "6 - Sexta"

        if diaSel == 7:
            return "7 - Sabado"


# funcionalidade14
def ex14lst2():
    n1 = request.form.get("n1")
    n2 = request.form.get("n2")
    if n1 and n2 != None:
        n1 = float(n1)
        n2 = float(n2)
        media = (n1 + n2) / 2
        msg = f"Notas {n1} / {n2} media {media}"

        if 9 <= media <= 10:
            return f"{msg} Aprovado"

        if 7.5 <= media <= 9:
            return f"{msg} Aprovado"

        if 6 <= media <= 7.5:
            return f"{msg} Aprovado"

        if 4 <= media <= 6:
            return f"{msg} Reprovado"

        if 0 <= media <= 4:
            return f"{msg} Reprovado"


# funcionalidade15
def ex15lst2():
    lsttri = []
    m1 = request.form.get("m1")
    m2 = request.form.get("m2")
    m3 = request.form.get("m3")
    if m1 and m2 and m3 != None:
        m1 = float(m1)
        m2 = float(m2)
        m3 = float(m3)
        if m1 + m2 > m3 and m1 + m3 > m2 and m2 + m1 > m3 and m2 + m3 > m1:
            msgTri = f"As medidas {m1} || {m2} || {m3} fornecidas formam um triangulo"
            if m1 == m2 == m3:
                tpTri = "equilatero"
                return f"{msgTri}: {tpTri}"

            if m1 == m2 or m1 == m3 or m2 == m3:
                tpTri = "Isósceles"
                return f"{msgTri}: {tpTri}"

            if m1 != m2 or m1 != m3 or m2 != m3:
                tpTri = "Escaleno"
                return f"{msgTri}: {tpTri}"

        else:
            return f"As medidas fornecidas NÃO formam um triangulo {m1} || {m2} || {m3}"


# funcionalidade16
def ex16lst2():
    a = request.form.get("a")
    b = request.form.get("b")
    c = request.form.get("c")
    if a and b and c != None:
        a = float(a)
        b = float(b)
        c = float(c)
        if a == 0:
            return "A IGUAL A ZERO não é uma equação do segundo grau!!!"
        else:
            D = b**2 - 4 * a * c
            if D < 0:
                return "A equação não possui raizes reais pois o DELTA é negativo"

            if D == 0:
                x1 = (-b + D ** (1 / 2)) / (2 * a)
                s1 = "Raiz 1: {:.2f}".format(x1)
                return s1

            if D > 0:
                x1 = (-b + D ** (1 / 2)) / (2 * a)
                x2 = (+b + D ** (1 / 2)) / (2 * a)
                s1 = "Raiz 1: {:.2f}".format(x1)
                s2 = "Raiz 2: {:.2f}".format(x2)
                return s1, s2


# funcionalidade17
def ex17lst2():
    ano = request.form.get("ano")
    if ano != None:
        ano = int(ano)
        if ano % 4 == 0:
            if ano % 100 != 0:
                return f"{ano} é BISEXTO"
            else:
                return f"{ano} Não é BISEXTO"

        if ano % 400 != 0:
            return f"{ano} Não é BISSEXTO"
        else:
            return f"{ano} é BISSEXTO"


# funcionalidade18
def ex18lst2():
    dados = request.form.get("data")
    if dados != None:
        dados = str(dados)
        if len(dados) != 8:
            return (
                "A data informada é invalida. a mesma deve estar no formato dd/mm/aaaa"
            )

        else:
            dd = int(dados[:2])
            mm = int(dados[2:4])
            aaaa = int(dados[4:8])
            if dd < 0 or dd > 31:
                return "Dia invalido"
            if mm < 0 or mm > 12:
                return "Dia invalido"
            if aaaa < 0 or aaaa > 3000:
                return "ano invalido"

            return f"Data de retorno {dd}/{mm}/{aaaa}"
