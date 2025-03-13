## QR Decomposition and Gram-Schmidt Process

### Matrix Decompositions Overview:
- **LU Decomposition**: Represents Gaussian elimination.
- **Eigenvalue Decomposition**: Represents eigenvalues and the eigenvalue procedure.
- **QR Decomposition**: Matrix representation of the **Gram-Schmidt process**.

---

### Orthogonal Matrices
- **Orthogonal matrices** are an important category of matrices.
- They do not arise until dealing with an **inner product space**.
- Inner products introduce additional structural properties needed for orthogonality.

---

### Orthogonalization and Orthonormalization
- **Goal**: Transform a set of vectors into an orthogonal set, and then normalize them to form an orthonormal set.
- **Definitions**:
  - Orthogonal: Vectors whose dot product equals zero.
  - Orthonormal: Orthogonal vectors with unit length.

#### Process:
1. **Orthogonalization**: Begin by making vectors orthogonal relative to an inner product.
2. **Orthonormalization**: Adjust the length of the orthogonal vectors to 1 by dividing by their magnitude.

---

### Inner Product
- **Default Inner Product**: Standard dot product.
- **Length of a Vector**:
  If $\mathbf{v} = \begin{bmatrix} 3 \\ 4 \end{bmatrix}$, its length is:
  $$
  \|\mathbf{v}\| = \sqrt{3^2 + 4^2} = \sqrt{9 + 16} = 5
  $$
  For more complex vectors, calculate length using:
  $$
  \|\mathbf{v}\| = \sqrt{\sum v_i^2}
  $$
- **Orthogonalization Process**: Achieved by subtracting projections.

---

### Gram-Schmidt Orthogonalization
#### Step-by-Step:
1. **Initialize**:
   - Start with a set of vectors $\{\mathbf{a}, \mathbf{b}, \mathbf{c}\}$.
   - Set $\mathbf{a}_1 = \mathbf{a}$.

2. **Orthogonalization of Next Vectors:**
   - For $\mathbf{b}_1$, subtract its projection onto $\mathbf{a}_1$:
     $$
     \mathbf{b}_1 = \mathbf{b} - \text{proj}_{\mathbf{a}_1}(\mathbf{b}),
     $$
     where $\text{proj}_{\mathbf{u}}(\mathbf{v}) = \frac{\mathbf{u}^\top \mathbf{v}}{\mathbf{u}^\top \mathbf{u}} \cdot \mathbf{u}$.

   - Check orthogonality by verifying $\mathbf{a}_1^\top \mathbf{b}_1 = 0$. If true, proceed.

3. **Extend to Third Vector**:
   - For $\mathbf{c}_1$, subtract its projections onto both $\mathbf{a}_1$ and $\mathbf{b}_1$:
     $$
     \mathbf{c}_1 = \mathbf{c} - \text{proj}_{\mathbf{a}_1}(\mathbf{c}) - \text{proj}_{\mathbf{b}_1}(\mathbf{c}).
     $$

4. **Normalize** (Optional to make vectors unit-length):
   - Divide each orthogonal vector by its magnitude to produce an orthonormal set:
     $$
     \mathbf{v}_{\text{unit}} = \frac{\mathbf{v}}{\|\mathbf{v}\|}.
     $$

---

### Example: Applying Gram-Schmidt
Given $\mathbf{a} = \begin{bmatrix} 1 \\ 0 \\ 0 \end{bmatrix}$, $\mathbf{b} = \begin{bmatrix} 1 \\ 1 \\ 0 \end{bmatrix}$, and $\mathbf{c} = \begin{bmatrix} 1 \\ 1 \\ 1 \end{bmatrix}$:

1. **Step 1**: Set $\mathbf{a}_1 = \mathbf{a}$.
2. **Step 2**: Compute $\mathbf{b}_1$:
   $$
   \mathbf{b}_1 = \mathbf{b} - \text{proj}_{\mathbf{a}_1}(\mathbf{b}),
   $$
   where $\text{proj}_{\mathbf{a}_1}(\mathbf{b}) = \frac{\mathbf{a}_1^\top \mathbf{b}}{\mathbf{a}_1^\top \mathbf{a}_1} \cdot \mathbf{a}_1$.
3. **Step 3**: Compute $\mathbf{c}_1$:
   $$
   \mathbf{c}_1 = \mathbf{c} - \text{proj}_{\mathbf{a}_1}(\mathbf{c}) - \text{proj}_{\mathbf{b}_1}(\mathbf{c}).
   $$

4. **Step 4**: Normalize to generate an orthonormal set:
   $$
   \mathbf{a}_2 = \frac{\mathbf{a}_1}{\|\mathbf{a}_1\|}, \quad \mathbf{b}_2 = \frac{\mathbf{b}_1}{\|\mathbf{b}_1\|}, \quad \mathbf{c}_2 = \frac{\mathbf{c}_1}{\|\mathbf{c}_1\|}.
   $$

---

### Orthonormalization Example in $\mathbb{R}^3$
- Start with three non-orthogonal vectors.
- Perform **Gram-Schmidt orthogonalization**.
- Normalize them to produce orthonormal vectors.

Result:
- The final orthonormal vectors form the columns of the **Q matrix** in the QR decomposition.

---

### Summary:
- **Gram-Schmidt Process**:
  1. Orthogonalize vectors relative to an inner product.
  2. Normalize to make them orthonormal.
- **Output**: Orthonormal vectors that can represent the **Q matrix** for QR decomposition.
- **Applications**: Efficient computation for solving linear systems, least squares problems, and eigenvalue computations in numerical analysis.