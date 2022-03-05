# -*- coding: utf-8 -*-
"""
Created on Sun Feb 27 14:35:34 2022
@author: Marcos Azevedo (judaspriest)
"""

# ------------------- Setup --------------------
import io
import os
import PySimpleGUI as sg
from PIL import Image

sg.theme('DarkTanBlue')

# file_types = [("JPEG (*.jpg)", "*.jpg"),
#               ("All files (*.*)", "*.*")]

# ------------------- Variaveis Globais --------------------
font = ("Arial, 11")
SIZE_FRAME_X = 600
SIZE_FRAME_Y = 200
folder = ''
a = b = c = 0                           # Variaveis que receberão os dados da identificação
total = a+b+c                           # Função a trabalhar.

# ------------------- Funções --------------------
def createColumn(elements,x,y):
    col = sg.Column(
        [[sg.Frame('', [[sg.Column(elements,expand_x=True,element_justification='center',justification='center', pad=(0, 0))]],size=(x, y),border_width=1,font=font)]])
    return col

def openImage(img,x,y):
    image = Image.open(img)
    image.thumbnail((x, y))
    bio = io.BytesIO()
    image.save(bio, format="PNG")
    return bio.getvalue()

# ------------------- Janelas do programa ------------------
def setup_window():
    global folder
    firstime = False

    coluna_layout = [   
        [sg.Text("Escolha um diretório para leitura das imagens:")],
        [sg.Text("Diretório:"),sg.In(size=(25, 1), enable_events=True, key="-FOLDER-"), sg.FolderBrowse()],
        [sg.Button('Ok',s=(5,1),disabled=True)]
        ]
    
    layout = [[sg.Column(coluna_layout, element_justification='center')]]
    setup_window = sg.Window('Classificador de Madeira', layout, keep_on_top=True, finalize=True, grab_anywhere=True)

    while True:
        event, values = setup_window.read()
        if event == sg.WIN_CLOSED:
            break
        elif event == "-FOLDER-":
            if folder == '': firstime = True
            else: firstime = False
            folder = values["-FOLDER-"]
            if os.path.isdir(folder):
                setup_window['Ok'].update(disabled=False)
        elif event == "Ok":
            if firstime:
                setup_window.close()
                main_window()
            break
    setup_window.close()

def main_window():

    # ----- variaveis -----
    x = SIZE_FRAME_X
    y = SIZE_FRAME_Y
    nnos = 0                 # (Variáveis a receber da identificação)
    classe = 'Nenhum'        # (Variáveis a receber da identificação)

    # ----- frames -----
    col1 = createColumn([[sg.Text('Capa Atual',expand_x=True,background_color='#005e80',justification='c',)],
                         [sg.Column([[sg.Column([[sg.Text("Número de Nós: "+str(nnos))]]), sg.Column([[sg.Text("Classe: "+classe)]])]],expand_x=True,element_justification='center')],
                         [sg.Text('Estatísticas Gerais',expand_x=True,background_color='#005e80',justification='c',)],

                         [sg.Column([[sg.Column([[sg.Text("Tipo A: "+str(a))]]),
                                      sg.Column([[sg.Text("Tipo B: "+str(b))]]),
                                      sg.Column([[sg.Text("Tipo C: "+str(c))]])]],expand_x=True,element_justification='center')],
                         [sg.Text("Total de Capas: " + str(total))],
                         [sg.Button('Configurações')]], x, y)
    col2 = createColumn([[sg.Image(key="-IMAGE-")]], x, y)
    col3 = createColumn([[sg.Image(key="-IMAGE1-")]], x, y*2)
    col4 = sg.Column([[createColumn([[sg.Image(key="-IMAGE2-")]], x, y)],[createColumn([[sg.Image(key="-IMAGE3-")]], x, y)]])
    # col4 = createColumn([[sg.Image(key="-IMAGE2-")]], x, y)
    # col5 = createColumn([[sg.Image(key="-IMAGE3-")]], x, y)
    # col6 = createColumn([[sg.Image(key="-IMAGE4-")]], x, y)
    col7 = sg.Column([[sg.Button("Iniciar",s=(10,1),disabled=False),sg.Button("Parar",s=(10,1),disabled=True)]],element_justification='center',justification='center')

    # ----- layout -----
    layout = [[col1, col2],
              [col3, col4],
              [col7]]
    #
    # layout_old = [[col1, col2],
    #           [col3, col4],
    #           [col5, col6],
    #           [col7]]

    # ----- window -----
    main_window = sg.Window(title="Classificador de Madeira", layout=layout, grab_anywhere=True) # margins=(200, 100), resizable=True

    # ----- event loop -----
    while True:
        event, values = main_window.read()
        if event == "Exit" or event == sg.WIN_CLOSED:
            break
        elif event == "Configurações":
            setup_window()
        elif event == "Iniciar":                                     # Gatilho para iniciar a identificação em tempo real
            main_window['Iniciar'].update(disabled=True)
            main_window['Parar'].update(disabled=False)
        elif event == "Parar":                                       # Gatilho para parar a identificação.
            main_window['Iniciar'].update(disabled=False)
            main_window['Parar'].update(disabled=True)



        elif event == "Load Image":
            filename = values["-FILE-"]
            # if os.path.exists(filename):
            #     # window["-IMAGE-"].update(filename=filename)
            #     main_window["-IMAGE-"].update(data=openImage(filename,size_frame_x,size_frame_y))
            #     main_window["-IMAGE2-"].update(data=openImage(filename,size_frame_x,size_frame_y))
            #     main_window["-IMAGE3-"].update(data=openImage(filename,size_frame_x,size_frame_y))
            #     main_window["-IMAGE4-"].update(data=openImage(filename,size_frame_x,size_frame_y))
    main_window.close()

# ------------------ void main ---------------------------
if __name__ == "__main__":
    # setup_window()
    main_window()