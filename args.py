"""
# Exemplos


def soma_todos_numeros(num1=1, num2=2, num3=3, num4=4):
    return num1 + num2 + num3 + num4


print(soma_todos_numeros(4, 6, 9))

print(soma_todos_numeros(4, 6))
print(soma_todos_numeros(4, 6, 9, 5))

# Entendendo o args


def soma_todos_numeros(nome, email, *args):
    return sum(args)


soma_todos_numeros('Angelina', 'Jolie')
soma_todos_numeros('Angelina', 'Jolie', 1)
soma_todos_numeros('Angelina', 'Jolie', 2, 3)
soma_todos_numeros('Angelina', 'Jolie', 2, 3, 4)
soma_todos_numeros('Angelina', 'Jolie', 3, 4, 5, 6)


# Outro exemplo de utilização do *args


def verifica_info(*args):
    if 'Geek' in args and 'University' in args:
        return 'Bem-Vindo Geek!'
    return 'Eu não tenho certeza quem você é ...'


print(verifica_info())
print(verifica_info(1, True, 'University', 'Geek'))
print(1, 'University', 3.145)


def soma_todos_numeros(*args):
    return sum(args)


print(soma_todos_numeros())
print(soma_todos_numeros(3, 4, 5, 6))

numeros = [1, 2, 3, 4, 5, 6, 7]

# Desempacotador
print(soma_todos_numeros(*numeros))

# O asterisco serve para que informemos ao Python que estamos passando como argumento uma coleção de dados.
# Desta forma, ele saberá que precisará antes desempacotar estes dados.
"""