# Notes on Matrix Multiplication with Perspectives

## 1. Matrix Product - Mechanical Approach

We begin by calculating a matrix product mechanically to understand the procedure and get an intuitive feel for it.

### Example 1

Matrix:

$$
\begin{bmatrix}
1 & 2 & 3 \\
4 & 5 & 6 \\
7 & 8 & 9
\end{bmatrix}
\quad \text{and Vector:} \quad
\begin{bmatrix}
0 \\
1 \\
0
\end{bmatrix}
$$

**Linear combination interpretation**:
- Multiply each column of the matrix by the corresponding entries of the vector on the right.
- The operation can be rewritten as:
  $$
  0 \cdot 
  \begin{bmatrix}
  1 \\
  4 \\
  7
  \end{bmatrix}
  +
  1 \cdot 
  \begin{bmatrix}
  2 \\
  5 \\
  8
  \end{bmatrix}
  +
  0 \cdot 
  \begin{bmatrix}
  3 \\
  6 \\
  9
  \end{bmatrix}
  $$
- Simplifying:
  $$
  \begin{bmatrix}
  2 \\
  5 \\
  8
  \end{bmatrix}
  $$

**Result**: The second column of the matrix:
$$
\text{Answer:} \quad 
\begin{bmatrix}
2 \\
5 \\
8
\end{bmatrix}
$$

---

## 2. Bird's Eye View on Matrix Multiplication

### Insights:
- Matrix multiplication can be thought of as **column selection or transformation**.
- It isn't just computation but understanding the action of one matrix on another.

---

### Example 2: Action Interpretation

Given the same matrix:
$$
\begin{bmatrix}
1 & 2 & 3 \\
4 & 5 & 6 \\
7 & 8 & 9
\end{bmatrix}
$$
and a vector:
$$
\begin{bmatrix}
0 \\
0 \\
1
\end{bmatrix}
$$

**Interpretation**:
- This vector "picks out" the third column of the matrix, as zeros in the first two entries eliminate contributions from the first two columns.

**Result**:
$$
\text{Answer:} \quad
\begin{bmatrix}
3 \\
6 \\
9
\end{bmatrix}
$$

---

## 3. Matrix as an Adder

### Example 3: Adding Columns

Consider:
$$
\begin{bmatrix}
1 & 1 & 1 \\
1 & 1 & 1 \\
1 & 1 & 1
\end{bmatrix}
\quad \text{and Vector:} \quad
\begin{bmatrix}
1 \\
1 \\
1
\end{bmatrix}
$$

**Action**:
- The vector of all ones adds up all columns of the matrix.

**Result**:
$$
\text{Answer:} \quad
\begin{bmatrix}
3 \\
3 \\
3
\end{bmatrix}
$$

---

## 4. General Perspective: Matrix as Action

Key takeaway:
- Matrix-vector multiplication can be seen as describing an **action**.
  - **Mechanically**: Following the linear combination procedure.
  - **Conceptually**: Understanding the **structural effect** (e.g., column selection or column addition).
- Multiple perspectives (mechanical & conceptual) enrich understanding:
  - **Mechanical**: Builds technical proficiency.
  - **Conceptual**: Offers insights into higher-level behavior.

Examples:
1. Vectors can "pick" columns.
2. Specific vectors may lead to summing columns.
  
### Practice:
- Begin by practicing **simple examples** (e.g., $2 \times 2$ or $3 \times 3$).
- Use both the **mechanical approach** and **conceptual understanding**.

😄 "Matrix multiplication is not only arithmetic; it's an action! Keep thinking about what matrices **do**, not just what they calculate."