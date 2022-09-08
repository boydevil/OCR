import cv2
import os.path
from test import traindata
from Detection import writetrain
PATH = 'test/'

def func(image) :
    
    traindata()
    writetrain('test/',image)
    
    recognizer = cv2.face.LBPHFaceRecognizer_create()
    exceptions = cv2.face.LBPHFaceRecognizer_create()
    recognizer.read('recognizer/trainningData.yml')
    exceptions.read('recognizer/exception.yml')

    test = [os.path.join(PATH,f) for f in os.listdir(PATH)]
    tempkey = 0
    key = ''
    temprow = 0
    for x in test :
        id = int(x.split('/')[1].split('-')[0])
        row = int(x.split('/')[1].split('-')[1].split('_')[0])
        if tempkey != id :
            key += ' '
            tempkey = id
        if temprow != row :
            key += '\n'
            temprow = row
        x = cv2.imread(x,cv2.COLOR_BGRA2GRAY)
        id,confidence =recognizer.predict(x)
        if(confidence<100):
            ids,confiden=exceptions.predict(x)
            if confiden<60 : 
                if ids == 33 :
                    key = key + 'ff'
                if ids == 34 : 
                    key = key + 'ft'
            else : 
                key = key + chr(id)
    for x in test :
        os.remove(x)
    return(key)