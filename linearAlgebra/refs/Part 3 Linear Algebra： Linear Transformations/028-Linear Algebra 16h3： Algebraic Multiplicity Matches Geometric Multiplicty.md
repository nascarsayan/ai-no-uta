## Eigenvalues, Algebraic, and Geometric Multiplicities

### Key Concepts

- **Geometric Multiplicity**:
  - The dimension of the eigenspace corresponding to an eigenvalue.

- **Algebraic Multiplicity**:
  - The number of times the eigenvalue appears as a root of the characteristic polynomial.

### Geometric vs Algebraic Multiplicity

- Fundamental Question: 
  - Does the geometric multiplicity always match the algebraic multiplicity?
  - Not answered exhaustively here but explored through examples.

---

### Example Walkthrough

#### Given Eigenvalue: $\lambda = 2$

1. Compute the corresponding eigenvector:
   
   There is one eigenvector corresponding to $\lambda = 2$. This eigenvalue is "simple" in this example.

#### Repeated Eigenvalue: $\lambda = 3$

1. Subtract $\lambda = 3$ from the diagonal of the matrix.
2. Analyze the resulting matrix:

   - Its null space is **two-dimensional**.
   - Elements in the null space:
     - $\begin{bmatrix} 1 \\ 2 \\ 0 \end{bmatrix}$
     - $\begin{bmatrix} 0 \\ 0 \\ 1 \end{bmatrix}$
   - These correspond to eigenvectors of the matrix.

3. Conclusions:
   - The eigenspace corresponding to $\lambda = 3$ is two-dimensional.
   - Therefore, the geometric multiplicity of this eigenvalue is 2.

4. Eigenvectors:
   - From the null space, you can pick any two **linearly independent** vectors to represent the eigenspace:
     - Example:
       $$
       \begin{bmatrix} 1 \\ 2 \\ 0 \end{bmatrix} \quad \text{and} \quad \begin{bmatrix} 0 \\ 0 \\ 1 \end{bmatrix}
       $$
     - Other valid choices exist (e.g., $\begin{bmatrix} 1 \\ 2 \\ 1 \end{bmatrix}$ and $\begin{bmatrix} 0 \\ 0 \\ 1 \end{bmatrix}$).

5. Conclusion for $\lambda = 3$:
   - **Geometric multiplicity**: 2.
   - Matches **algebraic multiplicity**.

---

### Partial Conclusions

- In this example, **geometric multiplicity matches algebraic multiplicity** for both eigenvalues.
- This supports the idea that, in some cases, the two multiplicities are equal.

---

### Next Steps

- Question: Does geometric multiplicity always match algebraic multiplicity?
  - **Answer**: It happens **most of the time**.
  
---

### Special Case: Defective Matrices

1. **Defective Matrices**:
   - **Algebraic multiplicity** exceeds **geometric multiplicity**.
   - These matrices will be examined in future discussions.

2. **Geometric Multiplicity > Algebraic Multiplicity**:
   - **Answer**: This is **not possible**.

---

### Final Conclusions

- Two scenarios:
  1. **Algebraic multiplicity matches geometric multiplicity**:
     - Happens most of the time.
  2. **Algebraic multiplicity exceeds geometric multiplicity**:
     - Occurs in defective matrices.

- **Next**: Explore defective matrices and their properties.