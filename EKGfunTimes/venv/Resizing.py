import cv2
import numpy
import PIL
import time
import math

dark_points = []
line_color = []

img = cv2.imread('ecg-sw2.png',0)
# print(img.shape[0])
# print(img.shape[1])
for i in range(img.shape[1]-1):
    scanImg = cv2.imread('ecg-sw2.png',0)
    print(scanImg[round(img.shape[0]*3/4),i])
    line_color.append(scanImg[round(img.shape[0]*3/4),i])
    scanImg = cv2.line(scanImg, (0,math.floor(img.shape[0]*3/4)), (img.shape[1],math.floor(img.shape[0]*3/4)), 0, 2)
    scanImg = cv2.line(scanImg, (i,0), (i,img.shape[0]), 0, 2)
    cv2.imshow('image2',scanImg)
    cv2.waitKey(1)
dark = numpy.average(line_color)

for i in range(img.shape[1]-1):
    scanImg = cv2.imread('ecg-sw2.png',0)
    print(scanImg[round(img.shape[0]*3/4),i])
    if scanImg[round(img.shape[0]*3/4),i]<=dark:
        dark_points.append((i,round(img.shape[0]*3/4)))
    scanImg = cv2.line(scanImg, (0,math.floor(img.shape[0]*3/4)), (img.shape[1],math.floor(img.shape[0]*3/4)), 0, 2)
    scanImg = cv2.line(scanImg, (i,0), (i,img.shape[0]), 0, 2)
    cv2.imshow('image2',scanImg)
    cv2.waitKey(1)
print(dark)
print(dark_points)