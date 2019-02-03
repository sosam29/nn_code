import cv2
import numpy as np 
import os
import matplotlib.pyplot as plt


srcfname = "/Users/samuelsonawane/Downloads/UDEMY_ML/MachineVision/Codes/Cmage_processing_projects/Image_9.jpg"


img = cv2.imread(srcfname,0)

cv2.imshow("Original", img)

# histequ = cv2.equalizeHist(img)

# # res =np.hstack((img, histequ))
# cv2.imshow("Hist equlize", histequ)
# cv2.waitKey()  

# kernel = np.array([[-1,-1,-1],[-1,-9,-1],[-1,-1,-1]])

# sharp = cv2.filter2D(img, -1, kernel)
# cv2.imshow("sharpe", sharp)
# cv2.waitKey()  
# kernel = np.ones((5,5), np.uint8)

# erode =cv2.erode(img, kernel, iterations=1)
# cv2.imshow("Erosion", erode)

# cv2.waitKey()  

# dilate =cv2.dilate(img, kernel, iterations=1)
# cv2.imshow("Dilation", dilate)

# cv2.waitKey()  

edgy =cv2.Canny(img, 50, 200)
cv2.imshow("Edge Detect", edgy)

cv2.waitKey()  
#####
###imgray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
ret,thresh = cv2.threshold(img,127,255,0)
im2, contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)


# contours, hierarchy  = cv2.findContours(edgy, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)


print("The number of contours {0}".format(len(contours)))
# cv2.drawContours(img, contours, -1, (255,0,0),10)

for cnt in contours:
    rect = cv2.minAreaRect(cnt)
    box = cv2.boxPoints(rect)
    box = np.int8(box)
    img = cv2.drawContours(img,(box),0,(0.255,0),3)
# cv2.imshow("Contours", img)

plt.figure("Example 1")
plt.imshow(img)
plt.title("Binary contours in an image")
plt.show()

cv2.waitKey()  

cv2.destroyAllWindows()
# ret,th1 = cv2.threshold(img,100,255,cv2.THRESH_BINARY)
# th2 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY_INV,11,2)
# th3 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY_INV,11,5)
# titles = ['Original Image', 'Global Thresholding (v = 100)',
#             'Adaptive Mean Thresholding', 'Adaptive Gaussian Thresholding']
# images = [img, th1, th2, th3]
# for i in range(4):
#     plt.subplot(2,2,i+1),plt.imshow(images[i],'gray')
#     plt.title(titles[i])
#     plt.xticks([]),plt.yticks([])
# plt.show()
