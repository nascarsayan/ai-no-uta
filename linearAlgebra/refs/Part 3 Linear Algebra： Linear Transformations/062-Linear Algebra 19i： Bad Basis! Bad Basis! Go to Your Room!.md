## Understanding the Role of Basis

### Importance of Basis Selection

- There's no inherently "bad" basis; all bases are valid mathematically.
- The suitability of a basis depends on the specific problem at hand.
- For certain problems, some bases are more advantageous, while others make computations more complex.

---

### Cartesian Basis: A Popular Yet Often Suboptimal Choice

- Cartesian basis (denoted as $C$) is commonly used, likely 99% of the time.
- However, it might not be ideal for ~90% of problems.
- **Key Point:** Choosing the wrong basis generally leads to more tedious computations and less elegant results.

---

## Constructing a Transformation Matrix with the Cartesian Basis

### Step-by-Step Strategy

1. **Apply the linear transformation** ($T$) to each basis vector ($e_1, e_2$) individually.
2. **Express the transformed vectors** in terms of the original basis.
3. Formulate the transformation matrix column by column using these coordinates.

---

### Example: Cartesian Basis and Reflection Transformation

#### First Basis Vector ($T(e_1)$):
- Reflect $e_1$ and decompose the resulting vector. 
- Approximation:
  $$
  T(e_1) \approx 
  \begin{bmatrix}
  0.9 \\ 
  0.6
  \end{bmatrix}
  $$

#### Second Basis Vector ($T(e_2)$):
- Reflect $e_2$ and decompose similarly.
- Approximation:
  $$
  T(e_2) \approx 
  \begin{bmatrix}
  0.6 \\
  -0.8
  \end{bmatrix}
  $$

#### Observations:
- The matrix for the transformation using the Cartesian basis:
  $$
  T =
  \begin{bmatrix}
  0.9 & 0.6 \\ 
  0.6 & -0.8
  \end{bmatrix}
  $$
- Approximation highlights that:
  - The **trace** is not exactly zero due to errors, even though it ideally should be.
  - The orthogonality isn't as "clean."

---

### General Approach Using Angles (Applied Mathematician's Perspective)

#### Key Idea:
Decompose the transformation based on general trigonometric relations for angle $\alpha$.

#### First Basis Vector ($T(e_1)$):
- Using the angle $2\alpha$:
  $$
  T(e_1) =
  \begin{bmatrix}
  \cos(2\alpha) \\ 
  \sin(2\alpha)
  \end{bmatrix}
  $$

#### Second Basis Vector ($T(e_2)$):
- Derived using angle relations ($\frac{\pi}{2} - 2\alpha$):
  $$
  T(e_2) =
  \begin{bmatrix}
  \sin(2\alpha) \\
  -\cos(2\alpha)
  \end{bmatrix}
  $$

#### Resulting Matrix:
- More general and accurate:
  $$
  T =
  \begin{bmatrix}
  \cos(2\alpha) & \sin(2\alpha) \\
  \sin(2\alpha) & -\cos(2\alpha)
  \end{bmatrix}
  $$

#### Matrix Properties:
- **Trace:** $0$, as expected.
- **Determinant:** $-1$, characteristic of a reflection transformation.

---

### Comparison of Approaches

| **Metric**                  | **Cartesian Basis**                          | **General (Angle-Based)**                  |
|-----------------------------|---------------------------------------------|------------------------------------------|
| **Ease of Computation**     | Approximation; numbers not clean            | Trigonometric relations make it elegant |
| **Matrix Properties**       | Approximation off (e.g., trace not 0)       | Properties hold exactly (e.g., trace=0) |
| **Suitability**             | Works but tedious for many problems         | More problem-specific and generalizable |

---

### Conclusion

- Using the Cartesian basis can work but often creates unnecessary computational complexity.
- For reflection transformations and similar problems, a tailored, problem-specific basis or a generalized trigonometric-based approach is much more effective.