## Orthogonal Sets of Polynomials

### Overview
- We are building an **orthogonal set of polynomials**.
- The process starts by choosing an **inner product**, which allows us to discuss orthogonality.

### Inner Product Definition
- The choice of inner product is arbitrary.
- For this exercise, we'll use the **standard inner product**.

### Initial Polynomial Basis
The basis we begin with is **not orthogonal**:
- $1$
- $x$
- $x^2$

### Motivation
- While the initial basis might seem convenient (easy to decompose, simple to work with), it is considered the **worst basis** from certain perspectives.
- Our goal: Transform this basis into a new orthogonal basis.

---

## Orthogonal Polynomials

### Building an Orthogonal Basis
- The new basis will consist of **Leander polynomials** (denoted by $L_1, L_2, \dots$).
- These polynomials are **special** because they are **orthogonal**.

### Key Idea: Orthogonality
Orthogonality is the foundation for concepts like Gaussian quadrature. It enables precise evaluation of integrals using only a few key points.

---

### Calculation of the Basis
1. **First Polynomial ($A_1$):**
    - The first polynomial remains unchanged: 
      $$
      A_1 = 1
      $$

2. **Second Polynomial ($B_1$):**
    - Process: Orthogonalize $x$ relative to $A_1$:
      $$
      B_1 = x - \frac{\langle x, 1 \rangle}{\langle 1, 1 \rangle} \cdot 1
      $$
    - Inner products:
      $$
      \langle x, 1 \rangle = \int_{-1}^{1} x \cdot 1 \, dx = 0 \quad (\text{Odd function over symmetric domain})
      $$
      $$
      \langle 1, 1 \rangle = \int_{-1}^{1} 1 \cdot 1 \, dx = 2 \quad (\text{Area of rectangle})
      $$
    - Result:
      $$
      B_1 = x
      $$
    
3. **Third Polynomial ($C_1$):**
    - Process: Orthogonalize $x^2$ relative to $A_1$ and $B_1$:
      $$
      C_1 = x^2 - \frac{\langle x^2, 1 \rangle}{\langle 1, 1 \rangle} \cdot 1 - \frac{\langle x^2, x \rangle}{\langle x, x \rangle} \cdot x
      $$
    - Inner products:
      $$
      \langle x^2, 1 \rangle = \int_{-1}^{1} x^2 \cdot 1 \, dx = \int_{-1}^{1} x^2 \, dx = \frac{2}{3}
      $$ 
      $$
      \langle x^2, x \rangle = 0 \quad (\text{Odd function over symmetric domain})
      $$
      $$
      \langle x, x \rangle = \int_{-1}^{1} x^2 \, dx = \frac{2}{3}
      $$
    - Result:
      $$
      C_1 = x^2 - \frac{1}{3}
      $$

### Higher-Order Polynomials
The same process can be extended for higher-order terms (e.g., $x^3$, $x^4$, etc.), yielding an orthogonal basis.

---

## Why Choose Orthogonal Polynomials?

### Gaussian Quadrature
- **Gaussian quadrature** is one of the most practical applications of orthogonal polynomials.
- It allows you to approximate definite integrals of **smooth functions** with extraordinary accuracy:
  - Evaluate the function at **specific points**.
  - Multiply the values by **prescribed weights**.
  - Sum them up to calculate the integral.

### Example:
Using orthogonal polynomials:
- Approximation of integrals can reach **16 digits of accuracy** with just 10 points.
- This method is faster and more precise than traditional numerical integration.

---

### Insights:
- While constructing orthogonal polynomials might seem arbitrary, their properties lead to powerful tools like Gaussian quadrature.
- The transformation from the initial basis into the orthogonal basis highlights the **importance of inner products** and the structure of vector spaces.

### Amazing Application:
Orthogonal polynomials are key to applications in:
1. Computational methods (integration, optimization).
2. Signal processing (Fourier series, filters).
3. Numerical simulations and approximations.

---

### Exercise Recap
- Built a new orthogonal basis starting from $\{1, x, x^2, \dots\}$.
- Illustrated the calculation process using inner products and properties of symmetry.
- Explained practical benefits, highlighting Gaussian quadrature as a remarkable technique deriving from this logic.