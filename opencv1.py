#!/usr/bin/env python
#_*_ coding: utf8 _*_
import cv2
import numpy as np

# Cargamos la imagen
imgColor = cv2.imread('img1.jpg', cv2.IMREAD_COLOR)
imgGray = cv2.imread('img1.jpg', cv2.IMREAD_GRAYSCALE)
imgOriginal = cv2.imread('img1.jpg', cv2.IMREAD_UNCHANGED)

cv2.imshow('Image color', imgColor)
cv2.imshow('Image gray', imgGray)
cv2.imshow('image original', imgOriginal)

# Esperamos a que se pulse una tecla
cv2.waitKey(0) # (0) valor ms, si el valor es 0 entonces espera a una pulsación

# Destruimos las ventanas abiertas
cv2.destroyAllWindows()