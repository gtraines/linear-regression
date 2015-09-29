__author__ = 'graham'
import scipy as sp
import numpy as np
import matplotlib.pyplot as mpl

data = sp.genfromtxt("/home/graham/Downloads/JWHT_Fig2.1.Data.csv", delimiter=",")
x = data[:, 0]
y = data[:, 1]
group = data[:, 2]
# if 0 = blue, if 1 = orange
color = ["blue" if point == 0 else "orange" for point in group]

# 1. Get X and Y for each row. Remember that X is 2-d matrix of two cols and N rows.
X = np.matrix(np.column_stack((x, y)))
Y = np.matrix(group)
print "X dimensions"
print np.shape(X)

print "Y dimensions"
print np.shape(Y)
# 2. Get the (matrix) transpose of X
XT = np.transpose(X)
# XT = X.transpose()
print "XT"
print np.shape(X)
# 3. Get the dot product of X and its transpose
XTX = XT.dot(X)
#  XTX = np.dot(X, XT)
print "XTX dimensions"
print np.shape(XTX)
# 4. Get the inverse of the vector you obtained in step 3
XTX_inv = np.linalg.inv(XTX)  # XTX ** (-1)
print "XTX_inv dimensions"
print np.shape(XTX_inv)
# 5. Get the W vector as
W = XTX_inv * (XT * Y.transpose())  # XTX_inv * XT * y
# 6. Get the transpose of  W
WT = W.transpose()
print "W-Transpose"
print WT
# 7. Finally with the W Vector, you have the parameters that you need to draw the line
# displayed in Fig 2.1 that sort of separates the data. As you  hopefully already surmised this is not a good separation.

# If you do the steps above correctly you may get W values that approximate to:
#  w_Vector[0] =  0.086
#  w_Vector[1] =  0.399

print WT[0,0]
print WT[0,1]
linY = [((WT[0, 0] * p) + WT[0, 1]) for p in x]

mpl.plot(x, linY)

mpl.scatter(x,
            y,
            c=color)
mpl.title("Fig 2.1 Linear Regression of 0/1 Response")
mpl.xlabel("Column 1")
mpl.ylabel("Column 2")
mpl.autoscale(tight=True)
mpl.grid()
mpl.show()







