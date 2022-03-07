# -*- coding: utf-8 -*-
"""
Created on Sun Feb 27 14:35:34 2022
@author: Marcos Azevedo (judaspriest)
"""
import errno
import threading

"""------------------- Setup -------------------- """
import io
import os
import time
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, FigureCanvasAgg
from matplotlib.figure import Figure
from random import randint
import PySimpleGUI as sg
from threading import Thread,Event
from PIL import Image, ImageTk

import teste_integracao_interface

sg.theme('DarkTanBlue')

# file_types = [("JPEG (*.jpg)", "*.jpg"),
#               ("All files (*.*)", "*.*")]

""" ------------------- Variaveis Globais -------------------- """
font = ("Any, 11")
SIZE_FRAME_X = 600
SIZE_FRAME_Y = 200
folder = ''

scatter = 'scatter.png'                            # path do scatter
hist = 'hist.png'
color = 'color.png'
pb = 'pb.png'

list = ['b.png','c.png']

"""-------------------- Classes ------------------- """
#
class Identificacao(Thread):
    def __init__(self, target, intervalo, name='Thread_identificacao'):
        super().__init__()
        self.name = name
        self._target = target
        self._finished = Event()
        self.daemon = True
        # self._stoped = False
        """Custom Atributos"""
        # self.flag = True
        self._nos = 0
        self._classe = ''
        # self.results = []
        self._intervalo = intervalo
        self._count = 0
        print(self.name, 'criada')

    def run(self):
        # while self.flag:
        print(self.name, 'iniciada')
        while not self._finished.is_set():
            # if self._finished.is_set(): return
            self._nos, self._classe,_,_,_,_ = self._target(list[self._count])          #Criar uma variavel só (results) #Teoricamente eu garanto que há dados para identificar.
            self._count += 1
            time.sleep(self._intervalo)
        # self._stoped = True
        print(self.name, 'destruida')

    def shutdown(self):
        # self.flag = False
        self._finished.set()
        print(self.name, 'Desativada')

    def contagemDados(self):
        return self._count

    def retornaDados(self):
        # return self.results
        return self._nos, self._classe

    def join(self):
        # self.flag = False
        pass

def thread_identif(img):
    return teste_integracao_interface.testeIntegracao(img)         #Aqui vai a função de identificação (setado como teste)
    # return main_function_identification


# class Cronometro(Thread):
#     def __init__(self, target, window, value,name='CronoThread'):
#         super().__init__()
#         self.name = name
#         self._target = target
#         self.window = window
#         self.value = value
#         self.daemon = True
#         self._stoped = False
#         self.time = 0
#         self.flag = True
#         print(self.name, 'começou')
#
#     def run(self):
#         startTime = time.time()
#         while self.flag:
#             self.time = time.time() - startTime
#             self.exibe()
#             time.sleep(0.01)
#         self._stoped = True
#
#     def exibe(self):
#         self.window[self.value].update('Tempo de execução: ' + str(round(self.time, 2)) + ' seg')
#         self._target(self.window)
#
#     def stop(self):
#         self.flag = False
#
#     def timer(self):
#         return self.time
#
#     def join(self):
#         self.flag = False
#         pass
""" ------------------- Funções -------------------- """
def verificaStatusThread(t):
    if t.is_alive():
        print('status thread:', t.is_alive())

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


def cronometro(startTime):
    return time.time() - startTime

def draw_figure(canvas, figure, loc=(0, 0)):
    figure_canvas_agg = FigureCanvasTkAgg(figure, canvas)
    figure_canvas_agg.draw()
    figure_canvas_agg.get_tk_widget().pack(side='top', fill='both', expand=1)
    return figure_canvas_agg

def redimensionar(filename,size):
    if os.path.isfile(filename):
        im = Image.open(filename)
    else:
        pass
        # print("erro")
        # raise FileNotFoundError("Arquivo não encontrado! Certifique-se de configurar a pasta correta")
        # raise "erro"
    im = im.resize(size, resample=Image.BICUBIC)
    return ImageTk.PhotoImage(image=im)


""" ------------------- Janelas do programa ------------------ """
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
    a, b, c = 0, 0, 0
    x = SIZE_FRAME_X
    y = SIZE_FRAME_Y
    elem_key = ['-IMAGE1-','-IMAGE2-','-IMAGE3-','-IMAGE4-']
    imagens = {elem_key[0]: pb, elem_key[1]: scatter, elem_key[2]: color, elem_key[3]: hist}
    periodo_amostragem = 3

    # ----- frames -----
    col1 = createColumn([[sg.Text('Capa Atual',expand_x=True,background_color='#005e80',justification='c')],
                         [sg.Column([[sg.Column([[sg.Text("Número de Nós: 0",k='-NOS-')]]), sg.Column([[sg.Text("Classe: Nenhum",k='-CLASSE-')]])]],expand_x=True,element_justification='center')],
                         [sg.Text('Estatísticas Gerais',expand_x=True,background_color='#005e80',justification='c',)],

                         [sg.Column([[sg.Column([[sg.Text("Tipo A: 0",k='-A-')]]),
                                      sg.Column([[sg.Text("Tipo B: 0",k='-B-')]]),
                                      sg.Column([[sg.Text("Tipo C: 0",k='-C-')]])]],expand_x=True,element_justification='center')],
                         [sg.Text("Total de Capas: 0", k='-TOTAL-')],
                         [sg.Button('Configurações')]], x, y)
    col2 = createColumn([[sg.Image(key=elem_key[0])]], x, y)
    col3 = createColumn([[sg.Image(key=elem_key[1])]], x, y*2)
    col4 = sg.Column([[createColumn([[sg.Image(key=elem_key[2])]], x, y)],[createColumn([[sg.Image(key=elem_key[3])]], x, y)]])
    # col4 = createColumn([[sg.Image(key="-IMAGE2-")]], x, y)
    # col5 = createColumn([[sg.Image(key="-IMAGE3-")]], x, y)
    # col6 = createColumn([[sg.Image(key="-IMAGE4-")]], x, y)
    col7 = sg.Column([[sg.Button("Iniciar",s=(10,1),disabled=False),sg.Button("Parar",s=(10,1),disabled=True)]],element_justification='center',justification='center')
    col8 = sg.Column([[sg.Push(),sg.Text('Tempo de execução: 0.00 seg',k='-TIME-',expand_x=True,justification='right')]])

    # ----- layout -----
    layout = [[col1, col2],
              [col3, col4],
              [col7, col8]]
    #
    # layout_old = [[col1, col2],
    #           [col3, col4],
    #           [col5, col6],
    #           [col7]]

    # ----- window -----
    main_window = sg.Window(title="Classificador de Madeira",finalize=True, layout=layout, grab_anywhere=True) # margins=(200, 100), resizable=True

    # Alias
    start = main_window['Iniciar']
    stop = main_window['Parar']
    crono = main_window['-TIME-']
    widnos = main_window['-NOS-']
    widclass = main_window['-CLASSE-']

    # ----- event loop -----
    startTime = 0
    atual = 0
    identify = Thread()

    while True:
        # verificaStatusThread(identify)
        event, values = main_window.read(timeout=10)

        if event == "Exit" or event == sg.WIN_CLOSED:
            break

        elif event == "Configurações":
            setup_window()

        elif event == "Iniciar":                                     # Gatilho para iniciar a identificação em tempo real
            start.update(disabled=True)
            stop.update(disabled=False)
            identify = Identificacao(target=thread_identif, intervalo=periodo_amostragem)
            identify.start()
            startTime = time.time()

        elif event == "Parar":                                       # Gatilho para parar a identificação.
            start.update(disabled=False)
            stop.update(disabled=True)
            identify.shutdown()
            startTime = 0
            atual = 0

        if startTime != 0:
            t = cronometro(startTime)
            crono.update('Tempo de execução: ' + str(round(t, 2)) + ' seg')
            anterior = atual
            atual = identify.contagemDados()
            if anterior != atual:
                nnos, classe = identify.retornaDados()
                widnos.update('Número de Nós: ' + str(nnos))
                widclass.update("Classe: " + classe)

                if classe == "A":
                    a += 1
                    main_window['-A-'].update("Tipo A: " + str(a))
                elif classe == "B":
                    b += 1
                    main_window['-B-'].update("Tipo B: " + str(b))
                elif classe == "C":
                    c += 1
                    main_window['-C-'].update("Tipo C: " + str(c))
                else:
                    pass  # Raise error#

                main_window['-TOTAL-'].update("Total de Capas: " + str(atual))

                for i in elem_key:
                    if i == '-IMAGE2-': size = (x,y*2)
                    else: size = (x,y)
                    try:
                        filename = os.path.join(folder,imagens[i])
                        image = redimensionar(filename,size)
                        main_window[i].update(data=image)
                    except:
                        pass
                main_window.refresh()

    main_window.close()


""" ------------------ void main ------------------- """
if __name__ == "__main__":
    # setup_window()
    main_window()