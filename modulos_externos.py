"""
Módulos Externos

Utilizamos o gerenciador de pacotes Python chamado Pip - Python Installer Package

Você pode conhecer todos os pacotes externos oficiais em: https://pypi.org

colorama -> É utilizado para permitir impressão de textos coloridos no terminal.

Instalando um módulo:

pip install (nome do módulo)

# Instalando o pacote colorama

pip install colorama

# Utilizando o pacote instalado

from colorama import init, Fore

init()

print(Fore.MAGENTA + 'Geek University')
print(Fore.BLUE + 'Geek University')

# Python PDF

import pydf

pdf = pydf.generate_pdf('<h1>Geek University</h1><br><br><strong>Programa&ccedil;&atilde;&o em Python: Essencial</strong>')

with open('test_doc.pdf', 'wb') as f:
    f.write(pdf)
"""