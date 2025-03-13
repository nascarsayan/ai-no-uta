## Length Preserving Linear Transformations

### Introduction
- **Length preserving linear transformations**:
  - Transformations that do not change the length of any vector.
  - Denoted by matrix $Q$ in Cartesian coordinates.
  - Algebraic property: $Q^\top Q = I$, where $I$ is the identity matrix.

---

### Definition and Properties of Length Preservation
1. A length-preserving linear transformation:
   - Maps a vector $v$ to $Qv$ such that $\lVert v \rVert = \lVert Qv \rVert$.

2. In the component space:
   - Represented using matrices.
   - For a vector $v$ represented by $\alpha$, transformation $Qv$ becomes $Q\alpha$ in components.

3. Equality of lengths in component space:
   - Using matrix notation:
     $$
     \alpha^\top \alpha = (Q\alpha)^\top (Q\alpha)
     $$
   - Expanding this:
     $$
     \alpha^\top \alpha = \alpha^\top Q^\top Q \alpha
     $$
   - Since this holds for all vectors $\alpha$, we conclude:
     $Q^\top Q = I$

4. **Key Result**:
   - The matrix $Q$ satisfies the property: $Q^\top Q = I$.
   - Such matrices are called **orthogonal matrices**.

---

### Orthogonal Matrices
- **Definition**:
  - A matrix $Q$ is orthogonal if:
    $$
    Q^\top Q = I
    $$

- **Examples**:
  - Consider an orthogonal matrix:
    $$
    Q = \begin{bmatrix}
    \frac{1}{\sqrt{5}} & \frac{2}{\sqrt{5}} \\
    \frac{2}{\sqrt{5}} & -\frac{1}{\sqrt{5}}
    \end{bmatrix}
    $$
    - Verify: $Q^\top Q = I$

---

### Important Properties of Orthogonal Matrices
1. **Transpose Equals Inverse**:
   - For orthogonal matrices:
     $$
     Q^\top = Q^{-1}
     $$

2. **Closure Under Multiplication**:
   - $Q^\top Q = I$ implies $Q Q^\top = I$ (order does not matter).

3. **Determinant**:
   - Determinants of orthogonal matrices satisfy:
     $$
     \det(Q)^2 = 1 \implies \det(Q) = \pm 1
     $$
   - $\det(Q) = 1$ corresponds to rotations.
   - $\det(Q) = -1$ corresponds to reflections.

4. **Eigenvalues**:
   - For orthogonal matrices, eigenvalues are constrained.
   - If eigenvalues are real, they must satisfy:
     $$
     \lambda = \pm 1
     $$
   - Complex eigenvalues (when applicable) lie on the unit circle.

---

### Implications of Orthogonal Matrices
1. **Ease of Inversion**:
   - The inverse of an orthogonal matrix is simply its transpose.

2. **Geometric Significance**:
   - Rotations and reflections are examples of orthogonal transformations as they preserve lengths and angles.
   - These operations do not distort the vector space.

3. **Connection to Linear Transformations**:
   - Orthogonal transformations are a subset of linear transformations that preserve the Euclidean metric.

---

### Summary
- **Core algebraic property**:
  $$
  Q^\top Q = I
  $$
- **Geometric insights**:
  - Preserves lengths and angles.
  - Includes rotations and reflections.

- Orthogonal matrices:
  - Determinant: $\det(Q) = \pm 1$.
  - Eigenvalues (when real): $\lambda = \pm 1$.

- Orthogonal matrices highlight the strong interplay between algebraic tools (like matrices) and geometric intuition.