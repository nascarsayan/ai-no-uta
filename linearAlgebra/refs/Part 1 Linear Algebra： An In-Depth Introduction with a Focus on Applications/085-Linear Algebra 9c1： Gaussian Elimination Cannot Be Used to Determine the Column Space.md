## Gaussian Elimination and Column Space

### Why Gaussian Elimination Cannot Determine Column Space

- **Key Issue:** Gaussian elimination changes the column space.
- To understand this concept, consider performing Gaussian elimination on any matrix. You'll observe that the column space of the resulting matrix has changed.
- **Important Note:** The null space remains unchanged during Gaussian elimination. This makes Gaussian elimination useful for determining the null space.

### Null Space and Transformation

- As we simplify a matrix using Gaussian elimination:
  - The **null space** is preserved.
  - Therefore, the null space of the resulting simplified matrix is also the null space of the original matrix.

### Column Space Example

#### Matrix and Column Space Justification

The column space of the following matrix can be expressed as:

$$
\begin{bmatrix}
a & b \\
a & b \\
\end{bmatrix}
$$

#### After Gaussian Elimination

Performing Gaussian elimination leads to a simplified matrix:

$$
\begin{bmatrix}
a & b & 0 \\
0 & 0 & 0 \\
\end{bmatrix}
$$

Despite the Gaussian elimination, the column space of this simplified matrix is:

$$
\begin{bmatrix}
a & b & 0 \\
\end{bmatrix}
$$

### Summary Points

1. **Null Space:** Gaussian elimination works for determining the null space because it remains invariant.
2. **Column Space:** The column space changes during Gaussian elimination, making it unsuitable for determining the column space.