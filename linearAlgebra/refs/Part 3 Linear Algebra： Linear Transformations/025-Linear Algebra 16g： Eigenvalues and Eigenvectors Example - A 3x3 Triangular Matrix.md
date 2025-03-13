## Problem 4: Eigenvalues and Eigenvectors of a 3x3 Matrix

### Context
This problem deals with finding the eigenvalues and eigenvectors of a $3 \times 3$ matrix, specifically a **lower triangular matrix**. The analysis is straightforward due to properties of triangular matrices.

---

### Key Observations
1. **Triangular Matrices**: The eigenvalues of a triangular matrix (upper or lower) are located on the diagonal.
2. Simplifications:
   - Determinants for triangular matrices simplify, as only the diagonal entries contribute to the determinant's computation.
   - Eigenvectors can be calculated by analyzing the null space.

---

### Finding Eigenvalues
#### Step 1: Subtract $\lambda$ from the diagonal
Start by constructing the matrix $A - \lambda I$, where $A$ is the given matrix and $I$ is the identity matrix. For a diagonal or triangular matrix:
$$
\text{Det}(A - \lambda I) = (1 - \lambda)(-1 - \lambda)(2 - \lambda).
$$

#### Step 2: Eigenvalue Solutions
The determinant simplifies to a product of terms on the diagonal:
$$
\lambda_1 = 1, \quad \lambda_2 = -1, \quad \lambda_3 = 2.
$$

---

### Finding Eigenvectors
For each eigenvalue, compute the **null space** of the corresponding matrix $A - \lambda I$.

#### Eigenvector for $\lambda = 1$
1. The matrix:
   $$
   A - \lambda I = 
   \begin{bmatrix}
   0 & 2 & 0 \\
   0 & -2 & 3 \\
   0 & 0 & 1
   \end{bmatrix}
   $$
2. Null space calculation shows proportionality between the first two columns, leading to:
   $$\mathbf{v}_1 = \begin{bmatrix} 1 \\ 1 \\ 1 \end{bmatrix},$$
   which satisfies:
   $$
   A \mathbf{v}_1 = 1 \cdot \mathbf{v}_1.
   $$

#### Eigenvector for $\lambda = -1$
1. The matrix:
   $$
   A - \lambda I = 
   \begin{bmatrix}
   2 & 2 & 0 \\
   0 & 0 & 3 \\
   0 & 0 & 3
   \end{bmatrix}
   $$
2. Simplification gives:
   $$\mathbf{v}_2 = \begin{bmatrix} 0 \\ 1 \\ 1 \end{bmatrix},$$
   satisfying:
   $$
   A \mathbf{v}_2 = -1 \cdot \mathbf{v}_2.
   $$

#### Eigenvector for $\lambda = 2$
1. The matrix:
   $$
   A - \lambda I =
   \begin{bmatrix}
   -1 & 2 & 0 \\
   0 & -3 & 3 \\
   0 & 0 & 0
   \end{bmatrix}
   $$
2. Null space analysis leads to:
   $$\mathbf{v}_3 = \begin{bmatrix} 0 \\ 0 \\ 1 \end{bmatrix},$$
   satisfying:
   $$
   A \mathbf{v}_3 = 2 \cdot \mathbf{v}_3.
   $$

---

### Key Takeaways
1. For triangular matrices, the eigenvalues are always found on the diagonal.
2. The eigenvectors are determined by solving the null space for $A - \lambda I$, which, in triangular matrices, is relatively straightforward.
3. Final results:
   - **Eigenvalues**: $\lambda_1 = 1$, $\lambda_2 = -1$, $\lambda_3 = 2$.
   - **Eigenvectors**:
     $$
     \mathbf{v}_1 = \begin{bmatrix} 1 \\ 1 \\ 1 \end{bmatrix}, \quad
     \mathbf{v}_2 = \begin{bmatrix} 0 \\ 1 \\ 1 \end{bmatrix}, \quad
     \mathbf{v}_3 = \begin{bmatrix} 0 \\ 0 \\ 1 \end{bmatrix}.
     $$

--- 
