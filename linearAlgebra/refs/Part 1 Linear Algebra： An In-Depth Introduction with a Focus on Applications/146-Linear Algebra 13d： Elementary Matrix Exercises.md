## Elementary Matrix Exercises and Matrix Multiplication

### 1. Introduction
- **Objective**: Explore elementary matrices through examples, focusing on matrix multiplication.
- **Types of Exercises**:
  1. Given an elementary matrix alongside another matrix, perform the product.
  2. Determine the elementary matrix when the result of the product is known.

---

### 2. Basic Exercises

#### Exercise 1: Column Operations
- **Matrix Placement**: Elementary matrix appears on the right.
- **Column action**: Add column 2 to column 1 to make the first column `\begin{bmatrix} 0 \\ -1 \\ 1 \end{bmatrix}`.
  
#### Exercise 2: Row Operations
- **Matrix Placement**: Elementary matrix appears on the left.
- **Row action**: Add row 1 to row 2 to make the second row `\begin{bmatrix} 0 \\ -1 \\ 1 \end{bmatrix}`.
  
- **Observation**: Non-commutativity is evident—switching matrix placement changes the product result.

---

### 3. Multiplication Effects of Elementary Matrices

#### Exercise 3: Zeroing Out a Column
- **Action**: Multiply the last column by 0, turning it into a zero column.
  
#### Exercise 4: Zeroing Out a Row
- **Action**: Multiply row 3 by 0, turning it into a zero row.

#### Exercise 5: Scalar Multiplication of Columns/Rows
- **Action**: Multiply the last column by 2, making it `\begin{bmatrix} 2 \\ 0 \\ 4 \end{bmatrix}`.
- **Generalization**: When on the left, multiply the corresponding row instead (left as an exercise).

---

### 4. Permutation Matrices

#### Exercise 6: Column Permutation
- **Action**: Rearrange columns; the last column moves to the first position, with others adjusted rightward.

#### Exercise 7: Row Permutation
- **Action**: Rearrange rows; the first row moves to the last position, with others shifted upward.

---

### 5. Non-Identity Diagonal Matrices

#### Exercise 8: Diagonal with Twists
- **Action**: Switch rows 1 and 3 if the matrix is on the left; switch columns 1 and 3 if the matrix is on the right.

---

### 6. Advanced Examples with $4 \times 4$ Matrices

#### Exercise 10: Adding Columns
- **Operation**: Add the values of columns 3 and 4 to column 1.

#### Exercise 11: Adding Rows
- **Operation**: Add row 1 to rows 3 and 4.

---

### 7. Unknown Elementary Matrices

#### Finding an Unknown Matrix:
- **Example**: Determine the elementary matrix that transforms a given matrix back to the identity matrix.
- **Procedure**:
  1. Analyze the desired transformation (e.g., subtracting `3 \times` column 3 from column 1).
  2. Apply these actions to the identity matrix.

---

### 8. Powers of Matrices ($A^{n}$)

#### Exercise 26: Powers of Matrices
- **Observation**: Repeated row or column addition accumulates scalar multiples at diagonal positions:
  $$
  A^{10} = \text{Matrix with } 10 \text{ at designated positions}.
  $$

#### Exercise 28: Summing Off-Diagonal Entries
- **Result**: Row multiplications lead to sums such as $1 + 2 + \dots + 10$, calculated via:
  $$
  \text{Sum} = \frac{n(n+1)}{2}.
  $$

---

### 9. Special Matrices

#### Exercise 32: Self-Inverse Matrix
- **Example**: A matrix that switches columns 1 and 2, and columns 3 and 4. Performing the operation twice restores the original order:
  $$
  A^2 = I \quad (\text{Identity Matrix}).
  $$

---

### 10. Cyclic Matrices

#### Exercise 33: Cyclic Matrix
- **Action**: Perform shifts cyclically (e.g., column 3 moves to first, and others shift right).
- **Observation**:
  - After three applications, the matrix returns to the identity.

---

### 11. Inverse Matrices

#### Exercise 34: Finding the Inverse
- **Procedure**: Undo the column/row operations:
  - Example involves undoing cycles (e.g., restoring columns shifted to the right).

---

### 12. Closing Remarks
- **Objective**: Extend understanding of matrix products via transformations.
- **Key Observations**:
  - Non-commutativity in general matrix multiplication.
  - Special cases of commutativity, self-inverse matrices, and cyclic matrices.