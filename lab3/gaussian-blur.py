import cv2
import numpy as np

def gaussianFilter(image, kernel):
    filteredImage = image.copy()
    offset = kernel.shape[0]//2
    for i in range(offset, filteredImage.shape[0]-offset):
        for j in range(offset, filteredImage.shape[1]-offset):
            filteredImage[i, j] = np.sum(filteredImage[i-offset:i+offset+1, j-offset:j+offset+1]*kernel)
    return filteredImage


def buildKernel(kernel_size, sigma):
    kernel = np.zeros((kernel_size, kernel_size))
    a = kernel_size // 2
    for x in range(kernel_size):
        for y in range(kernel_size):
            kernel[x, y] = (1/(2*np.pi*sigma**2))*np.exp(-((x-a)**2+(y-a)**2)/(2*sigma**2))
    return kernel

img = cv2.imread(r'C:\Users\bodya\PycharmProject\CompVisionLabs\img.jpg', 1)
cv2.namedWindow('grayscale image', cv2.WINDOW_FREERATIO)
grayscale = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
copy = grayscale.copy()
image_size = [grayscale.shape[0], grayscale.shape[1]]
print(image_size)
kernel_size = 7
sigma = 1.0
kernel = buildKernel(kernel_size, sigma)
print(kernel)
normalizedKernel = kernel/np.sum(kernel)
filteredImage = gaussianFilter(copy, normalizedKernel)
print(normalizedKernel)
print(np.sum(normalizedKernel))
gaussianBlurOpenCV = cv2.GaussianBlur(grayscale.copy(), (kernel_size, kernel_size), sigma)
cv2.imshow('OpenCV Gaussian Blur', gaussianBlurOpenCV)
cv2.imshow('grayscale image', grayscale)
cv2.imshow('filtered image', filteredImage)
cv2.waitKey(0)
cv2.destroyAllWindows()