## Polynomial Interpolation

### Importance of Interpolation
- Interpolation has considerable practical applications.
- Many aspects of interpolation involve **pure linear algebra.**
- It's one of the first applications we'll discuss in this context.

---

### Situations Requiring Interpolation:
1. **Limited Data:**
   - When you have limited data, interpolation helps estimate missing values **between available data points**.
2. **Extrapolation:**
   - Predict what happens **beyond the given data points** using trends or functions.
   - Extrapolation is generally more challenging and unreliable compared to interpolation.

---

### Control Parameters in Experiments
- Example:
    - Input parameter $x$ on the x-axis: $\{1, 2, 3, 4\}$
    - Corresponding experimental outputs (y-axis): $\{0, 1, 1, 1\}$
- Goals in interpolation:
  1. Understand the experimental data via a comprehensible **expression** (e.g., linear, quadratic).
  2. Predict intermediate values (e.g., at $x = 1.5$ or $x = 2.5$).

---

### Linear Interpolation
- **Definition:**
  A straight line is drawn between two data points to estimate intermediate values.
  
- **Advantages of Linear Interpolation:**
  - **Simplicity**: The simplest way to interpolate data.
  - Reliable unless there is a reason to believe in a higher-order behavior (e.g., quadratic function).

- **Prediction:**
  - At $x = 1.5$, use a straight line between $x = 1$ and $x = 2$:
    $$
    \text{Interpolated value at } x = 1.5 = 0.5
    $$

---

### Polynomial Interpolation
1. **Why Use Higher-Order Polynomials:**
   - When the data isn't well captured by simple lines or quadratics.
   - Example: A **cubic polynomial** can fit four data points ($n+1 = 4, \text{degree } n = 3$).

2. **Setting Up a Polynomial:**
   General cubic polynomial form:
   $$
   p(x) = ax^3 + bx^2 + cx + d
   $$

3. **Number of Degrees of Freedom:**
   - A cubic polynomial has **4 coefficients** ($a, b, c, d$) and requires **4 equations** derived from the data.

4. **Example Data Points Setup:**
   At given $x$ values, the function satisfies:
   - $p(1) = 0 \rightarrow a(1)^3 + b(1)^2 + c(1) + d = 0$
   - $p(2) = 1 \rightarrow a(2)^3 + b(2)^2 + c(2) + d = 1$
   - $p(3) = 1 \rightarrow a(3)^3 + b(3)^2 + c(3) + d = 1$
   - $p(4) = 1 \rightarrow a(4)^3 + b(4)^2 + c(4) + d = 1$

5. **Expressing in Matrix Form:**
   Writing this system as:
   $$
   \begin{bmatrix}
   1 & 1 & 1 & 1 \\
   8 & 4 & 2 & 1 \\
   27 & 9 & 3 & 1 \\
   64 & 16 & 4 & 1 \\
   \end{bmatrix}
   \begin{bmatrix}
   a \\ b \\ c \\ d
   \end{bmatrix} =
   \begin{bmatrix}
   0 \\ 1 \\ 1 \\ 1
   \end{bmatrix}
   $$
   - The left-hand matrix is a **Vandermonde matrix.**

6. **Solution:**
   - Solve using Gaussian Elimination or matrix inversion.
   - Result:
     $$
     p(x) = -3 + \frac{13}{3}x - 3x^2 + 16x^3
     $$

---

### Plotting the Polynomial
- The interpolated polynomial passes exactly through the data points:
  - At $x = 1$, $p(1) = 0$
  - At $x = 2$, $p(2) = 1$
  - At $x = 3$, $p(3) = 1$
  - At $x = 4$, $p(4) = 1$
  
- **Observation of Behavior:**
  - **Extrapolation Issue:** The polynomial may behave unexpectedly outside the data range.
  - **Wiggles:** The high-degree polynomial might oscillate unnecessarily between points.

---

### Challenges in Polynomial Interpolation
1. **Runge Phenomenon:**
   - Oscillations, especially for high-degree polynomials.
   - The polynomial fits the data but may show **undesired behavior in between.**
   
2. **Mitigation Strategies:**
   - Use lower-degree polynomials or piecewise polynomials (e.g., splines).
   - Choose functions that better suit the data behavior (e.g., rational functions like $p(x) = a + bx + cx^2 + d/x$).

---

### Takeaways:
- **Linear Interpolation:** Best for simplicity and quick estimates, and avoids unnecessary oscillations.
- **Polynomial Interpolation:** Captures exact data points but can introduce wiggles (Runge phenomenon).
- **Choice of Model:** Depends on data characteristics and the desired precision in interpolation or extrapolation.