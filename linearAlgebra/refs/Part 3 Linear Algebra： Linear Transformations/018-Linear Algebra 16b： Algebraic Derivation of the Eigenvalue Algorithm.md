## Rediscovering the Algorithm in Matrix Algebra

### Overview
- In a previous video, the celebrated equation was solved by treating it as a collection of equations and manipulating them step-by-step.
- In this video, the same algorithm is rediscovered but strictly using the language of matrix algebra.
- The goal is to:
  - Familiarize with matrix notation.
  - Learn to execute sophisticated manipulations and logic using it.

---

### Starting with the System
1. Begin with the equation:

   $$
   A \mathbf{x} - \lambda \mathbf{x} = 0
   $$

2. **Factorization Challenge**:
   - Directly factoring out $\mathbf{x}$ results in nonsensical subtraction of $\lambda$ (a scalar) from $A$ (a matrix).

---

### Resolving the Issue
3. Introduce the **Identity Matrix**:
   - Convert $\lambda \mathbf{x}$ to a matrix-vector operation using the identity matrix $I$:
   $$
   \lambda \mathbf{x} = (\lambda I) \mathbf{x}
   $$
   - Rewrite the equation:
   $$
   A \mathbf{x} - (\lambda I) \mathbf{x} = 0
   $$

4. Now, factor out $\mathbf{x}$:
   $$
   (A - \lambda I) \mathbf{x} = 0
   $$

---

### Conditions for Non-Trivial Solutions
5. For a non-trivial solution to exist, $(A - \lambda I)$ must be **singular**.  
   - Singular matrices have zero determinant:
   $$
   \det(A - \lambda I) = 0
   $$

---

### The Algorithm
6. The matrix algebra approach leads to the following steps:
   1. **Construct the Matrix**:
      Subtract $\lambda I$ from $A$: $(A - \lambda I)$.
   2. **Compute Determinant**:
      Solve $\det(A - \lambda I) = 0$ to find $\lambda$ (eigenvalues).
   3. **Find Null Space**:
      For each $\lambda$, substitute into:
      $$
      (A - \lambda I) \mathbf{x} = 0
      $$
      Solve for the **null space** to find eigenvectors.

---

### Explanation and Insights
- Subtracting $\lambda I$ from $A$ means subtracting $\lambda$ from each diagonal entry of $A$.
- The determinant condition ensures the existence of non-trivial solutions.

---

### Key Takeaways
- The matrix formulation is equivalent to the earlier discovered algorithm but is more compact and efficient in notation.
- Emphasis on treating matrices, vectors, and scalars as **indivisible objects** helps streamline operations.
- Matrix algebra is a powerful tool that allows sophisticated manipulations and logic, applicable across a broad range of problems.