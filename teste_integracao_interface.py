import cv2 as cv
import numpy as np
import time
import keyboard

import classificacao_script
import intermed
import tratament_preliminar

def testeIntegracao(img):

    a = cv.imread(img)
    # b = cv.imread('b.png')
    # cr = cv.imread('c.png')

    return intermed.intermediario(a,0,0,len(a),len(a[1]))

