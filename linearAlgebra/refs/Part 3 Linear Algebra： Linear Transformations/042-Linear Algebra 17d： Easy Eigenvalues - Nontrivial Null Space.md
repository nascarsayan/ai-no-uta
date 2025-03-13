## Eigenvalues and Null Spaces

### Equivalence of Null Space and Zero Eigenvalue
- The **null space** of a matrix is equivalent to the eigenspace corresponding to the **zero eigenvalue**.
- If a matrix \( A \) is singular and has a non-trivial null space, then:
  - All elements in the null space are eigenvectors corresponding to the **zero eigenvalue**.
  - Mathematically, \( A \vec{v} = 0 = 0 \times \vec{v} \), where \( \vec{v} \) is a null space vector.

---

### Determining Eigenvalues of a Matrix
- **Example Scenario:**
  - Null space is **two-dimensional**:
    - Second column is twice the first.
    - Third column is ten times the first.

- **Observation:**
  - There are **two eigenvalues** corresponding to zero:
    - Eigenvector 1: \( \begin{bmatrix} 2 \\ -1 \\ 0 \end{bmatrix} \)
    - Eigenvector 2: \( \begin{bmatrix} 10 \\ 0 \\ 1 \end{bmatrix} \)

---

### Using the Trace to Identify Eigenvalues
- The trace of a matrix equals the sum of all its eigenvalues.
- Example:
  - Trace of the matrix \( \text{tr}(A) = 35 \).
  - Two eigenvalues are already \( 0 \), so the remaining eigenvalue is \( 35 \).

#### Key Steps:
1. Subtract \( 35 \) (eigenvalue) from the diagonal entries of the matrix.
2. Form a new matrix and simplify using row reduction to identify the null space.

---

### Simplification Process for Null Space
1. Subtract eigenvalue (\( 35 \)) from diagonal:
   $$
   A' =
   \begin{bmatrix}
   34 & 10 & 3 \\
   2 & 31 & 6 \\
   2 & 20 & -5
   \end{bmatrix}
   $$

2. Use **row elimination** to simplify:
   - Target pivots (e.g., eliminate rows using \( 10 \) or \( -5 \) as pivots).
   - Perform operations until the null space becomes visible.

---

### Identifying the Third Eigenvector
- Through elimination, it's possible to see the relationship between column entries:
  - Eigenvector corresponds to the proportional rows \( \begin{bmatrix} 1 \\ 2 \\ 3 \end{bmatrix} \).

#### Observations:
- Simplifying further to confirm the solution:
  - Validate row consistency and proportionality.

---

### Summary of Results
- **Eigenvalues**:
  - \( \lambda_1 = 0, \lambda_2 = 0, \lambda_3 = 35 \)
- **Eigenvectors**:
  - \( \vec{v}_1 = \begin{bmatrix} 2 \\ -1 \\ 0 \end{bmatrix} \)
  - \( \vec{v}_2 = \begin{bmatrix} 10 \\ 0 \\ 1 \end{bmatrix} \)
  - \( \vec{v}_3 = \begin{bmatrix} 1 \\ 2 \\ 3 \end{bmatrix} \)

---

### Strategy Tips for Eigenvalue and Eigenvector Computation
1. Use the nullity of the matrix to quickly identify zero eigenvalues and their eigenvectors.
2. Leverage the trace to find the sum of all eigenvalues.
3. Apply enough row operations to simplify the problem without needing a full row-reduced form.

---

### Next Steps
- Explore additional properties and tricks for efficiently identifying eigenvalues and eigenvectors.