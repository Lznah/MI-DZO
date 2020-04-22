import argparse

parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument('-g', type=int,
                    help='Gaussian blur')
parser.add_argument('-m', type=int,
                    help='Median blur')
parser.add_argument('-bp', type=int,
                    help='Brigtness Plus')
parser.add_argument('-bm', type=int,
                    help='Brigtness Minus')
parser.add_argument('-n', action='store_true',
                    help='Negative')
parser.add_argument('image_src',
                    help='Path to image')

args = parser.parse_args()


import cv2
import numpy as np

img = cv2.imread(args.image_src)

if args.n:
    img=255-img

if args.g:
    try:
        img=cv2.GaussianBlur(img,(args.g,args.g),0)
    except:
        print("Kernel size must be ODD")

if args.m:
    try:
        img=cv2.medianBlur(img,args.m)
    except:
        print("Kernel size must be ODD")

if args.bp:
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    h, s, v = cv2.split(hsv)
    lim = 255 - args.bp
    v[v > lim] = 255
    v[v <= lim] += args.bp
    final_hsv = cv2.merge((h, s, v))
    img = cv2.cvtColor(final_hsv, cv2.COLOR_HSV2BGR)

if args.bm:
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    h, s, v = cv2.split(hsv)
    lim = args.bm
    v[v < lim] = 0
    v[v >= lim] -= args.bm
    final_hsv = cv2.merge((h, s, v))
    img = cv2.cvtColor(final_hsv, cv2.COLOR_HSV2BGR)
    
cv2.imwrite("edited_"+args.image_src,img)