import cv2 as cv
import numpy as np
import time
import keyboard

import classificacao_script
import intermed
import tratament_preliminar


a = cv.imread('a.png')
b = cv.imread('b.png')
cr = cv.imread('c.png')
# cr = cv.imread('coringa.jpg')



# crt = tratament_preliminar.tratamento_preliminar(cr,0,0,len(cr),len(cr[1]))
# [nnos,tipo,colorida,bw]=classificacao_script.classifica(crt,cr)

[numero_de_nos,tipo_norma,colorida_bounding_box,pb,g_scatter,g_hist] = intermed.intermediario(cr,0,0,len(cr),len(cr[1]))

cv.imshow('pb',pb)
cv.waitKey(0)

cv.imshow('cor',colorida_bounding_box)
cv.waitKey(0)

cv.imshow('scatter',g_scatter)
cv.waitKey(0)

cv.imshow('hist',g_hist)
cv.waitKey(0)

