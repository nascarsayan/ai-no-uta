## 1. Third and Final Explanation of the Matrix Inversion Algorithm

### Overview
- A different way to understand the matrix inversion algorithm using **elementary matrices** and associated **row operations**.
- Avoids focusing on individual matrix entries or drawing matrices explicitly.
- Focuses on **row operations** and actions on matrices as whole objects.

---

### Transforming the Matrix to Its Row-Reduced Echelon Form
1. **Invertible Square Matrix ($A$)**:
   - Only square matrices are invertible, so the **inversion algorithm** applies only to them.
   - $A$ will be transformed using **Gauss-Jordan elimination**.

2. **Gauss-Jordan Elimination**:
   - Sequentially apply row operations to transform $A$ into the **Identity Matrix ($I$)**.
   - Each column being a **pivot column** validates the process.

3. **Result of Transformation**:
   - After all steps, $A$ becomes $I$.
   - Steps of **Gaussian elimination**, **row scaling**, and **Jordan back-substitution** are followed.

---

### Capturing the Operations with Elementary Matrices
1. **Elementary Matrices**:
   - Each row operation (e.g., swapping rows, scaling rows, back substitution) can be expressed using a corresponding elementary matrix.
   - These operate by **left multiplication** on the matrix.

2. **Combining Operations**:
   - If multiple row operations are performed, the corresponding elementary matrices **stack** by multiplication in sequence:
     $$
     E_k \cdot E_{k-1} \cdots E_1 \cdot A = I
     $$

---

### Order of Operations in Gauss-Jordan Elimination
The sequence of operations generally involves:
1. **Gaussian Elimination**:
   - Operate on **lower-numbered rows** using **higher-numbered rows**.
   - Swap rows if necessary.
   - Example: $L_1, L_2$, etc. for row eliminations.

2. **Scaling Rows** to Obtain Unit Pivots:
   - Achieved using **diagonal elementary matrices ($D_1, D_2$)**.

3. **Jordan Back Substitution**:
   - Clears above-diagonal elements.
   - Done using **upper triangular matrices ($U_1, U_2$)**.

---

### Steps to Compute the Inverse
1. Start with $A$ and sequentially transform it into $I$.
2. Record all steps as corresponding elementary matrices (**$L$, $S$, $D$, $U$, etc.**).
3. On final transformation:
   - The sequence of matrices applied to $A$ to convert it into $I$ is precisely **$A^{-1}$**.

4. Express the inverse explicitly:
   $$
   A^{-1} = U_2 \cdot U_1 \cdot D_2 \cdot D_1 \cdot S_1 \cdot L_4 \cdot \ldots \cdot L_1
   $$

---

### Interpretation of the Algorithm
1. **Sequence of Gaussian Elimination Operations**:
   - Start with the identity matrix.
   - Apply the exact same row operations to the identity matrix as were applied to $A$ during its transformation to $I$.

2. **Final Result**:
   - The **identity matrix** evolves into $A^{-1}$.
   - At the end of eliminating $A$, the secondary matrix (initially the identity) is transformed into the inverse: **$A^{-1}$**.
  
---

### Key Takeaways
- The inversion algorithm leverages **elementary matrices** to systematize each row operation as a **matrix multiplication from the left**.
- The process reflects the deep interconnection between algorithms, matrices, and linear transformations in **linear algebra**.
- This approach simplifies operations and highlights the conceptual independence of the matrix as a whole, without examining individual elements.