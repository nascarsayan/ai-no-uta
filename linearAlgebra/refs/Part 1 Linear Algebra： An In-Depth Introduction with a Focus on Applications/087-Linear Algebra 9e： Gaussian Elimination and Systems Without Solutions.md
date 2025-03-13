## Understanding Inconsistent Linear Systems

### Identifying the Problem
- The linear system under discussion **does not have a solution**.
- **How do we know?**
  - From previous lessons, the **column space** of the matrix has a specific property:
    - The middle entry is the average of the other two.
  - The column space is defined as vectors of the form:  
    $$
    \begin{bmatrix} a \\ \frac{a+b}{2} \\ b \end{bmatrix}
    $$
  - If the vector on the **right-hand side** does not satisfy this property, it is not in the column space, implying **no solution** exists.

### Key Observation About Column Space
- The condition translates into:
  - The middle entry must equal the average of the first and last entries.
- If this condition is violated for the right-hand-side vector, the system is deemed inconsistent.

---

### Gaussian Elimination Steps and Observations

#### Step 1: Subtract $4$ times the first row from the second row
Result:
- Second row becomes:
  $$
  \begin{bmatrix} 0 & -3 & -6 \end{bmatrix}
  $$
- Right-hand side updates as well:
  $$
  \text{Second RHS entry: } -3
  $$

#### Step 2: Subtract $7$ times the first row from the third row
Result:
- Third row becomes:
  $$
  \begin{bmatrix} 0 & -6 & -2 \end{bmatrix}
  $$
- Right-hand side updates as well:
  $$
  \text{Third RHS entry: } -5
  $$

#### Step 3: Divide second row by $-3$
Result:  
Second row becomes:
$$
\begin{bmatrix} 0 & 1 & 2 \end{bmatrix}
$$
Second RHS:
$$
1
$$

#### Step 4: Add $6$ times the second row to the third row
Result:  
Third row becomes:
$$
\begin{bmatrix} 0 & 0 & 0 \end{bmatrix}
$$
Third RHS:
$$
1
$$

### Signal of Inconsistency:
- The third row now reads:
  $$
  0x + 0y + 0z = 1
  $$
- This is impossible because $0x + 0y + 0z = 0$ always holds true for all values of $x$, $y$, and $z$.  
- **Conclusion:** The system has no solution.

---

### Interpreting Results with Column Space

- The **column space of the matrix** contains only vectors where:
  - Last entry is $0$.
  - Right-hand side of the modified system has a $1$ in the last entry.  
- Therefore, the right-hand side vector is **not in the column space** of the matrix.  
- This confirms that the system is inconsistent.

### Key Properties of Gaussian Elimination
- **Column space is altered** during Gaussian elimination, so it is not preserved.  
- However, the **relationship between the right-hand side and the column space** remains consistent:
  - If the right-hand side is not in the column space of the original matrix, it is not in the column space of the transformed matrix either.

---

### Conclusion
- By observing both:
  1. Individual equations (leading to impossibilities like $0 = 1$).
  2. Column space relationships.  
- We determine that the original system is inconsistent (i.e., it has no solutions).  
- Gaussian elimination reveals this inconsistency efficiently.