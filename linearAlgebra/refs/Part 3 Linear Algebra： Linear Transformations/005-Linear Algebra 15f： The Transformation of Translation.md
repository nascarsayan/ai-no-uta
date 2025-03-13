## Translation as a Transformation

### Definition
- Given any vector **$U$**, the transformation **$T$** adds a fixed vector **$a$** to **$U$**:
  $$
  T(U) = U + a
  $$

### Example
- Translate vector **$v$** by **$a$**:
  $$
  T(v) = v + a
  $$

### Linearity Check
1. **Addition:**
    - Transform the sum:
      $$
      T(U + V) = (U + V) + a
      $$
    - Transform individually and then add:
      $$
      T(U) + T(V) = (U + a) + (V + a) = U + V + 2a
      $$
    - Result: **Not linear**, as $T(U + V) \neq T(U) + T(V)$.
      
2. **Scalar multiplication:**
    - The transformation also fails the scalar multiplication property (you can verify this yourself).

### Zero Vector Test
- For linear transformations, the image of the zero vector must be the zero vector:
  $$
  T(\mathbf{0}) \stackrel{\text{linear}}{=} \mathbf{0}
  $$
- Under translation:
  $$
  T(\mathbf{0}) = \mathbf{0} + a = a \neq \mathbf{0}
  $$
- Result: **Not linear**, as the zero vector condition fails.

### Consequences of Non-Linearity
- Eigenvalues and eigenvectors are properties of **linear transformations only**.
- Since this transformation is not linear:
  - The concepts like eigenvalues and eigenvectors do **not apply**.
  - We do not look for algebraic equations related to eigenvalues for such transformations.

### Summary
- Translation by a vector **$a$** is not a linear transformation because:
  - It fails the addition and scalar multiplication tests.
  - It does not map the zero vector to the zero vector.
- Moving forward, discussions will focus on linear transformations only, as they are central to studying eigenvalues, eigenvectors, and related properties.