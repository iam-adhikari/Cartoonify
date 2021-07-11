# importing required libraries

import cv2
import easygui
import numpy
import imageio
import sys
import matplotlib.pyplot as plt
import os
import tkinter as tk
from tkinter import filedialog
from tkinter import *
from PIL import ImageTk, Image

#FileBox to choose file
def upload_file():
    Imagepath = easygui.fileopenbox()
    print(Imagepath)
    cartoonify(Imagepath)

#Function to cartoonify the image
def cartoonify(Imagepath):
    originalImage = cv2.imread(Imagepath)
    originalImage = cv2.cvtColor(originalImage, cv2.COLOR_BGR2RGB)
    if originalImage is None:
        print('Cannot find any image. Choose appropriate file')
        sys.exit()
    resizedColoured = cv2.resize(originalImage, (960, 540))

    #Converting the image to grayscale to extract the edges
    grayscaleImage = cv2.cvtColor(originalImage, cv2.COLOR_BGR2GRAY)
    resizedGray = cv2.resize(grayscaleImage, (960,540))

    #Smoothening the picture to get edges
    smoothGray = cv2.medianBlur(grayscaleImage, 5)
    resizedSmooth = cv2.resize(smoothGray, (960, 540))

    #Recording the edges of the image using thresholding technique
    getEdge = cv2.adaptiveThreshold(smoothGray, 255,
                                    cv2.ADAPTIVE_THRESH_MEAN_C,
                                    cv2.THRESH_BINARY, 9, 9)

    resizedEdge = cv2.resize(getEdge, (960, 540))

    #masking the original picture to get lighter colour
    colorImage = cv2.bilateralFilter(originalImage, 9, 300, 300)
    resizedColor = cv2.resize(colorImage, (960, 540))

    #Giving the cartoon effect
    cartoonImage = cv2.bitwise_and(colorImage, colorImage, mask=getEdge)
    resizedCartoon = cv2.resize(cartoonImage, (540, 960))
    plt.imshow(resizedCartoon, cmap='gray')
    plt.show()

upload_file()