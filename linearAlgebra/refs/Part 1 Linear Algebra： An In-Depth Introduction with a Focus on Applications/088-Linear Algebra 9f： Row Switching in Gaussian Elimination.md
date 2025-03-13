## Gaussian Elimination and Row Operations

### Introduction
- The goal of this lesson is to illustrate the operation of row switching and use Gaussian elimination to solve a linear system.
- For this specific example, the solution is unknown a priori.

---

### Key Concepts

#### Eliminating Entries in Matrices Using Gaussian Elimination
1. Identify the first pivot:
   - Select the first row as the pivot row.
   - Perform the operation of subtracting a multiple of the pivot row from another row.

2. Example:
   - To eliminate a specific entry (e.g., "2"):
     - Subtract **2 times the first row** from the second row.
     - This multiplier equals the ratio of the entry to the pivot entry.
     
   - The result:
     $$
     \text{New matrix after transformation, e.g.,}
     \begin{bmatrix}
     1 & 0 & \dots \\
     0 & 0 & \dots \\
     0 & 1 & \dots \\
     \end{bmatrix}
     $$
   - Troublesome entries (such as 0 where a pivot was expected) require additional row operations.

#### Row Switching
- When a pivot entry of $0$ appears, pivoting must occur.
- Convention:
  - A pivot should appear in consecutive rows.
  - Pivots **should be as early as possible in terms of their column index**.
- For example:
  - Row switching might result in:
    $$
    \begin{bmatrix}
    1 & 2 & 0 \\
    0 & 1 & 0 \\
    0 & 0 & 1
    \end{bmatrix}
    $$

---

### Forward Elimination
- The process of marching from **left to right** and eliminating everything **below the pivot** in the pivot column.
- Mathematically, if the pivot is $p$, each of the steps reduces the entries in the same column to $0$ below position $p$.

---

### Back Substitution (Jordan Elimination)
- Once forward elimination is complete, begin marching **from right to left** to eliminate entries **above each pivot**.
1. Start from the last pivot (lowest row, rightmost column).
2. Progressively eliminate the corresponding values from rows above it.

#### Example of Back Substitution:
- Subtracting values to isolate variables.
- Adjust row values for simplicity:
    $$
    \begin{aligned}
    R_2 &\gets R_2 - 2R_3 \\
    R_1 &\gets R_1 - 3R_3
    \end{aligned}
    $$

---

### Terminology
1. **Gaussian Elimination**:
   - The process of forward elimination, marching left to right to eliminate entries below a pivot.
   - Example:
     $$
     \text{Transform a general system to an upper triangular form.}
     $$

2. **Jordan Substitution (for Michael Jordan 😉)**:
   - The backward substitution process, marching right to left to eliminate entries above a pivot.

---

### Final Result
1. **System Transformation**:
   - After the elimination process, the system typically transforms into:
     $$
     \begin{bmatrix}
     1 & 0 & 0 \\
     0 & 1 & 0 \\
     0 & 0 & 1
     \end{bmatrix}
     \begin{bmatrix}
     x \\
     y \\
     z
     \end{bmatrix}
     =
     \begin{bmatrix}
     3 \\
     -1 \\
     0
     \end{bmatrix}
     $$

2. **Linear Independence**:
   - If columns are linearly independent, the null space is trivial, and a **unique solution** exists.

3. **Solution**:
   - $x = 3, y = -1, z = 0$

---

### Key Takeaways
1. **Pivot Placement**:
   - The placement of pivots in rows is flexible because row switching is allowed.
   - However, the placement of pivots in columns is constrained by the structure of the system.

2. **System Transformation**:
   - Gaussian elimination simplifies a system to an upper triangular or reduced form where relationships are self-evident.

3. **Row Switching**:
   - Row switching can correct for unexpected pivot conditions but must be followed by further elimination.

4. **Final Solution**:
   - After both Gaussian elimination and backward substitution, the solution to the system becomes clear.

In the **next lesson**, we will explore how pivot column placements are constrained and how to handle such scenarios.