# Notes: Matrix Algebra - Identity Matrix and its Properties

## 1. Basic Properties of Matrix Multiplication

- **Key concepts we have established so far**:
  - Defined **matrix multiplication**.
  - Established **associativity**:
    $$
    (AB)C = A(BC)
    $$
    Without associativity, further progress in matrix algebra wouldn't be possible!
  - Determined that **matrix multiplication is non-commutative**:
    $$
    AB \neq BA
    $$
    This surprising discovery adds depth to matrix algebra and makes it more interesting.

---

## 2. Identity Matrix

- The **identity matrix** is analogous to the number **1** in ordinary multiplication. For any real number:
  $$
  5 \times 1 = 5
  $$
  - Similarly, multiplying any matrix by the identity matrix leaves it **unchanged**.

- **Definition**: The identity matrix is characterized by having `1s` on the diagonal and `0s` everywhere else. 

- **Example**: A $3 \times 3$ identity matrix:
  $$
  I = \begin{bmatrix}
  1 & 0 & 0 \\
  0 & 1 & 0 \\
  0 & 0 & 1
  \end{bmatrix}
  $$

---

## 3. Multiplying by the Identity Matrix

### 3.1. Right Multiplication: Matrix Remains Unchanged
- When the identity matrix appears **on the right**:
  $$
  A \cdot I = A
  $$
  - Let $A = \begin{bmatrix} 1 & 4 & 7 \\ 2 & 5 & 8 \\ 3 & 6 & 9 \end{bmatrix}$.
  - Multiplying by $I$:
    $$
    A \cdot I = \begin{bmatrix}
    1 & 4 & 7 \\
    2 & 5 & 8 \\
    3 & 6 & 9
    \end{bmatrix}
    $$

  - Perspective: The **columns** of the product are **column pickers**. For instance:
    - The first column of $I$ selects the first column of $A$, and so on.

### 3.2. Left Multiplication: Matrix Remains Unchanged
- When the identity matrix appears **on the left**:
  $$
  I \cdot A = A
  $$
  - Here, the **rows** of the identity matrix act as **row pickers**.
    - First row of $I$ picks the first row of $A$, and so on.

  - Example:
    $$
    I \cdot \begin{bmatrix}
    1 & 4 & 7 \\
    2 & 5 & 8 \\
    3 & 6 & 9
    \end{bmatrix}
    =
    \begin{bmatrix}
    1 & 4 & 7 \\
    2 & 5 & 8 \\
    3 & 6 & 9
    \end{bmatrix}
    $$

### 3.3. Vector Multiplication
- The identity matrix leaves any vector unchanged.
  $$
  I \cdot \begin{bmatrix} x \\ y \\ z \end{bmatrix} = \begin{bmatrix} x \\ y \\ z \end{bmatrix}
  $$

---

## 4. Big Picture of the Identity Matrix

- **Key observations**:
  - The identity matrix interacts with square matrices such that:
    $$
    A \cdot I = I \cdot A = A
    $$
  - It works as a **column picker** when on the right and as a **row picker** when on the left.
  - **Applicable to vectors**: Leaves both $3 \times 1$ and $1 \times 3$ matrices unchanged.

- **Why is it important?**
  - The identity matrix plays a critical role in solving linear equations using matrix algebra.
  - It provides the foundation for defining inverse matrices.

---

## 5. Final Remark

- Mastering the identity matrix completes an essential part of matrix algebra.
- **Next step**: Solving linear equations using matrix operations.