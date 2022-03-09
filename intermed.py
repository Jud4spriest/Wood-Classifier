import classificacao_script
import tratament_preliminar
import cv2
from time import time

def intermediario(imagem_a_classificar):
    dir = 'img/'
    pb = tratament_preliminar.tratamento_preliminar(imagem_a_classificar)

    [numero_de_nos,tipo_norma,colorida_bounding_box,scatter,hist,area_big_no] = classificacao_script.classifica(pb, imagem_a_classificar)   #Alterar o retorno do classifica
    cv2.imwrite(dir+'scatter.png',scatter)
    cv2.imwrite(dir+'hist.png',hist)
    cv2.imwrite(dir+'color.png',colorida_bounding_box)
    cv2.imwrite(dir+'pb.png',pb)

    return numero_de_nos, tipo_norma, colorida_bounding_box, pb, scatter, hist,area_big_no


