## Linear Properties of Functions and Polynomials

### 1. Linear Properties of Functions
- The space of functions is fundamentally richer than $\mathbb{R}^n$, which results in linear properties behaving differently. This discussion delves into those differences and similarities.

#### Key Idea: Linearity of Properties
- Certain properties of functions can or cannot be linear.
- **Linearity Test:** A property is linear if it holds under:
  1. Addition of functions.
  2. Scalar multiplication of functions.
  3. Closure of the property under these operations.

#### Example: Function Passing Through a Point
- Consider the property where functions pass through a specific point, e.g., $f(x_1) = 0$.
  - **Addition Test:** If $f_1(x_1) = 0$ and $f_2(x_1) = 0$, then $(f_1 + f_2)(x_1) = 0 + 0 = 0$. The property is preserved under addition.
  - **Scalar Multiplication Test:** If $f(x_1) = 0$, then $(k \cdot f)(x_1) = k \cdot 0 = 0$. The property is preserved under scalar multiplication.

#### Example: Integral Condition on Functions
- A function satisfies an integral condition if:
  $$
  \int_a^b f(x) \, dx = 0
  $$
  - **Addition Test:**
    - For $f_1$ and $f_2$ satisfying the property:
      $$
      \int_a^b (f_1(x) + f_2(x)) \, dx = \int_a^b f_1(x) \, dx + \int_a^b f_2(x) \, dx = 0 + 0 = 0
      $$
    - Hence, closed under addition.
  - **Scalar Multiplication Test:**
    - For $k \cdot f$:
      $$
      \int_a^b (k \cdot f(x)) \, dx = k \cdot \int_a^b f(x) \, dx = k \cdot 0 = 0
      $$
    - Hence, closed under scalar multiplication.
  - This is a **linear property** as it satisfies closure under both operations.

#### Example: Differential Condition on Functions
- A function satisfies a differential property if:
  $$
  \frac{d}{dx} f(x) = 0
  $$
  - Similar logic applies for addition and scalar multiplication, confirming that this is also a **linear property**.

---

### 2. Linear Properties in the Context of Polynomials
- Polynomials are a more specific subset of functions. Let's analyze linear properties for quadratic polynomials.

#### General Form of a Quadratic Polynomial
- A quadratic polynomial is given by:
  $$
  p(x) = ax^2 + bx + c
  $$

#### Translating Properties into Coefficient Constraints
1. **Property 1: The Polynomial Evaluates to 0 at a Point**
   - Let $p(x_0) = 0$, i.e., the polynomial passes through point $x_0$.
   - Substituting:
     $$
     ax_0^2 + bx_0 + c = 0
     $$
   - This provides a linear constraint on the coefficients $a$, $b$, and $c$.

2. **Property 2: Integral of the Polynomial Over an Interval is 0**
   - For $p(x)$:
     $$
     \int_a^b p(x) \, dx = \int_a^b (ax^2 + bx + c) \, dx
     $$
   - Calculating:
     $$
     \int_a^b p(x) \, dx = \left[\frac{a}{3}x^3 + \frac{b}{2}x^2 + cx\right]_a^b
     $$
   - The result is a constraint on $a$, $b$, and $c$ of the form:
     $$
     A \cdot a + B \cdot b + C \cdot c = 0
     $$

3. **Property 3: Differential Constraint**
   - If $p'(x) = 0$ satisfies a property, then for $p(x) = ax^2 + bx + c$:
     - $p'(x) = 2ax + b$.
     - Additional conditions such as $p'(x_0) = 0$ would further constrain $a$ and $b$:
       $$
       2ax_0 + b = 0
       $$

#### Simultaneous Constraints
- When applying multiple linear constraints to polynomials, the system of equations often results in a **template** represented as:
  $$
  c_1a + c_2b + c_3c = 0
  $$
  where $c_1, c_2, c_3$ are constants based on the property.

---

### 3. Conclusion
- Linear properties for functions and polynomials share a similar logical framework:
  1. **Closure under addition.**
  2. **Closure under scalar multiplication.**
  3. **Representable as a linear combination of coefficients equaling zero.**
- These properties define **subspaces** in the appropriate space (functions or polynomials).
- When narrowed to specific function types (e.g., polynomials), the constraints become more structured, often described by a system of linear equations.