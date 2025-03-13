## Structured Notes: Least Squares, Inner Products, and Matrix Representation

### 1. Introduction to the Problem
- **Context**: Relating inner products and metric matrices to least squares problems.
- **Key Objective**: Understand the connection between matrix representation of inner products and solving least squares problems.

---

### 2. Computing the Inner Product Matrix
To find the inner product matrix with respect to a basis $\mathbf{B}$ in $\mathbb{R}^3$:
1. Assign $\mathbf{B}$ as columns of a matrix, say $\mathbf{B} = \begin{bmatrix} \mathbf{b}_1 & \mathbf{b}_2 & \mathbf{b}_3 \end{bmatrix}$.
2. Compute the pairwise inner products of the basis vectors using:
   $$
   \text{Inner Product Matrix} = \mathbf{B}^\top \mathbf{B}.
   $$
   - Here, $\mathbf{B}^\top$ transposes the matrix, converting columns into rows.
   - The standard inner product in $\mathbb{R}^n$ is:
     $$
     \langle \mathbf{v}, \mathbf{w} \rangle = v_1w_1 + v_2w_2 + \cdots + v_nw_n.
     $$
   - Each entry $\langle \mathbf{b}_i, \mathbf{b}_j \rangle$ of $\mathbf{B}^\top \mathbf{B}$ is the dot product of $\mathbf{b}_i$ with $\mathbf{b}_j$.

**Geometric Insight**:
- $\mathbf{B}^\top \mathbf{B}$ compresses the information of the interactions (dot products) among the basis vectors into matrix form.

---

### 3. Solving the Least Squares Problem
**Problem Setup**:
- Over-determined system: Too many equations, not enough unknowns.
- Equivalent to finding vector $\mathbf{x}$ in $\mathbb{R}^n$ such that:
  $$
  \mathbf{A} \mathbf{x} \approx \mathbf{b},
  $$
  where:
  - $\mathbf{A}$ is the matrix with column vectors $\mathbf{a}_1, \mathbf{a}_2, \dots, \mathbf{a}_m$. 
  - $\mathbf{b}$ is the right-hand side vector.

---

#### Key Formula for Least Squares Solution
The least squares solution minimizes $||\mathbf{A} \mathbf{x} - \mathbf{b}||^2$. The solution is given by:
$$
\mathbf{x} = (\mathbf{A}^\top \mathbf{A})^{-1} \mathbf{A}^\top \mathbf{b}.
$$

1. **Components**:
   - $\mathbf{A}^\top \mathbf{A}$: Gram (or metric) matrix, capturing inner products of column vectors of $\mathbf{A}$.
   - $\mathbf{A}^\top \mathbf{b}$: Represents the projection of vector $\mathbf{b}$ onto the column space of $\mathbf{A}$.

2. **Interpretation**:
   - $(\mathbf{A}^\top \mathbf{A})^{-1}$ "scales" the projection to give the weights for the linear combination.

---

### 4. Connecting Inner Products with Basis Representation
- When $\mathbf{B}$ is a non-standard basis in $\mathbb{R}^n$, solving for an unknown vector $\mathbf{v}$ in terms of $\mathbf{B}$ requires:
  $$
  \mathbf{v} = \mathbf{B} \mathbf{c},
  $$
  where $\mathbf{c}$ is the coordinate vector.
- **Inner Product Connection**:
  - To compute $\mathbf{c}$:
    $$
    \mathbf{c} = (\mathbf{B}^\top \mathbf{B})^{-1} \mathbf{B}^\top \mathbf{v}.
    $$
  - This parallels the least squares formula:
    - Dot product ($\mathbf{B}^\top \mathbf{v}$).
    - Metric matrix inversion ($(\mathbf{B}^\top \mathbf{B})^{-1}$).

---

### 5. Least Squares as Projection
- **Context**: Suppose $\mathbf{b}$ is not in the column space of $\mathbf{A}$ (non-feasibility).
- **Projection Idea**:
  The goal is to find $\mathbf{\hat{b}}$ (closest approximation of $\mathbf{b}$ in the column space of $\mathbf{A}$).

- **Connection**:
  - The inner product metric $(\mathbf{A}^\top \mathbf{A})$ captures a coordinate shift, mapping $\mathbf{b}$ into a linear combination of the columns of $\mathbf{A}$.
  - The solution $\mathbf{x}$ ensures $\mathbf{\hat{b}} = \mathbf{A} \mathbf{x}$ minimizes the residual:
    $$
    ||\mathbf{b} - \mathbf{\hat{b}}||^2.
    $$

---

### 6. Conclusion: Generalized Framework
- Whether working with a legitimate basis or only a subspace approximation, the procedure ties back to:
  - **Dot Products**: Evaluating projection weights.
  - **Metric Matrix**: Encoding interactions among basis vectors.
  - **Inverse Metric**: Scaling appropriately to balance contributions from different basis vectors.

This systematic approach explains why even the "messiest" formulas for least squares or projection tasks are **natural outcomes** of geometric and algebraic principles tied to inner products and matrix mechanics.