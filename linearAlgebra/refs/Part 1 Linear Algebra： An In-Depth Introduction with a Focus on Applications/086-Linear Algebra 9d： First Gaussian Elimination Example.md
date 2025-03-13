## Gaussian Elimination: Solving a Linear System

### Row Operations and Their Properties
- Three types of row operations are used in Gaussian elimination:
  1. Swapping rows.
  2. Multiplying a row by a scalar (other than zero).
  3. Adding or subtracting a multiple of one row to another.
- These operations preserve relationships among columns, including:
  - The particular solution space.
  - The null space.
  
### Objective of Gaussian Elimination
- Simplify the matrix by introducing zeros in strategic places.
- Extract column relationships to make the solution set apparent.
  
---

### Example: Matrix Simplification Using Gaussian Elimination

#### Step 1: First Pivot Operation
Use the pivot (top-left element) in the first row to simplify the matrix:
- Eliminate `$4$` and `$7$` from the first column.
- Row operation: Subtract `$4$` times the first row from the second row.

Result:
$$
\begin{bmatrix}
1 & 5 & 6 & 9 \\
0 & -3 & -6 & -3 \\
7 & 8 & 9 & 15
\end{bmatrix}
$$

- Middle column relationship is preserved: `$-3$` is the average of `$0$` and `$-6$`.

---

#### Step 2: Second Pivot Operation
Use the pivot in the second row to eliminate `$7$` in the third row:
- Row operation: Subtract `$7$` times the first row from the third row.

Result:
$$
\begin{bmatrix}
1 & 5 & 6 & 9 \\
0 & -3 & -6 & -3 \\
0 & -6 & -12 & -6
\end{bmatrix}
$$

---

#### Step 3: Normalize the Pivot
Normalize the pivot `$-3$` in the second row to `$1$`:
- Row operation: Divide the second row by `$-3$`.

Result:
$$
\begin{bmatrix}
1 & 5 & 6 & 9 \\
0 & 1 & 2 & 1 \\
0 & -6 & -12 & -6
\end{bmatrix}
$$

---

#### Step 4: Eliminate Entries Below the Pivot
Use the normalized pivot in the second row to eliminate `$-6$` in the third row:
- Row operation: Add `$6$` times the second row to the third row.

Result:
$$
\begin{bmatrix}
1 & 5 & 6 & 9 \\
0 & 1 & 2 & 1 \\
0 & 0 & 0 & 0
\end{bmatrix}
$$

Note: Entire third row is eliminated, leaving zeros. This occurs in square matrices with linearly dependent columns.

---

### Observations and Relationships

#### Column Relationships
1. Columns 1 and 2 form a basis.
   - Column 3 is expressed as a linear combination:  
     $C_3 = -C_1 + 2C_2$.

#### Null Space Relation
- Null space derived using column relationships:  
  Vector in null space is:
  $$
  \begin{bmatrix}
  -1 \\ 
  2 \\
  -1
  \end{bmatrix}
  $$

#### Particular Solution
- Right-hand column (solution column) is the sum of the first and second columns.

---

### Gaussian Elimination Summary
- Purpose: Use pivots to simplify the matrix by introducing zeros.
- Output:
  - Revealed column relationships for decomposition and null space identification.
  - Exposed relationships among columns, evident after elimination.
  
Final Matrix:
$$
\begin{bmatrix}
1 & 0 & -1 & 1 \\
0 & 1 &  2 & 1 \\
0 & 0 &  0 & 0
\end{bmatrix}
$$

Perfect columns for decomposition:
- First column: $[1, 0, 0]^T$  
- Second column: $[0, 1, 0]^T$

---

### Next Steps
Perform more examples to reinforce understanding of Gaussian elimination techniques and uncover patterns in linear systems.