# Quadratic Form Minimization and Least Squares

## 1. Quadratic Form Minimization

### Importance
- Quadratic form minimization is widely used and important in fields like physics (energy minimization), engineering, and optimization problems in general.
- Natural phenomena are often framed in terms of optimization (Euler's minimization principle).

---

### Quadratic Function Representation
A quadratic function with linear terms can be expressed in matrix form, which helps in revealing its structure:
  
$$
f(x) = \frac{1}{2} x^T A x - b^T x
$$

Where:
- $A$ is a symmetric and positive definite matrix.
- $x$ is a vector variable.
- $b$ is a vector.
- The constant term can be ignored as it doesn't affect the location of the minimum.

**Key Insight:**  
To find the **minimum** of this function, it reduces to solving the linear system:  
$$
A x = b
$$

---

### Example: Single Variable Quadratic Case
The simplest quadratic function in one dimension:  

$$
f(x) = \frac{1}{2} a x^2 - b x
$$

1. Compute the derivative and set it to zero:
   $$
   \frac{\partial f(x)}{\partial x} = a x - b = 0
   $$
   $$ 
   x = \frac{b}{a}
   $$

2. Adding a linear term shifts the minimum:
   $$
   f(x) = \frac{1}{2} a x^2 - b x \implies x = \frac{b}{a}
   $$

---

### Multivariable Generalization
In a multi-variable setup, the same principle holds but requires **matrix operations**:
- For function $f(x) = \frac{1}{2} x^T A x - b^T x$:
  $$
  A x = b
  $$
- Minimum exists only if $A$ is positive definite (ensures convexity).

---

### Matrix Representation Challenges
- Matrix notation simplifies algebraic manipulation but complicates calculus:
  - E.g., taking derivatives involves treating $x$ as both a vector and its entries ($x_1, x_2, \dots$).

**Solution:** Use **tensor calculus** for consistency.  
**Observation:** Matrix notation is great for structure but breaks down for detailed calculus derivations.

---

### Gradient Descent
If solving $A x = b$ directly (e.g., via Gaussian elimination) is impractical (e.g., for large, sparse matrices):
1. Use an **iterative optimization method like Gradient Descent**:
   $$
   x_{\text{next}} = x_{\text{current}} - \alpha \nabla f(x_{\text{current}})
   $$
   where $\nabla f(x) = A x - b$.

2. Steps:
   - Start with a random $x$.
   - Update $x$ iteratively by moving in the direction opposite the gradient.
   
**Special Case:** Conjugate Gradient method is a more efficient extension of this approach.

---

### Philosophical Implications
- The fundamental problem of linear algebra (solving $A x = b$) arises naturally as a minimization problem of a quadratic form.
- Euler's principle of minimization connects optimization with the universe's natural laws.

---

## 2. Least Squares

### Overview
1. Least squares arises when solving $A x = b$ **approximately**, as in cases where:
   - $A$ has more rows than columns (overdetermined system).
   - Exact solutions don't exist.

2. The goal:
   - Minimize the **squared error**:
     $$
     \text{minimize } \|A x - b\|^2
     $$

3. Algebraic Connection:
   - Least squares leads to solving the **normal equations**:
     $$
     A^T A x = A^T b
     $$

---

### Applications
- Common in engineering, machine learning, and data fitting.
- Geometric interpretation involves projecting $b$ onto the column space of $A$.

---

### Gradient Descent in Least Squares
- Iterative methods like Gradient Descent apply here as well.
- Helps solve large-scale problems efficiently.

---

**Next Topic Preview:**  
- Detailed explanation of least squares, its geometric interpretation, and its engineering applications.