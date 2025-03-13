## Least Squares and Matrix Algebra

### 1. Introduction to Least Squares

- Least squares is an important topic, particularly in engineering, due to its geometric interpretation.
- Initially, the perspective of this discussion will be **purely algebraic**, though geometric intuition will follow.

---

### 2. The Problem Setup

- **The Goal**:
  - Solve a system of equations $\mathbf{A}\mathbf{x} = \mathbf{b}$ as accurately as possible, knowing a perfect solution may not exist.

- **Understanding the Setup**:
  - Consider a system with an $8 \times 3$ matrix $\mathbf{A}$. 
  - There are \(8\) equations and \(3\) unknowns: $\mathbf{x} \in \mathbb{R}^3$.
  - **Problem:
    - With more rows than columns, the system is **underdetermined**:
      - There are not enough degrees of freedom to satisfy all equations.
      - Geometrically speaking, the column space of $\mathbf{A}$ cannot span the 8-dimensional space \(\mathbb{R}^8\).
    - Thus, the target vector $\mathbf{b}$ is unlikely to lie in the column space of $\mathbf{A}$.

---

### 3. Reformulation of the Problem

- If $\mathbf{A}\mathbf{x} = \mathbf{b}$ is inconsistent, we find $\mathbf{x}$ such that the **discrepancy**, $\mathbf{r} = \mathbf{b} - \mathbf{A}\mathbf{x}$, is **minimized** in norm.
  
  $$
  \mathbf{r} = \mathbf{b} - \mathbf{A}\mathbf{x}
  $$

  - Minimize \(\|\mathbf{r}\|\), the **length of the residual vector**.
  - Motivation: Treat this as a problem of matrix algebra — **"matrix gymnastics."**

---

### 4. The Role of Inner Products

- To measure vector lengths, we employ an **inner product**:
  - Standard inner product: 
    $$
    \|\mathbf{r}\|^2 = \mathbf{r}^\top \mathbf{r}
    $$

---

### 5. Deriving the Objective Function

- Define the squared length of the residual vector $\mathbf{r}$:
  $$
  \|\mathbf{r}\|^2 = \|\mathbf{b} - \mathbf{A}\mathbf{x}\|^2
  $$
  
- Expand the expression:
  $$
  \|\mathbf{r}\|^2 = (\mathbf{b} - \mathbf{A}\mathbf{x})^\top (\mathbf{b} - \mathbf{A}\mathbf{x})
  $$

- Use properties of transposes:
  $$
  (\mathbf{b} - \mathbf{A}\mathbf{x})^\top (\mathbf{b} - \mathbf{A}\mathbf{x}) = \mathbf{b}^\top\mathbf{b} - 2\mathbf{x}^\top\mathbf{A}^\top\mathbf{b} + \mathbf{x}^\top\mathbf{A}^\top\mathbf{A}\mathbf{x}
  $$

---

### 6. Key Observations

#### Norm Reduction through Orthogonality:
- The residual vector $\mathbf{r}$ is minimized when it is **orthogonal** to the column space of $\mathbf{A}$.
  - This orthogonality condition ensures that $\mathbf{b} - \mathbf{A}\mathbf{x}$ is "closest" to the column space of $\mathbf{A}$.

#### Matrix Algebra Simplifications:
- **Key Matrix-Term Appearances:**
  1. $\mathbf{A}^\top\mathbf{A}$ — Often referred to as the **normal equations**.
  2. The inner product: $\mathbf{r}^\top\mathbf{r} = \|\mathbf{r}\|^2$.
  
- These notations leverage **matrix properties** to simplify vector operations into algebraic matrix terms.

---

### 7. Verbalizing Mathematical Results (Meta Note)

- **Tip for Learning:**
  - Writing or verbalizing matrix results yourself (e.g., properties of transposition or matrix dot products) often aids in comprehension compared to passively listening.

---

### 8. The Final Steps

- To solve for $\mathbf{x}$:
  - Use the **normal equations**:
    $$
    \mathbf{A}^\top \mathbf{A} \mathbf{x} = \mathbf{A}^\top \mathbf{b}
    $$
  
- Geometric and computational insights will be revisited in subsequent discussions.

---

### Summary

- Least squares combines **linear algebra** and **geometry** to address inconsistent systems.
- A critical tool is the **norm minimization framework** using the **inner product** and leveraging matrix notation.
