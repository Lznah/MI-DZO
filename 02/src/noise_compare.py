import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('gaussian_noise_rate30-butt.jpg',0)
img2 = cv2.imread('normal_noise_rate30-butt.jpg',0)
img3 = cv2.imread('monochromatic_normal_noise_rate30-butt.jpg',0)
img4 = cv2.imread('monochromatic_gaussian_noise_rate30-butt.jpg',0)

def magnitude_spectrum(im):
    f = np.fft.fft2(im)
    fshift = np.fft.fftshift(f)
    return 20*np.log(np.abs(fshift))

m_img = magnitude_spectrum(img)
m_img2 = magnitude_spectrum(img2)
m_img3 = magnitude_spectrum(img3)
m_img4 = magnitude_spectrum(img4)

plt.suptitle('Noise compare', fontsize=16)
plt.subplot(221),plt.imshow(m_img, cmap = 'gray')
plt.title('Gaussian noise'), plt.xticks([]), plt.yticks([])
plt.subplot(222),plt.imshow(m_img2, cmap = 'gray')
plt.title('Normal noise'), plt.xticks([]), plt.yticks([])
plt.subplot(223),plt.imshow(m_img4, cmap = 'gray')
plt.title('Monochromatic gaussian noise'), plt.xticks([]), plt.yticks([])
plt.subplot(224),plt.imshow(m_img3, cmap = 'gray')
plt.title('Monochromatic normal noise'), plt.xticks([]), plt.yticks([])
#plt.show()
plt.savefig("../results/noise_compare.png", dpi=300)
