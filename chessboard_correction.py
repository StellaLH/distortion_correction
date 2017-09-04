import numpy as np
import cv2
from matplotlib import pyplot as plt


K=np.array([[  5.10260934e+03 ,  0.00000000e+00,   7.58249618e+02],
 [  0.00000000e+00  , 2.36891166e+03 ,  5.46932220e+02],
 [  0.00000000e+00,   0.00000000e+00 ,  1.00000000e+00]]
)



# Define distortion coefficients d
d = np.array([[ -8.45353906e-02 ,  3.44200997e+00 ,  1.88306510e-03 , -3.70174586e-04,
   -4.78820505e+01]]
)



# Read an example image and acquire its size
img = cv2.imread("chessboard1.png")
h, w = img.shape[:2]

# Generate new camera matrix from parameters
newcameramatrix, roi = cv2.getOptimalNewCameraMatrix(K, d, (w,h), 0)

# Generate look-up tables for remapping the camera image
mapx, mapy = cv2.initUndistortRectifyMap(K, d, None, newcameramatrix, (w, h), 5)

# Remap the original image to a new image
newimg = cv2.remap(img, mapx, mapy, cv2.INTER_LINEAR)

# Display old and new image
fig, (oldimg_ax, newimg_ax) = plt.subplots(1, 2)
oldimg_ax.imshow(img)
oldimg_ax.set_title('Original image')
newimg_ax.imshow(newimg)
newimg_ax.set_title('Unwarped image')
#cv2.imshow('img',newimg)
plt.show()
