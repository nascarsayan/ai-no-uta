# Notes

## 1. An Interesting System

### Observation of the system:
- The system has two columns of zeros.
- Variables $Y$ and $T$ correspond to the zero columns, and do not participate in the equations.

### Equations:
1. $x + 2z = 3$ — Variables $Y$ and $T$ are absent.
2. $2x + 4z = 6$ — Again, variables $Y$ and $T$ are absent.

### Description:
- The system consists of **three equations** with **four unknowns**: $x$, $y$, $z$, and $t$.
- Only variables $x$ and $z$ appear in the system; $y$ and $t$ can take arbitrary values.

---

## 2. Solving the System

### Particular Solution:
- Here's how the particular solution is found:
  - The right-hand side column is the sum of two non-zero columns.
  - Ignore the zero columns during construction.
  
$$
\text{Particular solution: } 
\begin{bmatrix} 
1 \\ 
0 \\ 
1 \\ 
0 
\end{bmatrix}
$$

---

## 3. Null Space Analysis

### Description:
- Variables $Y$ and $T$ correspond to zero columns. They can take **arbitrary values**.
- Elements of the null space derive directly from the zero columns.

### Null Space Components:
1. **Contribution from the first zero column**:
$$
\begin{bmatrix}
0 \\ 
1 \\ 
0 \\ 
0 
\end{bmatrix}
$$

2. **Contribution from the second zero column**:
$$
\begin{bmatrix}
0 \\ 
0 \\ 
0 \\ 
1 
\end{bmatrix}
$$

### Representation of Null Space:
The null space is **two-dimensional** and spans:
$$
\alpha 
\begin{bmatrix}
0 \\ 
1 \\ 
0 \\ 
0 
\end{bmatrix}
+ 
\beta 
\begin{bmatrix}
0 \\ 
0 \\ 
0 \\ 
1 
\end{bmatrix}
$$

Where $\alpha$ and $\beta$ are arbitrary values.

---

## 4. Column Space Analysis

### Column Space:
- Observing all columns in the matrix:
  - Every column adheres to the pattern: the second entry is **twice** the first entry.
  
### General Column Space Representation:
$$
\text{Column space: } 
\begin{bmatrix} 
a \\ 
2a \\ 
b 
\end{bmatrix}
$$

Where $a$ and $b$ can take arbitrary values.

---

## 5. Likelihood of a Solution

### Are we lucky that the right-hand side is in the column space?
- The **system lives in $\mathbb{R}^3$ space** but only has **two useful vectors** due to the zero columns.
- This makes it unlikely for an arbitrary right-hand side to be in the column space.

### Example Failure:
A new right-hand side vector not satisfying the column space properties:
$$
\begin{bmatrix}
3 \\ 
16 \\ 
... 
\end{bmatrix}
$$
Does not belong to the column space as $16 \neq 2 \cdot 3$.

- **Outcome**: The system **does not** have a solution.

---

## 6. Importance of Null Space and Column Space

### Usefulness:
1. **Column Space**:
   - Determines whether a solution exists.
   - Helps verify if the right-hand side aligns with the linear system.

2. **Null Space**:
   - Represents all solutions to a homogeneous problem.
   - Complements the particular solution to derive all solutions of the full system.

---

## 7. Common Mistake in Null Space Representation

**Incomplete Representation**:
- Incorrectly expressing the null space as:
$$
\alpha 
\begin{bmatrix}
0 \\ 
1 \\ 
0 \\ 
0 
\end{bmatrix}
+ 
\beta 
\begin{bmatrix}
0 \\ 
0 \\ 
0 \\ 
1 
\end{bmatrix}
$$

**Why this fails**:
- Omits linear dependencies introduced by each zero column.
- Fails to acknowledge contribution from combinations like:
$$
\begin{bmatrix}
0 \\ 
1 \\ 
0 \\ 
2
\end{bmatrix}
$$

- Each zero column represents an independent linear dependence.

**Lesson**:
Zero columns inherently generate null space elements, irrespective of other factors.

---

## 8. Generalizations

1. **Column Space Patterns**:
   - Multiple zero columns shrink the effective dimension of the column space.

2. **Null Space Interplay**:
   - All zero columns correspond to independent contributions to the null space.

3. **Likelihood of Solution**:
   - Arbitrary right-hand sides rarely align with the column space of a sparse system.

