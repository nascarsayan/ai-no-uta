## Understanding Fourier Series in the Context of Linear Algebra

### Transition: Vectors to Functions
- Initially focused on **vectors, inner products, linear spaces**, and **matrices**—foundational concepts in **linear algebra**.
- Transitioned to **Fourier series**, introducing concepts from **calculus** such as **periodic functions, infinite series**, and **function analysis**.

**Key Idea:**
- The seemingly unrelated fields of **linear algebra** and **Fourier series** are deeply interconnected, highlighting a decomposition of functions into linear algebraic constructs.

---

### The Classical Problem of Fourier Series
- Goal: Represent a function $f(\theta)$ defined on $[-\pi, \pi]$ as a sum of **sines** and **cosines**:
  $$
  f(\theta) = a_0 + \sum_{n=1}^{\infty} \left( a_n \cos(n\theta) + b_n \sin(n\theta) \right)
  $$
- Assumptions: 
  - Function $f(\theta)$ is **periodic**.
  - Representation captures only the periodic segment, ignoring behavior outside $[-\pi, \pi]$.
- Inspiration: Similar to **Taylor series**, where any smooth function can be represented as an **infinite polynomial** sum.

---

### Decomposing Functions as Linear Combinations
- Analogous to **linear algebra**:
  - Representing vector $\vec{v}$ as a linear combination of basis vectors $\{\vec{b}_i\}$.
  - Representing $f(\theta)$ as a combination of basis functions $\{1, \cos(n\theta), \sin(n\theta)\}$.
- Determining coefficients $a_n$ and $b_n$ is a **decomposition problem**, where $f$ is written as:
  $$
  f(\theta) = a_0 \cdot 1 + \sum_{n=1}^{\infty} \left( a_n \cdot \cos(n\theta) + b_n \cdot \sin(n\theta) \right)
  $$

---

### Interpreting Fourier Series Using Linear Algebra
1. **Infinite-Dimensional Space**:
   - The space of functions is not finite-dimensional; cannot span it with finitely many basis functions.
   - Analogy: Infinite number of basis functions for smooth functions over $[-\pi, \pi]$.
   
2. **Decomposition Reformulated**:
   - Problem framed as solving an **overdetermined system** ($Ax = b$) where $A$ is "tall" (many rows, representing basis functions).

---

### Inner Product: Key Tool in Decomposition
- **Inner Product for Functions**:
  $$
  \langle f, g \rangle = \int_{-\pi}^\pi f(\theta) g(\theta) \, d\theta
  $$
- Coefficients ($a_n$, $b_n$) can be computed via inner products:
  $$
  a_n = \frac{\langle f, \cos(n\theta) \rangle}{\langle \cos(n\theta), \cos(n\theta) \rangle}, \quad 
  b_n = \frac{\langle f, \sin(n\theta) \rangle}{\langle \sin(n\theta), \sin(n\theta) \rangle}.
  $$

### On Orthogonality of the Basis
- Basis functions $\{1, \cos(n\theta), \sin(n\theta)\}$ are **orthogonal**:
  1. $\langle 1, \cos(n\theta) \rangle = 0$ and $\langle 1, \sin(n\theta) \rangle = 0$.
  2. $\langle \cos(m\theta), \cos(n\theta) \rangle = 0$ if $m \neq n$.
  3. $\langle \sin(m\theta), \sin(n\theta) \rangle = 0$ if $m \neq n$.
  4. $\langle \cos(m\theta), \sin(n\theta) \rangle = 0$ for all $m, n$.
- Orthogonality simplifies computation, as the matrix of inner products becomes diagonal.

---

### Coefficient Formulas
1. **For $a_0$** (Constant Term):
   $$
   a_0 = \frac{1}{2\pi} \int_{-\pi}^\pi f(\theta) d\theta
   $$
   - Represents the **average value** of $f$.

2. **For $a_n$** (Cosine Coefficients):
   $$
   a_n = \frac{1}{\pi} \int_{-\pi}^\pi f(\theta) \cos(n\theta) d\theta
   $$

3. **For $b_n$** (Sine Coefficients):
   $$
   b_n = \frac{1}{\pi} \int_{-\pi}^\pi f(\theta) \sin(n\theta) d\theta
   $$

---

### Comparison of Insights
- **PDE Context:**
  - Fourier series seemed like a **calculus-heavy** topic, relying on infinite series and integration.
- **Linear Algebra Perspective:**
  - Fourier series becomes a **least-squares approximation** problem in function space.
  - **Dominant theme: Orthogonality**, inner products, and projections.

---

### Recap: Fourier as a Linear Algebra Problem
- Decompose $f(\theta)$ into the best approximation using a finite sum of sines and cosines.
- Use the **orthogonality** of the Fourier basis for simplification.
- Insightfully blends ideas of **infinite series**, **calculus**, and **linear algebra** into a unified framework.