## Multivariable Calculus: Minima and Positive Definiteness

### Key Components of Calculus
- Calculus is centered on **differentiation** and **integration**.
- Differentiation:
  - **Critical points** occur where the derivative is zero.
  - At those points, additional tests (e.g., second derivative test) determine whether it's a maximum, minimum, or point of inflection.
- Integration:
  - Fundamentally tied to evaluating areas, volumes, etc.
  - **Fundamental Theorem of Calculus** bridges integration and differentiation.

### Multivariable Calculus Generalizations
1. **Critical points in higher dimensions:**
   - The generalization of "minimum occurs where derivative = zero."
2. **Integration over regions:**
   - **Divergence Theorem** (or Gauss's theorem) is the generalized Fundamental Theorem of Calculus in multivariable calculus.

---

### Applying Differentiation to Minima in Several Variables

#### 1D Case Recap:
- For a single-variable function $f(x)$:
  - Minimum conditions:
    $$
    f'(x) = 0 \quad \text{and} \quad f''(x) > 0
    $$

#### **Extension to Multiple Variables:**
- Consider a function $F(x, y, z)$.
- A **critical point** occurs where all partial derivatives are zero:
  $$
  F_x = 0, \quad F_y = 0, \quad F_z = 0
  $$
- But how do we determine whether it's a minimum?

---

### Restricting to 1D: Exploring Minima Using Lines
To simplify analysis, we restrict the function $F$ along a straight line through the critical point:

1. **Parameterization of Straight Line:**
   - Let the point of interest be $\mathbf{x}_0 = (x_0, y_0, z_0)$.
   - The equation of a straight line is:
     $$
     \mathbf{x}(\alpha) = \mathbf{x}_0 + \alpha \mathbf{n}
     $$
     where $\mathbf{n} = (n_1, n_2, n_3)$ is the unit vector in the chosen direction, and $\alpha$ is the line parameter.

2. **Restricted Function:**
   - Substitute the parameterization into $F(x, y, z)$ to get a 1D function $f(\alpha)$:
     $$
     f(\alpha) = F(\mathbf{x}_0 + \alpha \mathbf{n})
     $$
     
   - Compute its derivatives (using the chain rule):
     $$
     \frac{df}{d\alpha} = \nabla F \cdot \mathbf{n}
     $$

3. **Conditions Along Any Line:**
   - A minimum implies:
     $$
     \frac{df}{d\alpha} = 0 \quad \text{at} \quad \alpha = 0
     $$
   - This leads to:
     $$
     \nabla F \cdot \mathbf{n} = 0 \quad \forall \, \mathbf{n}
     $$
   - Since this must hold for **all directions $\mathbf{n}$**, we deduce:
     $$
     \nabla F = \mathbf{0} \quad (\text{i.e., } F_x = 0, F_y = 0, F_z = 0)
     $$

---

### Equivalent Criteria in Multivariable Calculus
For a function $F(x, y, z)$ to have a minimum at $(x_0, y_0, z_0)$:
1. **Gradient Condition**:
   $$
   \nabla F = \mathbf{0} \quad (\text{Zero gradient at critical point})
   $$
2. **Positive Definiteness of the Hessian Matrix**:
   - The second derivative test in higher dimensions examines the **Hessian matrix**:
     $$
     H = \begin{bmatrix}
     F_{xx} & F_{xy} & F_{xz} \\
     F_{yx} & F_{yy} & F_{yz} \\
     F_{zx} & F_{zy} & F_{zz}
     \end{bmatrix}
     $$
   - $H$ must be **positive definite**:
     - All eigenvalues of $H$ are positive.
     - Ensures that the critical point is a local minimum.
---

### Key Observations:
- Restricting multivariable functions to 1D allows us to connect the critical point analysis to familiar concepts from single-variable calculus.
- The **gradient condition** ($\nabla F = \mathbf{0}$) ensures the function is stationary (no slopes).
- The **Hessian test** guarantees convexity in all directions, confirming a minimum.

---

### Theoretical Insights:
1. Partial derivatives vanish at the critical point:
   $$
   F_x = 0, \quad F_y = 0, \quad F_z = 0
   $$
2. Minima along all lines through the critical point implies a **global gradient condition**:
   $$
   \nabla F = \mathbf{0}
   $$

3. Positive-definite Hessian ensures the critical point is a **local minimum**.

---

### Example Parameterization Recap
- Take a straight line through $(x_0, y_0, z_0)$:
  $$
  \mathbf{x}(\alpha) = \begin{bmatrix} x_0 \\ y_0 \\ z_0 \end{bmatrix} + \alpha \begin{bmatrix} n_1 \\ n_2 \\ n_3 \end{bmatrix}
  $$
- Derivatives:
  $$
  \frac{d\mathbf{x}}{d\alpha} = \begin{bmatrix} n_1 \\ n_2 \\ n_3 \end{bmatrix}
  $$
- Gradient projection along direction $\mathbf{n}$:
  $$
  \nabla F \cdot \mathbf{n} = 0 \quad \forall \, \mathbf{n}
  $$

### Conclusion:
This approach leverages the simplicity of 1D calculus to reason about multidimensional behavior, anchored in the equivalence of the gradient and Hessian tests.