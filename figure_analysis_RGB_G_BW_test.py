# In[0]
import cv2

image = cv2.imread("C:/Users/farewell/Desktop/unnamed.jpg")

image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# In[1]

(thresh, blackAndWhiteImage) = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY)









# In[2]
cv2.imshow('Result', blackAndWhiteImage)
cv2.waitKey(0)