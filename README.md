# polynomial_product_by_matrix

Let a(x) a polynomial with m coefficients A = [a0, a1, a2, ..........., am-2, am-1], size m, degree deg1 = m-1

Let b(x) a polynomial with n coefficients B = [b0, b1, b2, ..........., bn-2, bn-1], size n, degree deg2 = n-1

Assuming m >= n, we swap A, B in the function if not !

The product will have degrree_max = deg1 + deg2 which give the numbers of rows of the matrix M.

From row m of the matrix, we have to add zeros to A (A extended) to fit with all degrees exceeding deg1.

As the number of columns of this matrix is equal to deg2, each column will contain A extended with a rotation by one for the next one.

To get the product a(x).b(x), we have to create a matrix M with shape (degree_max, deg2). 

On the right, I show a column vector with n coeeficients of B.


|Matrix M|     0|  1|  2|  3| .............| n-1| dot |B|
|-----|:------:|------:| ------:|------:|------:|------:|---:|---:|
|**0**|     a0|  0|  0|  0| .............| 0|   |b0|
|**1**|     a1|  a0|  0|  0| .............| 0| |b1|
|**2**|     a2|  a1|  a0|  0| .............| 0 | |b2|
|**3**|     a3|  a2|  a1|  a0| .............| 0|   |.|
|**4**|     a4|  a3|  a2|  a1| .............| 0| |.|
|.|     .|  .|  .|  .| .............| 0||bn-3|
|.|     .|  .|  .|  .| .............| 0||bn-2|
|**m-1**|     am-1|  am-2|  am-3|  am-4| .............| a0| |bn-1|
|**m**|     0|  am-1|  am-2|  am-3| .............| a1|
|**m+1**|     0|  0|  am-1| am-2| .............| a2|
|**m+2**|     0|  0|  0|  am-1| .............| a3|
|.|     0|  0|  0|  0| .............| .| 
|.|     0|  0|  0|  0| .............| .| 
|**m+n-2**|     0|  0|  0|  0| .............| am-2| 
|**m+n-1**|  0|   0|    0|  0| .......... |am-1|

*Note that this matrix is composed by 2 triangular matrices.*

The dot product of M.B will give the coefficients of the polynomial product of a(x) and b(x) !
