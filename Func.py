import numpy as np
import os.path
from Detection import detect, train

def func(img) :
    detect('test/',img)
    test = [os.path.join('test/',f) for f in os.listdir('test/')]
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
        x = np.load(x)
        char = train(x,'dataset/')
        key = key + char  
    for x in test :
        os.remove(x)
    return(key)