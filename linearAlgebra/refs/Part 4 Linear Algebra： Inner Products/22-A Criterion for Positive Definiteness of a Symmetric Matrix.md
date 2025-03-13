## Positive Definite Quadratic Forms and Determinants

### Quadratic Forms and Positive Definiteness

A **quadratic form** is an expression of the form:

$$
Q(\mathbf{x}) = \mathbf{x}^T A \mathbf{x},
$$

where $A$ is a symmetric matrix, and $\mathbf{x}$ is a vector. To determine whether a quadratic form is **positive definite**, we focus on the following property:

#### Definition of Positive Definiteness
A quadratic form is positive definite if:
1. It is **strictly positive** for all non-zero inputs, i.e., $Q(\mathbf{x}) > 0 \; \forall \; \mathbf{x} \neq 0$.
2. The associated symmetric matrix $A$ satisfies certain conditions that guarantee this property.

---

### Conditions for Positive Definiteness

#### Symmetric Matrices and Quadratic Forms
We are analyzing symmetric matrices because symmetric matrices simplify quadratic forms and ensure eigenvalues are strictly real. 

#### Matrix Terminology
- **Diagonal terms** contribute to the primary quadratic terms (e.g., $x^2$, $y^2$), which must be large and positive for the form to be positive definite.
- **Off-diagonal terms** influence cross-term interactions (e.g., $xy$). While their signs do not directly matter, their relative size compared to diagonal terms is critical.

#### Positive Definiteness Criteria
A symmetric matrix $A$ is **positive definite** if and only if:
1. All **leading principal minors (determinants of submatrices)** are **positive**:
   - The **top-left $1 \times 1$ determinant** must be positive.
   - The **top-left $2 \times 2$ determinant** must be positive.
   - The **top-left $3 \times 3$ determinant**, and so on, must follow the same rule.
2. The **discriminant** of the associated quadratic equation satisfies specific conditions to ensure the parabola associated with the matrix does not cross zero.

---

### Example 1: Counterexamples and Negative Diagonal Terms
If a symmetric matrix has a **negative diagonal entry**, this is an **immediate indication** that the quadratic form cannot be positive definite.

#### Reason:
- When all but one component of the vector $\mathbf{x}$ is set to zero (e.g., $x_2 = x_3 = \cdots = 0$), the negative diagonal term dominates the quadratic form, making it negative.

#### Example:
Consider the matrix:

$$
A = \begin{bmatrix} 2 & 1 \\ 1 & -3 \end{bmatrix}.
$$

To evaluate:

1. Simplify the quadratic form as:

$$
Q(x, y) = 2x^2 + 2xy - 3y^2.
$$

2. Setting $x = 0$, the term left is $-3y^2$, which is negative for any $y \neq 0$.

#### Conclusion:
The quadratic form $Q(x, y)$ and its matrix $A$ are **not positive definite**.

---

### Example 2: Determining Positive Definite Matrices

#### Setup:
Let $A$ be a symmetric $2 \times 2$ matrix:

$$
A = \begin{bmatrix} a & b \\ b & c \end{bmatrix}.
$$

#### Positive Definiteness Conditions:
1. The top-left entry (1x1 determinant) must be:
   $$ a > 0. $$

2. The determinant of the full $2 \times 2$ matrix must be:
   $$ \text{det}(A) = ac - b^2 > 0. $$

#### Interpretation:
- The condition $a > 0$ ensures the quadratic term of $x_1^2$ is positive.
- The condition $ac - b^2 > 0$ ensures that the parabola corresponding to $Q(x_1, x_2)$ does not dip below the $x$-axis for any combination of $x_1$ and $x_2$.

---

### Discriminants for Quadratic Forms

#### For a Quadratic Equation:
If $Q(x)$ simplifies to a quadratic equation of the form:

$$
Q(x) = ax^2 + bx + c,
$$

the **discriminant** is given by:

$$
\Delta = b^2 - 4ac.
$$

#### Rules for Positive Definite Forms:
- For strictly positive quadratics, **parabolas must never cross or touch the x-axis**.
- This requires $\Delta < 0$ (negative discriminant).

#### Generalizing to Quadratic Forms:
For the matrix $A$, the discriminant for the quadratic form is often scaled by four to simplify computations.

---

### High-Dimensional Case and Principal Minors
#### Key Result:
For a symmetric $n \times n$ matrix $A$:
1. Compute **all leading principal minors** (determinants of top-left $k \times k$ submatrices).
2. Positive definiteness requires **all principal minors to be positive**.

Example of this hierarchy:
- For $n = 3$, the leading principal minors are:
   1. $a_{11} > 0$,
   2. $\text{det}\left(\begin{bmatrix} a_{11} & a_{12} \\ a_{12} & a_{22} \end{bmatrix}\right) > 0$,
   3. $\text{det}(A_{3 \times 3}) > 0$.

---

### Algorithm for Verifying Positive Definiteness
1. **Symmetry Check**: Ensure $A$ is symmetric.
2. **Compute Leading Minors**: For each $k$, where $k = 1, 2, \dots, n$, calculate the determinant of the top-left $k \times k$ submatrix.
3. **Verify Positivity**: Check that all determinants are positive.
   - Any negative determinant implies the matrix is **not positive definite**.

---

### Summary of Positive Definiteness Criterion
A symmetric matrix $A$ is positive definite if:
1. All its eigenvalues are positive.
2. All leading principal minors are positive.
3. The quadratic form $Q(\mathbf{x}) = \mathbf{x}^T A \mathbf{x}$ is strictly positive for all $\mathbf{x} \neq 0$.

The simplest numerical shortcut is to leverage determinants of submatrices to identify definiteness properties.

