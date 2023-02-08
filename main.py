# This is a sample Python script.
import matplotlib.image as mpimg
import numpy as np
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import numpy as np
import random
import cv2 as cv2
from matplotlib import image
from matplotlib import pyplot
from numpy import asarray
from PIL import Image


import matplotlib.pyplot as plt

def pmgBruit(name):
    with open(name) as f:
        data = image.imread(name)
        matrice0 = asarray(data)
        matrice =np.copy(matrice0)
        for i in range(matrice.shape[0]) :
           for j in range(matrice.shape[1]):
               randomNumber = random.randint(0, 20)
               if randomNumber == 0:
                   matrice[i][j] = 0
               if randomNumber == 20:
                   matrice[i][j] = 255
    return matrice

def convolution2D(X,H):
    s = X.shape
    py = int((H.shape[0]-1)/2)
    px = int((H.shape[1]-1)/2)
    Y = X.copy()
    xmax= int(s[1]-px) ;
    ymax= int(s[0]-py)
    for i in range(px,xmax):
        for j in range(py,ymax):
            somme = 0.0
            for k in range(-px,px+1):
                for l in range(-py,py+1):
                    somme += X[j+l][i+k]*H[l+py][k+px]
            Y[j][i] = somme
    return Y

def filtreMedian(X,N):
    s = X.shape
    py = int((N-1)/2)
    px = int((N-1)/2)
    Y = X.copy()
    iMed = int(N / 2)

    xmax= int(s[1]-px) ;
    ymax= int(s[0]-py)
    for i in range(px,xmax):
        for j in range(py,ymax):
            med = []
            for k in range(-px,px+1):
                for l in range(-py,py+1):
                    med.append(Y[k][l])
            med.sort()
            Y[j][i] = med[iMed]
    return Y







def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    data = pmgBruit('./chat.pgm')
    filterMoy= np.ones((3, 3)) * 1.0 / 9
    filtredData=convolution2D(data,filterMoy)
    print(filtredData)

    filtreMedian(data,3)
    img = cv2.imread('chat.pgm')
    cv2.imshow("chat.pmg", img)
    cv2.waitKey(0)

    # Press Ctrl+F8 to toggle the breakpoint.





# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
