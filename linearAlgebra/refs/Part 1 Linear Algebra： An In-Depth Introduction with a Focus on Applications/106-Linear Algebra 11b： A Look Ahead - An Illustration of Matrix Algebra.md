## Introduction to Matrix Multiplication

### Big Picture Goals:
1. Treat matrices as **whole, indivisible objects**:
   - No referencing individual entries of matrices.
2. Use **algebraic thinking**:
   - Denote matrices using capital letters (e.g., $A$), unknowns using lowercase letters (e.g., $x$), and results using lowercase letters (e.g., $b$).

### Revisiting Linear Systems:
- Recall the simple system of equations:
  $$
  ax = b
  $$
  Examples include:
  $$
  5x = 4 \quad \text{or} \quad 10x = 10
  $$
  Solution:
  $$
  x = \frac{b}{a} \quad \text{(when } a \neq 0\text{)}.
  $$

- **Matrix Inspiration**: We aim to extend this idea to matrix equations:
  $$
  Ax = b
  $$

---

## Matrix Division and Inverse

### Making Division Meaningful in Matrices:
1. Define **matrix multiplication** and **matrix division**.
2. Restate the goal:
   $$
   x = A^{-1}b
   $$
   - Here, $A^{-1}$ represents the **inverse** of matrix $A$.

### Notation Change:
- Instead of writing $\frac{b}{A}$, we use $A^{-1}b$ because it precisely captures the matrix operation (similar to division with scalars).

---

## Illustration of Matrix Algebra

### Key Operations:
1. Define the unknown matrix:
   $$
   x = A^{-1}b
   $$
   - Using a computer system, we compute $A^{-1}b$.

2. Verify the solution:
   - Multiply $A$ by $x$:
     $$
     A \cdot x = b
     $$
   - Example: If $A$ is a matrix and $b$ is $[6, 15, 25]^T$, then verifying means ensuring the product reconstructs $b$.

---

## Behind the Scenes: Gaussian Elimination

- While solving, **Gaussian Elimination** works in the background:
  - The matrix inverse computation indirectly relies on elimination techniques.

---

### Matrix Multiplication and Verification:
- Multiplication provides a test for correctness:
  - Multiply the original matrix $A$ with the computed solution $x$.
  - Ensure the result matches the right-hand side $b$.

---

## Final Illustration: Null Space and Solution Verification

### Verification of Solutions:
- Multiply the problem matrix $A$ with the solution matrix:
  $$
  A \cdot x = b
  $$
- For any values of $\alpha$, $\beta$, and $\gamma$ (from the null space), they should cancel out, leaving only $b$.

Example:
- Matrix result:
  $$
  A \cdot x = \begin{bmatrix} -4 \\ -6 \end{bmatrix}
  $$
  Matches the expected right-hand side.

---

## Summary
- **Matrix Multiplication** is a powerful tool that:
  1. Simplifies representation of linear systems.
  2. Enables efficient computation and verification of solutions.
- Next step: Explaining **how matrix multiplication works**! 🚀