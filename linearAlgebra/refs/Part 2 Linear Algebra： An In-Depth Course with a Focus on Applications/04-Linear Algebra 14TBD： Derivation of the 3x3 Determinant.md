## 1. Determinants of 2x2 and 3x3 Matrices

### 1.1 Determinant of a 2x2 Matrix
- In earlier discussions, we derived the formula for the determinant of a 2x2 matrix. This served as a foundation for understanding determinants of higher dimensions. 

### 1.2 Determinant of a 3x3 Matrix

**Goal**: To derive an algebraic criterion for determining if the columns of a 3x3 matrix are linearly dependent.

**Key differences**:
- For a 2x2 matrix, the columns are linearly dependent if one column is a scalar multiple of the other.
- For a 3x3 matrix, the columns are linearly dependent in richer scenarios:
  - One column is a scalar multiple of another.
  - One column is a linear combination of the other two columns.

### 1.3 Algebraic Criterion for Linearly Dependent Columns

1. **Gaussian Elimination**:
   - Assume the matrix is not singular (i.e., determinant $\neq 0$ initially). This assumption will eventually not matter.
   - Eliminate entries below the first pivot in the first column using row operations.

2. **Reduction**:
   - After elimination, if you encounter a submatrix where:
     - A column has a single non-zero entry at the pivot position, and
     - The other two entries in that column are zero,
     - Then, whether or not the original 3x3 matrix is linearly dependent depends on the determinant of the resulting 2x2 submatrix.

3. **Recursive Process**:
   - Reduce the 3x3 matrix problem to a 2x2 determinant problem.

### 1.4 Determinant of a 3x3 Matrix

**Method**: Perform Gaussian elimination and eliminate fractions to simplify the result. The determinant of the matrix will ultimately determine whether the columns are linearly dependent.

Here is the celebrated **formula for the determinant of a 3x3 matrix**:

$$
\text{det}(A) = a(ei - fh) - b(di - fg) + c(dh - eg)
$$

Where the matrix $A$ is:

$$
\begin{bmatrix} 
a & b & c \\ 
d & e & f \\ 
g & h & i 
\end{bmatrix}
$$

### 1.5 Key Observations
1. **Zero Determinant**: 
   - If $\text{det}(A) = 0$, the columns of the matrix are linearly dependent.
2. **Non-zero Determinant**:
   - If $\text{det}(A) \neq 0$, the columns of the matrix are linearly independent.

3. **General Properties**:
   - The determinant of a 3x3 matrix serves its purpose universally and robustly for all 3x3 matrices.
   - No memorization of the formula is necessary. Techniques like co-factor expansion and row/column eliminations can simplify calculations.

---

### 1.6 Practical Consideration
1. **Fractions and Robustness**:
   - The eventual goal is to eliminate fractional terms by multiplying through to simplify.
   - Dividing terms like $\frac{b}{a}$ in earlier 2x2 determinant calculations created robustness issues (e.g., dividing by zero). This simplification prevents similar pitfalls for 3x3 matrices.
   
2. **Higher-order Determinants**:
   - While the current focus is on 3x3 determinants, this logic extends to higher dimensions, such as 4x4 and beyond.

---

### 1.7 Tips for Application
- Understanding the formula for small matrices like 2x2 and 3x3 lays the foundation for more complex linear algebra problems.
- Focus on the process of deriving the determinant (expansion by minors, row operations) rather than rote memorization of the formula.