"""
# Exemplo de utilização de funções
cores = ['verde', 'amarelo', 'azul', 'branco']

# Utilizando a função integrada (Built-in) do Python print()
print(cores)

curso = 'Programação em Python: Essencial'
print(curso)

cores.append('roxo')
print(cores)

# curso.append('Mais dados...')  # AtributeError
# print(curso)

cores.clear()
print(cores)

# print(help(print))
# DRY - Don't Repeat Yourself - Não repita você mesmo / Não repita seu código.

# Mas então, como definir funções?

# Definindo a primeira função

# Exemplo 1
# Definição


def diz_oi():
    print('Oi!')

1 - Veja que, dentro das nossas funções podemos utilizar outras funções;
2 - Veja que nossa função só executa 1 tarefa, ou seja, a única coisa que ela faz é dizer oi;
3 - Veja que esta função não receber nenhum parâmetro de entrada;
4 - Veja que esta função não retorna nada

# Utilizando funções
# Chamada de execução
# diz_oi()

ATENÇÃO:
Nunca esqueça de utilizar o parênteses ao executar uma função.

Exemplo:
# Errado!
diz_oi

# Certo:
diz_oi()

# Exemplo 2


def cantar_parabens():
    print('Parabéns pra você')
    print('Nesta data querida')
    print('Muitas felicidades')
    print('Muitos anos de vida')
    print('Viva o aniversariante!')


for n in range(5):
    cantar_parabens()
"""