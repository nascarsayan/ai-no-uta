## Constructing a Matrix with Prescribed Eigenvalues and Eigenvectors

### Problem Statement

- The goal is to construct a matrix with **given eigenvalues** and **eigenvectors**.
- While the eigenvalue algorithm helps determine eigenvalues and eigenvectors when given a matrix, here we reverse the process.

### Ingredients for the Solution

1. **Diagonal Matrices**:
   - Eigenvalues appear on the diagonal.
   - Corresponding eigenvectors are the standard basis vectors in $\mathbb{R}^n$, such as:
     $$
     \begin{bmatrix} 1 \\ 0 \\ 0 \end{bmatrix}, \quad 
     \begin{bmatrix} 0 \\ 1 \\ 0 \end{bmatrix}, \quad 
     \begin{bmatrix} 0 \\ 0 \\ 1 \end{bmatrix}.
     $$

2. **Similarity Transformation**:
   - For a matrix $D$ (diagonal), a similarity transformation maintains eigenvalues but allows flexibility in eigenvector alignment:
     $$
     A = X D X^{-1},
     $$
     where:
     - $D$ is the diagonal matrix with eigenvalues.
     - Columns of $X$ are the target eigenvectors.
   - This transformation ensures:
     - The eigenvalues of $A$ match those in $D$.
     - The eigenvectors of $A$ are columns of $X$.

### Strategy for Constructing the Matrix

1. Place the desired eigenvalues (e.g., $3, 7, -8$) on the diagonal of a diagonal matrix $D$:
   $$
   D = \begin{bmatrix}
   3 & 0 & 0 \\
   0 & 7 & 0 \\
   0 & 0 & -8
   \end{bmatrix}.
   $$

2. Choose a matrix $X$ whose columns are the desired eigenvectors, denoted as $v_1$, $v_2$, and $v_3$:
   $$
   X = \begin{bmatrix}
   | & | & | \\
   v_1 & v_2 & v_3 \\
   | & | & |
   \end{bmatrix}.
   $$

3. Compute $X^{-1}$ to perform the similarity transformation.

4. Calculate the matrix $A$ using:
   $$
   A = X D X^{-1}.
   $$

### Example: Constructing a Matrix

1. **Eigenvalues**: $3, 7, -8$.
2. **Eigenvectors** (arbitrarily chosen example):
   $$
   v_1 = \begin{bmatrix} 1 \\ 1 \\ 1 \end{bmatrix}, \quad
   v_2 = \begin{bmatrix} 2 \\ 1 \\ 0 \end{bmatrix}, \quad
   v_3 = \begin{bmatrix} -1 \\ -1 \\ 2 \end{bmatrix}.
   $$
3. Construct $X$ and compute $X^{-1}$.
4. Perform the similarity transformation:
   $$
   A = X D X^{-1}.
   $$

### Testing the Matrix

- Verify the matrix $A$ by checking:
  1. The eigenvalues match the desired eigenvalues.
  2. Multiplying $A$ by each eigenvector produces the eigenvalue-scaled eigenvector:
     $$
     A v_1 = 3 v_1, \quad A v_2 = 7 v_2, \quad A v_3 = -8 v_3.
     $$

### Additional Notes

- **Uniqueness**: The constructed matrix $A$ depends on the choice of $X$. Multiple $X$ matrices are possible if the eigenvectors are not unique.
- **Numerical Example with Computer**:
  - Use software to compute $X^{-1}$ and evaluate $A$.
  - Verify the eigenvalue and eigenvector conditions.

### Recap

- Diagonalize with given eigenvalues and use eigenvector columns for the similarity transformation.
- This ensures the resulting matrix $A$ preserves the prescribed eigenvalues and eigenvectors.

