## Matrix Multiplication

### Definition of Matrix Multiplication

Matrix multiplication is a general operation involving the compatibility of matrix dimensions. Let's construct the definition starting with a specific example:

- A $3 \times 3$ matrix multiplied by a $3 \times 1$ matrix:
  - The dimensions must be compatible. The number of rows in the left matrix must match the number of rows in the right matrix (columns match rows).

### Example 1: $3 \times 3$ Matrix by $3 \times 1$ Matrix

Let the $3 \times 3$ matrix and $3 \times 1$ matrix be given as:

$A = \begin{bmatrix} 1 & 4 & 7 \\ 2 & 5 & 8 \\ 3 & 6 & 9 \end{bmatrix}$ and $B = \begin{bmatrix} 1 \\ 2 \\ 3 \end{bmatrix}$

The matrix product $A \times B$ results in a $3 \times 1$ matrix because we calculate the **linear combination of the columns in $A$** where the coefficients come from $B$.

1. Expanded form:

   $$
   A \times B = 1 \cdot \begin{bmatrix} 1 \\ 4 \\ 7 \end{bmatrix} 
   + 2 \cdot \begin{bmatrix} 2 \\ 5 \\ 8 \end{bmatrix} 
   + 3 \cdot \begin{bmatrix} 3 \\ 6 \\ 9 \end{bmatrix}
   $$

2. Substitute and simplify each entry:

   $$
   \text{First entry: } 1 + 8 + 21 = 30 \\
   \text{Second entry: } 4 + 10 + 24 = 38 \\
   \text{Third entry: } 7 + 16 + 27 = 50
   $$

   Result:

   $$
   \begin{bmatrix} 30 \\ 38 \\ 50 \end{bmatrix}
   $$

3. Insights:
   - Matrix multiplication is fundamentally about organizing **linear combinations** into compact forms.
   - The resulting $3 \times 1$ matrix lies in the **column space** of $A$, as validated by properties (e.g., $\text{Second entry} = \frac{\text{First + Third entries}}{2}$ for $A$).

---

### Example 2: $2 \times 2$ Matrix by $2 \times 1$ Matrix

We now move to a simpler example with smaller matrices. Let $C$ and $D$ be:

$C = \begin{bmatrix} 2 & 1 \\ 0 & -1 \end{bmatrix}, \; D = \begin{bmatrix} -1 \\ 1 \end{bmatrix}$

1. Matrix product $C \times D$ involves finding **one linear combination of the columns of $C$** using coefficients from $D$:

   $$
   C \times D = (-1) \cdot \begin{bmatrix} 2 \\ 0 \end{bmatrix} 
   + 1 \cdot \begin{bmatrix} 1 \\ -1 \end{bmatrix}
   $$

2. Substitution and simplification yield:

   $$
   \text{First entry: } -2 + 1 = -1 \\
   \text{Second entry: } 0 - 1 = -1
   $$

   Result:

   $$
   \begin{bmatrix} -1 \\ -1 \end{bmatrix}
   $$

3. Observations:
   - The resulting matrix ($2 \times 1$ column vector) lies in the **column space** of $C$.
   - This provides further intuition for the role of matrix multiplication in organizing information.

---

### Key Takeaways on Matrix Multiplication

- The **result** of a matrix product (e.g., $A \times B$) lies in the **column space of the left matrix**.
- Matrix multiplication is not a new operation but rather an **organization of linear combinations** into larger structures for efficiency.
- The compact **notations** in matrix algebra simplify many primary operations, providing clarity and unifying concepts.

### Extended Insight

While the resulting expressions in matrix notation are compact, the underlying operations (linear combinations, summing entries, etc.) remain conceptually simple:

- **Column Space**: Results are always in the column space of the left matrix.
- **Dimensional Check**: Ensure compatibility before multiplying.
- **Use Case**: By abstracting and compacting operations, matrix multiplication connects primary concepts into a single, powerful framework.

--- 

### Practice with Multi-Column and Higher-Dimensional Examples

Future examples involve matrices with multiple rows/columns, where concepts such as row space and column space meet. Even in larger-scale problems, the underlying principle— organizing **linear combinations**—remains consistent.