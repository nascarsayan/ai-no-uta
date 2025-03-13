# Matrix Decomposition: Orthogonal and Symmetric Matrices

## Theorem Statement
Any matrix $A$ can be decomposed into a product of an orthogonal matrix $Q$ and a symmetric matrix $S$ with non-negative eigenvalues:

$$
A = Q S
$$

### Key Properties of the Decomposition:
1. **Orthogonal Matrix Q**: Rows and columns are orthonormal, i.e., $Q^\top Q = I$.
2. **Symmetric Matrix S**: $S = S^\top$ and has non-negative eigenvalues.

### Concepts Involved:
- **Uniqueness**: This decomposition is unique, meaning there exists only one $Q$ and $S$ pair with the specified properties.
- **Geometric and Algebraic Interpretations**:
    - Geometrically, $Q$ represents a rotation or reflection, while $S$ represents a scaling transformation.
    - Algebraically, the decomposition is straightforward and relies heavily on matrix properties such as the transpose, eigenvalue decomposition, and square roots of matrices.

---

## Matrix Square Roots

### Definition
The square root of a matrix $M$ is another matrix $B$ such that:

$$
B^2 = M
$$

### Key Conditions for Matrix Square Roots:
1. $M$ must be symmetric.
2. $M$ must have a full set of eigenvalues.
3. All eigenvalues of $M$ must be non-negative.

### Construction of the Square Root of $M$:
Given $M$ with eigenvalue decomposition:

$$
M = V \Lambda V^\top
$$

The square root is constructed as:

$$
M^{1/2} = V \Lambda^{1/2} V^\top
$$

Where $\Lambda^{1/2}$ contains the square roots of the eigenvalues of $M$.

---

## Decomposition Process: Derivation of $Q$ and $S$

### Step 1: Constructing $S$
1. Compute $A^\top A$:
    - For any matrix $A$, the product $A^\top A$ is:
      - Symmetric.
      - Square, even if $A$ is rectangular.
2. Verify that all eigenvalues of $A^\top A$ are non-negative.
3. Compute the square root of $A^\top A$:
    - $S = (A^\top A)^{1/2}$.

Thus, $S$ satisfies:

$$
S^2 = A^\top A
$$

### Step 2: Constructing $Q$
1. Solve for $Q$ using $S$:
    $$
    Q = A S^{-1}
    $$
2. Verify $Q$ is orthogonal:
    $$
    Q^\top Q = I
    $$

---

## Uniqueness Proof
### Uniqueness of $S$:
1. Since $S^2 = A^\top A$, and $S$ is symmetric, $S$ is uniquely determined by the eigenvalue decomposition of $A^\top A$ constrained to non-negative eigenvalues.

### Uniqueness of $Q$:
1. $Q$ must satisfy $Q = A S^{-1}$.
2. Since both $A$ and $S$ are unique, $Q$ is uniquely determined.

---

## Algebraic Properties of Symmetric $A^\top A$
1. **Symmetry**:
   $$
   (A^\top A)^\top = A^\top (A^\top)^\top = A^\top A
   $$
   
2. **Non-Negative Eigenvalues**:
   - Intuitively, $A^\top A$ resembles squaring a matrix, which ensures all eigenvalues are non-negative.

3. **Positive Definite Case (Invertibility)**:
   - If $A^\top A$ is invertible (all eigenvalues are strictly positive), $S$ is also invertible.
   - Otherwise, invertibility must be explicitly considered.

---

## Key Observations on Decomposition
### Why Use $A^\top A$?
- Symmetry: Guarantees full diagonalizability and real eigenvalues.
- Non-negativity: Ensures eigenvalues are suitable for square roots.
- Universality: Works even if $A$ is rectangular.

### Behavior of Orthogonal Matrix $Q$:
- Captures rotational or reflectional transformations from $A$.
- Derived elegantly using $S$ as a scaling factor.

---

## Summary of the Proof
1. Compute $A^\top A$ and verify that it is:
   - Symmetric.
   - With non-negative eigenvalues.
2. Construct $S = (A^\top A)^{1/2}$.
3. Construct $Q = A S^{-1}$ and verify that $Q$ is orthogonal.
4. Conclude:
   $$
   A = Q S
   $$

---

## Final Notes
### Advantages of the Algebraic Approach:
1. Direct and guarantees correctness.
2. Avoids complications of geometric proof.
3. Leverages the fundamental properties of matrices such as symmetry and eigenvalues.

### Big Picture:
This decomposition underscores the interplay between **geometry** and **algebra**, where algebraic manipulations reveal geometric insights about transformations.