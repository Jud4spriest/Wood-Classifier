import cv2 as cv
import intermed
import os

f1 = cv.imread('fundo1.png')
f2 = cv.imread('fundo2.png')
f3 = cv.imread('fundo3.png')
f4 = cv.imread('fundo4.png')

m01 = cv.imread('meio_termo/01.png')
m02 = cv.imread('meio_termo/02.png')
m03 = cv.imread('meio_termo/03.png')
m04 = cv.imread('meio_termo/04.png')
m05 = cv.imread('meio_termo/05.png')
m06 = cv.imread('meio_termo/06.png')
m07 = cv.imread('meio_termo/07.png')
m08 = cv.imread('meio_termo/08.png')
m09 = cv.imread('meio_termo/09.png')
m10 = cv.imread('meio_termo/10.png')
m11 = cv.imread('meio_termo/11.png')
m12 = cv.imread('meio_termo/12.png')
m13 = cv.imread('meio_termo/13.png')
m14 = cv.imread('meio_termo/14.png')
m15 = cv.imread('meio_termo/15.png')
m16 = cv.imread('meio_termo/16.png')
m17 = cv.imread('meio_termo/17.png')



a = cv.imread('a.png')
c = cv.imread('database/c.png')

i = a

x = 350
y = 0
w = 150
h = 625


# arr = [ m10, m11, m12, m13, m14, m15, m16]
# # m01, m02, m03, m04, m05, m06, m07, m08, m09,
# for img in arr:
#
#     img2 = img[x:x + w, y:y + h]
#     [numero_de_nos,tipo_norma,colorida_bounding_box,pb,g_scatter,g_hist,area_maior_no] = intermed.intermediario(img2)
#     cv.imshow('web',colorida_bounding_box)
#     cv.waitKey(0)
#     if(area_maior_no>1200):
#         print("capa do tipo "+tipo_norma+" com um total de " + str(numero_de_nos)+"nós")

# 150 pixels corresponde 130 cm ?
# limiar bom é menor 1 1000


arr = [m01, m02, m03, m04, m05, m06, m07, m08, m09, m10, m11, m12, m13, m14, m15, m16]



mylist = os.listdir('rolls3/')
print(mylist)

for nome_arquivo in mylist:
    img = cv.imread('rolls3/'+ nome_arquivo)
    img2 = img[x:x + w, y:y + h]

    try :
        [numero_de_nos,tipo_norma,colorida_bounding_box,pb,g_scatter,g_hist,area_maior_no] = intermed.intermediario(img2)
        cv.imshow('pista', colorida_bounding_box)
        cv.waitKey(1)

    except:
        numero_de_nos = 0
        tipo_norma = 'A'
        area_maior_no = 0

        cv.imshow('pista', img2)
        cv.waitKey(1)



    if(area_maior_no<1000):
        #print("capa do tipo "+ tipo_norma + " com um total de " + str(numero_de_nos)+" nós")
        print("tem chapa do tipo " + tipo_norma + ", tamanho do maior nó = " +  str(area_maior_no))
        cv.imshow('com capa', img2)
        cv.waitKey(0)



cv.waitKey(0)