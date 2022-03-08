import cv2 as cv
import numpy as np
import time
import keyboard

import classificacao_script
import intermed
import tratament_preliminar

images = ['b.png','c.png']
list = []
for i in range(2):
    list.append(cv.imread(images[i]))

#del(list[0])        #Retira a capa tipo A por causa do bug

for i in list:
    [numero_de_nos,tipo_norma,colorida_bounding_box,pb,g_scatter,g_hist] = intermed.intermediario(i,0,0,len(i),len(i[1]))

    cv.imshow('pb',pb)
    cv.waitKey(0)
    cv.imshow('cor',colorida_bounding_box)
    cv.waitKey(0)
    cv.imshow('scatter',g_scatter)
    cv.waitKey(0)
    cv.imshow('hist',g_hist)
    cv.waitKey(0)

