
from flask import Flask, render_template, request

from src import funcionalidade

app=Flask(__name__)

@app.route("/")
@app.route("/index")
def index():
    return render_template("index.html")

@app.route('/ex01')
def ex1():
    return render_template('ex01.html')

@app.route("/ex01", methods=["POST"])
def ex01():
    msg = funcionalidade.ex01()
    return render_template("ex01.html", msg=msg)


@app.route('/ex02')
def ex2():
    return render_template('ex02.html')

@app.route('/ex02', methods=['POST'])
def ex02():
    numero = funcionalidade.ex02()
    return render_template('ex02.html', numero=numero)

@app.route('/ex03')
def ex3():
    return render_template('ex03.html')

@app.route('/ex03', methods=['POST'])
def ex03():
    soma=funcionalidade.ex03()
    return render_template('ex03.html', soma=soma)

@app.route('/ex04')
def ex4():
    return render_template('ex04.html')

@app.route('/ex04', methods = ['POST'])
def ex04():
    media = funcionalidade.ex04()
    return render_template('ex04.html', media=media)

@app.route('/ex05')
def ex5():
    return render_template('ex05.html')

@app.route('/ex05', methods = ['POST'])
def ex05():
    medida = funcionalidade.ex05()
    return render_template('ex05.html', medida=medida)

@app.route('/ex06')
def ex6():
    return render_template('ex06.html')

@app.route('/ex06', methods = ['POST'])
def ex06():
    area = funcionalidade.ex06()
    return render_template('ex06.html', area=area)


@app.route('/ex07')
def ex7():
    return render_template('ex07.html')

@app.route('/ex07', methods=['POST'])
def ex07():
    area = funcionalidade.ex07()
    return render_template('/ex07.html', area=area)

@app.route('/ex08')
def ex8():
    return render_template('ex08.html')

@app.route('/ex08', methods=['POST'])
def ex08():
    salario = funcionalidade.ex08()
    return render_template('/ex08.html', salario=salario)

@app.route('/ex09')
def ex9():
    return render_template('ex09.html')

@app.route('/ex09', methods = ['POST'])
def ex09():
    temp = funcionalidade.ex09()
    return render_template('/ex09.html', temp=temp)

@app.route('/ex10')
def ex_10():
    return render_template('ex10.html')

@app.route('/ex10', methods= ['POST'])
def ex10():
    temp = funcionalidade.ex10()
    return render_template('/ex10.html', temp=temp)

@app.route('/ex11')
def ex_11():
    return render_template('ex11.html')

@app.route('/ex11', methods=['POST'])
def ex11():
    lst = funcionalidade.ex11()
    return render_template('/ex11.html', lst=lst)

@app.route('/ex12')
def ex_12():
    return render_template('ex12.html')

@app.route('/ex12', methods=['POST'])
def ex12():
    peso = funcionalidade.ex12()
    return render_template('/ex12.html', peso=peso)

@app.route('/ex13')
def ex_13():
    return render_template('ex13.html')

@app.route('/ex13', methods=['POST'])
def ex13():
    peso = funcionalidade.ex13()
    return render_template('/ex13.html', peso=peso)

@app.route('/ex14')
def ex_14():
    return render_template('ex14.html')

@app.route('/ex14', methods = ['POST'])
def ex14():
    retorno = funcionalidade.ex14()
    return render_template('/ex14.html', retorno=retorno)

if __name__=='__main__':
    app.run(debug=True)
