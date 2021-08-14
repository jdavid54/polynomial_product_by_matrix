import numpy as np

def rotate(l, n):
    return l[n:] + l[:n]

def make_mat(P1, P2):
    # get rid of zero end trail
    #P1 =  np.trim_zeros(P1, trim='b')
    #P2 =  np.trim_zeros(P2, trim='b')
    m = len(P1)
    n = len(P2)
    deg1 = m-1
    deg2 = n-1
    deg_max = deg1 + deg2
    # P1 must have bigger degree than P2
    if m < n:
        P1,P2 = P2,P1
        m=len(P1)
        n=len(P2)
    if deg_max > m: # add zero only if final max degree is more than number of coefficients of P1
        P1.extend([0]*(n-1))
    print('P1\n',P1)
    a = []
    for k in range(n): 
        a.append(rotate(P1,-k))
    a = np.array(a).T
    if deg_max <= m :
        a = np.tril(a)
    print('Matrix\n',a)
    print('P2\n',P2)
    b = np.array(P2).reshape(n,1)    
    c = np.dot(a,b).T 
    return a,b,c

A = [1,5,3,4,5,1,5,6,7]
B = [1,1]
matrix, b, c = make_mat(A, B)
print(c)
C = [0,0,0,0,0,0,1]

matrix, b, c = make_mat(A, C)
print(c)

A = [1,5,3]
B = [1,3]
matrix, b, c = make_mat(A, B)
print(c)
