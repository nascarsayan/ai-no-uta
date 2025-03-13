# Notes on Numerical Integration and Weights

## 1. The Concept of "Weights"

- **Definition**: Weights are proportions used in numerical integration procedures. 
- **Purpose**: The goal is to pick specific points, evaluate the function at these points, and compute a weighted sum of the function's values. These weights determine how much "influence" each point has in the final approximation of the integral.

## 2. Numerical Integration Strategy

1. Choose **smart points** (not necessarily equally spaced).
2. Assign **weights** to each point, denoted as $W_1, W_2, \dots, W_n$.
3. Approximate the integral of a function $f(x)$ as:

   $$
   \int f(x) \, dx \approx W_1 f(X_1) + W_2 f(X_2) + \dots + W_n f(X_n)
   $$

### Example for Four Points:
If we choose four points $X_1, X_2, X_3, X_4$, the formula becomes:
   $$
   \int f(x) \, dx \approx W_1 f(X_1) + W_2 f(X_2) + W_3 f(X_3) + W_4 f(X_4)
   $$

---

## 3. Key Conditions for Accurate Integration

- The weights must satisfy certain conditions to ensure **exactness** for specific types of functions (polynomial integrals up to a given degree):
  - **Constant functions**: The sum of the weights should equal the length of the interval.
  - **Linear functions**: Ensure the integral of $f(x) = x$ is exact.
  - **Quadratic and cubic functions**: Extend the conditions to functions of the forms $f(x) = x^2$ and $f(x) = x^3$.

### System of Linear Equations
For a degree $n$ polynomial, the weights must satisfy $n+1$ equations formed by imposing exactness for:
1. $f(x) = 1$ (constant).
2. $f(x) = x$ (linear).
3. $f(x) = x^2$ (quadratic).
4. $f(x) = x^3$ (cubic).

**Example** (Four weights $\{W_1, W_2, W_3, W_4\}$):
- For $f(x) = 1$:
  $$
  W_1 + W_2 + W_3 + W_4 = 2
  $$
  (Here, the length of the interval is 2 for $[-1, 1]$).
  
- For $f(x) = x$:
  $$
  W_1 X_1 + W_2 X_2 + W_3 X_3 + W_4 X_4 = 0
  $$
  (The integral of $x$ over $[-1, 1]$ is 0).

- For $f(x) = x^2$:
  $$
  W_1 X_1^2 + W_2 X_2^2 + W_3 X_3^2 + W_4 X_4^2 = \text{exact value of } \int_{-1}^1 x^2 \, dx
  $$
  **Note**: Similarly, additional equations apply for higher-degree polynomials.

---

## 4. Limitations of the Method

1. **Degrees of Freedom**: The number of weights limits the degree of polynomials that can be integrated exactly. 
   - For $n$ weights, exact integration can be achieved up to degree $n-1$ polynomials.
   - Example: With four points ($W_1, W_2, W_3, W_4$), you can integrate exactly up to cubic ($x^3$) functions.

2. **Oscillating Weights**: 
   - When the number of points increases, the weights tend to exhibit wild oscillations (e.g., $\pm 100$, $\pm 500$), leading to large numerical errors.
   - This instability makes the direct approach impractical for high-degree polynomial approximation.

---

## 5. Gaussian Quadrature: A Smarter Strategy

- Instead of arbitrarily selecting points, **Gaussian quadrature** optimally chooses both:
  1. The points $X_1, X_2, \dots, X_n$.
  2. The corresponding weights $W_1, W_2, \dots, W_n$.
  
### Benefits:
- Significantly increases the degree of polynomial that can be integrated exactly for the same number of points.
- If $n$ points are used in Gaussian quadrature, exact integration is achieved for polynomials of degree up to $2n-1$.

---

## 6. Vandermonde Matrix

- **Relevance**: The weights are determined by solving a system of linear equations involving a Vandermonde matrix.
- **Definition**:
  $$
  \begin{bmatrix}
  1 & X_1 & X_1^2 & \cdots & X_1^{n-1} \\
  1 & X_2 & X_2^2 & \cdots & X_2^{n-1} \\
  \vdots & \vdots & \vdots & \ddots & \vdots \\
  1 & X_n & X_n^2 & \cdots & X_n^{n-1}
  \end{bmatrix}
  \begin{bmatrix}
  W_1 \\
  W_2 \\
  \vdots \\
  W_n
  \end{bmatrix}
  =
  \begin{bmatrix}
  \text{exact integral for } f_0(x) \\
  \text{exact integral for } f_1(x) \\
  \vdots \\
  \text{exact integral for } f_{n-1}(x)
  \end{bmatrix}
  $$

- **Application**: This matrix is common in numerical methods like interpolation and Gaussian quadrature.

---

## 7. Practical Challenges

- **High Degree Integration**:
  - While increasing the number of points ($n$) theoretically improves the approximation, the numerical instability of weights makes direct methods unreliable.
- **Alternative**:
  - For practical purposes, simpler rules like the **trapezoid rule** or Gaussian quadrature are preferred to avoid issues with oscillating weights.

---

## 8. Key Takeaway

The goal of numerical integration is to balance:
1. The **accuracy** of integration (in terms of polynomial degree).
2. The **stability** and computational feasibility of the weights.

Gaussian quadrature offers a powerful solution by optimizing both the points and weights to maximize the degree of exactness while maintaining numerical stability.