## Symmetric Property and Eigenvalue/Eigenvector Giveaways

### Symmetric Property Overview
- The symmetric property of a matrix plays a fundamental role in determining eigenvalues and eigenvectors.
- Symmetry provides useful shortcuts for understanding the eigenstructure of matrices, especially square symmetric matrices.

---

### Key Eigenvalue & Eigenvector Giveaways

#### 1. Row sums and eigenvalues:
- If all rows of a matrix add up to the same number:
  - That number is an eigenvalue.
  - The column vector of all ones is the corresponding eigenvector.

#### 2. Trace and determinant insights:
- Trace of a matrix equals the sum of its eigenvalues.
- If the matrix is singular (determinant = 0), at least one eigenvalue is 0.
- Any vector from the null space corresponds to the eigenvalue 0.

#### 3. Symmetric property of matrices:
- Symmetric matrices have orthogonal eigenvectors.
- Particularly for $2 \times 2$ matrices:
  - Knowing one eigenvector allows direct computation of the other (orthogonal to the first).

---

### Example: Applying the Symmetric Property

#### Matrix 1:
Given: 

$$
A = \begin{bmatrix} 2 & 2 \\ 2 & 2 \end{bmatrix}
$$

1. **Row Sum**:
   - Each row sums to 4.
   - Eigenvalue: $\lambda_1 = 4$.
   - Eigenvector: $\mathbf{v}_1 = \begin{bmatrix} 1 \\ 1 \end{bmatrix}$.

2. **Orthogonality for Second Eigenvector**:
   - The second eigenvector must be orthogonal to $\mathbf{v}_1$.
   - Orthogonal vector: $\mathbf{v}_2 = \begin{bmatrix} -1 \\ 1 \end{bmatrix}$.

3. **Trace Insight**:
   - Trace of $A = 4$.
   - Sum of eigenvalues: $\lambda_1 + \lambda_2 = 4$.
   - Since $\lambda_1 = 4$, $\lambda_2 = -2$.

Final Result:
- Eigenvalues: $\lambda_1 = 4$, $\lambda_2 = -2$.
- Eigenvectors: $\mathbf{v}_1 = \begin{bmatrix} 1 \\ 1 \end{bmatrix}$, $\mathbf{v}_2 = \begin{bmatrix} -1 \\ 1 \end{bmatrix}$.

---

#### Matrix 2:
Given: 

$$
B = \begin{bmatrix} 9 & 3 \\ 27 & 9 \end{bmatrix}
$$

1. **Singular Matrix**:
   - The second column is a scalar multiple of the first: $\mathbf{c}_2 = 3 \cdot \mathbf{c}_1$.
   - Eigenvalue: $\lambda_1 = 0$.
   - Corresponding eigenvector: $\mathbf{v}_1 = \begin{bmatrix} 3 \\ -1 \end{bmatrix}$ (from null space).

2. **Orthogonality for Second Eigenvector**:
   - The second eigenvector must be orthogonal to $\mathbf{v}_1$.
   - Orthogonal vector: $\mathbf{v}_2 = \begin{bmatrix} 1 \\ 3 \end{bmatrix}$.

3. **Trace Insight**:
   - Trace of $B = 18$.
   - Sum of eigenvalues: $\lambda_1 + \lambda_2 = 18$.
   - Since $\lambda_1 = 0$, $\lambda_2 = 18$.

Final Result:
- Eigenvalues: $\lambda_1 = 0$, $\lambda_2 = 18$.
- Eigenvectors: $\mathbf{v}_1 = \begin{bmatrix} 3 \\ -1 \end{bmatrix}$, $\mathbf{v}_2 = \begin{bmatrix} 1 \\ 3 \end{bmatrix}$.

---

### Verification of Eigenvalue-Eigenvector Pairs

#### For Matrix 2:
Verify $\mathbf{v}_2 = \begin{bmatrix} 1 \\ 3 \end{bmatrix}$ and $\lambda_2 = 18$:
- Multiply $B$ by $\mathbf{v}_2$:

$$
B \cdot \mathbf{v}_2 = \begin{bmatrix} 9 & 3 \\ 27 & 9 \end{bmatrix} \cdot \begin{bmatrix} 1 \\ 3 \end{bmatrix} = \begin{bmatrix} 9 \cdot 1 + 3 \cdot 3 \\ 27 \cdot 1 + 9 \cdot 3 \end{bmatrix} = \begin{bmatrix} 18 \\ 54 \end{bmatrix}.
$$

- Scale $\lambda_2$ times $\mathbf{v}_2$:

$$
\lambda_2 \cdot \mathbf{v}_2 = 18 \cdot \begin{bmatrix} 1 \\ 3 \end{bmatrix} = \begin{bmatrix} 18 \\ 54 \end{bmatrix}.
$$

Result:
- $B \cdot \mathbf{v}_2 = \lambda_2 \cdot \mathbf{v}_2$.
- Verification successful!

---

### Why the Symmetric Property Matters
- Symmetric matrices simplify eigenvector computation due to orthogonality.
- Symmetry enables direct "shortcuts" for finding eigenvalues and eigenvectors.
- Part of a robust toolkit for understanding matrix structure with minimal computation.