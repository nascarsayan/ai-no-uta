## Deriving the Expression for the Length of a Vector in a Non-Cartesian Basis

### Premise
- The goal of this discussion is to **derive the expression for the length of a vector** with respect to a new basis, denoted as $\mathbf{B}$.
- The new basis, $\mathbf{B}$, consists of two vectors:
  - $\mathbf{B}_1$ and $\mathbf{B}_2$, which are **orthogonal** but no longer unit length.
  - Specifically:
    - $\|\mathbf{B}_1\| = 3$
    - $\|\mathbf{B}_2\| = 1$

- This makes the basis **non-Cartesian**, and as a result:
  - The values for the components of the vector $\mathbf{v}$, denoted as $\alpha_1$ and $\alpha_2$, will change.
  - The expression for the **length of the vector** in terms of $\alpha_1$ and $\alpha_2$ will differ from the Cartesian case.

---

### Key Observations
#### Orthogonality and Scaling
1. **Pythagorean theorem** can still be used because $\mathbf{B}_1$ and $\mathbf{B}_2$ remain orthogonal.
2. The length of each segment decomposed along $\mathbf{B}_1$ and $\mathbf{B}_2$ changes due to scaling:
   - The length along $\mathbf{B}_1$ is now $3 \alpha_1$ (not just $\alpha_1$).
   - The length along $\mathbf{B}_2$ remains $\alpha_2$ because $\|\mathbf{B}_2\| = 1$.

#### Component Changes
- Previously, the length of $\alpha_1 \mathbf{B}_1$ was $\alpha_1$ because $\|\mathbf{B}_1\| = 1$ in a Cartesian basis.
- Now:
  - The length of the same segment is $3 \alpha_1$ because $\|\mathbf{B}_1\| = 3$.

---

### Expression for the Length of the Vector in the New Basis
1. Using the Pythagorean theorem:
   - Length squared equals the sum of the squares of segment lengths.
   - In Cartesian basis:
     $$
     \|\mathbf{v}\|^2 = \alpha_1^2 + \alpha_2^2
     $$
   - In the new basis:
     $$
     \|\mathbf{v}\|^2 = (3 \alpha_1)^2 + (\alpha_2)^2
     $$

2. Simplifying:
   $$
   \|\mathbf{v}\|^2 = 9\alpha_1^2 + \alpha_2^2
   $$

---

### Insights and Takeaways
- The **choice of basis** directly affects how the length of a vector is expressed.
- For the non-Cartesian basis $\mathbf{B}$:
  - Scaling factors (like 3 for $\mathbf{B}_1$) must be incorporated into the expression for the vector's length.

---

### Matrix Representation Challenge
**Question**:
- How can the expression for length, $\|\mathbf{v}\|^2 = 9\alpha_1^2 + \alpha_2^2$, be rewritten as a **matrix product**?
  
#### Hint:
- To represent this in matrix form:
  1. Use a **diagonal matrix** to encode scaling factors for the basis vectors.
  2. Generalize the length expression without explicitly referencing $\alpha_1$ and $\alpha_2$. Instead, work with the vector $\boldsymbol{\alpha} = \begin{bmatrix} \alpha_1 \\ \alpha_2 \end{bmatrix}$.

---

### General Notes
- The expression $\|\mathbf{v}\|^2 = \alpha^\top \alpha$ implies a **Cartesian basis** and is **not valid** for non-Cartesian bases.
- To rescue this matrix expression, a **new matrix** must be introduced:
  $$
  \|\mathbf{v}\|^2 = \boldsymbol{\alpha}^\top \mathbf{M} \boldsymbol{\alpha}
  $$
  - Where $\mathbf{M}$ is a **metric matrix** associated with the non-Cartesian basis.

---

### Conclusion
- By incorporating the scaling factor for $\mathbf{B}_1$, the new length expression is:
  $$
  \|\mathbf{v}\|^2 = 9\alpha_1^2 + \alpha_2^2
  $$
- This demonstrates how **changing the basis** alters geometric properties such as length.
  
---

### Open Question
How can the metric matrix $\mathbf{M}$ be constructed to represent the length of the vector in terms of $\boldsymbol{\alpha}$ as a whole, without separately identifying $\alpha_1$ and $\alpha_2$?