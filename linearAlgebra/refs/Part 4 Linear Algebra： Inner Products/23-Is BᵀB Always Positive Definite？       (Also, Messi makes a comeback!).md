## Understanding the Symmetry and Definiteness of $B^\text{T}B$

### Properties of $B^\text{T}B$
- **Symmetric Matrix**: The product of $B^\text{T}B$ is always symmetric regardless of the shape of matrix $B$. Even if $B$ is not a square matrix, $B^\text{T}B$ will remain symmetric.
- **Definiteness**:
  - The matrix $B^\text{T}B$ is **positive semi-definite**.
  - It becomes **positive definite** **if and only if** the columns of $B$ are linearly independent.

---

### Proof of Positive Semi-Definiteness
To establish that $B^\text{T}B$ is positive semi-definite:
1. Consider the quadratic form $x^\text{T}Ax$, where $A = B^\text{T}B$ and $x$ is a non-zero vector.
2. Substitute $A = B^\text{T}B$, letting $y = Bx$. Then the quadratic form becomes:
    $$
    x^\text{T}(B^\text{T}B)x = (Bx)^\text{T}(Bx) = y^\text{T}y
    $$
3. Observe that $y^\text{T}y$ is the sum of squared entries in the vector $y$:
    - If $y = [y_1, y_2, \dots, y_n]$, then $y^\text{T}y = y_1^2 + y_2^2 + \dots + y_n^2$.
    - The sum of squares of the entries of $y$ is always $\geq 0$ (equal to 0 if $y = 0$).
4. For $x \neq 0$, $y$ can still be zero if $x \in \text{null space of } B$, which demonstrates that $x^\text{T}Ax \geq 0$.

Thus, $B^\text{T}B$ is positive semi-definite.

---

### Proof of Positive Definiteness
To establish that $B^\text{T}B$ is positive definite:
1. If the columns of $B$ are linearly independent:
   - $Bx$ is non-zero for any non-zero $x$.
   - Hence, $y^\text{T}y = \sum_{i} y_i^2 > 0$.
   - It follows that $x^\text{T}Ax > 0$ for all $x \neq 0$, meaning $A$ is positive definite.

2. If the columns of $B$ are linearly dependent:
   - There exists a non-zero vector $x \in \text{null space of } B$ such that $Bx = 0$.
   - For such an $x$, $x^\text{T}Ax = x^\text{T}B^\text{T}Bx = (Bx)^\text{T}(Bx) = 0$.
   - Thus, $A$ cannot be positive definite, but remains positive semi-definite.

---

### Counterexample for Positive Definiteness
Consider a singular matrix $B$:
$$
B =
\begin{bmatrix}
2 & 4 \\
1 & 2
\end{bmatrix}
$$
1. Compute $B^\text{T}B$:
   $$
   B^\text{T}B = 
   \begin{bmatrix}
   2 & 1 \\
   4 & 2
   \end{bmatrix}^\text{T}
   \begin{bmatrix}
   2 & 4 \\
   1 & 2
   \end{bmatrix}
   =
   \begin{bmatrix}
   5 & 10 \\
   10 & 20
   \end{bmatrix}
   $$
2. Check positive definiteness:
    - This matrix is symmetric.
    - However, $B$ has linearly dependent columns (second column is twice the first).
    - $B^\text{T}B$ is **positive semi-definite**, not positive definite.

---

### Summary
1. $B^\text{T}B$ is always symmetric.
2. **Positive semi-definiteness**:
   - $B^\text{T}B$ is positive semi-definite regardless of whether $B$ is singular or non-square.
3. **Positive definiteness**:
   - $B^\text{T}B$ is positive definite **if and only if** the columns of $B$ are linearly independent.

These properties are fundamental criteria for symmetric matrices in linear algebra and commonly encountered in applications such as eigenvalue problems, optimization, and decomposition methods.