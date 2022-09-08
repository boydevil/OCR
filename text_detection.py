import cv2 as cv
import numpy as np

img = cv.imread('D:\\book.png',0)
# cv.imshow("",img)
# cv.waitKey(0)
# img = cv.resize(img,(600,800))
img = cv.fastNlMeansDenoising(img,None,10,7,21) # Lọc nhiễu
img = cv.fastNlMeansDenoising(img,None,10,7,21) # Lọc nhiễu
img = cv.adaptiveThreshold(img,255,cv.ADAPTIVE_THRESH_MEAN_C,cv.THRESH_BINARY,11,2) # Ngưỡng động

# cv.imshow("",img)
# cv.waitKey(0)
row_height = 0
for i in range(img.shape[0]-1):
    if 0 in img[i] and i < img.shape[0]-1:
        while 0 in img[i] and i < img.shape[0]-1:
            row_height+=1
            i+=1
        break

num_row = 0
rows = []
row = np.full((row_height+1,img.shape[1]),255)
print(row_height)
i = 0
while i in range(img.shape[0]):
    row_line = 0
    if 0 in img[i]:
        num_row+=1
        while 0 in img[i] and i < img.shape[0]-1:
            row[row_line] = img[i]
            i += 1
            row_line += 1
    if 0 in img[i-1] and 0 not in img[i]:
        rows.append(row)
        row = np.full((row_height+1,img.shape[1]),255)  
    i += 1
print("Số hàng của văn bản:",num_row)
rows = np.array(rows,dtype=np.uint8)
# print(len(rows))
# x = 40
# print(rows[3][:,x])
# cv.imshow("Display",rows[3][:,x:])
# cv.waitKey(0)
# print(img.shape)
# cv.imshow("1",img)
cv.waitKey(0)
letter = np.full((row_height+1,row.shape[1]),255)
letters = []
num_letter = 0
for row in rows:
    row = np.array(row)
    # print(row.shape)
    i = 0
    while i in range(row.shape[1]):
        # print(i)
        letter_line = 0
        if 0 in row[:,i]:
            # print(i)
            num_letter += 1
            while 0 in row[:,i] and i<row.shape[1]-1:
                # print(i)
                letter[:,letter_line] = row[:,i]
                i+=1
                letter_line+=1
        if 0 in row[:,i-1] and 0 not in row[:,i]:
            letters.append(letter)
            letter = np.full((row_height+1,row.shape[1]),255)
        i += 1

letters = np.array(letters,dtype=object)
letters = np.array(letters,dtype=np.uint8)
print(letters.shape[0])
for i in range(letters.shape[0]):
    for j in range(letters[i].shape[1]):
        if 0 not in letters[i,:,j]:
            Letter = letters[i,:,:j]
            # print(i)
            cv.imwrite('D:\\Output\\'+str(i)+'.png',Letter)
            break