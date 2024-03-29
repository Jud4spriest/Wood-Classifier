# -*- coding: utf-8 -*-
"""
Created on Sun Feb 27 14:35:34 2022
@author: Marcos Azevedo (judaspriest)
"""

"""------------------- Setup --------------------------------- """
import os
import time
import PySimpleGUI as sg
from threading import Thread,Event
from PIL import Image, ImageTk
import api
import webcam
import cv2 as cv

sg.theme('DarkTanBlue')

""" --------------- Variaveis Globais --------------- """
font = ("Arial, 11")
size = (600, 200)
folder = os.getcwd()+'/database/'
webcam_type = 0
modo_operacao = 0
periodo_amostragem = 0.5
imagens_file = ['scatter.png','hist.png','color.png','pb.png']

"""-------------------- Classes -------------------- """

class Identificacao(Thread):
    def __init__(self, target, cam=None, database=[], name='Thread_identificacao'):
        super().__init__()
        self.name = name
        self._target = target
        self._finished = Event()
        self.daemon = True
        """Custom Atributos"""
        self._database = database
        self.results = []
        self._count = 0
        self._cam = cam
        self._error = False
        self._interval = 0
        # print(self.name, 'criada')

    def run(self):                   #Teoricamente eu garanto que há dados para identificar. (tratar excessão)
        print(self.name, 'iniciada')
        while not self._finished.is_set():
            st = time.time()
            try:
                if len(self._database) != 0:
                    self.results = self._target(folder+self._database[self._count])   # Função que roda com database
                else:
                    self.results = self._target(getImagemWebcam(self._cam))                    # Função tempo real
                self._interval = cronometro(st,4)
                self._count += 1
                t = periodo_amostragem - cronometro(st)
                if t < 0:
                    t = 0
                time.sleep(t)
            except Exception as e:
                self._error = True
                time.sleep(2)
                raise e
        print(self.name, 'destruida')

    def shutdown(self):
        self._finished.set()
        print(self.name, 'Desativada')
        self.join()

    def contagemDados(self):
        return self._count

    def elapsedTime(self):
        return self._interval

    def isError(self):
        return self._error

    def retornaDados(self):
        nos, classe, _, _, _, _ = self.results
        # nos, classe, _, _, = self.results
        return nos, classe

""" ------------------- Funções -------------------- """

def setWebcam(cam):
    return webcam.setWebcam(cam)

def getImagemWebcam(cam):
    st = time.time()
    img_cam = webcam.chamaWebcam(cam)
    print('Elapsed Time intermed: ' + str(round(time.time() - st, 4)))
    return img_cam

# def printImageWebcam(frame, waitkey=1):
#     cv.imshow('teste',frame)
#     cv.waitKey(waitkey)

def identification(img):

    return api.integracao(img)

def getDatabase(folder):
    try:
        file_list = os.listdir(folder)
    except :
        file_list = []

    fnames = [
        f
        for f in file_list
        if os.path.isfile(os.path.join(folder, f))
           and f.lower().endswith(".png")
    ]
    return fnames

def verificaStatusThread(t):
    print('status thread:', t.is_alive())
    print('error:', t.isErrorThread())
    # if status: print('status thread:', status)
    # return status

def createColumn(elements,x,y):
    col = sg.Column([[sg.Frame('',
                               [[sg.Column(elements,
                                           expand_x=True,
                                           element_justification='center',
                                           justification='center',
                                           pad=(0, 0))]],size=(x, y),
                               border_width=1,
                               font=font)]])
    return col

# def openImage(img,x,y):
#     image = Image.open(img)
#     image.thumbnail((x, y))
#     bio = io.BytesIO()
#     image.save(bio, format="PNG")
#     return bio.getvalue()

def cronometro(start_time, trunc=3):
    return round(time.time() - start_time, trunc)

# def draw_figure(canvas, figure, loc=(0, 0)):
#     figure_canvas_agg = FigureCanvasTkAgg(figure, canvas)
#     figure_canvas_agg.draw()
#     figure_canvas_agg.get_tk_widget().pack(side='top', fill='both', expand=1)
#     return figure_canvas_agg

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

""" ------------- Janelas do programa -------------- """

def setup_window():
    global folder, periodo_amostragem, webcam_type, modo_operacao
    win_size = (500,400)
    p = (0,10)
    font = "Any 11 bold"

    coluna_layout = sg.Column([
        [sg.Text('Selecione o modo de operação: ', font=font, p=p)],
        [sg.Radio('Database', "RadioDemo",enable_events=True, default=True, size=(10, 1), k='-R1-'),
         sg.Radio('Tempo Real', "RadioDemo", default=False, enable_events=True, size=(10, 1), k='-R2-')],
        [sg.Text("Escolha um diretório para leitura do banco de dados:",font=font, p=p)],
        [sg.Text("Diretório:"),sg.In(size=(40,1), default_text=folder, enable_events=True, key="-FOLDER-", p=p), sg.FolderBrowse(k='-BROWSE-')],
        [sg.Text('Selecione a webcam: ', font=font, p=p)],
        [sg.Radio('Nativo', "RadioDemo2", default=True, size=(10, 1), k='-C1-'),
         sg.Radio('Externo-1', "RadioDemo2", default=False, size=(10, 1), k='-C2-'),
         sg.Radio('Externo-2', "RadioDemo2", default=False, size=(10, 1), k='-C3-')],
        [sg.Text('Selecione o intervalo de amostragem (ms):',font=font, p=p)],
        [sg.Slider(resolution=100,range=(100, 2000), size=(30, 8), default_value=periodo_amostragem*1000, orientation='h', key='-SLIDER-')],


        [sg.Button('Ok',s=(10,1),pad=(0,10))]],
    # background_color='red',
    # size=win_size,
    element_justification='center')

    layout = [[coluna_layout]]
    window = sg.Window('Classificador de Madeira', layout,element_justification='center', size=win_size, keep_on_top=True, finalize=True, grab_anywhere=True)

    while True:
        event, values = window.read()

        if event == sg.WIN_CLOSED:
            break

        elif event == "-FOLDER-":
            folder = values["-FOLDER-"]

        elif event == "-R1-":
            window['-FOLDER-'].update(disabled=False)
            window['-BROWSE-'].update(disabled=False)
            modo_operacao = 0
            # print(mode, values['-R1-'], values['-R2-'])

        elif event == "-R2-":
            window['-FOLDER-'].update(disabled=True)
            window['-BROWSE-'].update(disabled=True)
            modo_operacao = 1
            # print(mode, values['-R1-'], values['-R2-'])

        elif event == "Ok":
            if values['-C1-']:
                webcam_type = 0
            elif values['-C2-']:
                webcam_type = 1
            else:
                webcam_type = 2
            periodo_amostragem = float(values['-SLIDER-'])/1000
            # print(modo_operacao,folder, webcam_type, periodo_amostragem)
            break

    window.close()

def info_window():
    win_size = (600,200)
    font = "Any 11 bold"

    col1 = sg.Column([
        [sg.Text('About Us', background_color='#005e80', font='Any 13 bold')],
        [sg.Text('Projeto desenvolvido por Arthur Fey & Marcos Azevedo', font=font)]],expand_y=True,element_justification='center')
    col2 = sg.Column([[sg.Button('Fechar')]],expand_x=True,element_justification='center',p=(0,30))

    layout = [[col1],[col2]]
    window = sg.Window('Classificador de Madeira', layout,element_justification='center', size=win_size, keep_on_top=True, finalize=True, grab_anywhere=True)
    while True:
        event, values = window.read()
        if event == 'Fechar' or event == sg.WIN_CLOSED:
            break
    window.close()

def error_window():

    font = "Any 11 bold"

    col1 = sg.Column([
        [sg.Text('Aconteceu um erro que interrompeu a Thread de identificação', background_color='red',p=(0,20), font='Any 13 bold')]])
    col2 = sg.Column([[sg.Button('Fechar')]],expand_x=True,element_justification='center',p=(0,10))

    layout = [[col1],[col2]]
    window = sg.Window('Classificador de Madeira', layout,element_justification='center', keep_on_top=True, finalize=True, grab_anywhere=True)
    while True:
        event, values = window.read()
        if event == 'Fechar' or event == sg.WIN_CLOSED:
            break
    window.close()

def main_window():

    # ----- variaveis -----
    global size, webcam_type, modo_operacao, periodo_amostragem
    a, b, c = 0, 0, 0
    startTime, atual = 0, 0
    x, y = size
    elem_key = ['-IMAGE1-', '-IMAGE2-', '-IMAGE3-', '-IMAGE4-']
    dir_img = os.getcwd() + '\img'
    imagens = {}
    for i in range(len(elem_key)):
        imagens.update({elem_key[i]: imagens_file[i]})
    identify = Identificacao(None,None)

    # ----- frames -----

    col1 = createColumn([[sg.Text('Capa Atual', expand_x=True, background_color='#005e80', justification='c')],
                         [sg.Column([[sg.Column([[sg.Text("Número de Nós: 0",
                                                          k='-NOS-')]]),
                                      sg.Column([[sg.Text("Classe: Nenhum",
                                                          k='-CLASSE-')]])]],
                                    expand_x=True,
                                    element_justification='center')],
                         [sg.Text('Estatísticas Gerais',
                                  expand_x=True,
                                  background_color='#005e80',
                                  justification='c', )],
                         [sg.Column([[sg.Column([[sg.Text("Tipo A: 0",
                                                          k='-A-')]]),
                                      sg.Column([[sg.Text("Tipo B: 0",
                                                          k='-B-')]]),
                                      sg.Column([[sg.Text("Tipo C: 0",
                                                          k='-C-')]])]],
                                    expand_x=True,
                                    element_justification='center')],
                         [sg.Text("Total de Capas: 0",
                                  k='-TOTAL-')],
                         [sg.Button('Configurações')]], x, y)
    col2 = createColumn([[sg.Image(key=elem_key[0])]], x, y)
    col3 = createColumn([[sg.Image(key=elem_key[1])]], x, y*2)
    col4 = sg.Column([[createColumn([[sg.Image(key=elem_key[2])]], x, y)],
                      [createColumn([[sg.Image(key=elem_key[3])]], x, y)]])
    col5 = sg.Column([[sg.Button("Iniciar",
                                 s=(10,1),
                                 disabled=False),
                       sg.Button("Parar",
                                 s=(10,1),
                                 disabled=True)]],
                     # background_color='purple',
                     expand_x=True,
                     element_justification='center',
                     justification='center')
    col6 = sg.Column([[sg.Text('Tempo de execução:',
                               justification='left'),
                       sg.Text('0.00 seg',
                               k='-TIME-')]])
                     # justification='right',
                     # background_color='green')
    col7 = sg.Column([[sg.Button("Sobre o Projeto")]],
                     # background_color='yellow',
                     justification='left')
    # ----- layout -----
    layout = [[col1, col2],
              [col3, col4],
              [sg.Column([[col7, col5, col6]],expand_x=True)]]

    # ----- window -----
    main_window = sg.Window(title="Classificador de Madeira",finalize=True, layout=layout, grab_anywhere=True)

    # Alias
    start = main_window['Iniciar']
    stop = main_window['Parar']
    config = main_window['Configurações']
    crono = main_window['-TIME-']
    about = main_window["Sobre o Projeto"]


    # ----- event loop -----
    while True:
        # verificaStatusThread(identify)  # Código de logging
        event, values = main_window.read(timeout=10)

        if event == sg.WIN_CLOSED:
            break

        elif event == "Sobre o Projeto":
            info_window()

        elif event == "Configurações":
            setup_window()

        elif event == "Iniciar":                                     # Start identificação
            start.update(disabled=True)
            config.update(disabled=True)
            about.update(disabled=True)
            stop.update(disabled=False)
            if modo_operacao == 0:
                identify = Identificacao(target=identification, database=getDatabase(folder))
            elif modo_operacao == 1:
                identify = Identificacao(target=identification, cam=setWebcam(webcam_type))
            identify.start()
            startTime = time.time()

        elif event == "Parar" or (identify.isError()):                                       # Stop identificação
            start.update(disabled=False)
            config.update(disabled=False)
            about.update(disabled=False)
            stop.update(disabled=True)
            identify.shutdown()
            startTime = 0
            atual = 0
            if identify.isError():
                identify = Identificacao(None, None)
                error_window()

        if startTime != 0:                                           # Identificacao
            crono.update(str(cronometro(startTime)) + ' seg')  # Aprimorar exibição para hh:mm:ss:ms

            anterior = atual
            atual = identify.contagemDados()

            if anterior != atual:
                st = time.time()         # Código de logging

                nnos, classe = identify.retornaDados()
                main_window['-NOS-'].update('Número de Nós: ' + str(nnos))
                main_window['-CLASSE-'].update("Classe: " + classe)
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
                main_window['-TOTAL-'].update("Total de Capas: " + str(a+b+c))

                for i in elem_key:
                    if i == '-IMAGE2-': size = (x, y*2)
                    else: size = (x, y)
                    try:
                        filename = os.path.join(dir_img, imagens[i])
                        image = redimensionar(filename, size)
                        main_window[i].update(data=image)
                    except:
                        pass

                # Código de logging
                print('Amostra ' + str(atual) + ' - ' + str(cronometro(startTime, 4)))
                print('Delay acumulado: ' + str(cronometro(startTime, 4) - anterior * periodo_amostragem))
                print('Delay médio: ' + str((cronometro(startTime, 4) - anterior * periodo_amostragem) / atual))
                print("Elapsed Time função identificação: " + str(identify.elapsedTime()))
                print('Elapsed Time loop de exibição: ' + str(cronometro(st, 4)))
                # Código de logging

    main_window.close()


""" ------------------ void main ------------------- """
if __name__ == "__main__":
    # cam = setWebcam(0)
    # while True:
    #     printImageWebcam(getImagemWebcam(cam))  # Função Teste Print WebCam
    # print(getDatabase(folder))
    # setup_window()
    main_window()





