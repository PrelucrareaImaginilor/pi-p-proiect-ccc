import cv2
import numpy as np
import os

def preprocessing(image):

    resize = cv2.resize(image,(500,500))
    gray = cv2.cvtColor(resize,cv2.COLOR_BGR2GRAY)      # converteste imaginea grayscale
    blur = cv2.GaussianBlur(gray, (7, 7), 0)            # aplica filtrul gausian pt evidentia obiectele
    threshold = cv2.adaptiveThreshold(blur,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY_INV,11,2)  # pentru conturul obiectelor
    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(5,5))
    cleaned = cv2.morphologyEx(threshold, cv2.MORPH_CLOSE, kernel, iterations=2)
    edges = cv2.Canny(cleaned,50,150)

    return resize, edges
