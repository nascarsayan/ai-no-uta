### Notes on Gaussian Quadrature and Related Topics

---

#### Overview
- The lecture covers Gaussian quadrature, a numerical method for approximating integrals.
- Gaussian quadrature relies heavily on linear algebra concepts such as:
  - Viewing polynomials as vectors.
  - Inner products and orthogonality.
  - Gram-Schmidt orthogonalization.

---

### Gaussian Quadrature Insights

#### Connection to Linear Algebra
1. Polynomials as Vectors:
   - Interpretation of polynomials as vectors in vector space.
   - Orthogonality and projection play a key role.

2. Gram-Schmidt Orthogonalization:
   - Used to construct orthogonal polynomials.
   - Basis for constructing **Legendre polynomials**.

---

#### Construction of Orthogonal Polynomials
1. **Basis Selection**:
   - Start with the standard polynomial basis $\{1, x, x^2, x^3, \dots \}$.
   - For example, limit to degree-4 polynomials $\{1, x, x^2, x^3, x^4\}$.

2. **Orthogonalization via Gram-Schmidt**:
   - Orthogonal polynomials are not necessarily normalized.
   - They have an extra degree of freedom for scaling, which is often chosen for convenience, e.g., so the polynomial evaluates to 1 at $x = 1$.

---

#### Example: Orthogonal Polynomials
- Original basis: $\{1, x, x^2, x^3, x^4\}$.
- After Gram-Schmidt:
  - $L_0(x)$: A constant polynomial.
  - $L_1(x)$: Linear polynomial orthogonal to $L_0(x)$.
  - $L_2(x)$: Quadratic polynomial orthogonal to $L_0(x)$ and $L_1(x)$.
- The orthogonal polynomials span the same space as the original ones.

---

### Key Properties of Orthogonal Polynomials

1. **Orthogonality to Lower-Degree Polynomials**:
   - For instance, $L_4(x)$ is orthogonal to all polynomials of degree less than 4:
     - Orthogonal to $x^3$, $x^2$, $x$, and $1$.
   - This is because of the structure imposed by Gram-Schmidt and the symmetric interval $[-1, 1]$.

2. **Symmetric Interval Integral**:
   - Integration over a symmetric interval (e.g., $[-1, 1]$) ensures that odd polynomials yield 0 when integrated product-wise with even polynomials.

3. **Linear Independence**:
   - Each orthogonal polynomial contributes a unique degree term not present in previous polynomials.
   - The orthogonal polynomials are linearly independent.

---

### Polynomial Roots and Gaussian Quadrature

1. **Exact Number of Roots**:
   - A polynomial of degree $n$ has exactly $n$ roots within the interval $[-1, 1]$.

2. **Distribution of Roots**:
   - Roots are all real and lie in the interval $[-1, 1]$.
   - The locations of roots play a critical role in Gaussian quadrature.

3. **Root-Based Integration**:
   - Gaussian quadrature leverages the roots as integration "nodes."
   - Each node contributes optimally to numerical integration based on weights derived using orthogonal polynomial properties.

---

### Importance of Symmetry in Interval
- Symmetry of $[-1, 1]$:
  - Odd functions integrate to 0 due to symmetric limits.
  - Leads to preservation of even-odd orthogonality structure.

---

### Beyond Basics: Properties of Legendre Polynomials

1. **Degree Rules**:
   - Degree $n$ polynomials integrate efficiently over $[-1, 1]$.
   - Orthogonal polynomials are the foundation for quadrature rules.

2. **Root Structure**:
   - Every polynomial has exactly $n$ roots, critical for defining nodes in Gaussian quadrature.

3. **Useful Fact**:
   - Each polynomial crosses the $x$-axis exactly $n$ times within $[-1, 1]$.
   - This property simplifies integration strategy.

---

### Final Remarks
- Gaussian quadrature leads to an efficient integration method for approximating polynomials or functions.
- The elegant interplay of linear algebra concepts—orthogonality, inner products, and basis span—make Gaussian quadrature a powerful tool in numerical methods.

