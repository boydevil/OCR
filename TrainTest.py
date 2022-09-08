import cv2
import numpy as np
from math import dist
from Convert import convert

def convertLBPH(img_in) :
    img = convert(img_in)
    h, w = img.shape[:2]
    img_p = np.zeros([h,w])
    img_p[0:h,0:w] = img
    histogramLBP = []
    for i in range(0,256) :
        histogramLBP.append(i)
        histogramLBP[i] = 0
    for i in range(0,h) :
        for j in range(0,w) :
            histogramLBP[int(img_p[i,j])] += 1
    histogramLBP[255] = 0
    histogramLBP[254] = 0
    histogramLBP[253] = 0
    result = np.array(histogramLBP)
    return result 

if __name__ == "__main__":
    train = cv2.imread("dox.jpg",0)
    test = cv2.imread("test/test.jpg",0)

    train_H = convertLBPH(train)
    test_H = convertLBPH(test) 

    D = dist(train_H,test_H)
    print(D)