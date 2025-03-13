## Reflection and Change of Bases

### Starting Point
The reflection transformation from the last video was represented using a specific basis. We constructed a matrix for that basis and now shift our focus to another basis to repeat the process.

---

### Change of Basis
- **Original Basis**:
  - $\mathbf{E_1}$ and $\mathbf{E_2}$
- **New Basis**:
  - $\mathbf{F_1}$ (a vector at a $45^\circ$ angle to the line)
  - $\mathbf{F_2}$ (keeps its position as $\mathbf{E_2}$)

We'll denote the new basis vectors as $\mathbf{F_1}$ and $\mathbf{F_2}$. The goal is to compute the transformation matrix with respect to this new basis.

---

### Constructing the Transformation Matrix in the New Basis
1. **Columns Construction**:
   Each column of the transformation matrix represents the image of a basis vector under reflection, expressed in terms of the new basis vectors.

   - **First Column**:
     - $R(\mathbf{F_1}) = -\mathbf{F_2}$
     - In components: $\begin{bmatrix} 0 \\ -1 \end{bmatrix}$

   - **Second Column**:
     - $R(\mathbf{F_2}) = -\mathbf{F_1}$
     - In components: $\begin{bmatrix} -1 \\ 0 \end{bmatrix}$

2. **New Matrix**:
   The matrix representing the reflection with respect to the $\mathbf{F}$ basis is:

   $$
   M_F =
   \begin{bmatrix}
   0 & -1 \\
   -1 & 0
   \end{bmatrix}
   $$

This matrix differs completely from the one computed in the original basis, yet it still represents the same linear transformation.

---

### Example: Transforming a Vector
#### In Original Basis:
- $\mathbf{v} = \mathbf{E_2} - \mathbf{E_1} = \begin{bmatrix} -1 \\ 1 \end{bmatrix}$
- Applying $M_B$ (transformation matrix in the original basis):

  $$
  R(\mathbf{v}) = M_B \begin{bmatrix} -1 \\ 1 \end{bmatrix} = \begin{bmatrix} 1 \\ -1 \end{bmatrix}
  $$

#### In New Basis:
- In the new basis, $\mathbf{v}$ is expressed as:
  $$
  \mathbf{v} = \frac{1}{2} \mathbf{F_1} + \frac{1}{2} \mathbf{F_2} \implies \begin{bmatrix} \frac{1}{2} \\ \frac{1}{2} \end{bmatrix} \text{ (in components of $\mathbf{F}$)}
  $$
- Applying $M_F$:  
  $$
  R(\mathbf{v}) = M_F \begin{bmatrix} \frac{1}{2} \\ \frac{1}{2} \end{bmatrix} = \begin{bmatrix} -\frac{1}{2} \\ -\frac{1}{2} \end{bmatrix}
  $$

### Observations:
- The transformed vector in both bases corresponds to the same geometrical result, though the components differ depending on the basis used.

---

### Key Insights From Basis Change
1. **Transformation Matrix Changes**: The numbers in the transformation matrix depend entirely on the choice of basis.
2. **Geometric Consistency**:
   - The reflection as a geometric operation remains unchanged.
   - The input vector and its reflection have consistent real-world interpretations irrespective of the basis used.
3. **Eigenvalues Don't Change**:
   - Both matrices, despite being different, share the same eigenvalues ($+1$ and $-1$).

---

### The Invariant Nature of Linear Transformations
Fundamental properties of the transformation remain unchanged:
- Eigenvalues: The eigenvalues remain $+1$ and $-1$.
- Determinant: Both matrices have a determinant of $-1$.
- These invariants emphasize that a transformation’s geometric or physical interpretation does not depend on the basis.

---

### Questions for Further Exploration
- What exactly is the relationship between the matrices of the same transformation in different bases?
  - Hint: They are related by a **similarity transformation**.
- How can we construct similarity transformations systematically using change-of-basis matrices?

This exploration will be expanded under the topic of **Change of Basis**. For now, note:
- The choice of basis impacts the matrix representation, but the underlying transformation remains the same.