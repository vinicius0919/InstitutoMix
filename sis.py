from time import sleep
from zipfile import ZipFile
import PySimpleGUI as sg
from tkinter import filedialog, messagebox
import os
import re
import webbrowser

#DEFININDO O TEMA
sg.theme('Reds')

def atualizarLink(link):
    with open('sisloglink.txt', 'w', encoding='utf-8') as arquivo:
        arquivo.write(link)

def lerLink():
    with open('sisloglink.txt', 'r', encoding='utf-8') as arquivo:
        link = arquivo.read()
        return link

#BAIXA O ARQUIVO SISLOG 
def baixarIsi():
    link = lerLink()
    webbrowser.open(link)
    
#EXTRAI O ARQUIVO SISLOG NA PASTA PROGRAM DATA
def extrairMover():
    caminho = r'C:\ProgramData\Interativo2017'
    nomeCompactado = filedialog.askopenfilename()
    nomeArquivo = r'sislog.isi'
    
    with ZipFile(nomeCompactado, 'r') as file:
        file.extractall()
    caminhoInstalador = os.getcwd()
    arquivos = os.listdir()
    try:
        if nomeArquivo in arquivos:
            os.rename(f'{nomeArquivo}', f'{caminho}\{nomeArquivo}')
    except:
        os.chdir(caminho)
        os.remove(nomeArquivo)
        os.chdir(caminhoInstalador)
        arquivos = os.listdir()
        if nomeArquivo in arquivos:
            os.rename(f'{nomeArquivo}', f'{caminho}\{nomeArquivo}')



#MUDANDO O LINK DE DOWNLOAD
def escreverSis():
    
    layout = [
    [sg.Text("Insira o novo Link:")],
    [sg.InputText(key="texto_link")],
    [sg.Button("Confirmar"), sg.Button("Cancelar")],
    [sg.Text("", key="texto_desejado")],
]

    janela = sg.Window("Instituto Mix", layout)

    while True:
        evento, valores = janela.read()
        if evento == sg.WIN_CLOSED or evento == "Cancelar":
            break
        if evento == "Confirmar":
            link = valores["texto_link"]
            atualizarLink(link)
            break
    janela.close()

#FUNÇÃO PRINCIPAL SISLOG
def sisPrincipal():
    telaInicial = [
        [sg.Text("O que deseja fazer?")],
        [sg.Button("Atualizar Link de Download"),sg.Button("Baixar Sislog")], [sg.Button("Cancelar")]
        ]

    janela = sg.Window("INSTITUTO MIX", telaInicial, finalize=True, right_click_menu=sg.MENU_RIGHT_CLICK_EDITME_VER_EXIT)

    while True:
        evento, valores = janela.read()
        if evento == sg.WIN_CLOSED or evento == "Cancelar":
            break
        if evento == "Atualizar Link de Download":
            try:
                escreverSis()
                break
            except:
                messagebox.showerror('INSTITUTO MIX - ERRO', 'LINK NÃO ENCONTRADO\nCERTIFIQUE-SE DE INSERIR O TEXTO CORRETO')
                break
        if evento == "Baixar Sislog":
            try:
                baixarIsi()
                sleep(5)
                extrairMover()
                break
            except:
                messagebox.showerror('INSTITUTO MIX - ERRO', 'LINK NÃO ENCONTRADO\nCERTIFIQUE-SE DE INSERIR O TEXTO CORRETO')
                break
        janela.close()
