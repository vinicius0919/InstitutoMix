import os
import re

def limpar(caminho):
    padrao1 = re.compile(r'\\Apps')
    padrao2 = re.compile(r'\\configs')
    caminho = os.getcwd()
    if r'\Apps' in caminho:
        caminho = re.sub(padrao1, '', caminho)
    elif r'\configs' in caminho:
        caminho = re.sub(padrao2, '', caminho)
        
    return caminho