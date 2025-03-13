# Notes on 2x2 Linear Dependence and Determinants

## 1. Linear Dependence in a 2x2 Matrix
To determine whether the columns of a $2 \times 2$ matrix are linearly dependent, we rely on proportionality between the columns. Criterion involves checking ratios or equivalence.

### Example: Proportional Columns
Consider a matrix:
$$
\begin{bmatrix}
3 & 9 \\
7 & 21
\end{bmatrix}
$$

- The second column is proportional to the first column: 
  $$
  \frac{9}{3} = \frac{21}{7} = 3
  $$
  Thus, the columns are linearly dependent.

## 2. Criteria for Linear Dependence
Two approaches to identifying linear dependence:
1. **Column-wise Ratios**: Check if $\frac{b}{a} = \frac{d}{c}$ for columns $\begin{bmatrix} a \\ c \end{bmatrix}$ and $\begin{bmatrix} b \\ d \end{bmatrix}$.
2. **Row-wise Ratios**: Check if $\frac{a}{c} = \frac{b}{d}$.

### General Case
Let the matrix be:
$$
\begin{bmatrix}
a & b \\
c & d
\end{bmatrix}
$$

- According to the **first approach**, the columns are dependent if:
  $$
  \frac{b}{a} = \frac{d}{c} \quad \text{(or equivalently, } b \cdot c = a \cdot d \text{).}
  $$
  
- According to the **second approach**, the columns are dependent if:
  $$
  \frac{a}{c} = \frac{b}{d} \quad \text{(or equivalently, } a \cdot d = b \cdot c \text{).}
  $$

Both methods conclude the same, as $a \cdot d = b \cdot c$.

## 3. Issues with the Ratio-Based Approach
Problems arise when the matrix contains zeros:
- Division by zero causes both column-wise and row-wise criteria to fail.
- Example:
  $$
  \begin{bmatrix}
  0 & 8 \\
  5 & 0
  \end{bmatrix}
  $$
  Here, ratios like $\frac{0}{5}$ or $\frac{8}{0}$ are undefined.

Another edge case:
- Zero matrix, e.g.:
  $$
  \begin{bmatrix}
  0 & 0 \\
  0 & 0
  \end{bmatrix}
  $$
  Causes ratio-based methods to fail. 

## 4. Robust Criterion: Avoiding Division
To avoid division, compare proportionality using multiplication:
- Columns $\begin{bmatrix} a \\ c \end{bmatrix}$ and $\begin{bmatrix} b \\ d \end{bmatrix}$ are proportional if:
  $$
  a \cdot d = b \cdot c
  $$

This criterion works even with zeros in the matrix. Examples:
1. Apply to:
   $$
   \begin{bmatrix}
   3 & 9 \\
   7 & 21
   \end{bmatrix}
   $$
   Compute:
   $$
   3 \cdot 21 = 63, \quad 9 \cdot 7 = 63 \quad \implies \text{Columns dependent.}
   $$

2. Apply to:
   $$
   \begin{bmatrix}
   0 & 8 \\
   5 & 0
   \end{bmatrix}
   $$
   Compute:
   $$
   0 \cdot 0 = 0, \quad 8 \cdot 5 = 0 \quad \implies \text{Columns dependent.}
   $$

This avoids division by zero entirely.

## 5. Determinants and Linearity
The determinant is inspired by the robust criterion. For a $2 \times 2$ matrix:
$$
\text{Matrix } A = \begin{bmatrix}
a & b \\
c & d
\end{bmatrix}, \quad \text{Determinant: } \text{det}(A) = ad - bc
$$

- Linearly dependent columns:
  $$
  \text{det}(A) = 0
  $$

### Key Reformulation
Combine all terms into a single expression for robustness:
$$
ad - bc = 0
$$
This is equivalent to $a \cdot d = b \cdot c$ but provides a compact and unified formula that avoids ratio pitfalls.

## 6. Final Definition
For a $2 \times 2$ matrix $A$, the determinant is:
$$
\text{det}(A) = ad - bc
$$

- Linear dependence of columns occurs when $\text{det}(A) = 0$.

**Boxed Formula**:
$$
\boxed{\text{det}(A) = ad - bc}
$$

This definition is robust and works for all cases, including zero-containing matrices.

---

Next steps involve extending this determinant concept to $3 \times 3$ matrices and higher dimensions.