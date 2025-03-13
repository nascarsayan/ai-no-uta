## The Rank of a Matrix: A Spectacular Fact

### Introduction
- This lesson focuses on an extraordinary fact about matrices in linear algebra.
- It highlights the relationship between **row space** and **column space**, and their respective dimensions.

---

### A Fundamental Question

#### Question Setup:
1. Consider a matrix of any dimension, for example:
   - A $4 \times 8$ matrix.
   - A large $2880 \times 5120$ matrix (dimensions correspond to the resolution of a 5K iMac screen).
2. Question: 
   - Are there more **linearly independent columns** or more **linearly independent rows**?

#### Rephrased:
- Is the dimension of the **column space** greater than the dimension of the **row space**?

#### Definitions to Remember:
- **Column space**: The span of the columns of the matrix.
- **Row space**: The span of the rows of the matrix.
- The **dimension** of each space corresponds to the number of **linearly independent vectors** (columns or rows).

**Hint**:
- Both spaces arise naturally from matrices, but it’s unclear at first glance if one dimension exceeds the other.

---

### The Spectacular Fact
**Answer**:
- **The dimension of the column space is always equal to the dimension of the row space**.

Formally:
$$
\text{Dimension of Column Space} = \text{Dimension of Row Space}.
$$

#### Why is this surprising?
- A matrix could have a seemingly large mismatch between the number of rows and columns.
- Despite the potential imbalance, the dimensions of the column and row spaces remain equal.

---

### Understanding Through Examples

1. **Row-Reduced Echelon Form (RREF)**:
   - When a matrix is reduced to its **row-reduced echelon form**, this equality becomes evident.
   - **Key idea**: The number of **pivot columns** exactly corresponds to both the:
     - Number of **linearly independent columns**.
     - Number of **linearly independent rows** (non-zero rows in RREF).

2. **Concept of Pivots**:
   - Pivots represent leading entries in non-zero rows.
   - Each pivot corresponds to a linearly independent column and determines a unique basis vector in the row space.

---

### Why the Dimensions Stay Equal

#### Gaussian Elimination:
- Gaussian elimination (or row reduction) transforms a matrix but **does not alter the dimensions** of its row or column space.

#### Row Space:
- **Row operations don't change the row space:**
  1. Swapping rows doesn’t alter the linear span.
  2. Scaling rows multiplies a vector but keeps the span unchanged.
  3. Adding a multiple of one row to another also preserves the span.

#### Column Space:
- While Gaussian elimination **modifies the column space**, it doesn’t affect its **dimension**. 
  - The dimension of the column space remains constant because it depends on the number of pivot columns, which are preserved during elimination.

#### A Deeper Theorem:
- The **Rank-Nullity Theorem** ensures the dimension of the column space is consistent with transformations:
  $$
  \text{Dimension of Column Space} + \text{Dimension of Null Space} = \text{Number of Columns}.
  $$

---

### Rank of a Matrix

#### Definition:
- The **common dimension** of the row space and the column space is called the **rank** of the matrix.
  $$
  \text{Rank of a Matrix} = \text{Dimension of the Column Space} = \text{Dimension of the Row Space}.
  $$

#### Terminology:
- **Row Rank**: Dimension of the row space.
- **Column Rank**: Dimension of the column space.
- **Fact**: 
  $$
  \text{Row Rank} = \text{Column Rank}.
  $$

#### Summary:
- The rank of a matrix is one of its most fundamental properties, showcasing the overarching structure of its linear transformations and subspaces.

---

### Applications of the Rank Concept
1. **Solving Systems of Linear Equations**:
   - The rank determines the number of constraints in a system.
2. **Matrix Decomposition**:
   - Tools like Singular Value Decomposition (SVD) rely on understanding rank.
3. **Comparing Spaces**:
   - The rank provides a direct link between column space and row space, clarifying their equality.

