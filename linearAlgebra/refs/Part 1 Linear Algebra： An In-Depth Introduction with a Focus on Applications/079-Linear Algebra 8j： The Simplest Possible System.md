## Simplest Linear System: $ax = b$

### Overview
The equation $ax = b$ represents the simplest linear system:
- Involves one equation and one unknown ($x$).
- Constants $a$ and $b$ are given numbers.
  
#### Number of Solutions
- Linear systems can have:
  - **0 solutions** (no solution),
  - **1 solution** (unique solution), or
  - **Infinitely many solutions**.
- The outcome depends on the values of $a$ and $b$.

---

### Possible Cases for $ax = b$

#### Case 1: $5x = 10$
- Here, $a = 5$ and $b = 10$.
- Solving gives the unique solution:
  $$
  x = 2
  $$

#### Case 2: $5x = 0$
- Here, $b = 0$.
- Solving gives the unique solution:
  $$
  x = 0
  $$
- Both cases rely on $a \neq 0$ and the solution formula $x = \frac{b}{a}$.

#### Case 3: $0x = 10$
- $a = 0$ and $b \neq 0$.
- No solutions exist, as $0 \cdot x = 0$, making it impossible to satisfy $0x = 10$.

#### Case 4: $0x = 0$
- $a = 0$ and $b = 0$.
- Any value of $x$ satisfies the equation, leading to:
  $$
  x \in \mathbb{R}
  $$
  This case has infinitely many solutions.

---

### Connecting Solutions to Linear Algebra

#### Equation Reformulated in Vector Representation
The system $ax = b$ can be expressed using matrix-vector representation:
$$
\begin{bmatrix} a \end{bmatrix} 
\begin{bmatrix} x \end{bmatrix} 
= 
\begin{bmatrix} b \end{bmatrix}
$$
- $a$ represents a single column (vector) in $\mathbb{R}^1$.

#### Column Space Perspective
1. **Column Space**:
   - The single column $\begin{bmatrix} a \end{bmatrix}$ spans $\mathbb{R}^1$ if $a \neq 0$.
   - If $a = 0$, the column space is reduced to the trivial zero space: $\{\mathbf{0}\}$.
2. **Null Space**:
   - For $a \neq 0$, the null space is trivial: $\{\mathbf{0}\}$.
   - For $a = 0$, the null space includes all vectors: $\mathbb{R}$.

---

### Specific Scenarios

#### Case of $a \neq 0$
- Unique solution exists for any $b$ in the column space ($b \in \operatorname{Col}(A)$).
- Null space is trivial: $\{0\}$.
- Example:
  $$
  \begin{bmatrix} 5 \end{bmatrix} 
  \begin{bmatrix} x \end{bmatrix} 
  = 
  \begin{bmatrix} 10 \end{bmatrix}
  $$
  Solution: $x = 2$.

#### Case of $a = 0, b \neq 0$
- Column space is trivial ($\{0\}$).
- $b$ (right-hand side) is not in the column space, so no solutions exist.

#### Case of $a = 0, b = 0$
- Column space remains trivial ($\{0\}$).
- $b$ is in the column space, allowing infinitely many solutions:
  $$
  x \in \mathbb{R}
  $$

---

### General Solution
In cases with non-trivial null space:
$$
x = \text{particular solution} + \alpha \cdot \begin{bmatrix} 0 \end{bmatrix}
$$
Where $\alpha \in \mathbb{R}$ represents a scalar. Simplifications can yield:
$$
x = \alpha
$$
- This signifies infinitely many solutions for $a = 0, b = 0$.

---

### Summary
- **Linear Dependency**:
  - A single column in $\mathbb{R}^1$ is linearly independent unless it's the zero column ($a = 0$).
- **Column Space**:
  - Spans $\mathbb{R}^1$ for $a \neq 0$.
  - Reduced to $\{0\}$ for $a = 0$.
- **Null Space**:
  - Trivial ($\{0\}$) for $a \neq 0$.
  - Non-trivial ($\mathbb{R}$) for $a = 0$.