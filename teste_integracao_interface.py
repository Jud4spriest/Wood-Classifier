import cv2 as cv
import numpy as np
import time
import keyboard

import classificacao_script
import intermed
import tratament_preliminar

def testeIntegracao():

    a = cv.imread('a.png')
    b = cv.imread('b.png')
    cr = cv.imread('c.png')

    return intermed.intermediario(cr,0,0,len(cr),len(cr[1]))