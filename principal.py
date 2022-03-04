import cv2 as cv
import openpyxl
import datetime as dt

# import numpy as np
# import time
# import keyboard

import classificacao_script
import intermed
import tratament_preliminar

ler = True


dados = openpyxl.load_workbook("dados.xlsx")
plan1 = dados['Plan1']

webcam = cv.VideoCapture(0)
tempo_entre_frames = 3

if webcam.isOpened():
    validacao,frame = webcam.read()

while validacao: # aqui ocorre toda execução do programa principal
    if ler:

        # aqui precisamos fazer a métrica de loop para capturar um frame a cada X segundos

        validacao,frame = webcam.read() # imagens da webcam são colocadas na variável frame, a cada instante, gerando o vídeo

        [numero_de_nos, tipo_norma, colorida_bounding_box, pb, g_scatter, g_hist] = intermed.intermediario(frame, 0, 0,len(frame),len(frame[1]))

        # now = dt.datetime.now()# atualiza o momento atual
        # plan1.append([now.strftime("%d/%m/%Y %H:%M:%S"),nnos,tipo])
        # dados.save('book1.xlsx') #salva no excel



        cv.imshow('frame',colorida_bounding_box)
        cv.waitKey(0)

