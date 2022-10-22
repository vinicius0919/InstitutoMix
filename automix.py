import PySimpleGUI as sg
import main
import sis
from time import sleep
from tkinter import messagebox

resposta = True
telaInicial = [
    [sg.Text("O que deseja fazer?")],
    [sg.Text("As funções de Habilitar Online e Configurar os Gerenciador são experiementais e necessitam que a configuração da resolução esteja em HD(1280 x 720)")],
    [sg.Button("Instalar Aplicativos"),sg.Button("Conectar Interativo no Banco"),
     sg.Button("Baixar Sislog"), sg.Button("Exibir Módulos do Cursos")],
     [sg.Button("Habilitar Online - Sistema Interativo"), sg.Button("Configurar Gerenciador")], [sg.Button("Cancelar")]
    ]

janela = sg.Window("INSTITUTO MIX", telaInicial, finalize=True, right_click_menu=sg.MENU_RIGHT_CLICK_EDITME_VER_EXIT)

while resposta == True:    
    
    while True:
        evento, valores = janela.read()
        if evento == sg.WIN_CLOSED or evento == "Cancelar":
            break
        if evento == "Baixar Sislog":
            sis.sisPrincipal()
            break
        if evento == "Instalar Aplicativos":
            main.abrir()
            break
        if evento == "Exibir Módulos do Cursos":
            main.exibirModulos()
            break
        if evento == "Conectar Interativo no Banco":
            main.habilitar()
            break
        if evento == "Habilitar Online - Sistema Interativo":
            main.habOnline()
            break
        if evento == "Configurar Gerenciador":
            main.gerenciadorAt()
            break
        janela.close()
    resposta = messagebox.askyesno("INSTITUTO MIX", "DESEJA REALIZAR UMA NOVA EXECUÇÃO?")
