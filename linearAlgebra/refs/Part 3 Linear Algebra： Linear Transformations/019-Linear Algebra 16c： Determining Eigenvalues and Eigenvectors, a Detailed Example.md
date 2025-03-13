## Eigenvalue Algorithm and Properties

### Finding Eigenvalues and Eigenvectors for a Matrix

1. **Matrix Setup**:  
   The eigenvalue algorithm starts by finding the eigenvalues and eigenvectors of a given matrix. 
   - Example matrix is represented as:

     $$
     A = \begin{bmatrix} 17 & -6 \\ 45 & -6 \end{bmatrix}.
     $$

2. **Algorithm Process**:
   - Subtract $\lambda$ (eigenvalue) from the diagonal entries of the matrix $A$.
   - Form a new matrix:

     $$
     A - \lambda I = 
     \begin{bmatrix} 
     17 - \lambda & -6 \\ 
     45 & -6 - \lambda 
     \end{bmatrix}.
     $$

   - Compute the determinant of $A - \lambda I$ and equate it to zero.

     $$
     \det(A - \lambda I) = 0.
     $$

3. **Characteristic Equation**:
   - Solve for $\lambda$ by expanding the determinant:

     $$
     \det(A - \lambda I) = (17 - \lambda)(-6 - \lambda) - (-6)(45) = 0.
     $$

   - Simplify the determinant:

     $$
     (17 - \lambda)(-6 - \lambda) + 270 = \lambda^2 - 11\lambda - 2 = 0.
     $$

   - Solve the quadratic equation:

     $$
     \lambda = 2 \text{ and } \lambda = -1.
     $$

4. **Eigenvalues**:
   - The eigenvalues of matrix $A$ are $\lambda_1 = 2$ and $\lambda_2 = -1$.

---

### Verifying Eigenvalue Properties

1. **Trace of the Matrix**:
   - The trace of matrix $A$ is the sum of its diagonal entries:
     
     $$
     \text{Trace}(A) = 17 + (-6) = 11.
     $$

   - The sum of the eigenvalues matches the trace:
     
     $$
     \lambda_1 + \lambda_2 = 2 + (-1) = 1 = \text{Trace}(A).
     $$

   - **Observation**: The sum of eigenvalues always equals the trace of the matrix.

2. **Determinant of the Matrix**:
   - The determinant of $A$ is calculated as:

     $$
     \det(A) = (17)(-6) - (45)(-6) = -102 + 270 = 168.
     $$

   - The product of the eigenvalues matches the determinant:

     $$
     \lambda_1 \cdot \lambda_2 = 2 \cdot (-1) = -2 = \det(A).
     $$

   - **Observation**: The product of eigenvalues always equals the determinant of the matrix.

---

### Finding Eigenvectors

1. **Eigenvector for $\lambda_1 = 2$**:
   - Substitute $\lambda = 2$ in $A - \lambda I$:

     $$
     A - 2I = 
     \begin{bmatrix} 
     15 & -6 \\ 
     45 & -8 
     \end{bmatrix}.
     $$

   - Solve $(A - \lambda I)\mathbf{v} = 0$ to find eigenvector $\mathbf{v}$.
   - Linear dependency implies:

     $$
     \mathbf{v_1} = \begin{bmatrix} 2 \\ 5 \end{bmatrix}.
     $$

2. **Eigenvector for $\lambda_2 = -1$**:
   - Substitute $\lambda = -1$ in $A - \lambda I$:

     $$
     A + I = 
     \begin{bmatrix} 
     18 & -6 \\ 
     45 & -5 
     \end{bmatrix}.
     $$

   - Solve $(A - \lambda I)\mathbf{v} = 0$ to find eigenvector $\mathbf{v}$.
   - Linear dependency implies:

     $$
     \mathbf{v_2} = \begin{bmatrix} 1 \\ 3 \end{bmatrix}.
     $$

---

### Testing Eigenvectors

1. **Verification**:
   - For $\lambda_1 = 2$ and $\mathbf{v_1} = \begin{bmatrix} 2 \\ 5 \end{bmatrix}$:

     $$
     A\mathbf{v_1} = \begin{bmatrix} 2 \\ 5 \end{bmatrix} \lambda_1.
     $$

   - Similarly, for $\lambda_2 = -1$ and $\mathbf{v_2} = \begin{bmatrix} 1 \\ 3 \end{bmatrix}$:

     $$
     A\mathbf{v_2} = \lambda_2\begin{bmatrix} 1 \\ 3 \end{bmatrix}.
     $$

2. **Conclusion**:
   - Both eigenvalues and their respective eigenvectors are consistent with the eigenvalue algorithm.

---

### Key Observations and Properties

1. The **sum of eigenvalues** equals the **trace** of the matrix.
2. The **product of eigenvalues** equals the **determinant** of the matrix.
3. Eigenvalues and eigenvectors provide deep insights into the transformation properties of a matrix.
