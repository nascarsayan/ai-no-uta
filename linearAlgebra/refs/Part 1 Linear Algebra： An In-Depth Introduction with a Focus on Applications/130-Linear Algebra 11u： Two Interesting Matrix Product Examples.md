## Matrix Multiplications with Surprising Results

### 1. Two Matrices Producing a Zero Matrix
- Matrix multiplication differs from the multiplication of ordinary numbers, where the product is zero only if at least one number is zero.
- Surprising result: Two non-zero matrices can produce a zero matrix.

#### Example:
Let matrices $A$ and $B$ be such that their multiplication results in zero:
$$
A = \begin{bmatrix} 1 & -2 \\ 3 & -6 \end{bmatrix}, \quad 
B = \begin{bmatrix} 2 & 4 \\ -1 & -2 \end{bmatrix}, \quad
A \cdot B = \begin{bmatrix} 0 & 0 \\ 0 & 0 \end{bmatrix}.
$$

### Explanation:
- The columns of $B$ lie in the null space of $A$. Hence, $A \cdot B$ yields the zero matrix.
- You could generate more examples by utilizing the basis vectors of the null space of a matrix and creating integer linear combinations.

---

### 2. Matrices Combining to Produce the Identity Matrix
#### Example:
Let matrices $P$ and $Q$ be such that their multiplication produces the identity:
$$
P = \begin{bmatrix} 2 & 1 \\ 4 & 3 \end{bmatrix}, \quad 
Q = \begin{bmatrix} 3 & -1 \\ -4 & 2 \end{bmatrix}, \quad
P \cdot Q = \begin{bmatrix} 1 & 0 \\ 0 & 1 \end{bmatrix}.
$$

### Key Insights:
- When two matrices multiply to produce the identity matrix, they are inverses of each other.
- Although Gaussian elimination may introduce fractions during computations, it's possible for the result to have integers only.

---

### 3. Generating Matrices with Integer Inverses

#### Triangular Matrices:
- Triangular matrices (upper or lower) with integer values have a special property: Their inverses also consist of integers.

##### Examples:
###### Upper Triangular Matrix:
$$
U = \begin{bmatrix} 1 & 2 & 3 \\ 0 & 1 & 4 \\ 0 & 0 & 1 \end{bmatrix}.
$$

###### Lower Triangular Matrix:
$$
L = \begin{bmatrix} 1 & 0 & 0 \\ 5 & 1 & 0 \\ -3 & 2 & 1 \end{bmatrix}.
$$

- Both $U$ and $L$ are guaranteed to have integer values in their inverses because of their structural properties. The inversion algorithm involves only integer operations.
  
#### Multiplying $U$ and $L$:
The product of two triangular matrices:
$$
UL = \begin{bmatrix} 1 & 2 & 3 \\ 5 & 11 & 19 \\ -3 & -7 & -12 \end{bmatrix}.
$$

- The inverse of $UL$ is guaranteed to also consist of integers.

---

### 4. Understanding the Inverse of a Product
The formula for the inverse of a product of matrices is:
$$
\text{Inverse}(UL) = L^{-1} \cdot U^{-1}.
$$

- If $U$ and $L$ both have integer inverses, $UL$ will also result in an inverse consisting entirely of integers.

---

### Summary:
Creating matrices with surprising multiplication results often requires clever use of:
1. **Null Spaces**: To achieve zero product outcomes.
2. **Triangular Matrices**: To ensure integer values in inverses.
3. **Integer Linear Combinations**: To obscure simplicity while maintaining integrity.

