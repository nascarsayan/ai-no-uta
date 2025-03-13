## Projection as a Linear Transformation

### Definition
- **Projection** is a type of transformation that maps vectors onto a straight line passing through the origin.
- For a given vector $\mathbf{u}$:
  - Draw a line perpendicular to the given straight line.
  - The point where this perpendicular line meets the straight line is the **image** of $\mathbf{u}$ under the projection.

### Example
- If $\mathbf{u}$ is the starting vector, then its projection is denoted as $P(\mathbf{u})$. 

### Properties
1. Similar to **reflection**, but the projection **stops on the line** and doesn’t cross it.
2. All image vectors will lie on the straight line.

---

## Linearity of Projection

To test if projection is a **linear transformation**, we perform the following checks:

### **1. Sum Test**
- Consider two vectors $\mathbf{u}$ and $\mathbf{w}$.
- The projection of the sum is $P(\mathbf{u} + \mathbf{w})$.
- Compare this to adding the individual projections: $P(\mathbf{u}) + P(\mathbf{w})$.

#### Visualization:
- Draw $\mathbf{u}$ and $\mathbf{w}$.
- Their sum is $\mathbf{u} + \mathbf{w}$.
- Project all vectors to check if:
  $$
  P(\mathbf{u} + \mathbf{w}) = P(\mathbf{u}) + P(\mathbf{w}).
  $$

#### Conclusion:
- After performing the steps, it's evident that the **sum test is satisfied** for projection, confirming linearity.

### **2. Scalar Multiplication Test**
- Scaling vector $\mathbf{u}$ by a scalar $c$:
  $$
  P(c \cdot \mathbf{u}) = c \cdot P(\mathbf{u}).
  $$
- This holds true as well, confirming that projection satisfies the properties of scalar multiplication.

**Result:** Projection is a **linear transformation**.

---

## Eigenvalues and Eigenvectors of Projection

### Insight
Linear transformations often have **eigenvalues** and **eigenvectors** that reveal deeper properties.

- **Eigenvalue ($\lambda$):**
  $$
  T(\mathbf{v}) = \lambda \mathbf{v},
  $$
  where $\mathbf{v}$ is the eigenvector.

### Eigenvectors and Eigenvalues of Projection
1. **First Eigenvector ($\mathbf{v}_1$):**
   - Any vector **along the projection line**.
   - For such a vector $\mathbf{v}_1$, it holds that:
     $$
     P(\mathbf{v}_1) = \mathbf{v}_1.
     $$
   - The corresponding **eigenvalue** is $\lambda = 1$.

2. **Second Eigenvector ($\mathbf{v}_2$):**
   - Any vector **orthogonal to the projection line**.
   - For such a vector $\mathbf{v}_2$, it holds that:
     $$
     P(\mathbf{v}_2) = \mathbf{0}.
     $$
   - The corresponding **eigenvalue** is $\lambda = 0$.

#### Summary:
- Eigenvalues: $\lambda = 1$, $\lambda = 0$.
- Eigenvectors:
  - $\mathbf{v}_1$: Lies along the projection line.
  - $\mathbf{v}_2$: Orthogonal to the projection line.

---

## Key Observations about Projection

1. **Zero Eigenvalue**:
   - $\lambda = 0$ is a valid eigenvalue, with the eigenvector $\mathbf{v}_2$ (which is nonzero).
   - The zero vector ($\mathbf{0}$) is **never** an eigenvector, as eigenvectors must be nonzero.

2. **Linearity Implication**:
   - For any **linear transformation**, the zero vector always maps to the zero vector:
     $$
     T(\mathbf{0}) = \mathbf{0}.
     $$

---

## Algebraic Property of Projection

### Key Insight:
Applying projection twice yields the same result as applying it once:
$$
P(P(\mathbf{v})) = P(\mathbf{v}).
$$

### Algebraic Equation
This property translates algebraically to:
$$
P^2 = P.
$$

### Eigenvalues as Roots of a Quadratic Equation
- Consider the analogous equation:
  $$
  x^2 = x.
  $$
- Factorize:
  $$
  x(x-1) = 0.
  $$
- Roots are $x = 0$ and $x = 1$.

Thus, the **eigenvalues** of the projection transformation ($\lambda = 0$, $\lambda = 1$) are the roots of this equation.

---

## General Observations
1. **Projection as Inspiration**:
   - The property $P^2 = P$ is extended to define projections in other vector spaces (beyond geometry).

2. **Importance of Eigenvalues**:
   - The eigenvalues and eigenvectors provide deeper insights into the transformation.
   - Eigenvalues describe the "scaling" effect of the transformation along certain directions.

3. **Non-coincidence of Algebra and Geometry**:
   - The connection between geometrical transformations and algebraic equations (e.g., $x^2 = x$) is not coincidental—this is a general rule in linear algebra.

---

Next: Transitioning to **Rotations** for discussing another class of transformations.