# polynomial_product_by_matrix

Let a(x) a polynomial with m coefficients A = [a0, a1, a2, ..........., am-2, am-1], size m, degree deg1 = m-1

Let b(x) a polynomial with n coefficients B = [b0, b1, b2, ..........., bn-2, bn-1], size n, degree deg2 = n-1,

let m >= n 

We have degree_max = deg1 + deg2 which give the numbers of rows of the matrix M.

From row m of the matrix, we add zeros to A to fit for degree exceeding (degree_max - deg1) 

To get the product a(x).b(x) with degree_max=m+n, we have to create a matrix M with shape (degree_max, n) 

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


Then the dot product of M.B will give the coefficients of the polynomial product of a(x) and b(x) !
