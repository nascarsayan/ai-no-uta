## Linearity of the Determinant

### Overview

The linear property of the determinant, often referred to as linearity, applies to both rows and columns of a matrix. For convenience, this discussion focuses on rows (owing to the row-wise definition of the determinant), but the arguments apply equally well to columns due to the **transpose property**.

Linearity is broken down into **two primary parts**:
1. **Sum of two vectors (row addition property).**
2. **Scalar multiplication of a row.**

---

### 1. Linearity with Respect to the Sum of Two Vectors

#### Row Addition Property

When a particular row in a matrix can be expressed as the sum of two vectors, the determinant of the matrix equals the **sum of determinants** of two new matrices:
- The first matrix has the first vector replacing the row in question.
- The second matrix has the second vector in place of the row.

#### Example:

Consider a $4 \times 4$ matrix. Observe its **first row**. Assume the first row can be expressed as the sum:

$$
\text{Row}_1 = [30, 40, 60, 80] + [1, 1, 1, 1].
$$

By linearity (part 1), the determinant of the original matrix equals:
1. The determinant of a matrix where **Row 1 = [30, 40, 60, 80]**, and other rows remain the same.
2. Plus, the determinant of a matrix where **Row 1 = [1, 1, 1, 1]**, and all other rows remain unchanged.

#### Observations:

- You can break up **any row** in the matrix this way.
- However, you must always work on **one row at a time**.

This property mirrors the **distributive law** in algebra.

---

### 2. Linearity with Respect to Scalar Multiplication

#### Scalar Multiplication Property

If a particular row in a matrix is expressed as a scalar multiple of a vector, then the determinant of the matrix equals the **scalar multiplied by the determinant of a modified matrix**, where:
- The row in question is replaced by the vector itself.
- The remaining rows are unchanged.

#### Example:

Let the **third row** of a matrix be represented as:

$$
\text{Row}_3 = 11 \cdot [3, 1, 4, 0].
$$

By linearity (part 2), the determinant equals:

$$
\det(\text{Matrix}) = 11 \cdot \det(\text{Modified Matrix}),
$$

where the modified matrix has **Row 3 = [3, 1, 4, 0]**, while other rows stay the same.

---

### Special Case: A Matrix with a Zero Row/Column

If a matrix contains a **row or column of zeros**, its determinant is **zero**:

#### Example:

Consider a matrix with a **zero column** (e.g., the fourth column). Using the scalar multiplication property:
- Scaling the zero column by any number leaves the matrix **unchanged**, so the determinant remains the same.
- Simultaneously, the determinant is also multiplied by the scalar, leading to an equation:

$$
\text{Determinant} = \text{Number} \times \text{Determinant}.
$$

The only solution is:

$$
\text{Determinant} = 0.
$$

---

### Proofs of Linearity

#### Proof of Part 1: Row Addition Property 

When a row is thought of as the sum of two vectors (e.g., the **second row**), the resulting determinant can be broken into two components by the **distributive law**:

1. For any permutation contributing to the determinant, the entry corresponding to the second row is the sum: 
   $$ a + b, $$ 
   where:
   - $a$ comes from the first vector.
   - $b$ comes from the second vector.
2. This summation distributes across the terms of the determinant expansion, creating **two disjoint groups of terms**:
   - One corresponds to the determinant of the matrix with the first vector in the row.
   - The other corresponds to the determinant of the matrix with the second vector in the row.

Thus, the determinant equals the **sum of these two determinants**.

#### Proof of Part 2: Scalar Multiplication

When a row is represented as a scalar multiple of a vector:

1. Each term in the determinant expansion corresponding to the row can be expressed as:
   $$ k \cdot ( \text{entry from the vector} ), $$
   where $k$ is the scalar.
2. The scalar $k$ can be factored out of the determinant, as it is multiplied across all terms involving that row.
3. What remains is the determinant of the matrix where the scalar is replaced by the vector itself in that row.

Thus, scaling a row results in scaling the determinant by the same factor.

---

### Consequences of Linearity

1. **Matrices with Zero Rows or Columns**:
   - Determinants of such matrices are always **zero** (follows from Part 2 of linearity).
   
2. **Row/Column Operations**:
   - Linearity allows determinant calculations to break into simpler components, enabling mathematical simplification and useful operations like cofactor expansion.

3. **Geometric Interpretation**:
   - Linearity imbues determinants with connections to **area** (2D) and **volume** (3D), as these transformations respect the distributive and scaling properties.
   
