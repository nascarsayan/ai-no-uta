## Linear Dependence and Uniqueness in Decomposition

### Key Concept
- **Linear dependence** immediately implies a lack of uniqueness.
- **Linear independence** is required to justify uniqueness.

---

### Implications of Linear Dependence
- If there exists a **non-trivial linear combination** of vectors such that it equals the zero vector:  
    $c_1\vec{v}_1 + c_2\vec{v}_2 + \dots + c_n\vec{v}_n = \vec{0}$  
    where not all $c_i = 0$, then we can add any amount of this special linear combination to a decomposition of any vector, altering the coefficients without changing its value:
  
    $$
    \begin{aligned}
    \vec{d} &= \alpha_1\vec{v}_1 + \alpha_2\vec{v}_2 + \dots + \alpha_n\vec{v}_n \\
    &+ \lambda(c_1\vec{v}_1 + c_2\vec{v}_2 + \dots + c_n\vec{v}_n) \\
    &= \text{Same value of } \vec{d}, \text{but coefficients vary.}
    $$
  
- This means that for any decomposition, **infinitely many decompositions** exist as long as the vectors are linearly dependent.

---

### Proof that Linear Independence Implies Uniqueness
#### Theorem
If vectors $\vec{v}_1, \vec{v}_2, \vec{v}_3$ are **linearly independent**, then there exists a **unique decomposition** of any vector $\vec{d}$ in terms of these vectors.

#### Proof
1. **Assume two decompositions** for $\vec{d}$:
    $$
    \begin{aligned}
    \vec{d} &= \alpha \vec{v}_1 + \beta \vec{v}_2 + \gamma \vec{v}_3 \quad \text{(First decomposition)} \\
    \vec{d} &= \alpha_1 \vec{v}_1 + \beta_1 \vec{v}_2 + \gamma_1 \vec{v}_3 \quad \text{(Second decomposition)}.
    \end{aligned}
    $$
2. Subtract the two decompositions:
    $$
    \vec{0} = (\alpha - \alpha_1) \vec{v}_1 + (\beta - \beta_1) \vec{v}_2 + (\gamma - \gamma_1) \vec{v}_3.
    $$
3. Observe that at least one coefficient ($\alpha - \alpha_1$, $\beta - \beta_1$, $\gamma - \gamma_1$) **must be non-zero**, or else it would contradict the assumption of different decompositions.
4. Therefore, a **non-trivial linear combination** equals $\vec{0}$, which violates the assumption that $\vec{v}_1, \vec{v}_2, \vec{v}_3$ are linearly independent.

---

### Formal Connection Between Linear Independence and Uniqueness
1. **Linear dependence** implies that there exist infinitely many decompositions for a vector.
2. **Linear independence** guarantees that there is exactly **one unique decomposition** for a vector.

---

### Summary
- **Linear dependence $\rightarrow$ Lack of uniqueness**
- **Linear independence $\rightarrow$ Uniqueness**