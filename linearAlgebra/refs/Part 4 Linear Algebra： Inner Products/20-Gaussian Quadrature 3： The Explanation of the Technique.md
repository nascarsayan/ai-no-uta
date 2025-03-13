## Gaussian Quadrature

### Privilege to Discuss Gaussian Quadrature

- **A historical context**: Gaussian quadrature is a technique that showcases the brilliance of its discoverer, Gauss. Though Gauss doesn’t receive direct credit for this discussion, we benefit tremendously by exploring this elegant method.
- **Importance**: It beautifully exemplifies how certain mathematical ideas fit together perfectly.

---

### Polynomial Overview

1. **The Setup**:
   - Have a polynomial $P(x)$ of degree up to $2N-1$.
   - Consider the segment $[-1, 1]$. We are free to place $N$ points along this segment.

2. **Goal**:
   - Approximate integrals with these points and associated weights.
   - Achieve exact integration for polynomials up to degree $2N-1$.

---

### Polynomial Division & Orthogonal Polynomials

#### Polynomial Division:
- If dividing a polynomial:
  $$
  \text{Degree of } \frac{\text{(degree } 2N-1 \text{ polynomial)}}{\text{(degree } N \text{ polynomial)}} = N-1
  $$
- For any polynomial $P(x)$:
  $$
  P(x) = Q(x)L_N(x) + R(x)
  $$
  - $Q(x)$: Quotient of degree $\leq N-1$.
  - $R(x)$: Remainder, of degree $\leq N-1$.
  
#### Orthogonality:
- $L_N(x)$ (Legendre polynomial) is orthogonal to any polynomial of degree $< N$ over the interval $[-1, 1]$:
  $$
  \int_{-1}^{1} L_N(x) \cdot R(x) \, dx = 0
  $$
- Consequence: Integral of $P(x)$ is reduced to integrating $R(x)$.

---

### Integration Process and Gaussian Quadrature Scheme

#### Integration of $P(x)$:
- Using orthogonality, the integral decomposes to:
  $$
  \int_{-1}^{1} P(x) \, dx = \int_{-1}^{1} R(x) \, dx
  $$

#### Choosing Gaussian Points and Weights:
1. **Points** ($x_i$): Chosen as the roots of the $N$th Legendre polynomial $L_N(x)$.
   - $L_N(x)$ has $N$ real roots within $[-1, 1]$.
   - Roots are denser near $-1$ and $1$. 
   
2. **Weights** ($w_i$):
   - Calculated such that the approximate integral matches the true integral for polynomials up to degree $2N-1$.

#### Final Quadrature Approximation:
- Gaussian quadrature estimates the integral as:
  $$
  \int_{-1}^{1} f(x) \, dx \approx \sum_{i=1}^N w_i f(x_i)
  $$

- This approximation is **exact** for polynomials of degree $\leq 2N-1$.

---

### Why Gaussian Quadrature is Powerful

1. **Optimal Performance**:
   - Extracts the *maximum possible accuracy* for a given number of points and weights.
   - Unlike simpler methods (e.g., trapezoidal rule), it works “perfectly” for higher degrees of polynomials.

2. **Smoothness**:
   - Weights ($w_i$) are stable, positive, and distributed smoothly (roughly $2/N$ for large $N$).
   - This avoids issues like oscillations in approximations.

3. **Flexibility**:
   - Even functions beyond polynomials are approximated well if they are smooth enough.

---

### Practical Example

- Using 10 points (roots of the 10th Legendre polynomial):
  - Gaussian quadrature can exactly integrate polynomials of degree up to $19$.
  - A smooth function like a cosine wave is very well-approximated by a 19th-degree polynomial. Hence, Gaussian quadrature provides excellent results.

---

### Limitations and Insights

- If a function has features (e.g., many rapid oscillations or discontinuities) that require higher-degree polynomials, Gaussian quadrature may fail.
- The brilliance lies in the elegance of its construction: an insightful compression of numerical integration through the use of orthogonal polynomials.

---

### Broader Perspective

1. **Linear Algebra Foundation**:
   - Integration under Gaussian quadrature is rooted in linear algebra, using orthogonality and projection concepts.

2. **Significance**:
   - As a purely linear algebraic approach (without relying on calculus intricacies), Gaussian quadrature exemplifies the power of mathematical foundations.

3. **The Third Pillar**:
   - Orthogonal polynomials, inner product spaces, and the idea of projection make Gaussian quadrature a pillar of linear algebra.

---

### Final Remarks

- Gaussian quadrature highlights the depth and elegance of Gauss’s insights.
- It is an almost perfect method when applied to the right types of functions and remains widely used in applications due to its precision and efficiency.
