import cv2 as cv
import intermed


dir = 'database/'
images = ['a.png','b.png','c.png']
list = []
for i in range(3):
    list.append(cv.imread(dir+images[i]))

del(list[0])        #Retira a capa tipo  A por causa do bug

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

