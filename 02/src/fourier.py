import cv2
import numpy as np
from matplotlib import pyplot as plt
import argparse

parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument('path', help='Path to image')
args = parser.parse_args()

def magnitude_spectrum(im):
    f = np.fft.fft2(im)
    fshift = np.fft.fftshift(f)
    return 20*np.log(np.abs(fshift))


img = cv2.imread('butt.jpg',0)
img2 = cv2.imread(args.path,0)
m_img = magnitude_spectrum(img)
m_img2 = magnitude_spectrum(img2)

plt.suptitle(args.path, fontsize=16)
plt.subplot(221),plt.imshow(img, cmap = 'gray')
plt.title('Input Image'), plt.xticks([]), plt.yticks([])
plt.subplot(222),plt.imshow(m_img, cmap = 'gray')
plt.title('Magnitude Spectrum'), plt.xticks([]), plt.yticks([])
plt.subplot(223),plt.imshow(img2, cmap = 'gray')
plt.title('Edited Image'), plt.xticks([]), plt.yticks([])
plt.subplot(224),plt.imshow(m_img2, cmap = 'gray')
plt.title('Magnitude Spectrum'), plt.xticks([]), plt.yticks([])
plt.savefig("../results/"+args.path+".png", dpi=300)
