# polynomial_product_by_matrix

Let a(x) a polynomial with coefficients [a0, a1, a2, ..........., an], degree m-1

Let b(x) a polynomial with coefficients [a0, a1, a2, ..........., am], degree n-1,

let m >= n 

To get the product a(x).b(x) with degr_max m+n-2, we have to create a matrix (degre_max, n) as below :


  r\c     0  1  2  3 ............. n
  
  0      ao  0  0  0  0 ....... 0  0
  
  1      a1 a0  0  0  0 ........0  0
  
2      a2 a1 a0  0  0

3      a3 a2 a1 a0  0 ........0  0

.      a4 a3 a2 a1 a0 ........0  0

.                   .
.                   .
.                   .
.     am  am-1 am-2 ........a1  a0
.      0   0    0   ........a2  a1
.      0   0    0   ........a3  a2
.      0   0    0   ........a4  a3
.      0   0    0   ..........  a4
                   .
                   .
m+n-1  0   0    0   ..........  an-1
