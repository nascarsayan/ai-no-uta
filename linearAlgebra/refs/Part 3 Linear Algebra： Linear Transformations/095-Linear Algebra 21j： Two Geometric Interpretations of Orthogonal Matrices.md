## Orthogonal Matrix: Geometric Interpretations and Their Relationship

### 1. Two Geometric Interpretations of an Orthogonal Matrix
Orthogonal matrices can be interpreted in two ways:
1. **As a collection of column vectors** representing basis vectors.
2. **As a linear transformation** that preserves vector lengths.

These interpretations are not in conflict but rather complementary.

---

### 2. Interpretation 1: Matrix as a Collection of Column Vectors
- In an orthogonal matrix, the columns represent **orthonormal vectors**:
  - **Orthonormality** means:
    - Each vector has **unit length**.
    - Any two vectors are at **90 degrees** to each other.
  - Relative arrangement of the vectors is identical to the standard Cartesian basis, but their **orientation can be arbitrary**.

---

### 3. Interpretation 2: Matrix as a Linear Transformation
- An orthogonal matrix represents a **linear transformation**.
  - It **preserves lengths**, limiting transformations to:
    - **Rotations**
    - **Reflections**
- This interpretation aligns with the idea of transforming input basis vectors into output vectors as dictated by the matrix.

---

### 4. Relationship Between the Two Interpretations
The relationship between column vectors and the linear transformation can be summarized as:
- The **linear transformation** defined by the matrix directly maps **input basis vectors** into the **column vectors** of the matrix.

#### Example: Mapping Basis Vectors
- For simplicity, assume a basis: $e_1 = \begin{bmatrix} 1 \\ 0 \\ 0 \end{bmatrix}$, $e_2 = \begin{bmatrix} 0 \\ 1 \\ 0 \end{bmatrix}$, $e_3 = \begin{bmatrix} 0 \\ 0 \\ 1 \end{bmatrix}$. 
- Applying transformation $Q$:
  $$
  Q \cdot e_1 = \text{(first column of } Q \text{)} \quad
  Q \cdot e_2 = \text{(second column of } Q \text{)} \quad
  Q \cdot e_3 = \text{(third column of } Q \text{)} 
  $$
- Each input basis vector ($e_1$, $e_2$, $e_3$) is **rotated** (or reflected) into the corresponding column vector of $Q$.

---

### 5. Practical Verification
To verify the mapping:
1. Represent a basis vector (e.g., $e_1$) in component form: $\begin{bmatrix} 1 \\ 0 \\ 0 \end{bmatrix}$.
2. Multiply the matrix $Q$ by this vector:
   $$
   Q \cdot \begin{bmatrix} 1 \\ 0 \\ 0 \end{bmatrix} = \text{first column of } Q
   $$
   - The result is the **first column** of $Q$.
3. Similarly, apply $Q$ to $e_2$ and $e_3$ to extract the second and third columns.

---

### 6. Inverse Linear Transformation
#### Linear Transformation Mapping Vectors Back:
- Representing the **inverse transformation** is straightforward:
  - The **inverse of an orthogonal matrix** is its **transpose**:
    $$
    Q^{-1} = Q^T
    $$
- This means the inverse linear transformation is simply:
  $$
  Q^T \cdot (\text{column vectors of } Q \to \text{original basis vectors})
  $$
---
### 7. Summary of Transformations
- **Forward transformation** (using $Q$): Maps standard basis vectors into column vectors of $Q$.
- **Inverse transformation** (using $Q^T$): Maps column vectors of $Q$ back to standard basis vectors.

---

### 8. Applications and Next Steps
- These interpretations will be key when discussing the **eigenvalue decomposition** of symmetric matrices.