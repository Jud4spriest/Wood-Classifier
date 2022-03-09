import cv2 as cv
import maior
import matplotlib.pyplot as plt
from matplotlib import image
from matplotlib.figure import Figure



plt.style.use('seaborn-dark')

def classifica(fframe,color):
    output = cv.connectedComponentsWithStats(fframe,4,cv.CV_32S)
    stats = output[2]

    stats=stats[1:len(stats)]
    altura, largura = fframe.shape
    nnos = output[0]-1
    area_maior_no = max(stats[:,4])
    if output[0] ==1:
        # print('Capa tipo A')
        tipo = 'A'

    elif 1 < output[0] < 12 and maior.maiorlargura(stats)< 250 and maior.maioraltura(stats)<200:
        # print('Capa tipo B')
        tipo = 'B'
    else:
        # print('Capa tipo C')
        tipo = 'C'


    # Gerando gráficos


    plt.scatter(stats[:,3],stats[:,2])
    plt.xlabel('Altura do nó')
    plt.ylabel('Largura do nó')
    plt.title('Dispersão da dimensão dos nós')
    plt.savefig('scatter.png')
    scatter = cv.imread('scatter.png')
    plt.close()



    plt.hist(stats[:,4])
    plt.xlabel('Área do nó')
    plt.ylabel('Frequência')
    plt.title('Dispersão da dimensão dos nós')
    plt.savefig('hist.png')
    hist = cv.imread('hist.png')
    plt.close()




    for rows in stats:
        color = cv.rectangle(color, (rows[0], rows[1]), (rows[0] + rows[2], rows[1] + rows[3]), (255, 0, 0), 2)




    return nnos,tipo,color,scatter,hist,area_maior_no






