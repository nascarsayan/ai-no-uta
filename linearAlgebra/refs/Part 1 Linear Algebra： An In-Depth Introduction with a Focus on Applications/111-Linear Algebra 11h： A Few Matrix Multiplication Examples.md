## Matrix Multiplication Examples

This video covers various matrix multiplication examples, including properties of the resulting matrices and insights into their structure.

---

### 1. Matrix Multiplication: A 1x4 Matrix with a 4x1 Matrix

- **Key Points:**
  - The product of a $1 \times 4$ and a $4 \times 1$ matrix results in a $1 \times 1$ matrix.
  - The single value in the resulting matrix is obtained by summing the pairwise products of corresponding entries.

- **Matrix Dimensions and Compatibility:**
  $$1 \times 4 \quad \text{and} \quad 4 \times 1 \implies \text{Inner dimensions match. Resulting matrix is } 1 \times 1.$$

---

### 2. Reversing the Order: 4x1 Matrix Multiplying a 1x4 Matrix

- **Key Points:**
  - The product is a $4 \times 4$ matrix.
  - The inner dimensions "drop out," leaving $4 \times 4$ dimensions.
  - Each column of the resulting matrix is a scaled version of the input column.
  
- **Example:**
  
  Dimensions of the resulting matrix:
  $$4 \times 1 \quad \text{and} \quad 1 \times 4 \implies \text{Resulting matrix is } 4 \times 4.$$

  First column of the result:
  $$
  \text{(1st column)} = 
  \begin{pmatrix} 1 \\ 2 \\ 3 \\ 4 \end{pmatrix} \quad \text{scaled by coefficient from the 1st matrix.}
  $$
  
  Final 4x4 Matrix:
  $$
  \begin{bmatrix}
  1 & 2 & 3 & 4 \\
  2 & 4 & 6 & 8 \\
  3 & 6 & 9 & 12 \\
  4 & 8 & 12 & 16
  \end{bmatrix}.
  $$

  - **Rank Insight:** All columns are linearly dependent (multiples of the first). Hence, rank = 1.

---

### 3. Multiplying Two Opposite-Dimension Matrices (2x3 and 3x2)

- **Key Points:**
  - Compatibility: $2 \times 3$ and $3 \times 2$ matrices can be multiplied either way.
  - Dimensions of the resulting matrix depend on the multiplication order:
    - $2 \times 3$ followed by $3 \times 2$ results in a $2 \times 2$ matrix.
    - $3 \times 2$ followed by $2 \times 3$ results in a $3 \times 3$ matrix.

- **Example 1:** $2 \times 3$ multiplied by $3 \times 2$:
  
  First column:
  $$
  \begin{bmatrix}
  2 \\
  3
  \end{bmatrix}, 
  \quad \text{resulting in entries from linear combinations.}
  $$

  Resulting 2x2 Matrix:
  $$
  \begin{bmatrix}
  a & b \\
  c & d
  \end{bmatrix}.
  $$

- **Example 2:** The reverse order results in structured 3x3 matrices.

---

### 4. Triangular Matrices: Multiplications in 3x3 Matrices

- **Definitions:**
  - **Diagonal**: Entries at $(i, i)$ positions (e.g., $(1,1), (2,2), (3,3)$).
  - **Upper Triangular**: Zeros below the diagonal.
  - **Lower Triangular**: Zeros above the diagonal.

- **Insights:**
  - The multiplication of two upper triangular matrices results in another upper triangular matrix.
  - The multiplication of two lower triangular matrices results in another lower triangular matrix.

- **Generalization:**
  - For matrices of any dimension $n \times n$, the product of upper (or lower) triangular matrices of the same type remains triangular.

---

### 5. Sparse and Special Matrices: Structure and Effects

- **Example: Column-Based Multiplication:**
  - Sparse matrices can act as "column pickers" or "row switchers" during multiplication.
  - **Action Description:** Multiplying by a specific sparse matrix may switch columns or rows, depending on the multiplication order.

- **Analysis of Sparse Matrix Effects:**
  - Left multiplication might switch rows; right multiplication might switch columns.

  Sparse Matrix Example:
  $$
  \begin{bmatrix}
  0 & 1 & 0 \\
  1 & 0 & 0 \\
  0 & 0 & 1
  \end{bmatrix}.
  $$

---

### Concluding Remarks

- Matrix multiplication reveals rich structures:
  - Triangular matrices maintain their triangle type after multiplication.
  - Sparse matrices reveal specific transformation patterns.
  - Visualizing multiplication in terms of effects on the column/row space helps shift focus from computational mechanics to logical structure.