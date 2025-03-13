## Problem 6: Pivot Columns and Gaussian Elimination

### Purpose of the Problem:
To address confusion regarding pivot column locations in matrices during Gaussian elimination.

---

### Initial Observations:
- **Column 1** is the **zero column** and is **linearly dependent** by itself.
- Hence, **column 1 cannot contain the first pivot**. The first pivot must occur in **column 2**.  
  However, the pivot is initially in the wrong row and needs adjustment.

---

### Step-by-Step Gaussian Elimination:

#### 1. **Row Switching:**
   - Swap **rows 1 and 2** to place the first pivot in **row 1**.
   - Simultaneously switch values in the right-hand side vector:
     - Swap $3$ and $7$.

#### Updated Matrix:
We rewrite rows and record progress.

---

#### 2. **Eliminate Below Pivot (Row 3):**
   Use the pivot in **row 1** to eliminate below it:
   - **Operation:** Subtract $7 \cdot \text{row 1}$ from **row 3**.
   - Updated values:
     - Zero introduced below the pivot.
     - $9 - 42 = -33$ in the second column.
     - $16 - 49 = -33$ on the right-hand side.

---

#### 3. **Unit Pivot in Row 2:**
   To simplify further operations:
   - Divide all of **row 2** by $3$ to create a unit pivot.

#### Result:
Two unit pivots are now present.

---

#### 4. **Eliminate Below Second Pivot (Row 3):**
   Use the unit pivot in **row 2**:
   - **Operation:** Subtract $33 \cdot \text{row 2}$ from **row 3**.
   - Eliminate the $33$ in column 2 and update the value on the right-hand side.

#### Gin Elimination is Completed:
All entries below pivots are zeros.

---

#### 5. **Back Substitution:**
   Eliminate above the pivots:
   - **Operation:** Subtract $6 \cdot \text{row 2}$ from **row 1**.
   - The $6$ in the second column turns into a $1$ (unit entry).

#### Gaussian Elimination Completed:
The matrix is now in **Row-Echelon Form**.

---

### General Solution:

#### Particular Solution:
- From the right-hand side, note the columns align:
  - The vector corresponds to the **second column** + **third column**.
- Particular solution derived based on pivot positions:
  $$
  \begin{bmatrix} 0 \\ 1 \\ 1 \end{bmatrix}
  $$

#### Null Space:
- The null space corresponds to:
  $$
  \alpha \cdot \begin{bmatrix} 1 \\ 0 \\ 0 \end{bmatrix}
  $$

#### Combined General Solution:
- General solution expressed as:
  $$
  \begin{bmatrix} 0 \\ 1 \\ 1 \end{bmatrix} + \alpha \cdot \begin{bmatrix} 1 \\ 0 \\ 0 \end{bmatrix}
  $$

---

### Summary:
Problem 6 illustrates the key steps of **Gaussian Elimination**, tackling pivot misalignment, row switching, creating unit pivots, and deriving both the **particular solution** and **null space** for the system of equations.