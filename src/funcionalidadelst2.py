from ast import Return

from flask import request


# funcionalidade01
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
# funcionalidade02
def lst02ex02():
     n1 = request.form.get('n1')
     if n1 != None:
          n1 = int(n1)
          if n1 < 0:
               return 'Numero é NEGATIVO'
          else:
               return   'Numero é POSITIVO'
# funcionalidade03
def lst02ex03():
     letra = request.form.get('letra')
     if letra != None:
          letra = letra.upper()
          if letra == 'F':
               return 'FEMININO'
          else:
               return 'MASCULINO'
# funcionalidade04
def lst02ex04():
     lst_vogais = ['A','E','I','O','U']
     letra = request.form.get('letra')
     if letra != None:
          letra = letra.upper()

          if letra in lst_vogais:
               return 'É Vogal'
          else:
               return 'Não é vogal'
# funcionalidade05
def lst02ex05():
     n1 = request.form.get('n1')
     n2 = request.form.get('n2')
     if n1 and n2 != None:
          n1 = float(n1)
          n2 = float(n2)
          media = (n1 + n2) / 2
          if media == 10:
               return f'Media obtida {media} Aluno aprovado com distinção'
          elif media >= 7:
               return f'Media obtida {media} Aluno aprovado'
          elif media < 7:
               return f'Media obtida {media} Aluno reprovado'
# funcionalidade06
def lst02ex06():
     n1 = request.form.get('n1')
     n2 = request.form.get('n2')
     n3 = request.form.get('n3')
     if n1 and n2 and n3 != None:
          n1 = int(n1)
          n2 = int(n2)
          n3 = int(n3)
          #teste = max(n1,n2,n3) é uma possibilidade
          if n1 > n2 and n1 > n3:
               return f'Numero maior é {n1}'

          elif n2 > n3 and n2 > n1:
               return f'Numero maior é {n2}'

          elif n3 > n2 and n3 > n1:
               return f'Numero maior é {n3}'

# funcionalidade07
   
def lst02ex07():
     lst = []
     n1 = request.form.get('n1')
     n2 = request.form.get('n2')
     n3 = request.form.get('n3')
     if n1 and n2 and n3 != None:
          
          if n1 > n2 and n1 > n3:
               if n2 > n3:
                    return f'Numero maior111 é {n1} numero menor {n3}'
               else:
                    return f'Numero222 maior é {n1} numero menor {n2}'

          elif n2 > n3 and n2 > n1:
               if n3 > n1:
                    return f'Numero maior é {n2} numero menor {n1}'
               else:
                    return f'Numero maior é {n2} numero menor {n3}'

          elif n3 > n2 and n3 > n1:
               if n1 > n2:
                    return f'Numero maior é {n3} numero menor {n2}'
               else:
                    return f'Numero maior é {n3} numero menor {n1}'


