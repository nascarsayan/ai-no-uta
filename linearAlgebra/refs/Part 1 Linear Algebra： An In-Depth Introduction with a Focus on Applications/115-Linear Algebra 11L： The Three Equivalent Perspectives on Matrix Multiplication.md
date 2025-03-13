## Matrix Multiplication Perspectives

There are three main perspectives to matrix multiplication:

---

### 1. Columns Perspective
- The columns of the resulting matrix are **linear combinations** of the columns of the matrix on the left.
- The **coefficients** for these linear combinations come from the columns of the matrix on the right.

#### Example: First Column of the Result
- Coefficients: $[1, 2, 0]$
  
$$
\text{First Column of Result} = 1 \cdot \text{First Column of Left Matrix} + 2 \cdot \text{Second Column of Left Matrix}
$$

- Result: $[3, 2, -1, 3]$

#### Process for Each Column:
- Repeat for the second column, third column, and so on, using respective coefficients from the columns of the right matrix.

---

### 2. Dot Product Perspective
- Each **entry** in the resulting matrix is computed as the **dot product** of a row from the left matrix and a column from the right matrix.

#### Key Steps for a Single Entry:
- For an entry in the $i$th row and $j$th column:
  1. Take the $i$th **row** of the left matrix.
  2. Take the $j$th **column** of the right matrix.
  3. Perform the operation:
  
$$
\text{Entry in Result} = \sum_k (\text{Left\_Matrix}[i, k] \cdot \text{Right\_Matrix}[k, j])
$$

#### Example:
- Considering Coefficients $[2, 0, 1]$:
  - Compute only the **third entry** (row 3, column 2):
  
$$
\text{Value} = (2 \cdot \text{Left}[3,1]) + (0 \cdot \text{Left}[3,2]) + (1 \cdot \text{Left}[3,3])
$$

#### Advantage:
- You can compute **individual entries** or just the entries you need without calculating entire rows or columns.

---

### 3. Rows Perspective
- The **rows** of the resulting matrix are **linear combinations** of the rows of the matrix on the right.
- The **coefficients** for these linear combinations come from the rows of the matrix on the left.

#### Example: Fourth Row of the Result
- Coefficients: $[1, 1, 0]$
  
$$
\text{Fourth Row of Result} = 1 \cdot \text{First Row of Right Matrix} + 1 \cdot \text{Second Row of Right Matrix}
$$

- Result: Fourth row of the resulting matrix is $[3, 2, 1]$.

#### Process for Each Row:
- Repeat for the first row, second row, and so on, using respective coefficients from the rows of the left matrix.

---

### Summary of Perspectives
- **Columns Perspective**: Determine each column of the result as a linear combination of the columns of the left matrix.
- **Dot Product Perspective**: Compute individual entries of the result by taking dot products of rows of the left matrix and columns of the right matrix.
- **Rows Perspective**: Determine each row of the result as a linear combination of the rows of the right matrix.

---

### Advantages of Different Perspectives
- **Columns Perspective**: Useful when approaching matrix-vector multiplication or when focused on entire columns.
- **Dot Product Perspective**: Ideal for calculating **specific entries** without computing the entire matrix.
- **Rows Perspective**: Efficient when the left matrix has many zeros (sparse rows) or you’re dealing with sparse linear combinations.

### Choosing Which Perspective to Use
- Depends on the **purpose** and the **structure** of the matrices.
- Example:
  - Sparse left matrix → Rows Perspective.
  - Interested in a few entries of the resulting matrix → Dot Product Perspective.
  - Full computation prioritized → Columns Perspective.

