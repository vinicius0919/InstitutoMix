import os
from tkinter import filedialog
from zipfile import ZipFile
import PySimpleGUI as sg
import limpar
import pyautogui
import time

sg.theme('Reds')
#PERGUNTA PARA O USUÁRIO QUAL O ARQUIVO QUE DESEJA MOVER
def mover():
    caminho1 = filedialog.askdirectory()
    caminho2 = filedialog.askdirectory()
    os.chdir(caminho1)
    lista_arquivos = os.listdir(os.getcwd())
    for arquivo in lista_arquivos:
        if ".csv" in arquivo:
            os.rename(f"{arquivo}",f"{caminho2}/{arquivo}" )
def mover2(nome):
    caminho1 = filedialog.askdirectory()
    caminho2 = filedialog.askdirectory()
    os.chdir(caminho1)
    lista_arquivos = os.listdir(os.getcwd())
    for arquivo in lista_arquivos:
        if nome in arquivo:
            os.rename(f"{arquivo}",f"{caminho2}/{arquivo}" )

#ABRE OS INSTALARADORES (ARQUIVOS MSI)            
def abrir():
    caminho = os.getcwd()
    caminho = limpar.limpar(caminho)
    caminho = os.path.join(caminho,r'Apps')
    os.chdir(caminho)
    nome = os.listdir()
    
    layout = [
    [sg.Button("Sistema Interativo"), sg.Button("Gerenciador"), sg.Button("Todos"),sg.Button("Cancelar")],
]

    janela = sg.Window("O que deseja Instalar?", layout)

    while True:
        evento, valores = janela.read()
        if evento == sg.WIN_CLOSED or evento == "Cancelar":
            break
        if evento == "Sistema Interativo":
            os.startfile(f'{caminho}\{nome[1]}')
            break
        if evento == "Gerenciador":
            os.startfile(f'{caminho}\{nome[0]}')
            break
        if evento == "Todos":
            for i in range(2):
                os.startfile(f'{caminho}\{nome[i]}')
            break
    janela.close()
    

#ABRE O SISTEMA INTERATIVO E FAZ A HABILITAÇÃO ON-LINE
def habilitar():
    caminho = r'C:\ProgramData\Interativo2017'
    nomeArquivo = 'config.ini'
    nomeCompactado = 'config.zip'
    
    local = os.getcwd()
    local = limpar.limpar(local)
    caminhoOrigem = f'{local}\configs'
    os.chdir(caminhoOrigem)
    arquivos = os.listdir()
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

def exibirModulos():
    local = os.getcwd()
    local = limpar.limpar(local)
    os.startfile(local+r'\templates\teste.html')
    
    
    
def extrairMoverModulos():
    caminho = r'C:\ProgramData\Interativo2017'
    nomeCompactado = filedialog.askopenfilename()
    print(nomeCompactado)


def habOnline720():
    #os.startfile(r'C:\Program Files (x86)\Sistema Interativo\Sistema Interativo 3.1.3\Interativo 3.1.3.exe')
    pyautogui.press('win')
    pyautogui.sleep(0.5)
    pyautogui.write('Interativo 3.1.3.exe')
    pyautogui.press('backspace')
    pyautogui.press('enter')
    time.sleep(40)
    pyautogui.moveTo(737,321)
    pyautogui.click()
    time.sleep(1)
    pyautogui.write('admin')
    pyautogui.moveTo(737, 400)
    pyautogui.click()
    time.sleep(1)
    pyautogui.write('123456')
    pyautogui.moveTo(797,488)
    time.sleep(0.5)
    pyautogui.click()
    time.sleep(1)
    pyautogui.moveTo(328,291)
    pyautogui.click()
    time.sleep(0.5)
    pyautogui.moveTo(513,307)
    pyautogui.click()
    time.sleep(0.5)
    pyautogui.hotkey('ctrl', 'a')
    time.sleep(0.5)
    pyautogui.write('1272nh786NEMix')
    time.sleep(0.5)
    pyautogui.moveTo(845,544)
    pyautogui.click()
def habOnline1080():
    #os.startfile(r'C:\Program Files (x86)\Sistema Interativo\Sistema Interativo 3.1.3\Interativo 3.1.3.exe')
    pyautogui.press('win')
    pyautogui.sleep(0.5)
    pyautogui.write('Interativo 3.1.3.exe')
    pyautogui.press('backspace')
    pyautogui.press('enter')
    time.sleep(40)
    pyautogui.moveTo(1066,507)
    pyautogui.click()
    time.sleep(1)
    pyautogui.write('admin')
    pyautogui.moveTo(1066, 580)
    pyautogui.click()
    time.sleep(1)
    pyautogui.write('123456')
    time.sleep(1)
    pyautogui.moveTo(1135,663)
    time.sleep(0.5)
    pyautogui.click()
    pyautogui.moveTo(624,480)
    pyautogui.click()
    time.sleep(0.5)
    pyautogui.moveTo(750,480)
    pyautogui.click()
    time.sleep(0.5)
    pyautogui.hotkey('ctrl', 'a')
    time.sleep(0.5)
    pyautogui.write('1272nh786NEMix')
    time.sleep(0.5)
    pyautogui.moveTo(1158,719)
    pyautogui.click()
def gerenciadorAt():
    #os.startfile(r'C:\Program Files (x86)\Sistema Interativo\Gerenciador de Alunos 3.0\Gerenciador de Alunos.exe')
    pyautogui.press('win')
    pyautogui.sleep(0.5)
    pyautogui.write('Gerenciador de Alunos.exe')
    pyautogui.press('backspace')
    pyautogui.press('enter')
    time.sleep(30)
    pyautogui.moveTo(758,275)
    time.sleep(0.5)
    pyautogui.click()
    pyautogui.write(r'C:\IM01\Interativo2017egistros3.sqlite')
    pyautogui.moveTo(788,469)
    time.sleep(0.5)
    pyautogui.click()

#time.sleep(4)
#print(pyautogui.position())