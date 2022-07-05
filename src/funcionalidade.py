from webbrowser import get

from flask import request

comp = '\o/'

def ex01():
    msg = request.form.get('msg')
   
    if msg != None:
        msg = msg.upper()
        return f'{msg} {comp}'

def ex02():
    numero = request.form.get('numero')
    if numero != None:
        return f'{numero} {comp}'

def ex03():
    soma = 0
    n1 = request.form.get('n1')
    n2 = request.form.get('n2')
    if n1 and n2 != None:
        n1 = int(n1)
        n2 = int(n2)
        soma = n1 + n2
    return f'{soma} {comp}'

def ex04():
    media =  0
    n1 = request.form.get('n1')
    n2 = request.form.get('n2')
    n3 = request.form.get('n3')
    n4 = request.form.get('n4')
    if n1 and n2 and n3 and n4 != None:
        n1 = int(n1)
        n2 = int(n2)
        n3 = int(n3)
        n4 = int(n4)
        media = (n1+n2+n3+n4) / 4
    return f'A media para as notas {n1} {n2} {n3} {n4} é {media}'

def ex05():
    medida = 0
    medida = request.form.get('medida')
    if medida != None:
        medida = float(medida)
        medida = medida * 1000
    return f'{medida} centimetros.'
    
def ex06():
    raio = request.form.get('raio')
    if raio != None:
        raio = float(raio)
        area = 3.14 * (raio * raio)
        return f'A area do raio sinalizado possui {area}'

def ex07():
    area = 0
    altura = request.form.get('altura')
    largura = request.form.get('largura')
    if altura and largura != None:
        altura = float(altura)
        largura = float(largura)
        area = (altura * largura) * 2
    return f'A largura: {largura} x a altura: {altura} x 2 é {area}'

def ex08():
    salarioBruto = 0
    vlhora = request.form.get('vlhora') 
    qtdTrabalhados = request.form.get('qtdTrabalhados')
    if vlhora and qtdTrabalhados != None:
        vlhora = int(vlhora)
        qtdTrabalhados = int(qtdTrabalhados)
        salarioBruto = vlhora * qtdTrabalhados
    return f'O salario bruto para a {vlhora} x {qtdTrabalhados} é {salarioBruto}'

def ex09():
    temp = request.form.get('temp1')
    if temp != None:
        temp = float(temp)
        Celsius = 5 * ((temp-32) / 9)
        return Celsius

def ex10():
    temp = request.form.get('temp1')
    if temp != None:
        temp=float(temp)
        temp = (temp * 9/5) + 32
        return temp

def ex11():
    lst = []
    n1 = request.form.get('n1')
    n2 = request.form.get('n2')
    n3 = request.form.get('n3')
    if n1 and n2 and n3 != None:
        n1 = int(n1)
        n2 = int(n2)
        n3 = float(n3)
        n_1 = (n1*2) + n2 / 2
        lst.append(n_1) 
        n_2 = (n1*3) + n3
        lst.append(n_2)
        n_3 = n3 ** 3
        lst.append(n_3)
        return lst 

def ex12():
    altura = request.form.get('altura')
    if altura != None:
        altura = float(altura)
        peso_ideal = (72.7*altura) - 58

        return f'O peso ideal para a altura {altura} é {peso_ideal:.2f}'

def ex13():
    peso = 0
    altura = request.form.get('altura')
    sexo = request.form.get('sexo')
    se = ''
    if altura and sexo != None:
        altura = float(altura)
        sexo = str(sexo)
       
        if sexo == 'F':
            se = 'Feminino' 
            peso = (62.1*altura) - 44.7
        elif sexo == 'M':
            se = 'Masculino'
            peso = (72.7*altura) - 58

    return f'O peso ideal para altura {altura} e sexo {se} é {peso:.2f}'

def ex14():
    pesagem = request.form.get('pesagem')
    vlmulta = request.form.get('vlmulta')

    if pesagem and vlmulta != None:
        pesagem = int(pesagem)
        vlmulta = float(vlmulta)

        if pesagem > 50:
            exesso = pesagem - 50
            vlmulta = exesso * vlmulta
            return f'Multa a pagar pelo exesso {vlmulta}'
        
        else:
            return 'Livre de multa pesagem menor que limite permitido'
