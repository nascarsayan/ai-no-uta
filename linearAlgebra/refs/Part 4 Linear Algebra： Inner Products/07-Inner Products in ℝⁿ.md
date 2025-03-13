## 1. Distributive Properties in Vector Spaces

### Additive and Scalar Distributivity

1. **Distributivity over vector addition**:
    - The operation `$a(b + c) = ab + ac$` is defined and works naturally in vector spaces.
    - However, this is **half** of distributivity. The complete set of distributive laws in vector spaces involves both additive and scalar multiplication.

2. **Distributivity over scalar multiplication**:
    - If $a$ and $b$ are scalars, and $v$ is a vector, then scalar multiplication is distributive as:
      $$
      (a + b)v = av + bv
      $$
    - Note that both are crucial to maintain the structure of a vector space.

---

## 2. Vector Multiplication with Defined Inner Product Example

### Specific Inner Product Definition:
Given vectors in $\mathbb{R}^3$, $a = [a_1, a_2, a_3]^T$ and $b = [b_1, b_2, b_3]^T$, the inner product is defined as:
$$
\langle a, b \rangle = 3a_1b_1 + 4a_2b_2 + a_3b_3
$$

- Example Calculation:
  Multiply $[1, 2, 3]$ with $[2, -1, -1]$:
  $$
  \langle a, b \rangle = 3(1)(2) + 4(2)(-1) + (3)(-1) = 6 - 8 - 3 = -5
  $$

---

## 3. Verification of Inner Product Properties

### Properties in Inner Product Verification:
1. **Linearity for Addition**:
    - $a \cdot (b + c) = a \cdot b + a \cdot c$
    - Verified using individual components of vectors.
    
2. **Symmetry**:
    - $\langle b, a \rangle = \langle a, b \rangle$
    - This is naturally satisfied for standard and symmetrically defined inner products.

3. **Positive Definiteness**:
    - $\langle a, a \rangle > 0$ if $a \neq 0$.
    - Anything dotted with itself should not be negative.
    - **Counterexample**: For some inconsistent definitions, a vector dotted with itself can result in $0$ or less than $0$. Correct inner products avoid this case.

---

## 4. Standard Inner Product: $\mathbb{R}^n$

The **standard inner product** for vectors $x, y \in \mathbb{R}^n$ is defined as:
$$
\langle x, y \rangle = \sum_{i=1}^n x_i y_i
$$

### Example:
For $x = [1, 2, 3]$ and $y = [1, 2, 3]$:
$$
\langle x, y \rangle = 1^2 + 2^2 + 3^2 = 14
$$

---

## 5. Non-standard Inner Product Example (Semi-definiteness)

Define a custom inner product in $\mathbb{R}^3$:
$$
\langle x, y \rangle = x_1y_1 + 2x_1y_2 + 3x_3y_3
$$

### Verification:
1. **Symmetry**:
    - $\langle x, y \rangle \neq \langle y, x \rangle$ (violating symmetry due to the $2x_1y_2$ term).
    - Example: Dotting $[1, 0, 0]$ with $[0, 1, 0]$, $\langle x, y \rangle = 2$ but $\langle y, x \rangle = 0$.

2. **Positive Definiteness**:
    - Testing vector $[1, -1, 0]$ with itself:
      $$
      \langle a, a \rangle = (1)^2 + 2(1)(-1) + 0^2 = 1 - 2 = -1
      $$
    - Result violates positive definiteness as inner product is negative.

---

## 6. Positive Semi-definiteness and Fixing Definitions

### Insight into Positive Semidefinite Forms:
An inner product $\langle x, x \rangle$ results in $0$ for certain non-zero vectors, indicating *positive semi-definiteness*.

- Example:
    - If the custom inner product ignores one vector component, such as $z$, then $\langle [0, 0, 1], [0, 0, 1] \rangle = 0$.

### Rectifying Definitions:
- Modify the definition to include strict conditions ensuring $\langle x, x \rangle > 0 \ \forall x \neq 0$, aligning properly with **positive definiteness**.

---

## 7. Geometry and Algebra in Inner Products

### Interplay of Geometry and Algebra:

1. **Geometric View**:
    - Inner products interpret projections, lengths, and angles.
    - Orthogonality is characterized as $\langle x, y \rangle = 0$.

2. **Algebraic Perspective**:
    - Inner product definitions are tools to satisfy algebraic properties and form subspaces consistent with vector space axioms.

---

## 8. Standard Inner Products are Arbitrary Choices

### Misconception of "the" Inner Product
- Many textbooks introduce "the" inner product as standardized (dot product) without addressing the diversity of valid inner products.
- Emphasis: Be aware of the broader class of inner product definitions, not limited to geometry-derived special cases.

