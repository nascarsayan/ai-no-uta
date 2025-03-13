## Exceedingly Simple Linear Systems

### Overview
- Sometimes simple problems can be harder to solve because they don't easily fit into a general framework.  
- We'll analyze a few exceedingly simple linear systems, starting with the problem described below.

---

### Example Problem: Dollar Bills and Quarters
We have a drawer with dollar bills and quarters, and the total value is $100.  

Questions:
- How many dollar bills ($x$) are there?
- How many quarters ($y$) are there?

#### Observations:
- The problem is **underdetermined**:
  - No unique solution exists because the ratio of dollar bills to quarters can vary.
  - Examples of solutions:
    1. $x = 90$, $y = 40$
    2. $x = 99$, $y = 4$
    3. $x = 0$, $y = 400$
    4. $x = 101$, $y = -4$ (if negative/quasi-integral solutions are allowed)

---

### Matrix Form of the Problem
The system can be represented as:

$$
\begin{bmatrix}
1 & 0 \\
0 & 1
\end{bmatrix}
\begin{bmatrix}
x \\
y
\end{bmatrix}
=
\begin{bmatrix}
100
\end{bmatrix}
$$

- The vector $\begin{bmatrix} 100 \end{bmatrix}$ is decomposed as a linear combination of two vectors $\begin{bmatrix} 1 \\ 0 \end{bmatrix}$ and $\begin{bmatrix} 0 \\ 1 \end{bmatrix}$.  
- Columns here live in $\mathbb{R}^1$ (a one-dimensional space).  

#### Column Dependence
- These columns are **linearly dependent**, since one column is a scalar multiple of the other ($\alpha$ times).  

---

### General Solution
The general solution is captured as the sum of:
1. A **particular solution**.
   - Example: $x = 100, y = 0$ corresponds to 100 of the first column and none of the second column.
2. The **null space**:
   - The null space is expressed with $\alpha$ as:
     $$ \alpha \begin{bmatrix} 1 \\ -4 \end{bmatrix} $$

Thus, the solution is:
$$
\begin{bmatrix} x \\ y \end{bmatrix}
=
\begin{bmatrix} 100 \\ 0 \end{bmatrix}
+
\alpha
\begin{bmatrix} 1 \\ -4 \end{bmatrix}
$$

#### Particular Solutions (Examples):
1. **Case 1: $x = 90$, $y = 40$:**
   - $\alpha = -10$.  
   - Components:
     - $100 - 10 = 90$.
     - $0 + (-10 \times -4) = 40$.  

2. **Case 2: $x = 99$, $y = 4$:**
   - $\alpha = -1$.  
   - Components:
     - $100 - 1 = 99$.
     - $0 + (-1 \times -4) = 4$.  

3. **Case 3: $x = 0$, $y = 400$:**
   - $\alpha = -100$.  
   - Components:
     - $100 - 100 = 0$.  
     - $0 + (-100 \times -4) = 400$.  

4. **Case 4: $x = 101$, $y = -4$:**
   - $\alpha = 1$.  
   - Components:
     - $100 + 1 = 101$.  
     - $0 + (1 \times -4) = -4$.  

---

### Framework and Consistency
- The framework used here applies consistently to complicated, simple, and exceedingly simple systems.  
- By integrating the **null space** and **particular solution**, all possible solutions to the linear system can be recovered.

### Next Steps
- The next problem we'll consider will be **even simpler**—can you guess what it might be?  

---