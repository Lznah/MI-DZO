import cv2
import numpy as np
from matplotlib import pyplot as plt
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('path', help='Path to image')
args = parser.parse_args()

def magnitude_spectrum(im):
    f = np.fft.fft2(im)
    fshift = np.fft.fftshift(f)
    return 20*np.log(np.abs(fshift))


img = cv2.imread(args.path, 0)
m_img = magnitude_spectrum(img)
cv2.imwrite('fourier_'+args.path+'.png', m_img)