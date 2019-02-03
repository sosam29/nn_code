import cv2
import numpy as np 
import os
import matplotlib.pyplot as plt


srcfname = "/Users/samuelsonawane/Downloads/UDEMY_ML/MachineVision/Codes/Course_codes_image/Image_2.jpg"
# if os.path.isfile(srcfname):
#     img = cv2.imread(srcfname)
#     cv2.imshow("Original", img)
#     print(img.shape)
# else:
#     raise "No such file exists"
#cv2.imshow("Original", img)
# cv2.waitKey()

# # gray = cv2.cvtColor(img,cv2.COLOR_BGR2BGRA)
# # cv2.imshow("Gray", gray)
# # cv2.waitKey()

# ret, threshold = cv2.threshold(img,50, 255, cv2.THRESH_BINARY)
# cv2.imshow("Threshold", threshold)
# cv2.waitKey()

# ret, threshold2= cv2.threshold(img,20, 255, cv2.THRESH_BINARY_INV)
# cv2.imshow("Threshold2", threshold2)
# print(ret)
# cv2.waitKey()

# ret, threshold3= cv2.threshold(img,0,0, cv2.THRESH_TRIANGLE)
# cv2.imshow("Threshold3", threshold3)
# print(ret)
# cv2.waitKey()

# ret,thresh1 = cv2.threshold(img,127,255,cv2.THRESH_BINARY)
# ret,thresh2 = cv2.threshold(img,127,255,cv2.THRESH_BINARY_INV)
# ret,thresh3 = cv2.threshold(img,127,255,cv2.THRESH_TRUNC)
# ret,thresh4 = cv2.threshold(img,127,255,cv2.THRESH_TOZERO)
# ret,thresh5 = cv2.threshold(img,127,255,cv2.THRESH_TOZERO_INV)
# titles = ['Original Image','BINARY','BINARY_INV','TRUNC','TOZERO','TOZERO_INV']
# images = [img, thresh1, thresh2, thresh3, thresh4, thresh5]
# for i in range(6):
#     plt.subplot(3,2,i+1),plt.imshow(images[i])
#     plt.title(titles[i])
#     plt.xticks([]),plt.yticks([])
# plt.show()

# img = cv2.medianBlur(img,5)
#print(img.shape)

img = cv2.imread(srcfname, cv2.CV_8UC1)

ret,th1 = cv2.threshold(img,100,255,cv2.THRESH_BINARY)
th2 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY_INV,11,2)
th3 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY_INV,11,5)
titles = ['Original Image', 'Global Thresholding (v = 100)',
            'Adaptive Mean Thresholding', 'Adaptive Gaussian Thresholding']
images = [img, th1, th2, th3]
for i in range(4):
    plt.subplot(2,2,i+1),plt.imshow(images[i],'gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])
plt.show()

# cv2.waitKey()
# cv2.destroyAllWindows()
