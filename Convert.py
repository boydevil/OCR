import cv2
import numpy as np

def convertLBP(img, kernel=[[0.33, 0.33, 0.33], [0.33, 0.33, 0.33], [0.33, 0.33, 0.33]], padding=1, stride=1):
    h, w = img.shape[:2]
    img_p = np.zeros([h+2*padding, w+2*padding])
    img_p[padding:padding+h, padding:padding+w] = img
    

    kernel = np.array(kernel)
    assert len(kernel.shape) == 2 and kernel.shape[0] == kernel.shape[1] 
    assert kernel.shape[0] % 2 != 0 

    k_size = kernel.shape[0]
    k_half = int(k_size/2)
    
    y_pos = [v for idx, v in enumerate(list(range(k_half, h-k_half))) if idx % stride == 0]
    x_pos = [v for idx, v in enumerate(list(range(k_half, w-k_half))) if idx % stride == 0]
    
    new_img = np.zeros([len(y_pos), len(x_pos)])
    for new_y, y in enumerate(y_pos):
        for new_x, x in enumerate(x_pos):
            point = []
            for i in range(-1,2) : 
                for j in range (-1,2) :
                    if(i==0 and j==0) :
                        img_p[y,x] = img_p[y,x]
                    else :
                        if(img_p[y+i,x+j]<img_p[y,x]) :
                            point.append(0)
                        else :
                            point.append(1)
            binary = 0
            for i in point :
                binary = binary*10+i
            result = int(str(binary),2)
            new_img[new_y, new_x] = result
    return new_img

def convert(img_in, kernel=[[0.33, 0.33, 0.33], [0.33, 0.33, 0.33], [0.33, 0.33, 0.33]], padding=0, stride=1):
    img_cvt = convertLBP(img_in, kernel, padding, stride)
    new_img = img_cvt
    return new_img
