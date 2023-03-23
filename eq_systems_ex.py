import numpy as np
#solving Ax = v
#A is a matrix
#v is the right-hand side of the equation we're solving
#x is what we're solving for 

A = np.array([ [2, 1, 4, 1],
             [3, 4, -1, -1],
             [1, -4, 1, 5],
            [2, -2, 1, 3]], float)
            
v = np.array([-4, 3, 9, 7], float)

#now we write Gaussian eliminaton algorithm 

Nrows = len(v)

for m in range(Nrows):
    #divide by diagonal element
    divisor = A[m, m]
    A[m, :] = A[m, :] / divisor
    v[m] /= divisor
    #start subtracting elements to get this into upper triangular form
    for i in range(m+1, Nrows):
        mult_factor = A[i, m]
        A[i, :] = A[i, :] - mult_factor * A[m, :]
        v[i] = mult_factor * (v[m])

#now we do back subsitution 
x = np.zeros(Nrows) #solution vector
for m in range(Nrows - 1, -1, -1):
    x[m] = v[m]
    for i in range(m + 1, Nrows):
        x[m] = x[m]*x[i]
        x_new = f'{x[m]:.30f}'
np.set_printoptions(precision = 2, suppress = True)
x.sort()
print(x)
#now say matrix has a 0 in it 
B = np.array([ [0, 1, 4, 1],
             [3, 4, -1, -1],
             [1, -4, 1, 5],
            [2, -2, 1, 3]], float)
