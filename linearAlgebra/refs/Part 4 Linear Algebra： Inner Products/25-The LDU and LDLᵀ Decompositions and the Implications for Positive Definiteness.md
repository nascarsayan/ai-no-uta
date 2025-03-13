## LU and LDL Transpose Decompositions

### LU Decomposition

Property:
- The **LU decomposition** splits a matrix into two triangular matrices: \( L \) (lower triangular) and \( U \) (upper triangular).
- By convention, \( L \) has **ones on the diagonal**.

Why is this the convention?
- This makes sense as \( L \) captures the steps of Gaussian elimination.
- When steps involve adding a multiple of one row to another, the corresponding elementary matrix has ones on the diagonal.

Result:
- The product of these elementary matrices results in \( L \), with ones on the diagonal.

### LD U Decomposition

Definition:
- The **LDU decomposition** involves a diagonal matrix \( D \), so the decomposition looks like \( A = LDU \) where:
  - \( D \) is diagonal.
  - \( L \) and \( U \) still retain their respective triangular structures.

Details:
- \( D \) can capture factors like squares or positive/negative values on the diagonal.
- \( U \) adjusts so \(\text{when combined back with } D\), the property of the original matrix is preserved.
  
Example:
- Factor a \( 3 \times 3 \) matrix with \( [4, 9, 25] \) on the diagonal:
  $$
  D = \begin{bmatrix} 4 & 0 & 0 \\ 0 & 9 & 0 \\ 0 & 0 & 25 \end{bmatrix}
  $$

### Symmetric Matrices and Special Cases:

#### LDL Transpose Decomposition
Property:
- For symmetric matrices, an interesting phenomenon occurs:
    - The \( L \) in \( LDL^T \) decomposition turns out to be the **transpose of \( U \)**.
  
Proof (Brief):
- Symmetric matrices result in \( LDL^T \), showing symmetry in its factorization.

Applications:
- Indicates the matrix is symmetric.
- Positive definiteness analysis can be performed using LDL decomposition.

#### Positive Definiteness
Definition:
- A matrix is **positive definite** if \( x^T A x > 0 \) for all non-zero \( x \).

Key Insights from Decompositions:
1. Using Gaussian elimination:
    - If **all pivots** during Gaussian elimination are **positive**, the matrix is positive definite.
    - A negative pivot indicates the matrix is not positive definite.
2. Diagonal matrices:
    - A diagonal matrix with positive entries is positive definite.
    - Zero entries indicate semi-definiteness.

### Quadratic Form Diagonalization

Purpose:
- Simplifies quadratic forms into sums of individual squares by diagonalizing the matrix.

Steps:
1. Multiply by \( L \) and \( L^T \) from decomposition, reducing the matrix into diagonal form.
2. The diagonal matrix results in individual squares.

Example Quadratic Form:
- After diagonalization:
  $$
  Q(x, y, z) = 4x^2 + 9y^2 + 25z^2
  $$

### Cholesky Decomposition

Property:
- A special case of matrix decomposition exclusively for **positive definite matrices**.

Steps:
1. Decompose as \( A = LL^T \), where \( L \) is triangular.
2. The diagonal entries of \( L \) are the **square roots** of the diagonal entries from the LDL decomposition.

Notes:
- This decomposition is "half a step away" from the LDL decomposition.
- Particularly useful for solving systems of linear equations efficiently.

