## 4. Gaussian Elimination and Matrix Properties

### Problem Dimensions:
- Problem 4 has the same dimensions as Problem 3.
- A solution is likely, and the null space is guaranteed to be non-trivial.

### Observations and Problem Setup:
1. **Column Dependency:**
   - Column 3 is set as the sum of the first two columns.
   - The goal is to see how Gaussian elimination reveals this relationship.

2. **Matrix Example:**
   Starting matrix setup (symbolic vector for unknowns):
   $$
   \begin{bmatrix}
   2 & 2 & 4 & 1 \\
   5 & 3 & ? & 2 \\
   8 & 1 & ? & 4 
   \end{bmatrix}
   $$

### Gaussian Elimination Steps:
#### Step 1: Normalize the First Row
- The first pivot is **2**.
- Normalize row 1 by dividing it by **2**:
  $$
  \begin{bmatrix}
  1 & 1 & 2 & 0 \\
  5 & 3 & ? & 2 \\
  8 & 1 & ? & 4 
  \end{bmatrix}
  $$

#### Step 2: Eliminate Entries Below the First Pivot
1. Subtract **5 × Row 1** from Row 2:
    $$
    \text{Result: } 
    \begin{bmatrix}
    1 & 1 & 2 & 0 \\
    0 & 1 & 1 & -9 \\
    8 & 1 & ? & 4 
    \end{bmatrix}
    $$
  
2. Subtract **8 × Row 1** from Row 3:
    $$
    \text{Result: } 
    \begin{bmatrix}
    1 & 1 & 2 & 0 \\
    0 & 1 & 1 & -9 \\
    0 & -7 & ? & -15 
    \end{bmatrix}
    $$

#### Step 3: Work with the Second Pivot
- The second pivot is **1** (Row 2, Column 2).

1. Eliminate the entry in Row 3 (Column 2) by adding **7 × Row 2** to Row 3:
    $$
    \text{Result: } 
    \begin{bmatrix}
    1 & 1 & 2 & 0 \\
    0 & 1 & 1 & -9 \\
    0 & 0 & ? & 78 
    \end{bmatrix}
    $$

#### Step 4: Normalize the Third Pivot
- The third pivot is **78**.
- Divide Row 3 by **78**:
  $$
  \begin{bmatrix}
  1 & 1 & 2 & 0 \\
  0 & 1 & 1 & -9 \\
  0 & 0 & 1 & -1  
  \end{bmatrix}
  $$

#### Step 5: Back Substitution
1. Use Row 3 to eliminate the entry above it in Row 2 (Column 3) by adding **9 × Row 3** to Row 2:
    $$
    \text{Result: }
    \begin{bmatrix}
    1 & 1 & 2 & 0 \\
    0 & 1 & 0 & 113 \\
    0 & 0 & 1 & -1  
    \end{bmatrix}
    $$

2. Use Row 3 to eliminate the entry above it in Row 1 (Column 3) by subtracting **2 × Row 3** from Row 1:
    $$
    \text{Result: }
    \begin{bmatrix}
    1 & 1 & 0 & 539 \\
    0 & 1 & 0 & 113 \\
    0 & 0 & 1 & -1  
    \end{bmatrix}
    $$

#### Step 6: Eliminate Entries Above the Second Pivot
- Subtract Row 2 from Row 1:
  $$
  \text{Final Row Reduced Matrix: }
  \begin{bmatrix}
  1 & 0 & 0 & \text{Resulting Value} \\
  \ldots
  $$!END. minimal general-linkedmatax only accurate minimal