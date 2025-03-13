# 15. Problem Three: Gaussian Elimination in $\mathbb{R}^3$

## Context
- We start with **four vectors in a three-dimensional space ($\mathbb{R}^3$)**. 
- Since the number of columns exceeds the dimensions of the space, these vectors are guaranteed to be **linearly dependent**.
- This leads to a **non-trivial null space**, which means the system has **infinitely many solutions** when solvable.

---

## Key Arguments
1. **Linear Dependence and Spanning**:
    - When there are more vectors than space dimensions, these vectors **often span the entire space**, unless specific linear relationships exist between them.

2. **Gaussian Elimination and Structure Identification**:
    - Even if the structure is not immediately obvious, applying **Gaussian elimination** can systematically reveal dependencies or independence among columns.

---

## Gaussian Elimination Procedure

### Step 1: Row Switching to Position the First Pivot
- To position the **pivot (1)** in the desired location (first row), **swap rows 1 and 3**.

---

### Step 2: Eliminating Entries Below the Pivot
- **First pivot column** cleared by subtracting multiples of row 1.

---

### Step 3: Adjusting the Second Pivot
- The second pivot equals $2$. Instead of dividing the row immediately, work with it for elimination purposes.

---

### Step 4: Subtraction to Clear Entries
- To eliminate entries below the **second pivot ($2$)**:
  
  $$
  \text{Row 3} \to \text{Row 3} - (\text{Row 2})
  $$

---

### Step 5: Row Manipulation for the Third Pivot
- Adjust the **third pivot**:

  $$
  \text{Row 3} \to -1 \times \text{Row 3} 
  $$

---

### Step 6: Back Substitution
1. Normalize pivots to $1$:
    - Multiply or divide rows as necessary.
2. Eliminate **non-zero entries above pivots** in earlier rows.

---

### Final Matrices and Checks
- Resulting matrix confirms:
    - Linear independence among the first three columns.
    - Relationships among columns preserved post elimination.

---

## General Solution
- **Constructing the Solution**:
    - Decompose the **right-hand side** based on pivot columns.
    - Solve for $x$, $y$, $z$, and $t$ using Gaussian elimination results.

### Steps:
1. Decompose the **right-hand side**:
   $$
   -3, 0, 1, 0
   $$

2. Find the **null space** relationship for the fourth column:
   $$
   \text{Null Space Vector: } (2, 1, -1)
   $$

3. Validate solution via tests:
    - **Spot checks** using sums/multiples of columns.

---

## Key Observations
- **Null Space**: Represents dependencies among vectors or columns in the original setup.
- **Pivot Columns**:
    - Help identify independent components of the original system.
- **Running Sum**:
    - Useful for performing spot-checks during validation.

---

### Final Solution
Gaussian elimination and back-substitution lead to a general solution for the system in $\mathbb{R}^3$.