import cv2 as cv
import openpyxl
import intermed



limiar_area = 10000


# regioes de corte
x = 350
y = 0
w = 150
h = 625




webcam = cv.VideoCapture(0)
tempo_entre_frames = 3

if webcam.isOpened():
    validacao,frame = webcam.read()

while validacao: # aqui ocorre toda execução do programa principal
        validacao,frame = webcam.read() # imagens da webcam são colocadas na variável frame, a cada instante, gerando o vídeo
        frame = frame[x:x + w, y:y + h]
        [numero_de_nos, tipo_norma, colorida_bounding_box, pb, g_scatter, g_hist,area_maior_no] = intermed.intermediario(frame)
        # if area_maior_no > limiar_area:
        #         cv.imshow('Identificacao', colorida_bounding_box)
        #         cv.waitKey(1)
        #         cv.imshow('pb', pb)
        #         cv.waitKey(1)
        #         cv.imshow('Dispersao', g_scatter)
        #         cv.waitKey(1)
        #         cv.imshow('Histograma', g_hist)
        #         cv.waitKey(1)

        cv.imshow('Identificacao',colorida_bounding_box)
        cv.waitKey(1)
        cv.imshow('pb',pb)
        cv.waitKey(1)
        # cv.imshow('Dispersao',g_scatter)
        # cv.waitKey(1)
        # cv.imshow('Histograma',g_hist)

        cv.waitKey(1)



