##########################################################################
#------------------------------------------------------------------------#
#
#         |
#         |       
#         |      P1.(x, y)
# |       |
# |       |			   P2.(tx, ty)
# y    |  |
# |    ty |
# |    |  |______________________
# M(cx,cy) ---x---
#		   ------y------
#s
#	tx-cx = rcos(ẞ) (1)
#	ty-cy = rsin(ẞ) (2)
#	ẞ : Angle between |MP2| and x axis 
#	
#	x-cx = cos(angle+ẞ) = cosẞcos30 - sinẞsin30
#	y-cy = sin(angle+ẞ) = sinẞcos30 + cosẞsin30
#
#	Now we will use equation (1) and (2) instead of cos(ẞ) and sin(ẞ) 
#
#	x-cx = (tx-cx)cos30 / r + (ty-cy)sin30 / r
#	y-cy = (ty-cy)cos30 / r + (tx_cx)sin30 / r
#
# For questions: konanomer@gmail.com
#
#------------------------------------------------------------------------#
##########################################################################

import math

def point_position(turned_p1, center, r, angle=30):

	cx, cy = center
	tx, ty = turned_p1

	cosa = float(cos(angle))
	sina = float(sin(angle))

	print(cosa)
	print(sina)

	x = ((tx-cx)/r)*cosa - ((ty-cy)/r)*sina + cx
	y = ((ty-cy)/r)*cosa + ((tx-cx)/r)*sina + cy

	point = x, y

	return point

def cos(angle):

	radians = math.radians(angle)
	cosa = math.cos(radians)
	#cosa = round(cosa,2) #Uncomment if you want two digit after comma
	return cosa

def sin(angle):

	radians = math.radians(angle)
	sina = math.sin(radians)
	#sina = round(sina,2) #Uncomment if you want two digit after comma
	return sina


"""
#######TEST_CODE#######
#---------------------#

def main():

	pt = (5,1)
	center = (0,0)
	r = 5

	point = point_position(pt, center, r)

	print(point)

if __name__ == "__main__":
	main()

#---------------------#
#######################
"""