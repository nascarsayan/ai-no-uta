## Incompatible Matrix Products

### Matrix compatibility
- A matrix product can only be formed if the number of columns in the first matrix matches the number of rows in the second matrix.

### Example:
- Consider two matrices:
    - The matrix on the left:
        $$
        \begin{bmatrix}
        a_{11} & a_{12} & a_{13} \\
        a_{21} & a_{22} & a_{23}
        \end{bmatrix}
        $$
        (3 columns)
    - The matrix on the right:
        $$
        \begin{bmatrix}
        b_{11} & b_{12} \\
        b_{21} & b_{22}
        \end{bmatrix}
        $$
        (2 rows)
- Since the number of columns in the left matrix (3) does not match the number of rows in the right matrix (2), the multiplication is **incompatible**.

### Implications:
1. **Matrix structure**: You cannot form a legitimate linear combination when the dimensions are mismatched.
   - For a matrix product to work, the second matrix must have entries corresponding to every column in the first matrix.

### Practical Usefulness:
#### 1. Prevention of mistakes:
- Encountering incompatible matrices signals an error in the setup or formulation of the problem.
- This helps pinpoint where assumptions or calculations went wrong.

#### 2. Exam scenarios:
- Incompatible matrix products might be included in exams as trick questions to test understanding.
- **Advice**: If you find an incompatible matrix product on an exam, it's likely the examiner only included one such example (to avoid frustration).

### Final Note:
- Watch out for incompatible matrices in both theoretical and practical problems to ensure correct computation.