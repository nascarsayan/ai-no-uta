## Linear Systems as Decomposition Problems

### Key Concept:
- "Linear Algebra is not just about solving linear systems; solving linear systems is one of its many applications."
- Solving a **linear system** can be reinterpreted as solving a **decomposition problem**.

---

### Decomposition Example:

This problem is about decomposing a vector into a linear combination of four basis vectors with four unknown coefficients. For example:
- Coefficients: $x$, $y$, $z$, and $t$.
- The problem reduces to finding specific values for these coefficients so that:

$$
x + y + z + 11t = 73
$$

and similar constraints on other components.

---

### Equivalence of Linear Systems and Decomposition

To solve a linear system:

- Finding values of $x$, $y$, $z$, and $t$ to satisfy the system of equations:
  1. $x + y + z + 11t = 73$
  2. (other similar linear equations).

To solve the decomposition problem:

- Find values for $x$, $y$, $z$, and $t$ such that the linear combination evaluates to the target vector:
  \[
  \text{e.g., } x \cdot \mathbf{v}_1 + y \cdot \mathbf{v}_2 + z \cdot \mathbf{v}_3 + t \cdot \mathbf{v}_4 = \mathbf{b},
  \]
  where $\mathbf{b}$ is the target vector.

Thus, solving a decomposition problem is equivalent to solving a linear system—it involves finding the same coefficients.

---

### Solution:
Using the decomposition insights (without tedious techniques like Gaussian elimination), the solution to the system/decomposition problem is:

$$
\begin{aligned}
  x &= 13 + 20\alpha, \\
  y &= 2 + 15\alpha, \\
  z &= 58 - 24\alpha, \\
  t &= -\alpha.
\end{aligned}
$$

Here, $\alpha$ is a free parameter capturing the infinite solutions in terms of linear combinations.

---

### Takeaway:
- Solving **linear systems** is essentially solving **decomposition problems**.
- This approach emphasizes understanding **linear dependence** and **decomposition** over rigid numerical methods like Gaussian elimination.