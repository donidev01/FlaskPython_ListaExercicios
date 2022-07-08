from flask import request


def ex001():
    n1 = request.form.get('n1')
    n2 = request.form.get('n2')
    if n1 and n2 != None:
       n1 = int(n1)
       n2 = int(n2)
    
       if n1 > n2:
            return f'Maior é {n1} e menor é {n2}'
       else:
            return f'Maior é {n2} e menor é {n1}'
