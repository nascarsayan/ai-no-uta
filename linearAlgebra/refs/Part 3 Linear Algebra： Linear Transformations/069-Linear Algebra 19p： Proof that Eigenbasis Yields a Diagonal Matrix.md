## Diagonalization of Linear Transformations with Eigenbases

### Key Idea

When a linear transformation is represented in the component space with respect to an **eigenbasis** (a basis consisting of a complete set of eigenvectors of the transformation), the resulting matrix is a **diagonal matrix**.

---

### General Explanation

Linear algebra often emphasizes generality. To develop a general understanding:

1. Consider a **general linear transformation** \( T \) and assume:
   - \( T \) has a **full set** of eigenvectors.
   - The **dimension** of the vector space is \( n \).

2. Construct an **eigenbasis** \( \{v_1, v_2, \ldots, v_n\} \), where \( v_i \) are eigenvectors of \( T \).

   - Eigenvectors are denoted as \( v_1, v_2, \ldots, v_n \).
   - Corresponding eigenvalues \( \lambda_1, \lambda_2, \ldots, \lambda_n \) are associated with each \( v_i \).

---

### Linear Transformation and Eigenvectors

- Applying the linear transformation \( T \) to an eigenvector \( v_i \) yields:
  $$
  T(v_i) = \lambda_i v_i
  $$
  where \( \lambda_i \) is the eigenvalue associated with \( v_i \).

---

### Constructing the Matrix

1. **Columns Correspond to Basis Vectors:**
   - Each column of the matrix corresponds to the coefficients obtained when decomposing \( T(v_i) \) with respect to the eigenbasis.

2. **Decompositions:**
   
   - For \( T(v_1) = \lambda_1 v_1 \), the coefficient decomposition with respect to the eigenbasis yields:
     $$
     \text{Column 1: } \begin{bmatrix} \lambda_1 \\ 0 \\ 0 \\ \vdots \\ 0 \end{bmatrix}
     $$
   
   - For \( T(v_2) = \lambda_2 v_2 \), the decomposition:
     $$
     \text{Column 2: } \begin{bmatrix} 0 \\ \lambda_2 \\ 0 \\ \vdots \\ 0 \end{bmatrix}
     $$

   - For the last eigenvector \( v_n \) and eigenvalue \( \lambda_n \):
     $$
     \text{Column \( n \): } \begin{bmatrix} 0 \\ 0 \\ \vdots \\ \lambda_n \end{bmatrix}
     $$

---

### Resulting Matrix

The resulting matrix is **diagonal**, with eigenvalues \( \lambda_1, \lambda_2, \ldots, \lambda_n \) along the diagonal:
$$
\begin{bmatrix}
\lambda_1 & 0 & 0 & \cdots & 0 \\
0 & \lambda_2 & 0 & \cdots & 0 \\
0 & 0 & \lambda_3 & \cdots & 0 \\
\vdots & \vdots & \vdots & \ddots & \vdots \\
0 & 0 & 0 & \cdots & \lambda_n
\end{bmatrix}
$$

---

### Insights

- The **generality** of this approach makes the argument simpler because:
  - The decomposition is guaranteed to be **unique** based on the properties of eigenvectors.
  - No assumptions about specific dimensions, vector types, or transformations are required.

### Summary

By constructing the matrix representation of \( T \) in this eigenbasis:
- \( T \) is represented as a **diagonal matrix**.
- The diagonal entries are the eigenvalues \( \lambda_1, \lambda_2, \ldots, \lambda_n \).

This explains why diagonalization is always possible when using an eigenbasis for transformations with a complete set of eigenvectors.