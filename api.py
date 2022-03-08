import cv2 as cv
import intermed
from time import time

def integracao(img):
    if type(img) is str:
        capa = cv.imread(img)
    else:
        capa = img
    st = time()
    results = intermed.intermediario(capa,0,0,len(capa),len(capa[1]))
    print('Elapsed Time intermed: '+str(round(time()-st,4)))
    return results

