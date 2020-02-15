import cv2
import numpy as np

from circle_equ import *
#def find_points():
img = cv2.imread("./test_images/test10.jpg")
img = cv2.resize(img,(480,640))
gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, 1.2, 100)
if circles is not None:
	# convert the (x, y) coordinates and radius of the circles to integers
	circles = np.round(circles[0, :]).astype("int")
	print(circles)
	for x, y, r in circles:
		# draw the circle in the output image, then draw a rectangle
		# corresponding to the center of the circle
		cv2.circle(img, (x, y), r, (0, 255, 0), 4)
		cv2.circle(img, (x, y), 1, (255, 0, 0), 4)
		#cv2.rectangle(img, (x - 5, y - 5), (x + 5, y + 5), (0, 128, 255), -1)
	# show the output image
cv2.imshow("output", img)
cv2.waitKey(0)
"""edges = cv2.Canny(img,100,200)


hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
mask = cv2.inRange(hsv,(10, 50, 20), (25, 255, 255) )
print("mask\n", mask)


if np.any(edges[500,212] != [0]):
	print("tested1")
if np.any(edges[501,240] != [0]):
	print("tested2")
if np.any(edges[120,240] != [0]):
	print("tested3")

#print(edges[:,:])
bool_array = np.any(edges != [0], axis=-1)
#print(bool_array)
result = np.argwhere(bool_array==True)
#print("result:", result)
#cv2.imshow("test",img)
cv2.imshow("mask",edges)


p1 = (307, 427)
p2 = (501, 240)
p3 = (120,240)

x,y = circle_center(p1, p2, p3)
center = int(x), int(y)
radius = radius(center, p1)

print("center:",center)
print("radius:",radius)

cv2.circle(img, center,int(radius), (255,0,0), 3)
cv2.circle(img, (240,310), 1, (0,255,0), 5)
cv2.imshow("drawed",img)
cv2.waitKey(0)
"""
