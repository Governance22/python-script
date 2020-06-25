# In[0]
import cv2

image = cv2.imread("C:/Users/farewell/Desktop/unnamed.jpg")

image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# In[1]

(thresh, blackAndWhiteImage) = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY)









# In[2]
blackAndWhiteImageS = cv2.resize(blackAndWhiteImage, ( x, y))                    # Resize image, ratio of width : x, ratio of height : y => fit in your screen
cv2.imshow('Result', blackAndWhiteImageS)
cv2.waitKey(0)                                                                   # Display the image infinitely until any keypress
