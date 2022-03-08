import cv2 as cv

def chama_webcam(n_webcam):
    #normalmente é 1 ou 2, 0 é o nativo do not
    webcam = cv.VideoCapture(n_webcam)
    if webcam.isOpened():

        validacao, frame = webcam.read(n_webcam)
        cv.imshow('teste',frame)
        cv.waitKey(3)

        return frame