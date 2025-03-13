## Gaussian Elimination Process

### Idea and Goal
1. Gaussian elimination aims to simplify a system of linear equations by eliminating as many coefficients as possible.
2. The process must preserve the solution set of the system.

---

### Operations That Preserve Solution Sets
1. **Multiply an Entire Equation by a Number**  
   - Multiplying both sides of a linear equation by a non-zero scalar does not change the solution set.
   - Example:
     $$
     3x + y = 3
     $$
     Multiply by $4$:
     $$
     4(3x + y) = 4(3) \implies 12x + 4y = 12
     $$

2. **Add or Subtract One Equation from Another**  
   - Adding or subtracting one equation to/from another eliminates a variable without altering the set of solutions.  
   - Example: Subtract the first equation from the second:
     $$
     \text{First: } 4x + y + z = 12 
     $$
     $$
     \text{Second: } 4x + 5y + 6z = 9
     $$
     Subtract:
     $$
     (4x + 5y + 6z) - (4x + y + z) = 9 - 12
     $$
     Result:
     $$
     4y + 5z = -3
     $$

3. **Switch Two Equations**  
   - Switching two equations does not alter the solution set, but can help in organizing the system.

---

### Matrix Representation
Gaussian elimination in matrix form uses row operations. Operations include:
1. **Multiply an Entire Row by a Scalar**
   - Similar to multiplying an entire equation by a scalar.  
   $R_i \to \lambda R_i, \, \lambda \neq 0$
   
2. **Add/Subtract a Multiple of One Row to Another**
   - Key operation for elimination:
   $R_j \to R_j - \lambda R_i$

3. **Switch Two Rows**
   - Rearrange rows for easier elimination:
   $R_i \leftrightarrow R_j$

---

### Step-by-Step Example

#### Step 1: Eliminating Variables Using Multiplication
- Given equations:
  $$
  \text{First: } x + 2y + 3z = 3 \\
  \text{Second: } 4x + 5y + 6z = 12
  $$
  Multiply the first equation by $4$, making the $x$ coefficients match:
  $$
  4(x + 2y + 3z) = 4(3) \implies 4x + 8y + 12z = 12
  $$

#### Step 2: Subtract to Eliminate First Coefficient
- Subtract the new first equation from the second:
  $$
  (4x + 5y + 6z) - (4x + 8y + 12z) = 12 - 12
  $$
  Result:
  $$
  -3y - 6z = -3
  $$

#### Step 3: Divide to Normalize
- Divide the equation $-3y - 6z = -3$ by $-3$:
  $$
  y + 2z = 1
  $$

---

### Observations of Row Operations
1. The purpose of Gaussian elimination is to simplify the system into a form where back-substitution becomes easy.
   - For example, transform into an upper triangular matrix:
     $$
     \begin{bmatrix}
     1 & 2 & 3 & | & 3 \\
     0 & -3 & -6 & | & -3 \\
     \end{bmatrix}
     $$

2. The primary operation involves the elimination of lower triangular entries by subtracting multiples of rows.

---

### Advanced Notes: Pivots
1. The leading non-zero entry in a row or column is referred to as a **pivot**.
2. It is advantageous to normalize pivots to $1$ by dividing the row by the pivot value.

---

### Summary of Gaussian Elimination Operations

1. **Row Operations** in matrix form:
   - Multiply a row by a scalar.
   - Add/subtract a multiple of one row to another.
   - Switch rows.

2. Effective elimination involves the following sequence:
   - **Aligning Pivots:** Normalize pivot entries (divide by scalar).
   - **Eliminating Variables:** Use row operations to create zeros below pivots.

Try to simplify the system iteratively until a triangular or simpler form is achieved.