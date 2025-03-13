## 7. Gaussian Elimination and Row Operations

### Objective:
Illustrate the flexibility in performing Gaussian elimination and explore strategies to simplify the calculations by avoiding fractions.

---

### Problem Setup:
Initial matrix with rows represented as:

$$
\text{Row 1: } [3, \, 4, \, 5] \quad \text{Row 2: } [2, \, 5, \, 9] \quad \text{Row 3: } [1, \, 4, \, 7]
$$

---

### Step 1: Row Switching to Avoid Fractions

#### Reason:
Using the first element of Row 1 ($3$) as the pivot leads to many fractions during calculations. To simplify, switch Row 1 and Row 3. This places the $1$ (from Row 3) in the top-left corner for a cleaner pivot.

#### After Switching:
$$
\text{New Row 1: } [1, \, 4, \, 7] \quad \text{Row 2: } [2, \, 5, \, 9] \quad \text{Row 3: } [3, \, 4, \, 5]
$$

---

### Step 2: Gaussian Elimination - Eliminate Below the Pivot

#### Pivot: $1$ (Row 1)

1. **Eliminate Row 2:** Subtract $2 \times \text{Row 1}$ from Row 2 to zero out the first entry in Row 2.
   $$ 
   \text{Row 2} = [2, \, 5, \, 9] - 2 \times [1, \, 4, \, 7] = [0, \, -3, \, -5]
   $$
2. **Eliminate Row 3:** Subtract $3 \times \text{Row 1}$ from Row 3 to zero out the first entry in Row 3.
   $$
   \text{Row 3} = [3, \, 4, \, 5] - 3 \times [1, \, 4, \, 7] = [0, \, -8, \, -16]
   $$

---

### Step 3: Row Switching to Position the Next Pivot

#### Reason:
Switch Row 2 and Row 3. This places the smaller absolute value $(-3)$ from Row 2 into the pivot position for easier operations.

#### After Switching:
$$
\text{New Row 1: } [1, \, 4, \, 7] \quad \text{New Row 2: } [0, \, -8, \, -16] \quad \text{New Row 3: } [0, \, -3, \, -5]
$$

---

### Step 4: Gaussian Elimination on Remaining Rows

#### Pivot: $-8$ (Row 2)

1. **Eliminate Row 3:** Subtract $\frac{-3}{-8} \times \text{Row 2}$ from Row 3 to zero out the second entry in Row 3.
   $$
   \text{Row 3} = [0, \, -3, \, -5] - \frac{-3}{-8} \times [0, \, -8, \, -16] = [0, \, 0, \, -1]
   $$

---

### Step 5: Jordan Back Substitution

#### Process:
Work backwards to eliminate entries above each pivot while simplifying rows.

1. **Eliminate Row 2 using Row 3:** Subtract $-2 \times \text{Row 3}$ from Row 2.
   $$
   \text{Row 2} = [0, \, -8, \, -16] - (-2) \times [0, \, 0, \, -1] = [0, \, -8, \, -14]
   $$

2. **Eliminate Row 1 using Row 3:** Subtract $7 \times \text{Row 3}$ from Row 1.
   $$
   \text{Row 1} = [1, \, 4, \, 7] - 7 \times [0, \, 0, \, -1] = [1, \, 4, \, 0]
   $$

3. **Eliminate Row 1 using Row 2:** Subtract $\frac{4}{-8} \times \text{Row 2}$ from Row 1.
   $$
   \text{Row 1} = [1, \, 4, \, 0] - \frac{4}{-8} \times [0, \, -8, \, -14] = [1, \, 0, \, 0]
   $$

---

### Final Matrix:
The matrix is now in reduced row echelon form:
$$
\begin{bmatrix}
1 & 0 & 0 \\
0 & 1 & 0 \\
0 & 0 & 1
\end{bmatrix}
$$

---

### Results:
1. **Solution:** $x = 6, \, y = -10, \, z = 5$
2. **Observation:** The columns are linearly independent, confirming the existence of a unique solution.

### Lesson:
We have significant freedom in choosing pivots and row operations during Gaussian elimination. Leveraging this freedom smartly can simplify the process and avoid cumbersome calculations.