import classificacao_script
import tratament_preliminar


def intermediario(imagem_a_classificar,x,y,w,h):
    pb = tratament_preliminar.tratamento_preliminar(imagem_a_classificar,x, y, w, h)

    """Retorno Antigo"""
    # [numero_de_nos,tipo_norma,colorida_bounding_box,scatter,hist] = classificacao_script.classifica(pb, imagem_a_classificar)   #Alterar o retorno do classifica
    # return numero_de_nos,tipo_norma,colorida_bounding_box,pb,scatter,hist

    """Retorno Novo"""
    return classificacao_script.classifica(pb,imagem_a_classificar)  # Retorno Alterado