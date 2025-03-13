## Elementary Matrices

### Introduction
- Elementary matrices are derived by applying row or column operations to the identity matrix. 
- They represent the simplest actions in linear algebra related to matrix manipulation.
- Matrix products of elementary matrices can be thought of as actions, making them insightful tools for matrix transformations.

---

### Definition of Elementary Matrices
An **elementary matrix** is obtained by performing basic row or column operations on an identity matrix:
- A single row or column modification (addition, subtraction, scalar multiplication, or swapping).

---

### Example 1: Add Row 1 to Row 2
Starting from the identity matrix:

$$
\begin{bmatrix}
1 & 0 & 0 \\
0 & 1 & 0 \\
0 & 0 & 1
\end{bmatrix}
\longrightarrow
\begin{bmatrix}
1 & 0 & 0 \\
1 & 1 & 0 \\
0 & 0 & 1
\end{bmatrix}
$$

#### Interpretation:
1. From the **row perspective**: Add Row 1 to Row 2.
2. From the **column perspective**: Add Column 2 to Column 1.

---

### Example 2: Multiply Row 2 by 3
Starting from the identity matrix:

$$
\begin{bmatrix}
1 & 0 & 0 \\
0 & 1 & 0 \\
0 & 0 & 1
\end{bmatrix}
\longrightarrow
\begin{bmatrix}
1 & 0 & 0 \\
0 & 3 & 0 \\
0 & 0 & 1
\end{bmatrix}
$$

#### Interpretation:
1. From the **row perspective**: Multiply Row 2 by 3.
2. From the **column perspective**: Multiply Column 2 by 3.

---

### Example 3: Row Operations that Accumulate
Starting from the identity matrix:

$$
\text{Step 1: Add 2 of Row 1 to Row 2.}
\begin{bmatrix}
1 & 0 & 0 \\
2 & 1 & 0 \\
0 & 0 & 1
\end{bmatrix}

\text{Step 2: Add 3 of Row 1 to Row 3.}
\begin{bmatrix}
1 & 0 & 0 \\
2 & 1 & 0 \\
3 & 0 & 1
\end{bmatrix}
$$

#### Key Insight:
- Full row operations must be followed without directly modifying matrix entries outside the rules (e.g., "add a number here").
- Similar logic applies for column transformations.

---

### Highlight: Order of Operations Matters
The sequence of row or column operations can lead to different matrices.

#### Example: Multiply Row 2 by 3, Then Add Row 2 to Row 3
1. Multiply Row 2 by 3:
   $$
   \begin{bmatrix}
   1 & 0 & 0 \\
   0 & 3 & 0 \\
   0 & 0 & 1
   \end{bmatrix}
   $$

2. Add Row 2 to Row 3:
   $$
   \begin{bmatrix}
   1 & 0 & 0 \\
   0 & 3 & 0 \\
   0 & 3 & 1
   \end{bmatrix}
   $$

#### Reverse Order:
- If you add Row 2 to Row 3 first and then multiply Row 2 by 3, the result differs.

#### Column Perspective:
1. Example equivalent for columns: Multiply Column 2 by 3 and then add 3 of Column 3 to Column 2.

---

### Example 4: Swapping Rows or Columns
Starting from the identity matrix:

$$
\text{Switch Rows 1 and 2.}
\begin{bmatrix}
0 & 1 & 0 \\
1 & 0 & 0 \\
0 & 0 & 1
\end{bmatrix}
$$

#### Column Perspective:
- The same transformation applies for swapping Columns 1 and 2.

---

### Complex Example: Accumulating Multiple Operations
Given:

$$
\begin{bmatrix}
1 & 0 & 0 \\
0 & 1 & 0 \\
0 & 0 & 1
\end{bmatrix}
$$

#### Row Perspective:
1. Multiply Row 3 by 2.
2. Add Row 3 to Row 1.
3. Add Row 3 to Row 2.
4. Multiply Row 2 by 2.

#### Column Perspective:
1. Multiply Column 3 by 2.
2. Add 4 of Column 2 to Column 3.
3. Add 2 of Column 1 to Column 3.
4. Multiply Column 2 by 2.

---

### Final Thoughts
Elementary matrices showcase various matrix operations systematically:
1. **Elementary Actions** → Clear transformations (addition, multiplication, swaps).
2. **Order Matters** → Pay close attention to the sequence of operations.
3. **Insightful Exercises** → Helpful for mental agility and deep understanding.

In the next discussion, explore how these matrices act on general matrices through matrix products! 🚀