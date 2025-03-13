## Structured Notes on Linear Algebra Transcript

### 1. The Importance of Linear Algebra
- Linear algebra is a subject with immense significance across mathematics and its applications.
- Central focus: Solving linear systems and understanding their solutions.
- Key considerations:
  1. Does a solution exist for a given system?
  2. Is the solution unique, or are there infinitely many?

---

### 2. Key Concepts of Linear Systems
- Linear systems are decomposition problems:
  - The vector on the right-hand side must be decomposed into a linear combination of the left-hand side's coefficient vectors.
  - Unknown coefficients correspond to variables like $x, y, z$, and $t$ in the system.

---

### 3. Vector Decomposition and Span
- To determine if a solution exists:
  - Check if the right-hand side vector lies in the **span** of the left-hand vectors.
  - If the vector is in the span, a solution exists.

#### Geometric Illustration of Span:
- Random vector orientations:
  - Tossing vectors in random directions in $3$D space rarely results in collinear or coplanar vectors.
  - Spanning observations:
    - Two random vectors likely span a plane.
    - A third vector randomly added is unlikely to lie in the same plane, resulting in spanning the entire space.
- Practical implication:
  - With $n$ linearly independent vectors in an $n$-dimensional space, **any vector** can be expressed as a linear combination of these vectors.

---

### 4. Dimension of $\mathbb{R}^3$ and Basis
- Confirming $\mathbb{R}^3$ is three-dimensional:
  - A **basis** for $\mathbb{R}^3$ can be defined using the following vectors:
    $$
    \begin{bmatrix} 1 \\ 0 \\ 0 \end{bmatrix},
    \begin{bmatrix} 0 \\ 1 \\ 0 \end{bmatrix},
    \begin{bmatrix} 0 \\ 0 \\ 1 \end{bmatrix}
    $$
  - These vectors are:
    1. **Linearly independent**:
       - None can be expressed as a linear combination of the others.
    2. **Spanning $\mathbb{R}^3$**:
       - Any vector can be expressed as a linear combination of these three vectors.

#### Implications of Four Vectors in $\mathbb{R}^3$:
- Four vectors in a 3D space are:
  - **Linearly dependent** (more vectors than dimensions).
  - At least one non-trivial linear combination will sum to zero.
- Linear dependence implies:
  1. Lack of uniqueness for solutions.
  2. Solutions, if they exist, are **infinitely many**.

---

### 5. Solving Linear Systems
- **Gaussian Elimination**:
  - Used to find exact coefficients in linear combinations.
- General insights into solutions:
  1. If the right-hand side vector is not in the span, **no solution exists**.
  2. If the right-hand side vector is in the span:
     - If the vectors are **linearly independent**, a **unique solution** exists.
     - If the vectors are **linearly dependent**, **infinitely many solutions** exist.

---

### 6. Universal Truths about Linear Systems
- Linear systems have three possible solution cases:
  1. **No solution**:
     - Right-hand side vector is **not in the span** of left-hand vectors.
  2. **A single unique solution**:
     - Right-hand side vector is in the span, and left-hand vectors are **linearly independent**.
  3. **Infinitely many solutions**:
     - Right-hand side vector is in the span, and left-hand vectors are **linearly dependent**.

---

### 7. Special Cases in Linear Systems
#### Case 1: More Unknowns Than Equations
- Systems where the number of unknowns exceeds the number of equations:
  - More vectors than the space's dimension.
  - Solutions are either:
    - **No solution**, or
    - **Infinitely many solutions**.
  - A **unique solution is impossible**.

#### Case 2: "Square" Systems
- Systems with the same number of equations as unknowns:
  - If treated as a decomposition problem, the left-hand vectors must be linearly independent.
  - Outcome:
    - Always a **unique solution**.
    - Vectors form a **basis** for the space.

---

### 8. Summary and Practical Conclusions
- Linearly independent vectors span the entire space:
  - For $n$ equations in $n$ unknowns, a solution always exists and is unique.
- Linear dependence leads to infinitely many solutions if a solution exists.
- Linear systems are best understood geometrically through decomposition and span.

