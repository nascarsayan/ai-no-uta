# Problem 2: Dealing with Square Roots in Eigenvalues

### Goal of the Problem:
- Understand how to handle square roots when they appear in eigenvalues.

---

### Step-by-Step Solution:

1. **Subtracting λ from the diagonal**:
   - Start by subtracting $\lambda$ from the diagonal of the matrix.
   - Let a computer system compute the determinant (though it can be done manually for simplicity).
   - The determinant equation is:
     
     $$
     \lambda^2 - 4\lambda - 1
     $$

---

2. **Solving the Quadratic Equation**:
   - Solve the quadratic equation to find the eigenvalues $\lambda$:
     
     $$
     \lambda = 2 \pm \sqrt{2^2 + 1}
     $$
     
   - Simplify:
     
     $$
     \lambda = 2 \pm \sqrt{5}
     $$

---

3. **Working with the First Eigenvalue**:
   - The first eigenvalue is $2 - \sqrt{5}$.
   - Subtract $2 - \sqrt{5}$ from each diagonal entry in the matrix:
     
     - One entry becomes $-1 + \sqrt{5}$.
     - Another entry becomes $1 + \sqrt{5}$.

4. **Checking Matrix Singularity**:
   - Verify that the matrix is singular.
   - Methods to check:
     1. Compute the determinant of the matrix:
        
        - The determinant simplifies to $0$, confirming singularity.
     2. Check if the columns are linearly dependent:
        
        - Verify that dividing corresponding entries yields a consistent ratio.

---

5. **Finding the First Eigenvector**:
   - Form the eigenvector corresponding to the first eigenvalue:
   - After simplifications, the eigenvector becomes:
     
     $$
     \mathbf{v}_1 = \begin{bmatrix} 2 \\ -1 + \sqrt{5} \end{bmatrix}
     $$

   - Check consistency:
     - Multiply the original matrix by $\mathbf{v}_1$ and confirm the result satisfies the eigenvalue equation.

---

6. **Working with the Second Eigenvalue**:
   - The second eigenvalue is $2 + \sqrt{5}$.
   - Like before, subtract $2 + \sqrt{5}$ from the diagonal entries:
     
     - One entry becomes $-1 - \sqrt{5}$.
     - Another entry becomes $1 - \sqrt{5}$.

7. **Finding the Second Eigenvector**:
   - Form the eigenvector corresponding to the second eigenvalue:
   - After simplifications, the eigenvector becomes:
     
     $$
     \mathbf{v}_2 = \begin{bmatrix} 2 \\ -1 - \sqrt{5} \end{bmatrix}
     $$

   - Check consistency:
     - Repeat the verification process and ensure this eigenvector satisfies the eigenvalue equation.

---

### Final Results:
- The two **eigenvalues** are:
  $$
  \lambda_1 = 2 - \sqrt{5}, \quad \lambda_2 = 2 + \sqrt{5}
  $$
- The corresponding **eigenvectors** are:
  $$
  \mathbf{v}_1 = \begin{bmatrix} 2 \\ -1 + \sqrt{5} \end{bmatrix}, \quad
  \mathbf{v}_2 = \begin{bmatrix} 2 \\ -1 - \sqrt{5} \end{bmatrix}
  $$

---

### Key Takeaway:
- Eigenvalues and eigenvectors involving square roots can be handled without altering the fundamental algorithm.