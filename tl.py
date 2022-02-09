# python code
import cv2 as cv
import numpy as np
c=cv.VideoCapture("iss-6feb.mp4")
r,m=c.read()
while(c.isOpened()):
    r,f=c.read()
    if(r==True):
        m=np.maximum(f,m)
    else:
        break
cv.imwrite("mp2.png",m)
