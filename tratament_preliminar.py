import cv2 as cv

def tratamento_preliminar(fframe):
    fframe = cv.cvtColor(fframe, cv.COLOR_BGR2GRAY)
    tresh,binaria = cv.threshold(fframe, 175, 255, cv.THRESH_BINARY)
    binaria = ~binaria
    img_erosion = cv.erode(binaria, cv.getStructuringElement(cv.MORPH_ELLIPSE, (2, 2)), iterations=1)
    img_dilation = cv.dilate(img_erosion, cv.getStructuringElement(cv.MORPH_ELLIPSE, (3, 3)), iterations=3)
    pronta = cv.morphologyEx(img_dilation, cv.MORPH_CLOSE, cv.getStructuringElement(cv.MORPH_ELLIPSE, (5, 5)))
   # pronta = ~pronta

    return pronta




