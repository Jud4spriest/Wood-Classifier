# -*- coding: utf-8 -*-
"""
Created on Sun Feb 27 14:35:34 2022

@author: mazev
"""

# Hello World ------------------------

import io
import os
import PySimpleGUI as sg
from PIL import Image

sg.theme('DarkAmber')

file_types = [("JPEG (*.jpg)", "*.jpg"),
              ("All files (*.*)", "*.*")]

def createColumn(elements,x,y):
    col = sg.Column(
        [[sg.Frame('', [[sg.Column(elements,expand_x=True,background_color='gray',element_justification='center',justification='center', pad=(0, 0))]],size=(x, y),border_width=1)]])
    return col

def openImage(img,x,y):
    image = Image.open(img)
    image.thumbnail((x, y))
    bio = io.BytesIO()
    image.save(bio, format="PNG")
    print(type(image))
    print(type(bio))
    return

# def openImage(img,x,y):
#     image = Image.open(img)
#     image.thumbnail((x, y))
#     bio = io.BytesIO()
#     image.save(bio, format="PNG")
#     return image

def init_window():
    
    coluna_layout = [   
        [sg.Text("Escolha um diretório para leitura das imagens")],
        [sg.Text("Diretório:"),sg.In(size=(25, 1), enable_events=True, key="-FILE-"), sg.FileBrowse(file_types=file_types)],
        [sg.Button('Sair'),sg.Button('Ok')]
        ]
    
    layout = [[sg.Column(coluna_layout, element_justification='center')]]
        
    init_window = sg.Window('Classificador de Madeira', layout, finalize=True, grab_anywhere=True)
    while True:
        event, values = init_window.read()
        if event == "Sair" or event == sg.WIN_CLOSED:
            break
        elif event == "Ok":
            # filename = values["-FILE-"]
            filename = "C:/Users/mazev/Downloads/defeitos-por-milhao.jpg"
            main_window(filename)
            break
    init_window.close()
    return

a = b = cM = cm = d = 0
total = a+b+cM+cm+d

def main_window(filename):

    size_frame_x = 600
    size_frame_y = 200

    col1 = createColumn([[sg.Text("Nós")], [sg.Text("Classe:")]], size_frame_x, size_frame_y)
    col2 = createColumn([[sg.Image(key="-IMAGE-")]], size_frame_x, size_frame_y)

    col3 = createColumn([[sg.Text("Estatísticas",expand_x=True,justification='center')],
                                                 [sg.Text("Total: "+ str(total))],
                                                 [sg.Column([[sg.Column([[sg.Text("Tipo A: "+str(a))]]),
                                                 sg.Column([[sg.Text("Tipo B: "+str(b))]]),
                                                 sg.Column([[sg.Text("Tipo C+: "+str(cM))]]),
                                                 sg.Column([[sg.Text("Tipo C-: "+str(cm))]]),
                                                 sg.Column([[sg.Text("Tipo D: "+str(d))]])]],expand_x=True,element_justification='center')],
                                                 [sg.Button('Load Image')]], size_frame_x, size_frame_y)

    col4 = createColumn([[sg.Image(key="-IMAGE2-")]], size_frame_x, size_frame_y)
    col5 = createColumn([[sg.Image(key="-IMAGE3-")]], size_frame_x, size_frame_y)
    col6 = createColumn([[sg.Image(key="-IMAGE4-")]], size_frame_x, size_frame_y)

    col7 = sg.Column([[sg.Button("Iniciar"),sg.Button("Parar")]],element_justification='center',justification='center')
    # ----- layout -----
    
    layout = [[col1, col2],
              [col3, col4],
              [col5, col6],
              [col7]]
    
    # layout = [
    #     [
    #         sg.Column(file_list_column,element_justification='center'),
    #         sg.VSeperator(k='c'),
    #         sg.Column(image_viewer_column),
    #     ]
    # ]
    
    # Window
    
    main_window = sg.Window(title="Classificador de Madeira", layout=layout, resizable=True, grab_anywhere=True) # margins=(200, 100)
    
    
    # Eventos 
    
    while True:
        event, values = main_window.read()
        if event == "Exit" or event == sg.WIN_CLOSED:
            break
        if event == "Load Image":
            # filename = values["-FILE-"]
            if os.path.exists(filename):
                main_window["-IMAGE-"].update(size=(300,200), data=openImage(filename,size_frame_x,size_frame_y))
                main_window["-IMAGE2-"].update(data=openImage(filename,size_frame_x,size_frame_y))
                main_window["-IMAGE3-"].update(data=openImage(filename,size_frame_x,size_frame_y))
                main_window["-IMAGE4-"].update(data=openImage(filename,size_frame_x,size_frame_y))


    main_window.close()



if __name__ == "__main__":
    # init_window()
    main_window("C:/Users/mazev/Downloads/defeitos-por-milhao.jpg")



# window.close()