## General Linear Transformations and Eigenvalues

### Key Question
- Can a general linear transformation (not just a matrix transformation), such as the derivative on the space of cubic polynomials, be recognized as defective? 
- Can the **algebraic multiplicity** of an eigenvalue be established without relying on characteristic polynomials or other matrix characteristics?

The answer lies in leveraging **generalized eigenvectors**.

---

### Review: Matrix Case

For a matrix with eigenvalue $\lambda = 5$ and high algebraic multiplicity:
1. Subtracted $\lambda = 5$ from the diagonal:
   $$ A - 5I $$

2. Why use $A - 5I$ instead of saying "subtract five from the diagonal"? 
    - This algebraic expression can be interpreted in terms of **linear transformations**:
        $$ T_{\text{new}} = T_{\text{original}} - 5 \cdot I $$

3. Define eigenvectors and eigenvalues:
    - A vector $v$ in the **kernel** (null space) of $T_{\text{new}}$ is an **eigenvector**.
    - The scalar $\lambda$ associated with $v$ is the corresponding **eigenvalue**.

4. Multiplicities:
    - **Algebraic Multiplicity**: Number of times the eigenvalue is repeated.
    - **Geometric Multiplicity**: Dimension of eigenspace associated with $\lambda$.

---

### Generalized Eigenvectors 
The story continues if an eigenvector lies:
- In the **null space** *and* the **range** of the transformation.

#### Generalized Eigenvector Process
1. If $v$ is in the null space and range, its **pre-image** exists and is called a **generalized eigenvector**.
2. Examples in sequence:
    - **Rank 1 (eigenvector)**: $T(v) = 0$
    - **Rank 2**: Pre-image under $T$, e.g., $v_2 = T^{-1}(v_1)$.
    - **Rank 3**: Pre-image of $v_2$, e.g., $v_3 = T^{-1}(v_2)$.

#### Multiplicities
- **Algebraic Multiplicity** increases as generalized eigenvectors are added to the chain. 
- **Geometric Multiplicity** often remains less than algebraic multiplicity, indicating **deficiency** or defectiveness.

---

### Example: Derivative on Cubic Polynomials $\mathbb{P}_3$
#### Known Facts
1. The transformation $D$, the derivative operator, corresponds to:
    $$ D(p(x)) = p'(x) $$

2. It has an eigenfunction (eigenvector in a function space) that's constant, $f(x) = 1$, with the eigenvalue $\lambda = 0$.

#### Process
1. Transform $\lambda=0$:
   $$ T_{\text{new}} = D - 0 \cdot I = D $$

2. **Algebraic Steps**:
   - Eigenvector for $\lambda = 0$: $f(x) = 1$.
   - Generalized eigenvector (rank 2): $f(x) = x$, as $D(1) = 0$ implies $D(x) = 1$.
   - Further generalized eigenvector (rank 3): $f(x) = x^2$, as $D(x) = 1$ implies $D(x^2) = 2x$.
   - Final generalized eigenvector (rank 4): $f(x) = x^3$, as $D(x^2) = 2x$ implies $D(x^3) = 3x^2$.

#### Multiplicity Summary
- **Algebraic Multiplicity**: 4 (due to chain of generalized eigenvectors).
- **Defectiveness**: The geometric multiplicity is less than algebraic multiplicity (e.g., geometric multiplicity = 1 for $\lambda = 0$).

---

### Key Takeaways
1. Concepts of **algebraic multiplicity** and **generalized eigenvalues** extend seamlessly to general linear transformations.
2. These ideas apply intrinsically—without invoking matrices or characteristic polynomials.

