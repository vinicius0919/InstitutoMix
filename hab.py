import time
import main
import PySimpleGUI as sg
from tkinter import messagebox
import pyautogui
def interfaceHab():
    telaInicial = [
        [sg.Text("Selecione a resolução da sua tela")],
        [sg.Text("As funções de Habilitar Online e Configurar os Gerenciador são experiementais e necessitam que a configuração da resolução esteja em HD(1280 x 720)")],
        [sg.Text("ou FULL HD (1920 X 1080) com a escala em 100%")],
        [sg.Text("ATENÇÃO: \nO programa irá esperar 40 segundos para abrir os aplicativos")],
        [sg.Text("Não mova o mouse durante o processo!")],
        [sg.Button("FULL HD (1920 X 1080)"),sg.Button("HD (1280 x 720)")]
        ]
    
    janela = sg.Window("INSTITUTO MIX", telaInicial, finalize=True, right_click_menu=sg.MENU_RIGHT_CLICK_EDITME_VER_EXIT)
    
        
    while True:
        evento, valores = janela.read()
        if evento == sg.WIN_CLOSED or evento == "Cancelar":
            break
        if evento == "FULL HD (1920 X 1080)":
            main.habOnline1080()
            break
        if evento == "HD (1280 x 720)":
            main.habOnline720()
            break
        
        janela.close()