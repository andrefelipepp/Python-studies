### Operadores aritméticos

# Esses operadores permitem realizar operações matemáticas:

# Adição: 2 + 3 = 5
soma = 2 + 3 # operador: +

# Subtração: 5 - 2 = 3
subtracao = 5 - 2 # operador: -

# Multiplicação: 3 * 4 =  12
multiplicacao = 3 * 4 # operador: *

# Divisão: 10 / 2 = 5
divisao = 10 / 2 # operador: /

# Divisão Inteira: 10 // 3 = 3
divisaoInteira = 10 // 3 # operador: //

# Módulo ou Resto: 10 % 3 = 1
resto = 10 % 3 # operador: %

# Potência: 2 ** 3 = 8
potencia = 2 ** 3 # operador: **

print("Operadores Aritméticos: ")
print(soma)
print(subtracao)
print(multiplicacao)
print(divisao)
print(divisaoInteira)
print(resto)
print(potencia)
print("              ")

# ### Operadores relacionais
# Esses operadores comparam valores e retornam `True` ou `False`:

# Igual: 5 == 5 = True
igual = 5 == 5 # operador: ==

# Diferente: 5 != 3 = True
diferente = 5 != 3 # operador: !=

# Maior que: 5 > 3 = True
MaiorQue = 5 > 3 # operador: >

# Menor que: 2 < 4 = True
MenorQue = 9 < 4 # operador: <

# Maior ou Igual: 8 >= 8 = True
MaiorIgual = 4 >= 8 # operador: >=

# Menor ou Igual: 3 <= 5 = True
MenorIgual = 3 <= 5 # operador: <=

print("Operadores Relacionais: ")
print(igual)
print(diferente)
print(MaiorQue)
print(MenorQue)
print(MaiorIgual)
print(MenorIgual)
print("                ")


# Operadores Lógicos
# São usados para combinar expressões:

print("Operadores Lógicos: ")
# E:  True and True = True
    # True and False = False
    # False and False = False
print(True and True)
print(True and False)
print(False and False)

# Ou: True and True = True
    # True and False = True
    # False and False = False
print(True or True)
print(True or False)
print(False or False)

# Não: not True = False
    #  not false = True
print(not True)
print(not False)

# 💡 Pense nos operadores como sinais de trânsito 🚦. 
# Eles orientam como o fluxo do seu código deve prosseguir, 
# baseando-se nas condições que você estabelece.