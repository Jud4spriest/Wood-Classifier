import classificacao_script
import tratament_preliminar
import cv2

def save_figure(filename,image):
    cv2.imwrite(filename, image)

def intermediario(imagem_a_classificar,x,y,w,h):
    pb = tratament_preliminar.tratamento_preliminar(imagem_a_classificar,x, y, w, h)

    # """Retorno Antigo"""
    # [numero_de_nos,tipo_norma,colorida_bounding_box,scatter,hist] = classificacao_script.classifica(pb, imagem_a_classificar)   #Alterar o retorno do classifica
    # return numero_de_nos,tipo_norma,colorida_bounding_box,pb,scatter,hist

    """Retorno Novo"""
    [numero_de_nos,tipo_norma,colorida_bounding_box,scatter,hist] = classificacao_script.classifica(pb, imagem_a_classificar)   #Alterar o retorno do classifica
    save_figure('scatter.png',scatter)
    save_figure('hist.png',hist)
    save_figure('color.png',colorida_bounding_box)
    save_figure('pb.png',pb)

    return numero_de_nos, tipo_norma, colorida_bounding_box, pb, scatter, hist

