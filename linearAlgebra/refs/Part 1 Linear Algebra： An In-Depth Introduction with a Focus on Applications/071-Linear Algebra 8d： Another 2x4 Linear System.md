## Solving Linear Systems

### Overview
This section covers solving a linear system by understanding relationships among the columns of the matrix and the right-hand-side vector. Key aspects include determining particular solutions and finding the null space.

---

### Another System

- The new system is similar to the previously solved system but has minor numeric changes (e.g., a "1" instead of a "0" in one entry).
- These changes **do not affect**:
  - The **strategy** for solving the problem.
  - The **dimension** of the null space.
  - The general **structure** of the solution.
- However, the numeric adjustments may make the decomposition of columns slightly more complex.

---

### Decomposition of Columns

To solve the new system:
1. **Choose "go-to columns"**: Some columns retain a "bootstrapping structure," simplifying decomposition.
2. **Find coefficients** for linear combinations:
   - For the column on the right-hand side:
     - Start with **8 of the first column**, which ensures the required entry (`8`) is achieved in the first position.
     - Add **3 of the second column** to complete the decomposition and match the second entry.
     - No contribution needed from the third or fourth columns.

#### Particular Solution:
The particular solution is:

$$
\begin{bmatrix} 8 \\ 3 \\ 0 \\ 0 \end{bmatrix}
$$

---

### Null Space Construction

1. **Relationship of Columns**:
   The **null space** is spanned by non-trivial linear combinations of the columns that result in the zero vector.

#### Step 1: First Null Space Vector
- From the relationship of the third column with the first two:
  - Coefficients are calculated to cancel out entries.
  - Subtract the third column from this combination to yield the zero column.

Resulting null space vector:

$$
\begin{bmatrix} 1 \\ -1 \\ 0 \\ 0 \end{bmatrix}
$$

---

#### Step 2: Second Null Space Vector
- Consider the fourth column's relationship to the first two:
  - Example: Taking 7 times the first column and 4 times the second column produces the fourth column.
  - Modify with signs (e.g., `-7`, `-4`) to yield the zero column.

Resulting null space vector:

$$
\begin{bmatrix} -7 \\ -4 \\ 0 \\ 1 \end{bmatrix}
$$

---

### General Solution

The **general solution** of the system combines:
1. The particular solution.
2. The null space vectors (scaled by scalars $c_1$ and $c_2$).

$$
\mathbf{x} = \begin{bmatrix} 8 \\ 3 \\ 0 \\ 0 \end{bmatrix} + c_1 \begin{bmatrix} 1 \\ -1 \\ 0 \\ 0 \end{bmatrix} + c_2 \begin{bmatrix} -7 \\ -4 \\ 0 \\ 1 \end{bmatrix}
$$

---

### Notes on Sign Flipping
- Whether the last number is $1$ or $-1$ for null space vectors is up to personal preference. Flipping one sign corresponds to flipping all other signs in the vector.

Both approaches are equivalent:
- With last number $-1$: $[-7, -4, 0, 1]$
- With last number $1$: $[7, 4, 0, -1]$

Choose the format that feels more intuitive.

---

### Scaling Up: Gauss Elimination

- In more complex systems, relationships between columns may not be obvious.
- **Gauss Elimination** will be introduced later to simplify such systems into a form where relationships are clearer.

For now, focus on recognizing and leveraging relationships in simpler scenarios.