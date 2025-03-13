## Eigenvalues and Matrix Properties

### Magical Properties of Eigenvalues
1. **Sum of Eigenvalues**:
   - The sum of the eigenvalues equals the **trace** of the matrix (the sum of diagonal entries).
2. **Product of Eigenvalues**:
   - The product of the eigenvalues equals the **determinant** of the matrix.

### Why Are These Properties Magical?
- Eigenvalues depend on matrix entries in a complex and nonlinear way.
- Small changes in matrix entries can lead to dramatic changes in eigenvalues or the spectrum structure.
- Despite this complexity, these properties hold universally for all matrices (excluding defective or complex eigenvalue cases, for which further discussion occurs later).

---

### Characteristic Polynomial of a Matrix
1. **Definition**:
   - To find eigenvalues, subtract $\lambda$ from each diagonal entry of matrix $A$, forming $A - \lambda I$, and evaluate its determinant.
   - This corresponds to solving the equation $\det(A - \lambda I) = 0$, where $\lambda$ represents eigenvalues.

2. **Expansion**:
   - The determinant of $A - \lambda I$ results in a **characteristic polynomial**:
   $$
   P(\lambda) = c_0 \lambda^n + c_1 \lambda^{n-1} + \dots + c_n,
   $$
   where $n$ is the dimension of the matrix.

3. **Key Coefficients**:
   - **Leading Coefficient ($c_0$)**:
     - $+1$ if $n$ is even, $-1$ if $n$ is odd.
   - **Second Coefficient ($c_1$)**:
     - Related to the **trace**: $-($trace$)$ when $n$ is even, $+$trace when $n$ is odd. 
   - **Free (constant) Term ($c_n$)**:
     - Equals the **determinant** of the matrix.

### Example of Component Extraction
- Consider a matrix $A$, expanded polynomial has roots as eigenvalues:
  $$
  P(\lambda) = (\lambda - \lambda_1)(\lambda - \lambda_2) \dots (\lambda - \lambda_n)
  $$

---

### Algebraic Properties of Eigenvalues

1. **Sum of Eigenvalues**:
   - The sum of the eigenvalues corresponds to the coefficient of $\lambda^{n-1}$, matching the trace of the matrix.
   - Algebraic Derivation:
     - Expand:
     $$
     (\lambda - a_{11})(\lambda - a_{22}) \dots (\lambda - a_{nn})
     $$
     Each eigenvalue contributes to the trace $a_{ii}$, which equals the sum of eigenvalues.

2. **Product of Eigenvalues**:
   - The product of eigenvalues equals the determinant of the matrix.
   - Algebraic Validation:
     - Plug $\lambda = 0$ into the characteristic polynomial:
     $$
     P(0) = \det(A - 0\cdot I) = \det(A)
     $$

3. **Signs of Coefficients**:
   - Parity (odd/even dimension $n$) determines coefficient signs:
       - Leading Coefficient is $+/-1$.
       - Second Coefficient alternates sign based on matrix dimension.

---

### Summary
- Universal properties linking the eigenvalues to matrix entries:
  - **Sum of eigenvalues** = Trace of the matrix.
  - **Product of eigenvalues** = Determinant of the matrix.
- These properties are profound algebraic results holding under very general circumstances (excluding defective or complex eigenvalue cases).
- They are derived purely algebraically in a manner that is both simple and beautiful.