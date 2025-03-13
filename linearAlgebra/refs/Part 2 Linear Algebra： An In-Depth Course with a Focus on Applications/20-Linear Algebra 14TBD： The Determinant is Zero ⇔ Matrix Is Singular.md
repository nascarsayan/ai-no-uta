## Determinant and Matrix Singularity

### Governing Property
- **Main Statement:**  
  The determinant being 0 is equivalent to the matrix being singular.
  - When $\text{det}(A) = 0$, the matrix $A$ is singular.
  - When $\text{det}(A) \neq 0$, the matrix $A$ is non-singular.

- **Two-Way Equivalence:**  
  - If the matrix is singular, $\text{det}(A) = 0$.
  - If the matrix is non-singular, $\text{det}(A) \neq 0$.

### Effective Algebraic Criterion
The determinant provides a straightforward way to decide whether a matrix is singular:
- Singularity of the matrix aligns with $\text{det}(A) = 0$.
- Non-singularity aligns with $\text{det}(A) \neq 0$.

---

### Proof Outline
**Key Tools:**
1. Gaussian Elimination.
   - Gaussian elimination preserves the correctness of determinant-related properties.

#### Singular Matrix Condition
- Gaussian elimination preserves:
  - The **null space** of the matrix.
  - The singularity or non-singularity of the matrix.

---

#### Operations and Their Effects on Determinants
1. **Add a multiple of one row to another:**  
   $\text{det}(A)$ remains unchanged.
   
2. **Switch two rows:**  
   Changes the **sign** of $\text{det}(A)$ but not whether it is 0.
   
3. **Multiply a row by a nonzero scalar:**  
   Changes the magnitude of $\text{det}(A)$, but not whether it is 0.

Thus, **Gaussian Elimination preserves whether $\text{det}(A) = 0$.**

---

### Upper Triangular Matrix and Determinants
At the end of Gaussian elimination:
- The matrix will become **upper triangular**, and determinant computation is simplified:
  $$
  \text{det}(A) = \prod \text{(diagonal entries)}.
  $$

#### Non-Singular Matrix Case
- **Linearly independent columns** guarantee non-zero diagonal entries.
- $\text{det}(A) \neq 0$.

#### Singular Matrix Case
- **Linearly dependent columns** result in at least one zero diagonal entry.
- $\text{det}(A) = 0$.

---

### Final Recap
- If the matrix is **non-singular** after Gaussian elimination:
  - $\text{det}(A) \neq 0$.
- If the matrix is **singular** after Gaussian elimination:
  - $\text{det}(A) = 0$.

Since Gaussian elimination preserves the determinant's property of being zero or nonzero:
- The determinant value at the end reflects the properties of the **original matrix**.

This completes the proof. ✅