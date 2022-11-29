"""
OBS: Lambda são funções sem nome, que podem ou não receber parâmetros de entrada e retornar valores.

# Fazendo import
from collections import defaultdict
dicionario = defaultdict(lambda: 0)
dicionario['curso'] = 'Programação em Python: Essencial'
print(dicionario)
print(dicionario['outro'])  # KeyError no dicionário comum, mas aqui não
print(dicionario)
"""