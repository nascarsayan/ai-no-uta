## Linearly Dependent and Independent Vectors

### Definitions of Linear Dependence

1. **First Definition**:
    - A set of vectors is linearly dependent if **one of the vectors can be expressed as a linear combination of the others**.

2. **Second Definition**:
    - A set of vectors is linearly dependent if there exists a **non-trivial linear combination** of the vectors that equals zero.

    $$
    c_1 \mathbf{v}_1 + c_2 \mathbf{v}_2 + \cdots + c_n \mathbf{v}_n = \mathbf{0}
    $$

    - **Non-trivial** means at least one of the scalars $c_1, c_2, \ldots, c_n$ is **non-zero**.

---

### Equivalence of Definitions

#### From the First to the Second:
- Assume one vector is a linear combination of the others:
    $$
    \mathbf{v}_1 = c_2 \mathbf{v}_2 + c_3 \mathbf{v}_3 + \cdots + c_n \mathbf{v}_n
    $$
- Rearrange all terms to one side:
    $$
    \mathbf{v}_1 - c_2 \mathbf{v}_2 - c_3 \mathbf{v}_3 - \cdots - c_n \mathbf{v}_n = \mathbf{0}
    $$
- Set coefficients for $\mathbf{v}_1$ and the others:
    $$
    c_1 = 1, c_2 = -c_2, \ldots, c_n = -c_n
    $$
- This is a **non-trivial linear combination**, so the second definition is satisfied.

#### From the Second to the First:
- Assume there exists a non-trivial linear combination:
    $$
    c_1 \mathbf{v}_1 + c_2 \mathbf{v}_2 + \cdots + c_n \mathbf{v}_n = \mathbf{0}
    $$
- Without loss of generality, assume $c_1 \neq 0$. Rearrange to isolate $\mathbf{v}_1$:
    $$
    \mathbf{v}_1 = -\frac{c_2}{c_1} \mathbf{v}_2 - \frac{c_3}{c_1} \mathbf{v}_3 - \cdots - \frac{c_n}{c_1} \mathbf{v}_n
    $$
- This shows $\mathbf{v}_1$ is a linear combination of the others, satisfying the **first definition**.

---

### Key Perspective

- The two definitions of linear dependence are equivalent.
- Moving forward, both definitions can be used interchangeably depending on the context.

---

### Practical Interpretation

- **Non-Trivial Linear Combination**:
    - Any equation involving vectors that equals \( \mathbf{0} \) where at least one coefficient is non-zero.

- **Expressing a Vector**:
    - If any vector in the set is a combination of others, the set is linearly dependent.

