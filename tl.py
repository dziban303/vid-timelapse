# python code
import cv2 as cv
import numpy as np
import sys
import argparse
# argparse to give help if not enough args passed
parser = argparse.ArgumentParser()
parser.add_argument("file",help = "filename of video")
a = sys.argv[1]
file = a
newfile = file
c=cv.VideoCapture(file)
r,m=c.read()
while(c.isOpened()):
    r,f=c.read()
    if(r==True):
        m=np.maximum(f,m)
    else:
        break
cv.imwrite("output.png",m)
