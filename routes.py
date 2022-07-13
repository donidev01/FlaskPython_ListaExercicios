
from flask import Flask, render_template, request

from src import funcionalidade, funcionalidadelst2

app=Flask(__name__)

@app.route("/")
#index lst1
@app.route("/index")
def index():
    return render_template("index.html")

#index lst2
@app.route("/indexlst2")
def indexlst2():
    return render_template("indexlst2.html")

#index lst3
@app.route("/indexlst3")
def indexlst3():
    return render_template("indexlst3.html")

#fim index(s)

# route exercicio 01 lst1
@app.route('/ex01')
def ex1():
    return render_template('ex01.html')

@app.route("/ex01", methods=["POST"])
def ex01():
    msg = funcionalidade.ex01()
    return render_template("ex01.html", msg=msg)

# route exercicio 02 lst1
@app.route('/ex02')
def ex2():
    return render_template('ex02.html')

@app.route('/ex02', methods=['POST'])
def ex02():
    numero = funcionalidade.ex02()
    return render_template('ex02.html', numero=numero)

# route exercicio 03 lst1
@app.route('/ex03')
def ex3():
    return render_template('ex03.html')

@app.route('/ex03', methods=['POST'])
def ex03():
    soma=funcionalidade.ex03()
    return render_template('ex03.html', soma=soma)

# route exercicio 04 lst1
@app.route('/ex04')
def ex4():
    return render_template('ex04.html')

@app.route('/ex04', methods = ['POST'])
def ex04():
    media = funcionalidade.ex04()
    return render_template('ex04.html', media=media)

# route exercicio 05 lst1
@app.route('/ex05')
def ex5():
    return render_template('ex05.html')

@app.route('/ex05', methods = ['POST'])
def ex05():
    medida = funcionalidade.ex05()
    return render_template('ex05.html', medida=medida)

# route exercicio 06 lst1
@app.route('/ex06')
def ex6():
    return render_template('ex06.html')

@app.route('/ex06', methods = ['POST'])
def ex06():
    area = funcionalidade.ex06()
    return render_template('ex06.html', area=area)

# route exercicio 07 lst1
@app.route('/ex07')
def ex7():
    return render_template('ex07.html')

@app.route('/ex07', methods=['POST'])
def ex07():
    area = funcionalidade.ex07()
    return render_template('/ex07.html', area=area)

# route exercicio 08 lst1
@app.route('/ex08')
def ex8():
    return render_template('ex08.html')

@app.route('/ex08', methods=['POST'])
def ex08():
    salario = funcionalidade.ex08()
    return render_template('/ex08.html', salario=salario)

# route exercicio 09 lst1
@app.route('/ex09')
def ex9():
    return render_template('ex09.html')

@app.route('/ex09', methods = ['POST'])
def ex09():
    temp = funcionalidade.ex09()
    return render_template('/ex09.html', temp=temp)

# route exercicio 10 lst1
@app.route('/ex10')
def ex_10():
    return render_template('ex10.html')

@app.route('/ex10', methods= ['POST'])
def ex10():
    temp = funcionalidade.ex10()
    return render_template('/ex10.html', temp=temp)

# route exercicio 11 lst1
@app.route('/ex11')
def ex_11():
    return render_template('ex11.html')

@app.route('/ex11', methods=['POST'])
def ex11():
    lst = funcionalidade.ex11()
    return render_template('/ex11.html', lst=lst)

# route exercicio 12 lst1
@app.route('/ex12')
def ex_12():
    return render_template('ex12.html')

@app.route('/ex12', methods=['POST'])
def ex12():
    peso = funcionalidade.ex12()
    return render_template('/ex12.html', peso=peso)

# route exercicio 13 lst1
@app.route('/ex13')
def ex_13():
    return render_template('ex13.html')

@app.route('/ex13', methods=['POST'])
def ex13():
    peso = funcionalidade.ex13()
    return render_template('/ex13.html', peso=peso)

# route exercicio 14 lst1
@app.route('/ex14')
def ex_14():
    return render_template('ex14.html')

@app.route('/ex14', methods = ['POST'])
def ex14():
    retorno = funcionalidade.ex14()
    return render_template('/ex14.html', retorno=retorno)

# route exercicio 15 lst1
@app.route('/ex15')
def ex_15():
    return render_template('ex15.html')

@app.route('/ex15', methods=['POST'])
def ex15():
    lst_menu = ['Vl_Hora, Qtd_horas Trabalhadas']
    lst = funcionalidade.ex15()
    return render_template('/ex15.html', lst=lst, lst_menu=lst_menu)

# route exercicio 16 lst1
@app.route('/ex16')
def ex_16():
    return render_template('ex16.html')

@app.route('/ex16', methods=['POST'])
def ex16():
    v = 'ValorTotal a pagar R$: '
    l = 'Quantidade Total de latas: '
    lst = funcionalidade.ex16()
    return render_template('/ex16.html', lst = lst, v=v, l=l)
# route exercicio 17 lst1
# route exercicio 18 lst1


#Rota exercicios lst2
# route exercicio 01 lst2
@app.route('/ex01lst2')
def ex01lst2():
    return render_template('ex01lst2.html')

@app.route('/ex01lst2', methods=['POST'])
def ex01lst_2():
    numero = funcionalidadelst2.ex001()
    return render_template('ex01lst2.html', numero=numero)

# route exercicio 02 lst2
@app.route('/ex02lst2')
def ex2lst():
    return render_template('ex02lst2.html')

@app.route('/ex02lst2', methods=['POST'])
def ex02lst2():
    msg1 = funcionalidadelst2.lst02ex02()
    return render_template('ex02lst2.html', msg1=msg1)

# route exercicio 03 lst2
@app.route('/ex03lst2')
def ex3lst2():
    return render_template('ex03lst2.html')

@app.route('/ex03lst2', methods=['POST'])
def ex03lst2():
    msg = funcionalidadelst2.lst02ex03()
    return render_template('ex03lst2.html', msg=msg)

# route exercicio 04 lst2
@app.route('/ex04lst2')
def ex4ls2():
    return render_template('ex04lst2.html')

@app.route('/ex04lst2', methods=['POST'])
def ex04lst2():
    letra = funcionalidadelst2.lst02ex04()
    return render_template('ex04lst2.html', letra=letra)

# route exercicio 05 lst2
@app.route('/ex05lst2')
def ex5lst2():
    return render_template('ex05lst2.html')

@app.route('/ex05lst2', methods=['POST'])
def ex05lst2():
    media = funcionalidadelst2.lst02ex05()
    return render_template('ex05lst2.html', media=media)

# route exercicio 06 lst2
@app.route('/ex06lst2')
def ex6lst2():
    return render_template('ex06lst2.html')

@app.route('/ex06lst2', methods=['POST'])
def ex06lst2():
    numero = funcionalidadelst2.lst02ex06()
    return render_template('ex06lst2.html', numero = numero)

# route exercicio 04 lst2
# route exercicio 04 lst2
# route exercicio 04 lst2
# route exercicio 04 lst2
# route exercicio 04 lst2
# route exercicio 04 lst2
# route exercicio 04 lst2
# route exercicio 04 lst2


if __name__=='__main__':
    app.run(debug=True)
