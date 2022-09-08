import cv2
import numpy as np
import os.path
from PIL import Image
from Detection import writedata
def traindata() :
    #writedata('dataset/','data.jpg')
    #writedata('exception/','data_exception.jpg')
    recognizer = cv2.face.LBPHFaceRecognizer_create()
    exceptions = cv2.face.LBPHFaceRecognizer_create()
    path = 'dataset/'
    def getImageWithId(path):
        imagepath= [os.path.join(path,f) for f in os.listdir(path)]
        chars = []
        IDs = []
        for x in imagepath:
            charimg = Image.open(x).convert('L')    
            char = np.array(charimg,'uint8')
            id = int(x.split('/')[1].split('.')[0])
            id = (id-10000)%94+33
            chars.append(char)
            IDs.append(id)
        return chars,IDs
    chars,Ids=getImageWithId(path)
    exp,ids = getImageWithId('exception/')
    exceptions.train(exp,np.array(ids))
    recognizer.train(chars,np.array(Ids))
    if not os.path.exists('recognizer'):
        os.makedirs('recognizer')
    recognizer.save('recognizer/trainningData.yml')
    exceptions.save('recognizer/exception.yml')
