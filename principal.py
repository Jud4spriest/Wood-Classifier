import cv2 as cv
import faz_tudo

limiar_area = 1000

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

        [numero_de_nos,tipo_norma,colorida_bounding_box,pb,g_scatter,g_hist,is_chapa] = faz_tudo.fazTudo(frame,x,y,w,h)
        cv.imshow('pista',colorida_bounding_box)
        cv.waitKey(1)

        if (is_chapa):
                cv.imshow('chapa',colorida_bounding_box)
                cv.imshow('pb',pb)
                cv.imshow('histograma',g_hist)
                cv.imshow('scatter',g_scatter)
                cv.waitKey(100)


