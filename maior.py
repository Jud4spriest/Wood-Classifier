def maioraltura(saida):
    saida = saida[:,3]
    maior_vertical = max(saida)

    return maior_vertical

def maiorlargura(saida):
    saida = saida[:, 2]
    maior_horizontal = max(saida)

    return maior_horizontal