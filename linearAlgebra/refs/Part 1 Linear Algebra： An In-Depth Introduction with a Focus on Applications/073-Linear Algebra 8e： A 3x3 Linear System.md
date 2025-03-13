## The Dial Pad Matrix Linear System

### Problem Setup
A special linear system, referred to as the **Dial Pad Matrix**, exhibits interesting properties. The goal is to explore its solution properties, the relationships among its columns, and the interplay between the column space and the right-hand side vector.

---

### 1. Particular Solution
To find a particular solution:

- It is observed that the **right-hand side** vector is obtained as `10 \times` the middle column in the given system. 
- Thus, the solution is straightforward:

$$
x = 
\begin{bmatrix} 
0 \\ 
10 \\ 
0 
\end{bmatrix}
$$

This is the **particular solution** to the system.

---

### 2. Null Space (Kernel)
The **null space** is determined as follows:

#### Key Property:
- The **middle column** is the average of the first and third columns:
  - $2 = \frac{1 + 3}{2}$
  - $5 = \frac{4 + 6}{2}$
  - $8 = \frac{7 + 9}{2}$
  
#### Non-Trivial Linear Combination:
Using the relationship among columns, we can construct a linear combination that sums to zero:
$$
\frac{1}{2}C_1 - C_2 + \frac{1}{2}C_3 = 0
$$
or equivalently:
$$
C_1 - 2C_2 + C_3 = 0
$$

- The coefficients of this combination are:
  $$
  \begin{bmatrix} 
  1 \\ 
  -2 \\ 
  1 
  \end{bmatrix}
  $$
  
This vector spans the null space. 

To simplify:
- Multiply the coefficients by a scalar (e.g., 2) to avoid fractions, keeping integer values.

---

### 3. Column Space
The column space of the matrix includes all vectors that can be expressed as linear combinations of the columns.

#### Critical Property:
- The **middle entry** of any vector in the column space is the **average** of its first and third entries. For example:
  $$
  \text{Column Space Pattern: } 
  \begin{bmatrix}
  a \\ 
  \frac{a + b}{2} \\ 
  b
  \end{bmatrix}
  $$

---

### 4. Modifying the System

#### Updated Right-Hand Side:
A small change is introduced to the system by modifying the right-hand side:
$$
\text{New RHS: } 
\begin{bmatrix}
120 \\ 
50 \\ 
80
\end{bmatrix}
$$

#### Observations:
- The **null space** of the system remains unchanged because the columns of the matrix (left-hand side) remain the same.
- However, the **column space** is tested by checking if the new right-hand side is in the span of the columns.

---

### 5. Why No Solution Exists
The new right-hand side violates the column space property:
- The middle entry $50$ is **not** the average of $120$ and $80$:
  $$
  \frac{120 + 80}{2} = 100 \neq 50
  $$

#### Conclusion:
- The right-hand side is not in the column space. Therefore, the system has **no solution**.

---

### Summary of Key Insights

1. **Null Space**:
   - Represents all solutions to the homogeneous equation $Ax = 0$.
   - Constructed from linear dependencies among the columns.

2. **Column Space**:
   - Represents all possible vectors producible by linear combinations of the matrix’s columns.
   - Determines if a right-hand side vector allows for a solution.

3. **General Solution**:
   - If the system has a solution, it is expressed as:
     $$
     \text{General Solution} = \text{Particular Solution} + \text{Null Space}
     $$

4. **Inconsistent System**:
   - If the right-hand side vector violates the constraints of the column space, the system lacks solutions.