## Infinite Series and Hilbert Spaces

### Finite vs Infinite Series
- In the case of finite series, calculations are **riskless** in terms of convergence:
    - No need to consider **calculus** or **convergence**.
    - It's simply a linear problem, involving a linear fit.

### Behavior of Approximation as $n$ Grows
- Increasing $n$ makes the approximation better:
    - More degrees of freedom lead to closer results.
    - Larger $n$ unequivocally implies better approximations.
- When transitioning to **infinite-dimensional spaces**:
    - **Hilbert spaces** are used to extend linear algebra to infinite cases.
    - Hilbert spaces answer whether approximation continues improving as $n \to \infty$.
    - **Yes**, larger $n$ improves approximations for appropriate series.

### Fourier Series and Convergence
1. **Pointwise Convergence**:
    - For a **continuously periodic function** $f(\theta)$, Fourier series converge pointwise to $f(\theta)$ at continuity points.
    - At discontinuity points, the series converges to the **average** value on either side:
      - $$ \text{Discontinuity Convergence: Average Value} $$

2. **Theory’s Beauty**:
    - Clean and structured:
        - At points of continuity, Fourier decomposition matches the function.
        - At discontinuities, convergence is adjusted but still meaningful.

### Infinite Series and Basis in Hilbert Space
- Shift from finite least squares to decomposition in **Hilbert space**:
    - The basis now contains **infinitely many sinusoidal functions** (sine and cosine).
    - Transition from least squares to:
        - **Classical decomposition** using orthogonal basis.
        - Involves inner products with respect to the orthogonal basis of the Hilbert space.

### Linear Algebra as Driving Logic
- The framework stems from **linear algebra**, not calculus.
  - Focus on basis decomposition.
  - Orthogonality and classical decomposition techniques ensure accurate representations.

---

## Viewing Problems Through Linear Algebra
- **Skill Focus**: Ability to conceptualize problems as linear algebra problems.
- Even partial linear algebra problems demand identifying and imposing linear algebra techniques.
- Universality of approaches applies to:
    - **Tensor calculus**: Imposing tensor frameworks.
    - **Probability** or **Statistics**: Extracting the probability/statistical crux.

---

### Conclusion: Unified Frameworks in Mathematics
- A good mathematical topic teaches the ability to:
    - View **any problem** through its framework.
    - Relate external phenomena to the central principles of the discipline (e.g., linear algebra, tensor calculus, probability/statistics).