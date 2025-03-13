# Structured Markdown Notes: Polynomials as Vectors

## 1. Introduction to Polynomials

- **Geometric vectors** were discussed extensively. Now, focus briefly shifts to **polynomials** (or functions more generally).
- Unlike geometric vectors:
  - Polynomials are familiar to everyone:
    - Addition: Adding two polynomials results in another polynomial.
    - Scalar multiplication is intuitive.
    - Common operations include graphing, finding roots, evaluating integrals/derivatives, etc.

---

## 2. Polynomials as Vectors in Linear Algebra

- **Key idea**: Polynomials can be thought of as vectors in the context of linear algebra.
- Polynomials satisfy:
  - **Addition**: The sum of two polynomials is another polynomial.
  - **Scalar multiplication**: Scaling a polynomial still results in another polynomial.
  - They adhere to **commutativity**, **associativity**, and **distributivity**.

---

## 3. Why Polynomials are Important

- **Applications**:
  - Widely used in applied mathematics and physics.
  - Approximating complex problems with simpler polynomial expressions is considered elegant.
  - Example: **Gaussian quadrature** relies on understanding polynomials as vectors.
- Terms like **orthogonal polynomials**:
  - Blend concepts from geometry (orthogonality) and algebra (polynomials).
  - Illustrate the connection between geometry and algebra.

---

## 4. Polynomials Form a Vector Space

- **Vector Space Properties**:
  - The sum of two polynomials is another polynomial.
  - A polynomial multiplied by a scalar or zero is still a polynomial.
  - Example: Quadratic polynomials can also form a subspace if defined carefully.

---

## 5. Degree Restriction and Subspaces

### Quadratic Polynomials:
- **Challenge**: Adding two quadratic polynomials can sometimes result in a linear polynomial (if the quadratic terms cancel out).
- **Solution**: Broaden to include **polynomials of degree up to 2**:
  - Allows inclusion of constants and linear polynomials.
  - Generalize:
    - Instead of "cubic polynomials," refer to **polynomials of degree up to 3**.
    - Similarly, for "nth degree polynomials," consider **polynomials of degree up to n**.

---

## 6. Subspaces: Polynomials vs Geometry

### Connection to Geometric Vectors:
- Polynomials may not be inherently geometric, but their behavior parallels geometric ideas:
  - **Example**: Geometric vectors constrained to a plane.
    - Scalar multiplication or vector addition keeps results within the plane.
  - Similarly, within a polynomial subspace, operations keep results within the subspace.

### Polynomials Passing Through Specific Points:
- Consider a subspace:
  - **Polynomials that pass through (1, 0)**.
  - These polynomials have a root at $x = 1$:
    1. Property: $x = 1$ is a root.
    2. Property: The coefficients sum to 0.

---

## 7. Subspace Example: Polynomials with Roots at $x=1$

### Example:
- Polynomials such as:
  $$
  p(x) = (x-1)^2, \quad q(x) = (x-1)(x+2), \ldots
  $$
- **Operations within the subspace**:
  - Adding two such polynomials results in another polynomial with a root at $x = 1$.
  - Scalar multiplication maintains this property.
  - These polynomials cannot "escape" the subspace, much like vectors constrained to a plane cannot exit the plane.

### Geometric Inspiration:
- Though polynomials are algebraic, their subspace behavior mirrors geometric intuition:
  - Being "stuck" in a subspace is analogous to geometric vectors constrained to a plane or line.

---

## 8. Broader Insights: Geometry in Linear Algebra

- Geometry influences linear algebra:
  - Subspaces are universal irrespective of the vector type (e.g., geometric, symbolic, numerical).
- Although polynomials and geometric vectors are entirely different:
  - Their shared **vector properties** unify them in the context of linear algebra.
  - Key properties: Addition and scalar multiplication apply meaningfully to both.

---

## 9. Conclusion

- Viewing polynomials as vectors provides new perspectives and examples in linear algebra.
- Moving forward:
  - Explore other vector spaces like $\mathbb{R}^n$ and their unique structures.
- Polynomials, $\mathbb{R}^n$, and geometric vectors offer 3 distinct but interconnected examples foundational to linear algebra.