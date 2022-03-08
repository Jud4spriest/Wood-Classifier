import cv2 as cv

def chamaWebcam(n_webcam):
    webcam = cv.VideoCapture(n_webcam)     #normalmente é 1 ou 2, 0 é o nativo do not
    if webcam.isOpened():
        _, frame = webcam.read(n_webcam)
        return frame