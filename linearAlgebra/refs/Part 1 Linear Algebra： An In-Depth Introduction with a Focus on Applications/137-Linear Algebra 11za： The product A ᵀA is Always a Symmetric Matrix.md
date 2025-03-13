## Symmetry of $\mathbf{A^\top A}$

### Overview

- **Objective**: Prove that for any matrix $\mathbf{A}$, the combination $\mathbf{A^\top A}$ is symmetric.
- **Approaches**:
  1. **Entry-by-entry approach**: Focus on individual entries.
  2. **Matrix algebra approach**: Use properties of matrix transposes.

---

### Entry-by-entry Approach

#### Matrix Compatibility
- When multiplying $\mathbf{A}$ by its transpose $\mathbf{A^\top}$:
  - Inner dimensions match (e.g., if $\mathbf{A}$ is $3 \times 2$, then $\mathbf{A^\top}$ is $2 \times 3$).
  - Outer dimensions match, resulting in a square matrix.

#### Calculating Entries
1. **Example calculation for a symmetric matrix:**
   - Compute the first entry.
     \[
     1 + 4 + 9 = 14
     \]
   - Compute another entry (e.g., last entry).
     \[
     16 + 25 + 36 = 77
     \]
   - Symmetry check: Compare off-diagonal entries:
     \[
     4 + 10 + 18 = 32
     \]

2. **Why entries are the same?**
   - Entries correspond to dot products of rows and columns.
   - For example:
     - Entry at $(1, 2)$ is the dot product of the first row of $\mathbf{A}$ and the second column of $\mathbf{A^\top}$.
     - Entry at $(2, 1)$ is the dot product of the second row of $\mathbf{A}$ and the first column of $\mathbf{A^\top}$.
   - These pairs involve the same set of vectors because rows of $\mathbf{A^\top}$ equal columns of $\mathbf{A}$.

#### Generalization
- The entries of $\mathbf{A^\top A}$ represent all pairwise dot products between columns of $\mathbf{A}$. 
- For an $n \times m$ matrix $\mathbf{A}$ with $m$ columns:
  - $\mathbf{A^\top A}$ is an $m \times m$ matrix, containing ${m \choose 2}$ distinct combinations of column pairs.

---

### Matrix Algebra Approach

#### Symmetric Definition via Transpose
- A matrix $\mathbf{M}$ is **symmetric** if $\mathbf{M^\top = M}$.

#### Proof Steps
1. Compute the transpose of $\mathbf{A^\top A}$:
   \[
   (\mathbf{A^\top A})^\top = \mathbf{A^\top}^\top \cdot \mathbf{A^\top}
   \]
   - Recall: $(\mathbf{B \cdot C})^\top = \mathbf{C^\top \cdot B^\top}$.
   - The transpose of the transpose restores the original:
     \[
     \mathbf{A^\top}^\top = \mathbf{A}
     \]
   - Hence:
     \[
     (\mathbf{A^\top A})^\top = \mathbf{A^\top A}
     \]
   - $\mathbf{A^\top A}$ is symmetric.

---

### Generalization: $\mathbf{A^\top M A}$

#### Statement
- If $\mathbf{M}$ is symmetric, then $\mathbf{A^\top M A}$ is also symmetric for any compatible $\mathbf{A}$.

#### Proof
1. Compute the transpose of $\mathbf{A^\top M A}$:
   \[
   (\mathbf{A^\top M A})^\top = \mathbf{A^\top M^\top A^\top}
   \]
2. Using symmetry of $\mathbf{M}$:
   \[
   \mathbf{M^\top} = \mathbf{M}
   \]
3. Transpose of $\mathbf{A^\top}$:
   \[
   \mathbf{A^\top}^\top = \mathbf{A}
   \]
4. Result:
   \[
   (\mathbf{A^\top M A})^\top = \mathbf{A^\top M A}
   \]
   - $\mathbf{A^\top M A}$ is symmetric.

---

### Insights and Applications

1. **Pairwise Dot Products**:
   - $\mathbf{A^\top A}$ contains all pairwise combinations of dot products for the columns of $\mathbf{A}$.
   - Example: $(i, j)$ entry corresponds to the dot product of column $i$ and column $j$.

2. **Extension to Larger Matrices**:
   - For $\mathbf{A}$ with 10 columns, $\mathbf{A^\top A}$ becomes a $10 \times 10$ symmetric matrix.

3. **Special Case**:
   - $\mathbf{A^\top A}$ is a specific instance where $\mathbf{M}$ is the identity matrix.

---

### Conclusion

- Two proofs have been provided:
  1. Entry-by-entry approach highlights symmetry explicitly via individual computations.
  2. Matrix algebra approach demonstrates symmetry using transposition properties.
- The result $\mathbf{A^\top A}$ being symmetric is extended to $\mathbf{A^\top M A}$ when $\mathbf{M}$ is symmetric.