import cv2 as cv
import intermed

def testeIntegracao(img):
    capa = cv.imread(img)
    return intermed.intermediario(capa,0,0,len(capa),len(capa[1]))

