## Properties of Symmetric Matrices

### Eigenvalues of Symmetric Matrices
1. When solving the eigenvalue problem for a general matrix, issues may arise:
   - **Complex eigenvalues:** Non-real eigenvalues for non-symmetric matrices.
   - **Defective matrices:** Eigenvalues may have algebraic multiplicities that exceed their geometric multiplicities.

2. For symmetric matrices, **these issues do not occur**. A symmetric matrix has:
   - Exactly **n real eigenvalues**.
   - **n linearly independent eigenvectors**.

3. **Theorem**: If a matrix is symmetric:
   - Eigenvalues are guaranteed to be real.
   - Geometric multiplicity equals algebraic multiplicity of each eigenvalue (no defects).

### Orthogonality of Eigenvectors
1. **Key Property**: Eigenvectors corresponding to distinct eigenvalues in symmetric matrices are orthogonal.

2. **Standard Inner Product**:
   - All calculations assume the **standard inner product** unless explicitly stated otherwise.

3. **Proof**:
   - Let $\mathbf{x}$ and $\mathbf{y}$ be eigenvectors corresponding to distinct eigenvalues $\lambda_1$ and $\lambda_2$, respectively.
   - Key algebraic relationship from eigenvector equations:
     $$
     A\mathbf{x} = \lambda_1 \mathbf{x}, \quad A\mathbf{y} = \lambda_2 \mathbf{y}
     $$
   - Perform manipulations:
     - Multiply the equation for $\mathbf{x}$ by $\mathbf{y}^T$ (transpose).
     - Multiply the equation for $\mathbf{y}$ by $\mathbf{x}^T$ (transpose).
     - Subtract the expressions to conclude that $\mathbf{x}^T\mathbf{y} = 0$, proving orthogonality.

#### General Case:
- For eigenvalues with multiplicities:
  - Eigenvectors corresponding to the same eigenvalue can **always be chosen to be orthogonal** using Gram-Schmidt orthogonalization.

### Eigenvalue Decomposition
1. **Eigenvalue Decomposition**:
   - For symmetric matrices, eigenvectors can be chosen to be **orthogonal** or even **orthonormal** (unit length).
   - This makes the matrix of eigenvectors ($X$) an **orthogonal matrix**, satisfying:
     $$
     X^T X = I \quad \text{(identity matrix)}
     $$
   - Eigenvalue decomposition formula:
     $$
     A = X \Lambda X^T
     $$
     - $X$: Matrix of orthonormal eigenvectors.
     - $\Lambda$: Diagonal matrix of eigenvalues.

2. **Importance**:
   - The orthonormal property allows $X^{-1} = X^T$, simplifying calculations.

### Positive Definiteness 
1. **Criterion for Positive Definiteness**:
   - A symmetric matrix $A$ is **positive definite** if *all eigenvalues are positive*.

   - Four equivalent criteria for positive definiteness:
     - $x^T A x > 0$ for all nonzero vectors $x$.
     - All principal **determinants** are positive.
     - All **pivots** during Gaussian elimination are positive.
     - All **eigenvalues** are positive.

2. **Implications of Eigenvalue Decomposition**:
   - Positive eigenvalues ensure positive definiteness due to the diagonal matrix in the decomposition:
     $$
     A = X \Lambda X^T
     $$
   - The diagonal entries of $\Lambda$ (eigenvalues) dictate the definiteness of $A$.

---

### Special Significance of Symmetric Matrices
1. **Unique Properties**:
   - Symmetric matrices exhibit remarkable properties, such as orthogonality of eigenvectors and real eigenvalues.
   - These properties make symmetric matrices particularly desirable in applications like optimization and physics.

2. **Positive Definite Symmetric Matrices**:
   - Combining symmetry and positive definiteness creates matrices with exceptional theoretical and practical importance.