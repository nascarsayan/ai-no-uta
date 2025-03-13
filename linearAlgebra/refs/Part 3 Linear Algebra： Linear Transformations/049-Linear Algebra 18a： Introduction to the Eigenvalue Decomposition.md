## Eigenvalue Decomposition

### Matrix Decomposition in Linear Algebra
- **Key Idea**: Every fundamental algorithm in linear algebra involves a matrix decomposition:
  - A central matrix in a problem is expressed as a product of two or more matrices.
  - For example:
    - **LU Decomposition**: Used for **Gaussian Elimination**.
    - **Eigenvalue Decomposition**: Used for the **Eigenvalue Algorithm**.

- **Applications**:
  - Study of eigenvalues and eigenvectors has **conceptual beauty** and **enormous practical applications**.
  - Example: **Google Search** uses **Singular Value Decomposition (SVD)** to process enormous matrices (e.g., $3 \times 10^6$ by $3 \times 10^6$).

---

### Eigenvalue Basics
#### Definitions:
1. **Eigenvalues ($\lambda$)**:
   - A scalar $\lambda$ satisfying $A v = \lambda v$ for a matrix $A$ and vector $v$.
2. **Eigenvectors ($v$)**:
   - The corresponding vector $v$ that does not get changed in direction under transformation by $A$.

#### Example:
- Consider a matrix $A$. Its eigenvalues and eigenvectors are determined algebraically:
    - Eigenvalues: $\lambda_1 = 7$, $\lambda_2 = 4$, $\lambda_3 = 3$.
    - Eigenvectors: 
        - $\lambda_1$: Corresponding vector $v_1$.
        - $\lambda_2$: Corresponding vector $v_2$.
        - $\lambda_3$: Corresponding vector $v_3$.

---

### Matrix Representation of Eigen Equations
#### Conversion from Vector Equations to Matrix Equations
- Suppose $A v_i = \lambda_i v_i$ for $i=1, 2, 3$. Combine all eigenvector equations into a single matrix equation:
  
$$
A X = X \Lambda
$$

Where:
- $A$: Original matrix.
- $X$: Matrix containing eigenvectors as columns:
  $$
  X = \begin{bmatrix} v_1 & v_2 & v_3 \end{bmatrix}
  $$
- $\Lambda$: Diagonal matrix of eigenvalues:
  $$
  \Lambda = \begin{bmatrix} 
  \lambda_1 & 0 & 0 \\ 
  0 & \lambda_2 & 0 \\ 
  0 & 0 & \lambda_3 
  \end{bmatrix}
  $$

---

### Eigenvalue Decomposition Formula
- Rearranging the matrix equation:
  
$$
A = X \Lambda X^{-1}
$$

#### Properties:
1. $X$: Matrix of eigenvectors (columns).
2. $\Lambda$: Diagonal matrix of eigenvalues.

#### Non-Commutativity:
- Matrix multiplication is **non-commutative**. Be mindful that:
  - $X \Lambda X^{-1} \neq X^{-1} \Lambda X$
  - Multiplying by the inverse inappropriately alters the row/column operations.

---

### **Concluding Notes:**
- **Utility of Eigenvalue Decomposition**:
  - Provides insight and simplification for matrix operations.
  - Basis for powerful computational tools (e.g., Google Search’s singular value decomposition).
- **Similarity Transformation**:
  - $A = X \Lambda X^{-1}$ represents a similarity transformation.
- Future discussions will explore deeper properties and uses of eigenvalue decompositions.