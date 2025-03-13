# Notes on Eigenvalues and Eigenvectors

---

## 1. Importance of Eigenvalues and Eigenvectors

- Eigenvalues and eigenvectors, collectively referred to as the **spectrum** of a linear transformation, encapsulate all the essential information about the transformation.
- They **reduce a linear transformation** to its bare essentials and communicate all relevant details efficiently.

---

## 2. Number of Eigenvalues and Eigenvectors

1. **Scenarios:**
   - Some transformations have as many eigenvalues and eigenvectors as the dimension of the space.
   - Other transformations have fewer eigenvalues and eigenvectors.
   - Transformations like rotation in a plane may have no real eigenvalues and eigenvectors.
   
2. **Observation:**
   - The number of eigenvectors cannot exceed the **dimension of the space** due to their **linear independence**.
   - Eigenvectors corresponding to different eigenvalues are linearly independent.

3. **Special Cases:**
   - Sometimes eigenvalues are double-counted when the dimension of the eigenspace is greater than one.
   - Certain transformations are "defective," where an eigenvalue is repeated, but there is only one corresponding eigenvector.

---

## 3. Eigenvalues, Eigenvectors, and Basis

- If a transformation has as many eigenvalues and eigenvectors as the dimension of the space:
  - The eigenvectors form a **basis** for the space.
  - This is because the eigenvectors are **linearly independent** and span the space.

### Basis and Linear Transformations:
- A **basis** is the "lens" through which we view vectors in a space.
- Choosing eigenvectors as the basis simplifies calculations for transformations.
- The basis choice depends on the linear transformation and is problem-dependent.

---

## 4. Eigen Decomposition and Applications

### Representing a Vector Using Eigen Basis:
1. Any vector $\mathbf{v}$ in the space can be decomposed as:
   $$
   \mathbf{v} = \alpha_1 \mathbf{e}_1 + \alpha_2 \mathbf{e}_2 + \alpha_3 \mathbf{e}_3
   $$
   - $\alpha_1, \alpha_2, \alpha_3$ are the **coefficients** w.r.t. the eigenbasis $\{ \mathbf{e}_1, \mathbf{e}_2, \mathbf{e}_3 \}$.

2. Linear transformations preserve this decomposition due to **linearity**:
   $$
   T(\mathbf{v}) = T(\alpha_1 \mathbf{e}_1 + \alpha_2 \mathbf{e}_2 + \alpha_3 \mathbf{e}_3)
   $$
   Applying linearity:
   $$
   T(\mathbf{v}) = \alpha_1 T(\mathbf{e}_1) + \alpha_2 T(\mathbf{e}_2) + \alpha_3 T(\mathbf{e}_3)
   $$

### Special Case: Transformation Using Eigen Basis
- If $\mathbf{e}_1, \mathbf{e}_2, \mathbf{e}_3$ are **eigenvectors**, applying the transformation becomes simple:
  $$
  T(\mathbf{e}_1) = \lambda_1 \mathbf{e}_1, \quad T(\mathbf{e}_2) = \lambda_2 \mathbf{e}_2, \quad T(\mathbf{e}_3) = \lambda_3 \mathbf{e}_3
  $$

- With these, the transformation of $\mathbf{v}$ leads to:
  $$
  T(\mathbf{v}) = \alpha_1 \lambda_1 \mathbf{e}_1 + \alpha_2 \lambda_2 \mathbf{e}_2 + \alpha_3 \lambda_3 \mathbf{e}_3
  $$

### Interpretation in Component Space:
- In component (basis) space, the transformation scales the coefficients:
  $$
  \text{Original coefficients: } (\alpha_1, \alpha_2, \alpha_3)
  $$
  $$
  \text{Transformed coefficients: } (\alpha_1 \lambda_1, \alpha_2 \lambda_2, \alpha_3 \lambda_3)
  $$

### Recipe for Simplification:
1. Decompose the vector $\mathbf{v}$ with respect to the eigenbasis.
2. Multiply each component by the respective eigenvalue.
3. Reconstruct the transformed vector.

---

## 5. Eigen Basis and Linear Transformation Simplification

- Knowing the eigenvalues $(\lambda_1, \lambda_2, \lambda_3)$ and eigenvectors $(\mathbf{e}_1, \mathbf{e}_2, \mathbf{e}_3)$ is sufficient to understand and compute the transformation.
- It reduces any complicated transformation to simple scaling operations in the eigenbasis.

---

## 6. Takeaways

- **Eigenvalues and eigenvectors** serve as a fundamental tool in simplifying and analyzing transformations in **linear algebra**.
- By using eigenvectors as a basis, a linear transformation becomes a diagonal operation in the new basis.
- This approach allows efficient computation and a deeper understanding of the transformation itself.