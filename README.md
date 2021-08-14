# polynomial_product_by_matrix

Let a(x) a polynomial with m coefficients A = [a0, a1, a2, ..........., am-2, am-1], degree m-1

Let b(x) a polynomial with n coefficients B = [b0, b1, b2, ..........., bn-2, bn-1], degree n-1,

let m >= n 


To get the product a(x).b(x) with degr_max m+n-2, we have to create a matrix M (degre_max, n) as below :


|Matrix M|     0|  1|  2|  3| .............| n-1| +++++++ |B=coeff. bn in column|
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
