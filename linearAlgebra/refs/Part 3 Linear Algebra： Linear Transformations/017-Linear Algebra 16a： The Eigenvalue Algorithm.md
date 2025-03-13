## Eigenvalue Algorithm Notes

### 1. Introduction to Eigenvalue Algorithm

- The goal is to find eigenvalues ($\lambda$) and eigenvectors of a linear transformation or matrix.
- **Problem setup**: Typically, there are more unknowns (eigenvalues + eigenvectors) than equations, leading to a system where non-unique solutions are expected.

---

### 2. Key Observations on Nullspaces

- Eigenvectors are **non-trivial vectors** (non-zero).
- The eigenspace corresponding to an eigenvalue is the nullspace of $(A - \lambda I)$:
  $$
  (A - \lambda I) \mathbf{v} = 0
  $$
- **Nullspaces** are not necessarily one-dimensional; for certain eigenvalues, they could be multi-dimensional, forming eigenspaces of the matrix.

---

### 3. Eigenvalues $\lambda$ and Eigenvectors $\mathbf{v}$

#### Deriving $\lambda$:
1. Begin with the equation:
   $$
   A \mathbf{v} = \lambda \mathbf{v}
   $$
   or equivalently:
   $$
   (A - \lambda I) \mathbf{v} = 0
   $$

2. For **non-trivial solutions**, the determinant of $(A - \lambda I)$ must be zero:
   $$
   \text{det}(A - \lambda I) = 0
   $$

3. Solve the **characteristic equation** (from the determinant) to find the eigenvalues $\lambda$.

#### Deriving $\mathbf{v}$:
1. For each eigenvalue $\lambda_i$, substitute $\lambda_i$ into $(A - \lambda I) \mathbf{v} = 0$.
2. Solve for the nullspace of $(A - \lambda_i I)$ to find eigenvectors $\mathbf{v}$.
3. If the nullspace is multi-dimensional, the solution represents a subspace (basis of the eigenspace).

---

### 4. Example Walkthrough

#### Example System:
Suppose we have a matrix:
$$
A = \begin{bmatrix} 
2 & 1 \\ 
1 & 2 
\end{bmatrix}.
$$

1. **Rewrite System**:
   Convert the system to standard eigenvalue form:
   $$
   A \mathbf{v} = \lambda \mathbf{v} 
   \quad \implies \quad 
   (A - \lambda I) \mathbf{v} = 0.
   $$

   Expand:
   $$
   (A - \lambda I) = 
   \begin{bmatrix}
   2 - \lambda & 1 \\
   1 & 2 - \lambda
   \end{bmatrix}.
   $$

2. **Characteristic Equation**:
   Find the determinant of $(A - \lambda I)$:
   $$
   \text{det}(A - \lambda I) = 
   \begin{vmatrix}
   2 - \lambda & 1 \\
   1 & 2 - \lambda
   \end{vmatrix}.
   $$
   
   Compute:
   $$
   \text{det}(A - \lambda I) = (2 - \lambda)(2 - \lambda) - (1)(1) = \lambda^2 - 4\lambda + 3.
   $$

   Set determinant to zero:
   $$
   \lambda^2 - 4\lambda + 3 = 0 \quad \implies \quad (\lambda - 3)(\lambda - 1) = 0.
   $$
   
   **Eigenvalues**:
   $$
   \lambda_1 = 1, \quad \lambda_2 = 3.
   $$

3. **Eigenvectors**:
   - For $\lambda = 1$:
     Substitute $\lambda = 1$ into $(A - \lambda I) \mathbf{v} = 0$:
     $$
     \begin{bmatrix}
     2 - 1 & 1 \\
     1 & 2 - 1
     \end{bmatrix}
     \begin{bmatrix}
     x \\ y
     \end{bmatrix}
     = 0.
     $$

     Simplify:
     $$
     \begin{bmatrix}
     1 & 1 \\ 
     1 & 1
     \end{bmatrix}
     \begin{bmatrix}
     x \\ y
     \end{bmatrix}
     = 0 \quad \implies \quad x + y = 0.
     $$

     Eigenvector:
     $$
     v_1 = \begin{bmatrix} 1 \\ -1 \end{bmatrix}.
     $$

   - For $\lambda = 3$:
     Substitute $\lambda = 3$ into $(A - \lambda I) \mathbf{v} = 0$:
     $$
     \begin{bmatrix}
     2 - 3 & 1 \\
     1 & 2 - 3
     \end{bmatrix}
     \begin{bmatrix}
     x \\ y
     \end{bmatrix}
     = 0.
     $$

     Simplify:
     $$
     \begin{bmatrix}
     -1 & 1 \\ 
     1 & -1
     \end{bmatrix}
     \begin{bmatrix}
     x \\ y
     \end{bmatrix}
     = 0 \quad \implies \quad -x + y = 0.
     $$

     Eigenvector:
     $$
     v_2 = \begin{bmatrix} 1 \\ 1 \end{bmatrix}.
     $$

4. **Final Eigenvalue-Eigenvector Pairs**:
   $$
   \lambda_1 = 1, \, v_1 = \begin{bmatrix} 1 \\ -1 \end{bmatrix};
   \quad
   \lambda_2 = 3, \, v_2 = \begin{bmatrix} 1 \\ 1 \end{bmatrix}.
   $$

---

### 5. Eigenvalue Algorithm Summary

1. **Subtract $\lambda$ from the diagonal**:
   $$
   A - \lambda I.
   $$

2. **Find determinant and solve for $\lambda$**:
   $$
   \text{det}(A - \lambda I) = 0 \quad \implies \quad \lambda_i \text{ (eigenvalues)}.
   $$

3. **Solve for eigenvectors**:
   For each eigenvalue $\lambda_i$, solve the nullspace of $(A - \lambda_i I)$:
   $$
   (A - \lambda_i I) \mathbf{v} = 0 \quad \implies \quad v_i.
   $$

4. **Interpret Results**:
   - Eigenvalues represent "scaling factors."
   - Eigenvectors represent the directions that remain unchanged under the transformation (up to scaling).

5. **Potential Challenges**:
   - Higher-order systems (e.g., $4\times4$ matrices) may involve complex roots or polynomials that are computationally challenging to solve.
   - Utilize numerical methods or computers for such cases. 

---

### 6. Additional Properties

- For a matrix $A$ with eigenvalues $\lambda_1, \lambda_2, \dots$, the determinant of $A$ is:
  $$
  \text{det}(A) = \lambda_1 \lambda_2 \dots \lambda_n.
  $$

- Trace of $A$ (sum of diagonal elements) equals the sum of eigenvalues:
  $$
  \text{Tr}(A) = \lambda_1 + \lambda_2 + \dots + \lambda_n.
  $$

