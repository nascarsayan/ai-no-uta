## 1. Diagonal Matrices and Eigenvalues

### Key Points:
- **Diagonal matrices**:
  - Their eigenvalues appear on the diagonal.
  - Their eigenvectors form the standard basis in $\mathbb{R}^n$.

### Satellite Feature of Diagonal Matrices:
- A **single nonzero entry** in an entire column is considered a "satellite office" of a diagonal matrix.
    - The nonzero entry must appear **on the diagonal** and be in the same position as it would in a diagonal matrix.

---

## 2. Example: Single Nonzero Entry on Diagonal

### Matrix and Eigenvalue:
- Consider a matrix with $12$ as an eigenvalue:
    - Eigenvalue: $12$
    - Corresponding eigenvector: $\begin{bmatrix} 0 \\ 1 \\ 0 \end{bmatrix}$.

### Verification:
1. Multiply the matrix by the eigenvector:
   $$
   M \begin{bmatrix} 0 \\ 1 \\ 0 \end{bmatrix} = \begin{bmatrix} 0 \\ 12 \\ 0 \end{bmatrix}
   $$
   Result: $\begin{bmatrix} 0 \\ 12 \\ 0 \end{bmatrix}$ is $12 \times \begin{bmatrix} 0 \\ 1 \\ 0 \end{bmatrix}$.  

2. Eigenvalue: $12$, Eigenvector: $\begin{bmatrix} 0 \\ 1 \\ 0 \end{bmatrix}$.

---

## 3. Important Notes on Placement:
- If the **nonzero entry** is **not on the diagonal**, the previous conclusions do **not** apply:
    - Example: Consider a nonzero entry in the third row of the second column. Multiplication with the matrix does not yield correct eigenvalues or eigenvectors.

---

## 4. Effect of Rows with Nonzero Entries

### Single Nonzero Entry in a Row:
- If the nonzero entry is:
  - **In the diagonal position**, and it's the only one in the row:
    - It resembles a row extract from a diagonal matrix.
    - However, eigenvalue logic does **not** apply directly here.

### Why Logic Fails:
- Multiplying the matrix by a corresponding eigenvector (e.g., $\begin{bmatrix} 0 \\ 0 \\ 1 \end{bmatrix}$) picks out the wrong column, hence eigenvalues/eigenvector relationships are lost.

---

## 5. Transpose and Relation to Eigenvalues

### Transpose Matrix:
- Consider the **transpose** of the matrix:
  - Nonzero entry appears **alone** in a column and in a proper diagonal position.

### Properties:
1. Transposed matrix:
   - Eigenvalue: $s$
   - Eigenvector: $\begin{bmatrix} 0 \\ 0 \\ 1 \end{bmatrix}$.

2. **Claim**:
   - The original matrix and its transpose have **identical eigenvalues**.
   - Eigenvalue $s$ applies to both the matrix and the transpose.

---

## Summary:
- Nonzero entries **on the diagonal** play a key role in determining eigenvalues and eigenvectors.
- Placement is critical—entries off-diagonal compromise eigen relationships.
- Transposed matrices retain identical eigenvalues, extending the claims about $s$ being the eigenvalue.