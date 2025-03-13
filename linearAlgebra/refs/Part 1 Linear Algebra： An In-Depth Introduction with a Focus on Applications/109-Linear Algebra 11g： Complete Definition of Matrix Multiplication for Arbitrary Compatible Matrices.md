## Extending Matrix Multiplication

### 1. Matrix Multiplication Beyond Single Column

- The definition of matrix multiplication is now extended to matrices on the right with **more than one column**.
- The extension involves **calculating multiple linear combinations** of the columns on the left matrix.

#### Key Idea:
If there are $n$ columns in the matrix on the right, the output will also have $n$ columns, with each column computed by a **linear combination**.

### 2. Linear Combinations and Outputs

#### General Rule:
- Each column of the result matrix is obtained by a **linear combination of the columns** of the left matrix.
- The coefficients for the linear combination come **from the corresponding column** of the right matrix.

#### Example:
Given the left matrix:

$$
\begin{bmatrix}
1 & 2 & 3 \\
4 & 5 & 6 \\
7 & 8 & 9
\end{bmatrix}
$$

and the right matrix:

$$
\begin{bmatrix}
1 & 0 \\
2 & 1 \\
3 & 1
\end{bmatrix}
$$

1. The first column of the output is the linear combination of the columns of the left matrix with coefficients $[1, 2, 3]$:

$$
1 \cdot \begin{bmatrix} 1 \\ 4 \\ 7 \end{bmatrix} +
2 \cdot \begin{bmatrix} 2 \\ 5 \\ 8 \end{bmatrix} +
3 \cdot \begin{bmatrix} 3 \\ 6 \\ 9 \end{bmatrix} =
\begin{bmatrix} 14 \\ 32 \\ 50 \end{bmatrix}
$$

2. Similarly, the second column of the output is:
   - Compute with coefficients $[0, 1, 1]$:
   
   $$
   0 \cdot \begin{bmatrix} 1 \\ 4 \\ 7 \end{bmatrix} +
   1 \cdot \begin{bmatrix} 2 \\ 5 \\ 8 \end{bmatrix} +
   1 \cdot \begin{bmatrix} 3 \\ 6 \\ 9 \end{bmatrix} =
   \begin{bmatrix} 5 \\ 11 \\ 17 \end{bmatrix}
   $$

Thus, the final result of the matrix multiplication:

$$
\begin{bmatrix}
14 & 5 \\ 
32 & 11 \\
50 & 17
\end{bmatrix}
$$

---

### 3. Properties of the Result
1. **Column Space Compatibility:**
   - The result columns are guaranteed to lie within the **column space** of the left matrix because they are **linear combinations** of its columns.

2. **Compatibility of Dimensions:**
   - If the left matrix is $m \times n$ and the right matrix is $n \times p$, the result will be an $m \times p$ matrix.
   - **Inner dimensions must match**: The number of columns in the left matrix must equal the number of rows in the right matrix.

---

### 4. Compatibility Criteria for Matrix Multiplication

- **Height of Matrix on the Right = Width of Matrix on the Left**
- In terms of dimensions:
   - The left matrix is $3 \times 3$, and the right matrix is $3 \times 2$.
   - The resulting matrix will have dimensions $3 \times 2$.

Alternatively:
- **Match Inner Dimensions:** $3 \times \mathbf{3}$ and $\mathbf{3} \times 2 \Rightarrow$ the inner $3$'s match.

---

### 5. Example with 2x2 and 2x4 Matrices

#### Question:
Calculate the product of the 2x2 matrix:

$$
\begin{bmatrix}
1 & 2 \\
3 & 4
\end{bmatrix}
$$

and the 2x4 matrix:

$$
\begin{bmatrix}
1 & -1 & 0 & 0.5 \\
1 & 1 & 1 & 1
\end{bmatrix}
$$

#### Steps:
Each column of the result is a linear combination of the columns of the first matrix, using coefficients from the corresponding column of the second matrix.

1. **First Column:**
   Coefficients: $[1, 1]$

   $$
   1 \cdot \begin{bmatrix} 1 \\ 3 \end{bmatrix} +
   1 \cdot \begin{bmatrix} 2 \\ 4 \end{bmatrix} =
   \begin{bmatrix} 3 \\ 7 \end{bmatrix}
   $$

2. **Second Column:**
   Coefficients: $[-1, 1]$

   $$
   -1 \cdot \begin{bmatrix} 1 \\ 3 \end{bmatrix} +
   1 \cdot \begin{bmatrix} 2 \\ 4 \end{bmatrix} =
   \begin{bmatrix} 1 \\ 1 \end{bmatrix}
   $$

3. **Third Column:**
   Coefficients: $[0, 1]$

   $$
   0 \cdot \begin{bmatrix} 1 \\ 3 \end{bmatrix} +
   1 \cdot \begin{bmatrix} 2 \\ 4 \end{bmatrix} =
   \begin{bmatrix} 2 \\ 4 \end{bmatrix}
   $$

4. **Fourth Column:**
   Coefficients: $[0.5, 1]$

   $$
   0.5 \cdot \begin{bmatrix} 1 \\ 3 \end{bmatrix} +
   1 \cdot \begin{bmatrix} 2 \\ 4 \end{bmatrix} =
   \begin{bmatrix} 2.5 \\ 5.5 \end{bmatrix}
   $$

#### Final Result:

$$
\begin{bmatrix}
3 & 1 & 2 & 2.5 \\ 
7 & 1 & 4 & 5.5
\end{bmatrix}
$$

---

### 6. Description of Columns as Linear Actions

- **Column 1:** Adds the columns.
- **Column 2:** Takes the difference ($2^\text{nd} - 1^\text{st}$).
- **Column 3:** Picks the 2nd column only.
- **Column 4:** Averages the columns ($0.5 \cdot 1^\text{st} + 1 \cdot 2^\text{nd}$).

---

### 7. Conclusion and Practice

To develop an intuitive understanding of matrix multiplication:
1. **Practice extensively:** Solve many examples varying in size and complexity.
2. **Think geometrically:** Interpret the columns of the resulting matrix as **effects of linear transformations** applied to the input.

