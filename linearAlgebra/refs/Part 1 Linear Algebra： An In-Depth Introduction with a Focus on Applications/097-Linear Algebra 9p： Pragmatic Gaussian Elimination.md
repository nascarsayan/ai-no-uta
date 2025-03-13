# Gaussian Elimination: Pragmatic Approach

## 1. Introduction
- The video demonstrates:
   1. A Gaussian elimination example.
   2. A pragmatic approach to Gaussian elimination.
     - You don’t need to start at the top-left and move systematically down and to the right.
     - You can start wherever you want, provided you don’t undo previous work.

---

## 2. Setting Up the System
- **System Example**:
  - When solving the system by hand, unit pivots are desirable.
  - Multiple approaches are possible:
    1. Divide the first row by its leading coefficient for a unit pivot.
    2. Swap rows for an alternate top-left pivot.
    3. Start at an unconventional pivot (e.g., bottom-right) and work pragmatically.

---

## 3. Unorthodox Gaussian Elimination
- **Pivot Choice**:
  - Start with the **bottom-right element** as the first pivot.

### Step-by-Step Process:
1. **Copy Row Three Down**:
   - Use the bottom-right pivot.

2. **Eliminate Entry Above Pivot**:
   - Eliminate the value using row operations.
   - Example:
     
     Subtraction from second row yields:
     $$
     \begin{bmatrix} 
     1 & 0 & 5 & 6 & 0 \\ 
     0 & 0 & 6 & 0 & 0 \\ 
     ... & ... & ... & ... & ...
     \end{bmatrix}.
     $$
     
3. **Copy Row One Down**:
   - Scale or transform row values as needed for subsequent pivots.

4. **Continue With Alternate Pivot**:
   - The process begins eliminating entries pragmatically (not necessarily top-left).

5. **Final Pivot**:
   - Use the pivot column to eliminate remaining non-zero elements row by row.

---

## 4. Back Substitution (Jordan Form)
- Transition process from Gaussian elimination **to back substitution**:
  - "Upside-down and reversed".
  
### Eliminating Entries:
1. Subtract coefficients using previous row calculations:
   $$
   R_2 \to R_2 - c \times R_1
   $$

2. Continue eliminating columns one at a time (columns 4 & 5 as pivots).

---

## 5. General Solution to the System

### Particular Solution:
- Combine pivots (columns) to identify a single solution:
  $$
  \begin{bmatrix}
  0 \\ 0 \\ 0 \\ 1 \\ 1
  \end{bmatrix}.
  $$

### Null Space:
- Null space arises from non-pivot columns.
- Example:
  - Take specific proportions of pivot columns to represent null vectors:
    $$
    \begin{bmatrix}
    2 \\ 0 \\ -4 \\ 3 \\ 10
    \end{bmatrix}.
    $$
  - Adjust for integer representation by scaling:
    - Multiply coefficients to simplify.

---

## 6. Summary
- **Key Takeaways**:
  - Gaussian elimination can be executed in non-traditional order pragmatically.
  - The process still yields accurate results, as long as no previous steps are undone.
  - **Practical Message**:
    - Flexibility in Gaussian elimination is viable and efficient.