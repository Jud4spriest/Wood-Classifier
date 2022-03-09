import cv2 as cv
import intermed

def fazTudo(img_base,x,y,w,h):
    is_chapa = False
    img2 = img_base[x:x + w,y:y + h]
    try:
        [numero_de_nos,tipo_norma,colorida_bounding_box,pb,g_scatter,g_hist,area_maior_no] = intermed.intermediario(img2)


    except:
        numero_de_nos = 0
        tipo_norma = 'A'
        area_maior_no = 0


    if (area_maior_no < 1000):
        # print("capa do tipo "+ tipo_norma + " com um total de " + str(numero_de_nos)+" nós")
        print("tem chapa do tipo " + tipo_norma + ", tamanho do maior nó = " + str(area_maior_no))
        is_chapa = True

    return numero_de_nos,tipo_norma,colorida_bounding_box,pb,g_scatter,g_hist,is_chapa