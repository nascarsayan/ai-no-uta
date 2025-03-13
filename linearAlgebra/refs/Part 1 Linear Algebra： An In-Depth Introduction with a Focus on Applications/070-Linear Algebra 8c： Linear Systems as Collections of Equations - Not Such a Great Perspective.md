# Solving Linear Systems: Different Perspectives

## 1. Introduction
- Previously, we analyzed a linear system, solved it, and derived a solution using the decomposition approach.
- A key takeaway: Interpreting a linear system as a decomposition problem provides insightful and effective results.

## 2. Alternative Approach
There's another common approach to solving linear systems:
- **Traditional "Equation Manipulation" Approach**:
  - Treats the system as a collection of equations.
  - Focuses on manipulating equations via Gaussian elimination.
  - Reduces the system to solve variables in terms of others.

### Steps:
1. Rearrange the system to solve for some variables (e.g., $x$ and $y$) in terms of free variables ($z$ and $t$).
2. Assign arbitrary values to free variables ($z$ and $t$), determining the dependent variables ($x$ and $y$).

### Observations:
- Free variables $z$ and $t$ offer **two degrees of freedom**, matching the decomposition approach's parameters $\alpha$ and $\beta$.

---

## 3. Symmetry and Parameters
- The traditional method breaks symmetry: $z$ and $t$ are free, but $x$ and $y$ are dependent.
- To restore symmetry:
  - Introduce new parameters $\alpha$ and $\beta$:
    $$
    z = \alpha, \quad t = \beta
    $$
  - Express dependent variables $x$ and $y$ using $\alpha$ and $\beta$.

### Resulting System (In Terms of $\alpha$ and $\beta$):
- Each variable is expressed symmetrically, yielding a more elegant solution.
- Reducing the system yields four rows (one per variable), with two degrees of freedom.

---

## 4. Vector Formulation
Linear algebra focuses on organizing equations into **vector equations** for simplicity and elegance:
- Group variables $\begin{bmatrix} x \\ y \\ z \\ t \end{bmatrix}$ into a vector.
- Separate expressions on the right-hand side into components:
  - Terms without $\alpha, \beta$.
  - Terms with $\alpha$.
  - Terms with $\beta$.

### Example:
Organizing terms:
1. Terms with no $\alpha$ or $\beta$:
   $$
   \begin{bmatrix} 8 \\ 11 \\ 0 \\ 0 \end{bmatrix}
   $$
2. Terms with $\alpha$:
   $$
   \alpha \begin{bmatrix} -4 \\ -5 \\ 1 \\ 0 \end{bmatrix}
   $$
3. Terms with $\beta$:
   $$
   \beta \begin{bmatrix} -7 \\ -1 \\ 0 \\ 1 \end{bmatrix}
   $$

### Final Vector Equation:
$$
\begin{bmatrix} x \\ y \\ z \\ t \end{bmatrix} =
\begin{bmatrix} 8 \\ 11 \\ 0 \\ 0 \end{bmatrix} +
\alpha \begin{bmatrix} -4 \\ -5 \\ 1 \\ 0 \end{bmatrix} +
\beta \begin{bmatrix} -7 \\ -1 \\ 0 \\ 1 \end{bmatrix}
$$

---

## 5. Comparison to Decomposition Approach
- Both approaches (traditional and decomposition):
  - Yield equivalent results.
  - Represent the same solution space.
- Key Differences:
  - The two methods may produce **opposite vectors**, but these opposites span the same space.

### Null Space Interpretation:
- Decomposition interprets the solution space as the **null space**.
- The traditional approach does not assign a specific interpretation to the space.

---

## 6. Flexibility in Choosing Free Variables
- Traditional method allows different choices for free/dependent variables:
  - Example: Making $x$ and $y$ free, and solving for $z$ and $t$ instead.
  - Different free variable choices yield different expressions while spanning the **same solution space**.

---

## 7. Conclusion
- Despite methodological variations, all solutions represent the same collection of vectors.
- Expressing solutions in vector form aligns with linear algebra's goals of elegance and clarity:
  - Example:
    $$
    \text{Vector solution: } 
    \begin{bmatrix} x \\ y \\ z \\ t \end{bmatrix} =
    \text{constant vector} + \text{scalar multiples of basis vectors}
    $$
- Both approaches highlight the deep connections between linear systems and vector spaces.