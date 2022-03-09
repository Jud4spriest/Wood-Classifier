import cv2 as cv

def setWebcam(n_webcam):
    webcam = cv.VideoCapture(n_webcam)  # normalmente é 1 ou 2, 0 é o nativo do not
    return webcam

def chamaWebcam(webcam):
    if webcam.isOpened():
        _, frame = webcam.read()
        return frame