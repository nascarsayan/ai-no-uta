## The Effect of Elementary Matrices on Matrix Products

### Key Observations:
1. **Elementary Matrix Operations:**
   - Elementary matrices are derived from the identity matrix by performing basic row or column operations.
   - Examples include adding a multiple of one row/column to another, swapping rows/columns, or scaling a row/column.

2. **Impact on Multiplicands:**
   - When an elementary matrix appears on the **right** of another matrix in a product, it performs **column operations**.
   - When it appears on the **left**, it performs **row operations**.

---

### Steps to Analyze Elementary Matrices:

#### From Rows Perspective:
1. Start with the identity matrix.
2. Apply a row operation, e.g., _adding two times row 1 to row 2_.
3. The resulting matrix is the elementary matrix.

#### From Columns Perspective:
1. Start with the identity matrix.
2. Apply a column operation, e.g., _adding two times column 2 to column 1_.
3. The resulting matrix becomes the elementary matrix.

> **Example:** 
> Consider an elementary matrix derived by adding $2 \times$ Row 1 to Row 2 in the identity matrix. This matrix, when multiplied on the left, adds $2 \times$ Row 1 of the multiplicand to Row 2.

---

### Understanding Elementary Matrix Products:

#### Takeaway 1:
- Multiplying a matrix **on the right** by an elementary matrix results in **column operations**:
  - For example, adding $2 \times$ Column 2 to Column 1.

#### Takeaway 2:
- Multiplying a matrix **on the left** by an elementary matrix results in **row operations**:
  - For example, adding $2 \times$ Row 1 to Row 2.

---

### General Observations:

1. **Column Operations:**
   - If matrix $E$ is formed by adding $k \times$ Column 2 to Column 1 of the identity matrix:
     
     $E = \begin{bmatrix} 
     1 & k \\ 
     0 & 1 
     \end{bmatrix}$.

     Then, for any matrix $A$, the product $A \cdot E$ performs the same operation on the columns of $A$.

2. **Row Operations:**
   - If $E$ is formed by adding $k \times$ Row 1 to Row 2 of the identity matrix:
     
     $E = \begin{bmatrix} 
     1 & 0 \\ 
     k & 1 
     \end{bmatrix}$.

     Then, for any matrix $A$, the product $E \cdot A$ performs the same operation on the rows of $A$.

---

### Summary Rule:
- The operations that turn the identity matrix into an elementary matrix:
  - Determine the effect the elementary matrix will have on another matrix it multiplies.
  - If $E$ is an elementary matrix:
    - Appearing **on the right**: Affects **columns**.
    - Appearing **on the left**: Affects **rows**.

---

### Exploring Examples:

#### Column Transformation:
- Suppose we have matrix $A$ and an elementary matrix $E$ formed by adding $2 \times$ Column 2 to Column 1:
  
  $$
  E = \begin{bmatrix} 
  1 & 2 & 0 \\ 
  0 & 1 & 0 \\ 
  0 & 0 & 1 
  \end{bmatrix}.
  $$

  Then, multiplying $A$ with $E$ as $A \cdot E$ will add $2 \times$ the second column of $A$ to its first column.

#### Row Transformation:
- If $E$ is instead formed by adding $3 \times$ Row 1 to Row 3:

  $$
  E = \begin{bmatrix} 
  1 & 0 & 0 \\ 
  0 & 1 & 0 \\ 
  3 & 0 & 1 
  \end{bmatrix},
  $$

  then multiplying $E \cdot A$ will add $3 \times$ Row 1 of $A$ to Row 3.

---

### Takeaway:
- Elementary matrices "store" the transformations applied to the identity matrix.
- Each operation performed on the identity matrix is "replayed" on any matrix it multiplies:
  - On the **right**: as column operations.
  - On the **left**: as row operations.

