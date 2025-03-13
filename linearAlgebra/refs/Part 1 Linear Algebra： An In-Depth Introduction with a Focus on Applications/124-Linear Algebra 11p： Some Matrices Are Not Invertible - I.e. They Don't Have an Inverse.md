## Non-Invertible Matrices and Properties of Inverses

### Not All Matrices Have an Inverse

- Some matrices do not have an inverse.  
- Example of a familiar matrix that **does not have an inverse**:
  - Key question to consider: _Why is it impossible to find nine numbers that would transform this matrix into the identity matrix?_
  - **Hint:** Linear dependence among columns.

---

### Key Explanation: Dependence and Null Space

1. **Linear Dependence** of Columns:
   - The columns of the matrix are linearly dependent.  
   - For example: The middle column is the average of the other two.  

2. **Importance of Null Space**:
   - If the null space of a matrix is non-trivial (contains vectors other than the zero vector), then the matrix is **not invertible**.  
   - In this case, the null space is **one-dimensional**.  

3. **Column Space Dimensions**:
   - If the null space is one-dimensional, the column space is **two-dimensional** (fewer than the number of columns).  
   - This is because the rank (number of linearly independent columns) and nullity (dimension of the null space) must satisfy the equation:
     $$
     \text{Rank} + \text{Nullity} = \text{Number of Columns}
     $$
   - Since the column space is two-dimensional, the matrix cannot have a three-dimensional column space required for invertibility.

---

### Conditions on Column Space

- The column space of the matrix is restricted:  
  - Any vector in the column space must satisfy:
    $$
    \text{Middle Entry = Average of First and Third}
    $$

- **Implication**: This property prevents the existence of three linearly independent columns, as required for the identity matrix.

---

### Non-Invertibility and System of Equations

- Consider the implication of an inverse in the context of the system of equations $A \mathbf{x} = \mathbf{b}$ where $A$ is non-invertible:
  1. If an inverse existed:
     $$
     \mathbf{x} = A^{-1} \mathbf{b}
     $$  
     _This implies a solution always exists_, which contradicts reality in cases where $\mathbf{b}$ is not in the column space of $A$.

  2. **Second Contradiction**:  
     If an inverse existed, there would only be a **unique solution**.  
     - For non-invertible matrices with a non-trivial null space, if any solution exists, there are **infinitely many solutions**.

---

### Characteristics of Invertible Matrices

#### When a Matrix is Invertible:
1. Columns are **linearly independent**.
2. The null space is **trivial** (only the zero vector).
3. The column space spans all of $\mathbb{R}^n$.

#### Synonyms for Invertibility:
- Linearly independent rows.
- Linearly independent columns.
- Full rank (rank = number of rows/columns).

#### Key Property for Inverse:
- For a square matrix $A$:
  $$
  \text{If } A \text{ is invertible, the system } A \mathbf{x} = \mathbf{b} \text{ always has a unique solution given by } A^{-1} \mathbf{b}.
  $$

---

### Summary of Non-Invertibility

- If columns are **linearly dependent**, then the matrix **is not invertible**.
- The system $A \mathbf{x} = \mathbf{b}$:
  1. May have **no solutions** (when $\mathbf{b}$ is not in the column space).
  2. May have **infinitely many solutions** (when $\mathbf{b}$ is in the column space).
- Non-invertibility arises because the column space is lower-dimensional than required, and the null space is non-trivial.  

--- 

### Looking Ahead

- As we study linear algebra further, we will explore additional criteria and characteristics that signal matrix invertibility.  
- For now, focus on understanding the **linear independence of columns** as the foundational property of invertible matrices.  
