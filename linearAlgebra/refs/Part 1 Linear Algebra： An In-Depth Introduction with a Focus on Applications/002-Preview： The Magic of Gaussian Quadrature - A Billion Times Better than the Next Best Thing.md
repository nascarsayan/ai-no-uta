# Gaussian Quadrature and Numerical Integration

## 1. Introduction
Gaussian quadrature is a powerful technique used for numerical integration, allowing us to approximate areas under curves. Named after Carl Friedrich Gauss, this method relies heavily on ideas from **linear algebra** rather than **calculus**, making it a noteworthy example of linear algebra's utility in computation.

## 2. Problem Overview
We aim to compute the area under the curve $y = \cos(x^2)$ from $x = -1$ to $x = 1$. The anti-derivative of $\cos(x^2)$ is not easily obtainable using the fundamental theorem of calculus, so approximate numerical methods are required.

## 3. Numerical Methods for Integration

### 3.1. Rectangle Rule
The Rectangle Rule breaks the interval $[-1, 1]$ into sub-intervals of equal width $h$ and approximates the area using rectangles.

Steps:
1. Divide the interval into $N$ equal portions, each with width $h = \frac{2}{N}$.
2. Compute the area of each rectangle:
   $$
   \text{Area of rectangle} = f(x_{\text{left edge}}) \cdot h
   $$
   where $x_{\text{left edge}}$ is the left edge of the rectangle.
3. Sum the areas to approximate the total:
   $$
   \text{Total Area} = \sum_{i=1}^{N} f(x_i) \cdot h
   $$

**Key Points:**
- Computationally simple.
- The error decreases as $N$ increases (more rectangles).
- Misses small areas due to approximation.

### 3.2. Improving the Rectangle Rule
- **Midpoint Rule**: Use the midpoint of each interval instead of the left edge. Results in more accurate approximations.
- **Trapezoid Rule**: Replace rectangles with trapezoids for better estimation.

### 3.3. Gaussian Quadrature
Gaussian quadrature provides a **much more accurate approximation** by computing the integral using optimal sampling points and weights:
1. **Choose Special Points**: Gaussian quadrature prescribes **non-equally spaced points** $x_i$ within the domain.
2. **Apply Specific Weights**: Multiply the function values at those points by specific weights $w_i$.
3. Sum the weighted values:
   $$
   \text{Area} = \sum_{i=1}^{N} w_i \cdot f(x_i)
   $$

#### Key Features:
- Optimal points and weights are **universal** and can be precomputed.
- Requires fewer evaluations of the function but provides extreme accuracy.
- Relies significantly on linear algebra rather than calculus.

---

## 4. Comparison of Methods

### 4.1. True Value of the Area
Using computational tools like SymPy Gamma, we can evaluate the true area under the curve as:
$$
\text{True Area} = 1.89
$$

### 4.2. Rectangle Rule Estimation
For $N=10$:
- **Approximated Value:** $1.797$
- **Error:** $\text{True Area} - \text{Approximated Value} = 0.01$

### 4.3. Gaussian Quadrature Estimation
For $N=10$ points:
- **Approximated Value:** $1.89$ (accurate to within **one part in a trillion**!)
- **Error:** $\text{True Area} - \text{Approximated Value} = 0.000000...01$ (12 zeros).

---

## 5. Mathematical Insights

### A. Linear Algebra in Gaussian Quadrature
1. **Optimal Points**: Sampling points are derived from solving linear algebra problems related to polynomials (e.g., zeros of Legendre polynomials in specific domains).
2. **Optimal Weights**: Weights $w_i$ are calculated using linear algebra methods that ensure minimal error across a wide class of functions.

### B. Extreme Accuracy
Gaussian Quadrature achieves an **astounding level of accuracy** compared to straightforward rules like rectangles or trapezoids. This accuracy is attributed not only to Gauss's genius but also to the computational power of **linear algebra**.

---

## 6. Conclusion
Gaussian Quadrature:
- Enables evaluating integrals with exceptional precision using minimal effort.
- Demonstrates the power of linear algebra in practical computations.
- For $N=10$ points, it provides results with accuracy surpassing all standard approximation methods by nearly 100 billion times.

This remarkable improvement highlights the strength of **linear algebra** techniques when paired with clever mathematical insights.

