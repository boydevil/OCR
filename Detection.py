from math import dist
import cv2 as cv
import numpy as np
from TrainTest import convertLBPH
import os.path

def detect(PATH,image) :
    img = cv.imread(image,0)
    img = cv.fastNlMeansDenoising(img,None,10,7,21)
    img = cv.adaptiveThreshold(img,255,cv.ADAPTIVE_THRESH_GAUSSIAN_C,cv.THRESH_BINARY,11,20)
    row_height = 0
    for i in range(img.shape[0]):
        if 0 in img[i]:
            while 0 in img[i]:
                row_height+=1
                i+=1
            break
    num_row = 0
    rows = []
    row = np.full((row_height+1,img.shape[1]),255)
    i = 0
    while i in range(img.shape[0]):
        row_line = 0
        if 0 in img[i]:
            num_row+=1
            while 0 in img[i]:
                row[row_line] = img[i]
                i += 1
                row_line += 1
        if 0 in img[i-1] and 0 not in img[i]:
            rows.append(row)
            row = np.full((row_height+1,img.shape[1]),255)  
        i += 1
    rows = np.array(rows,dtype=np.uint8)
    cv.waitKey(0)
    letter = np.full((row_height+1,row.shape[1]),255)
    letters = []
    num_letter = 0
    for row in rows:
        row = np.array(row)
        i = 0
        space = 0
        while i in range(row.shape[1]):
            letter_line = 0
            if 0 in row[:,i]:
                num_letter += 1
                while 0 in row[:,i] and i<row.shape[1]-1: 
                    letter[:,letter_line] = row[:,i]
                    i+=1
                    letter_line+=1
                space = 0
            if 0 in row[:,i-1] and 0 not in row[:,i]:
                letters.append(letter)
                letter = np.full((row_height+1,row.shape[1]),255)
                space = 0
            space+=1
            if space == 24 :
                SPACE = np.full((row_height+1,row.shape[1]),255)
                letters.append(SPACE)
            if space == 60 :
                SPACE = np.full((row_height+1,row.shape[1]),255)
                letters.append(SPACE)
            if space == 90 :
                SPACE = np.full((row_height+1,row.shape[1]),255)
                letters.append(SPACE)
            i += 1
    letters = np.array(letters,dtype=object)
    letters = np.array(letters,dtype=np.uint8)
    a ='-'
    b ='_'
    space = 0
    check = 0
    EXCEP = []
    EXCEP.append(SPACE)
    EXCEP = np.array(EXCEP,dtype=object)
    EXCEP = np.array(EXCEP,dtype=np.uint8)
    text = 0
    row = 0
    for i in range(letters.shape[0]):
        A = np.array(letters[i])
        B = np.array(EXCEP[0])
        if (A==B).all() and check == 1 :
            space+=1
            check = 2
            text = 0
            continue
        if (A==B).all() and check == 2 :
            check = 3
            row +=1
            continue
        if (A==B).all() and check == 3 :
            check = 0
            row +=1
            continue
        for j in range(letters[i].shape[1]):
            if 0 not in letters[i,:,j]:
                check = 1
                Letter = letters[i,:,:j]
                Letters = convertLBPH(Letter)
                np.save(f'{PATH}{str(1000+space)}{str(a)}{str(1000+row)}{str(b)}{str(text)}.npy',Letters)
                text+=1
                break
def writetrain(PATH,image) :
    img = cv.imread(image,0)
    img = cv.fastNlMeansDenoising(img,None,10,7,21)
    img = cv.adaptiveThreshold(img,255,cv.ADAPTIVE_THRESH_GAUSSIAN_C,cv.THRESH_BINARY,11,15)
    row_height = 0
    for i in range(img.shape[0]):
        if 0 in img[i]:
            while 0 in img[i]:
                row_height+=1
                i+=1
            break
    num_row = 0
    rows = []
    row = np.full((row_height+1,img.shape[1]),255)
    i = 0
    while i in range(img.shape[0]):
        row_line = 0
        if 0 in img[i]:
            num_row+=1
            while 0 in img[i]:
                row[row_line] = img[i]
                i += 1
                row_line += 1
        if 0 in img[i-1] and 0 not in img[i]:
            rows.append(row)
            row = np.full((row_height+1,img.shape[1]),255)  
        i += 1
    rows = np.array(rows,dtype=np.uint8)
    cv.waitKey(0)
    letter = np.full((row_height+1,row.shape[1]),255)
    letters = []
    num_letter = 0
    for row in rows:
        row = np.array(row)
        i = 0
        space = 0
        while i in range(row.shape[1]):
            letter_line = 0
            if 0 in row[:,i]:
                num_letter += 1
                while 0 in row[:,i] and i<row.shape[1]-1: 
                    letter[:,letter_line] = row[:,i]
                    i+=1
                    letter_line+=1
                space = 0
            if 0 in row[:,i-1] and 0 not in row[:,i]:
                letters.append(letter)
                letter = np.full((row_height+1,row.shape[1]),255)
                space = 0
            space+=1
            if space == 24 :
                SPACE = np.full((row_height+1,row.shape[1]),255)
                letters.append(SPACE)
            if space == 60 :
                SPACE = np.full((row_height+1,row.shape[1]),255)
                letters.append(SPACE)
            if space == 90 :
                SPACE = np.full((row_height+1,row.shape[1]),255)
                letters.append(SPACE)
            i += 1
    letters = np.array(letters,dtype=object)
    letters = np.array(letters,dtype=np.uint8)
    a ='-'
    b ='_'
    space = 0
    check = 0
    EXCEP = []
    EXCEP.append(SPACE)
    EXCEP = np.array(EXCEP,dtype=object)
    EXCEP = np.array(EXCEP,dtype=np.uint8)
    text = 0
    row = 0
    for i in range(letters.shape[0]):
        A = np.array(letters[i])
        B = np.array(EXCEP[0])
        if (A==B).all() and check == 1 :
            space+=1
            check = 2
            text = 0
            continue
        if (A==B).all() and check == 2 :
            check = 3
            row +=1
            continue
        if (A==B).all() and check == 3 :
            check = 0
            row +=1
            continue
        for j in range(letters[i].shape[1]):
            if 0 not in letters[i,:,j]:
                check = 1
                Letter = letters[i,:,:j]
                cv.imwrite(f'{PATH}{str(1000+space)}{str(a)}{str(1000+row)}{str(b)}{str(text+100)}.jpg',Letter)
                text+=1
                break
def traindata(PATH,image) :
    img = cv.imread(image,0)
    img = cv.fastNlMeansDenoising(img,None,10,7,21)
    img = cv.adaptiveThreshold(img,255,cv.ADAPTIVE_THRESH_MEAN_C,cv.THRESH_BINARY,11,20)
    row_height = 0
    for i in range(img.shape[0]):
        if 0 in img[i]:
            while 0 in img[i]:
                row_height+=1
                i+=1
            break
    num_row = 0
    rows = []
    row = np.full((row_height+1,img.shape[1]),255)
    i = 0
    while i in range(img.shape[0]):
        row_line = 0
        if 0 in img[i]:
            num_row+=1
            while 0 in img[i]:
                row[row_line] = img[i]
                i += 1
                row_line += 1
        if 0 in img[i-1] and 0 not in img[i]:
            rows.append(row)
            row = np.full((row_height+1,img.shape[1]),255)  
        i += 1
    rows = np.array(rows,dtype=np.uint8)
    cv.waitKey(0)
    letter = np.full((row_height+1,row.shape[1]),255)
    letters = []
    num_letter = 0
    for row in rows:
        row = np.array(row)
        i = 0
        while i in range(row.shape[1]):
            letter_line = 0
            if 0 in row[:,i]:
                num_letter += 1
                while 0 in row[:,i] and i<row.shape[1]-1: 
                    letter[:,letter_line] = row[:,i]
                    i+=1
                    letter_line+=1
            if 0 in row[:,i-1] and 0 not in row[:,i]:
                letters.append(letter)
                letter = np.full((row_height+1,row.shape[1]),255)
            i += 1

    letters = np.array(letters,dtype=object)
    letters = np.array(letters,dtype=np.uint8)
    
    for i in range(letters.shape[0]):
        for j in range(letters[i].shape[1]):
            if 0 not in letters[i,:,j]:
                Letter = letters[i,:,:j]
                Letters = convertLBPH(Letter)
                Letters = np.array(Letters,'uint8')#
                np.save(f'{PATH}{str(10000+i)}.npy',Letters)
                break
def writedata(PATH,image) :
    img = cv.imread(image,0)
    img = cv.fastNlMeansDenoising(img,None,10,7,21)
    img = cv.adaptiveThreshold(img,255,cv.ADAPTIVE_THRESH_GAUSSIAN_C,cv.THRESH_BINARY,11,15)
    row_height = 0
    for i in range(img.shape[0]):
        if 0 in img[i]:
            while 0 in img[i]:
                row_height+=1
                i+=1
            break
    num_row = 0
    rows = []
    row = np.full((row_height+1,img.shape[1]),255)
    i = 0
    while i in range(img.shape[0]):
        row_line = 0
        if 0 in img[i]:
            num_row+=1
            while 0 in img[i]:
                row[row_line] = img[i]
                i += 1
                row_line += 1
        if 0 in img[i-1] and 0 not in img[i]:
            rows.append(row)
            row = np.full((row_height+1,img.shape[1]),255)  
        i += 1
    rows = np.array(rows,dtype=np.uint8)
    cv.waitKey(0)
    letter = np.full((row_height+1,row.shape[1]),255)
    letters = []
    num_letter = 0
    for row in rows:
        row = np.array(row)
        i = 0
        while i in range(row.shape[1]):
            letter_line = 0
            if 0 in row[:,i]:
                num_letter += 1
                while 0 in row[:,i] and i<row.shape[1]-1: 
                    letter[:,letter_line] = row[:,i]
                    i+=1
                    letter_line+=1
            if 0 in row[:,i-1] and 0 not in row[:,i]:
                letters.append(letter)
                letter = np.full((row_height+1,row.shape[1]),255)
            i += 1

    letters = np.array(letters,dtype=object)
    letters = np.array(letters,dtype=np.uint8)
    
    for i in range(letters.shape[0]):
        for j in range(letters[i].shape[1]):
            if 0 not in letters[i,:,j]:
                Letter = letters[i,:,:j]
                cv.imwrite(f'{PATH}{10000+i}.jpg',Letter)
                break
def train(sample, datapath) : 
    data = [os.path.join(datapath,f) for f in os.listdir(datapath)]
    min = 10000
    i = 10000
    j = 32
    for x in data :
        source = np.load(x)
        d = dist(sample,source)
        if d < min :
            min = d
            j = (i-10000)%94+33
        i+=1
    return chr(j)