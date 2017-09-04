# distortion_correction
Codes used alongside the MatLab Calib_Results tool for image distortion correction

#perspective_correction
Python code used to adjust tangential perspective distortions of an image. Edit the curront cornet locations, desired cornet locations and desired final image size, then run the script.

# chessboard_coefficients.py

This script finds the camera matrix and correction coefficients, you select an image of chessboard style. You must:
1. Choose a chessboard image. Count the number of sqaures that form the grid inside the outer-most squares. (i.e. the ouer-most square are just the border)
2. Edit lines 19 and 44 with the name of the chessboard image (saved to the same directory as the script)
3. Edit lines 11 & 12 with the number of interior square across and number of interior squares down in your test image

For example, if you use the chessboard1.png image with the current versions of the script, there are 9 interior squares across and 6 interior squares down.

The output of this script is the camera matrix, distortion coefficients, the rotation vecotrs and teh translation vectors.

# chessboard_correction.py

Edit teh values of K and d with the camera matrix and distortion coefficients respectively. These can be determined using the chessboard_coefficients script. Also edit the image name & directory (if required).

