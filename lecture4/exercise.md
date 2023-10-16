# Algorithms 4 - exercises
### Exercise 1  
- a.
Use Strassen’s algorithm to compute the following matrix product (remember to keep track of the required number of multiplications and additions):
    - i.  
$$
\begin{pmatrix}
2 & 5\\
8 & 4
\end{pmatrix}
\begin{pmatrix}
3 & 1\\
6 & 2
\end{pmatrix}
$$
    - ii.
$$
\begin{pmatrix}
6 & 4 & 9 & 8\\
5 & 5 & 1 & 2\\
2 & 3 & 1 & 6\\
0 & 8 & 4 & 4\\
\end{pmatrix}
\begin{pmatrix}
4 & 4 & 2 & 5\\
2 & 8 & 1 & 2\\
1 & 5 & 0 & 2\\
7 & 5 & 3 & 9
\end{pmatrix}
$$

**Answer for i:**

```matlab
A11 = [2];
A12 = [5];
A21 = [8];
A22 = [4];
B11 = [3];
B12 = [1];
B21 = [6];
B22 = [2];
P = (A11 + A22)*(B11 + B22);
Q = (A21 + A22)*B11;
R = A11 * (B12 - B22);
S = A21 * (B21 - B11);
T = (A11 + A12) * B22;
U = (A21-A11)*(B11 + B12);
V = (A12-A22)*(B21+B22);
C11 = P+S-T+V;
C12 = R+T;
C21 = Q+S;
C22 = P+R-Q+U;
C = [C11 C12; C21 C22];
disp(C)
>> algorithms3exercise
    48    12
    60    16
```

Multiplications = 7 (P to V)

Addition = 12 (C11, C12, C21, C22)

**Answer for ii:**
```matlab
A11 = [6 4; 5 5];
A12 = [9 8; 1 2];
A21 = [2 3; 0 8];
A22 = [1 6; 4 4];
B11 = [4 4; 2 8];
B12 = [2 5; 1 2];
B21 = [1 5; 7 5];
B22 = [0 2; 3 9];
P = (A11 + A22)*(B11 + B22);
Q = (A21 + A22)*B11;
R = A11 * (B12 - B22);
S = A21 * (B21 - B11);
T = (A11 + A12) * B22;
U = (A21-A11)*(B11 + B12);
V = (A12-A22)*(B21+B22);
C11 = P+S-T+V;
C12 = R+T;
C21 = Q+S;
C22 = P+R-Q+U;
C = [C11 C12; C21 C22];
disp(C)
>> algorithms3exercise
    79   151    40   128
    77    59    21    55
    39    77    25    72
    80    88    20    60
```
Source: https://medium.com/@ananyasingh1618/strassens-multiplication-matrix-62bbb10225e6

Same amount of multiplication and addition as answer for **i.**

- b.
Write the pseudocode for Strassen’s algorithm. 

**Answer:**
```
n=A.rows
let C be  a  new n×n matrix 
if n==1
	c11​=a11​⋅b11​
else  partition A,B, and C
	let S1,​S2,​…, and S10​ be 10 new n/2×n/2 matrices
	let P1,​P2,​…, and P7​ be 7 new n/2×n/2 matrices

//  calculate  the  sum  matrices 

	S1​=B12​−B22​
	S2​=A11​+A12​
	S3​=A21​+A22​
	S4​=B21​−B11​
	S5​=A11​+A22​
	S6​=B11​+B22​
	S7​=A12​−A22​
	S8​=B21​+B22
​	S9​=A11​−A21​
	S10​=B11​+B12

​//  calculate  the  product  matrices 
	P1=Square-Matrix-Multiply-Strassen(A11,​S1)​
	P2=Square-Matrix-Multiply-Strassen(S2,​B22)
​	P3=Square-Matrix-Multiply-Strassen(S3,​B11)
​	P4=Square-Matrix-Multiply-Strassen(A22,​S4)
​	P5=Square-Matrix-Multiply-Strassen(S5,​S6)​
	P6=Square-Matrix-Multiply-Strassen(S7,​S8)
​	P7=Square-Matrix-Multiply-Strassen(S9,​S10)

​//  calculate  the  final  product  sub  matrices 
	C11​=P4​+P5​+P6​−P2​
	C12​=P1​+P2​
	C21​=P3​+P4​
	C22​=P1​+P5​−P3​−P7

return C​
```

- c.
Implement Strassen’s algorithm in any programming language of your choice. Test your implementation with the manually obtained results above.

**Answer:**
```python
import numpy as np  # You can use NumPy for matrix operations

def strassen_multiply(A, B):
    # Base case: If the matrices are 1x1, just multiply and return
    if len(A) == 1:
        return A * B

    # Split matrices into four equal-sized submatrices
    n = len(A)
    m = n // 2

    A11 = A[:m, :m]
    A12 = A[:m, m:]
    A21 = A[m:, :m]
    A22 = A[m:, m:]

    B11 = B[:m, :m]
    B12 = B[:m, m:]
    B21 = B[m:, :m]
    B22 = B[m:, m:]

    # Recursive steps
    P1 = strassen_multiply(A11 + A22, B11 + B22)
    P2 = strassen_multiply(A21 + A22, B11)
    P3 = strassen_multiply(A11, B12 - B22)
    P4 = strassen_multiply(A22, B21 - B11)
    P5 = strassen_multiply(A11 + A12, B22)
    P6 = strassen_multiply(A21 - A11, B11 + B12)
    P7 = strassen_multiply(A12 - A22, B21 + B22)

    # Compute the result submatrices
    C11 = P1 + P4 - P5 + P7
    C12 = P3 + P5
    C21 = P2 + P4
    C22 = P1 - P2 + P3 + P6

    # Combine the result submatrices to get the final result
    C = np.zeros((n, n))
    C[:m, :m] = C11
    C[:m, m:] = C12
    C[m:, :m] = C21
    C[m:, m:] = C22

    return C
```

### Exercise 2
- a. Generalize the MATRIX-MULTIPLY-RECURSIVE algorithm to multiply $n \times n$ matrices in which n is not necessarily an exact power of 2.

Løsning: 
By letting $m = 2^{⌈lg(n)⌉}$ and augmenting the $n × n$ matrix with zeros in the additional $(m−n)$ rows  and  columns,  we  can  effortlessly  apply  our  original  recursive  algorithm  to  the  new $m × m$ matrix where m is an exact power of 2:

- b. Give a recurrence describing its running time. 

Løsning:
It is the same because it pads the uneven matrices so they still divide by 2 so you still get your base case of 2x2

- c. Argues that it has $\Theta(𝑛^3)$ worst case time complexity.  

Løsning:
Because it's still the same recurrence it must have the same worst case time complexity still.

- d. Implement the generalized MATRIX-MULTIPLY-RECURSIVE algorithm in a. Does your implementation work as expected?

### Exercise 3
- a. Discuss the puzzle and the algorithm SIMPLE-HANOI-TOWER.
Does it make sense why this algorithm solves the puzzle?  
- b. Describe a divide-and-conquer algorithm for solving the problem.  
- c. How many moves do the algorithms in a. and b. for moving n disks in the Towers of Hanoi problem take?  

### Exercise 4
- a. Write the recurrence relation for the running time of algorithm fact.  
- b. Using the substitution method, solve the recurrence in a. 
- c. Prove that algorithm fact is correct. (Hint: use strong induction).  
- d. The following Python code implements algorithm fact.  
    - i. Is this implementation correct? If not, what is wrong with it.  
    - ii. Run the provided Python code (or an equivalent implementation in any programming language of your choice) with n = 100 as input? What is the result?  
    - iii. If the implementation in ii returns an error, modify the code to correct the error and re-run the algorithm with 𝑛 = 103, 𝑛 = 104, 𝑛 = 105 and 𝑛 = 106. How long does the algorithm take for each value of n. Does the growth agree with your 
    solution in b?  