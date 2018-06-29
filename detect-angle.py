#!/bin/python3

import numpy as np
import cv2 as cv2
import math
from scipy import ndimage
from matplotlib import pyplot as plt
import matplotlib.image as mpimg
import sys

if len(sys.argv) < 3 :
    print("Usage: python %s input.jpg output.jpg" % (sys.argv[0]))
    exit()

def captch_ex(file_name):
    img = cv2.imread(file_name)

    img_final = cv2.imread(file_name)
    img2gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    ret, mask = cv2.threshold(img2gray, 180, 255, cv2.THRESH_BINARY)
    image_final = cv2.bitwise_and(img2gray, img2gray, mask=mask)
    #cv2.imshow('Final', image_final)
    ret, new_img = cv2.threshold(image_final, 180, 255, cv2.THRESH_BINARY_INV)  # for black text , cv.THRESH_BINARY_INV
    cv2.imshow('New_Img', new_img);
    cv2.waitKey();
    '''
            line  8 to 12  : Remove noisy portion 
    '''
    # to manipulate the orientation of dilution , large x means horizonatally dilating  more, large y means vertically dilating more
    kernel = cv2.getStructuringElement(cv2.MORPH_CROSS, (3, 3))
    dilated = cv2.dilate(new_img, kernel, iterations=9)  # dilate , more the iteration more the dilation

    # for cv2.x.x

    _, contours, hierarchy = cv2.findContours(dilated, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)  # findContours returns 3 variables for getting contours

    # for cv3.x.x comment above line and uncomment line below

    #image, contours, hierarchy = cv2.findContours(dilated,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)


    for contour in contours:
        # get rectangle bounding contour
        [x, y, w, h] = cv2.boundingRect(contour)

        # Don't plot small false positives that aren't text
        if w < 35 and h < 35:
            continue

        # draw rectangle around contour on original image
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 255), 2)

        '''
        #you can crop image and send to OCR  , false detected will return no text :)
        cropped = img_final[y :y +  h , x : x + w]

        s = file_name + '/crop_' + str(index) + '.jpg' 
        cv2.imwrite(s , cropped)
        index = index + 1

        '''
    # write original image with added contours to disk
    cv2.imshow('captcha_result', img)
    cv2.waitKey()

#captch_ex(sys.argv[1]);
#cv2.waitKey()
#exit(0)

img_before = cv2.imread(sys.argv[1])
img_final = cv2.imread(sys.argv[1])
img2gray = cv2.cvtColor(img_before, cv2.COLOR_BGR2GRAY)
ret, mask = cv2.threshold(img2gray, 180, 255, cv2.THRESH_BINARY)
image_final = cv2.bitwise_and(img2gray, img2gray, mask=mask)
ret, new_img = cv2.threshold(image_final, 150, 255, cv2.THRESH_BINARY_INV)  # for black text , cv.THRESH_BINARY_INV

cv2.imwrite(sys.argv[1] + "_new_img.jpg", new_img)

image = mpimg.imread(sys.argv[1])
shape = image.shape
sigma=0.33

v = np.median(img_before)
lower = int(max(0, (1.0 - sigma) * v))
upper = int(min(255, (1.0 + sigma) * v))

edges = cv2.Canny(new_img,lower,upper, apertureSize=3)

cv2.imwrite(sys.argv[1] + "_edges.jpg", edges)
#cv2.imshow('canny_edge', img_edges)
key = cv2.waitKey(0)
angles = []


lines_image = img_before.copy()

lines = cv2.HoughLinesP(edges,1,np.pi/180, 80, 30, 10)
for k in range(0,len(lines)):
    for x1,y1,x2,y2 in lines[k]:
        angle = math.degrees(math.atan2(y2 - y1, x2 - x1))
        if angle != 0 and angle != 90 and angle != -90:
            print("Angle is %f" % angle)
            angles.append(angle)
            cv2.line(lines_image,(x1,y1),(x2,y2),(0,255,0),10)

cv2.imwrite(sys.argv[1] + "_houghlines.jpg", lines_image)

#cv2.imshow('After', img_before)
key = cv2.waitKey(0)

median_angle = np.median(angles)
print("Median angle is: %f" % median_angle)
img_rotated = ndimage.rotate(img_before, median_angle)

cv2.imwrite(sys.argv[2], img_rotated)
