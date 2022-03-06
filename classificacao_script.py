import cv2 as cv
import maior
import matplotlib.pyplot as plt



plt.style.use('seaborn-dark')

def classifica(fframe,color):

    output = cv.connectedComponentsWithStats(fframe,4,cv.CV_32S)
    stats = output[2]
    stats=stats[1:len(stats)]
    altura, largura = fframe.shape
    nnos = output[0]-1

    print(stats)
    print('largura do maior nó = ' + str(maior.maiorlargura(stats)) + ' ||| altura do maior nó + ' + str(maior.maioraltura(stats)))
    print('Número de nós : ' + str(nnos))

    if output[0] ==1:
        print('Capa tipo A')
        tipo = 'A'

    elif 1 < output[0] < 12 and maior.maiorlargura(stats)< 250 and maior.maioraltura(stats)<200:
        print('Capa tipo B')
        tipo = 'B'
    else:
        print('Capa tipo C')
        tipo = 'C'


    # Gerando gráficos
    """OBS: deve apenas criar imagens .png (verificar o custo computacional de atualizar a cada nova capa?)"""

    plt.scatter(stats[:,3],stats[:,2])
    plt.xlabel('Altura do nó')
    plt.ylabel('Largura do nó')
    plt.title('Dispersão da dimensão dos nós')
    plt.savefig('scatter.png')
    scatter = cv.imread('scatter.png')        # Retirar (não há necessidade)
    plt.close()


    plt.hist(stats[:,4])
    plt.xlabel('Área do nó')
    plt.ylabel('Frequência')
    plt.title('Dispersão da dimensão dos nós')
    plt.savefig('hist.png')
    hist = cv.imread('hist.png')              # Retirar (não há necessidade)



    for rows in stats:
        color = cv.rectangle(color, (rows[0], rows[1]), (rows[0] + rows[2], rows[1] + rows[3]), (255, 0, 0), 2)         # Precisa Salvar imagem em .png
        # print(type(color))


    """Retorno Antigo"""
    # return nnos,tipo,color,scatter,hist           #Substituir, não precisando retornar as imagens. (talvez retornar o diretório delas)

    """Retorno Novo"""
    return nnos,tipo





