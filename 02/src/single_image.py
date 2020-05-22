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


img = cv2.imread(args.path,0)
m_img = magnitude_spectrum(img)

plt.suptitle('Noise compare', fontsize=16)
plt.subplot(121),plt.imshow(img, cmap = 'gray')
plt.title('Gaussian noise'), plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(m_img, cmap = 'gray')
plt.title('Magnitude plane'), plt.xticks([]), plt.yticks([])
plt.show()