import os

print(os.getcwd())  # C:\Users\Caio\PycharmProjects\exemplo_aulas

res = os.path.join(os.getcwd(), 'geek', 'university')

os.chdir(res)

print(os.getcwd())  # C:\Users\Caio\PycharmProjects\exemplo_aulas\geek\university

# Veja que o os.path.join() recebe dois parâmetros, sendo o primeiro o diretório atual e o segundo o diretório que
# será juntado ao atual.
