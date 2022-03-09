import classificacao_script
import tratament_preliminar
import cv2
from time import time

def intermediario(imagem_classificar,x,y,w,h):
    dir = 'img/'
    # st = time()
    pb = tratament_preliminar.tratamento_preliminar(imagem_classificar, x, y, w, h)
    # print('Elapsed Time tratamento preliminar: '+str(round(time()-st,4)))
    # st = time()
    [numero_de_nos,tipo_norma,colorida_bounding_box,scatter,hist] = classificacao_script.classifica(pb, imagem_classificar)   #Alterar o retorno do classifica
    # [numero_de_nos, tipo_norma, colorida_bounding_box] = classificacao_script.classifica(pb, imagem_classificar)
    # print('Elapsed Time classificacao: '+str(round(time()-st,4)))
    # cv2.imwrite(dir+'scatter.png',scatter)
    # cv2.imwrite(dir+'hist.png',hist)
    cv2.imwrite(dir+'color.png',colorida_bounding_box)
    cv2.imwrite(dir+'pb.png',pb)

    # return numero_de_nos, tipo_norma, colorida_bounding_box, pb
    return numero_de_nos, tipo_norma, colorida_bounding_box, pb, scatter, hist
