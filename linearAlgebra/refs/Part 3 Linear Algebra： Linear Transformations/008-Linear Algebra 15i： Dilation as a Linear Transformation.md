```markdown
## Dilation Transformation

### Introduction
- Dilation is an interesting transformation:
  - It's unlike anything commonly encountered.
  - It has significant importance in applications like **wavelet theory**, which is a critical area in **signal processing**.
  - Gilbert Strang has applied linear algebra concepts to wavelet theory, making dilation a topic of interest in linear algebra.

- The discussion on dilation will highlight:
  - Its linear nature.
  - Motivation for developing robust algorithms to find eigenvalues and eigenfunctions.

---

### Definition of Dilation
- **Notation**: Denoted by $D$, dilation operates on a function $f(x)$ by inviting a substitution operation.

- **Example Rule**: Wherever $x$ is seen, replace it with $2x - 1$.  
  This is the result or "image" of the function $f(x)$ after applying $D$.

---

### Examples of Dilation

#### 1. Dilation applied to $f(x) = x^2$:
   - Substitution: Replace $x$ with $2x - 1$.
   - Computation:
     $$
     D(x^2) = (2x - 1)^2 = 4x^2 - 4x + 1
     $$
   - Result: A simple function $x^2$ transforms into a more complicated function.

#### 2. Dilation applied to $f(x) = x - 1$:
   - Substitution: Replace $x$ with $2x - 1$.
   - Computation:
     $$
     D(x - 1) = 2x - 1 - 1 = 2x - 2
     $$
   - **Observation**:  
     The function $x - 1$ becomes $2(x - 1)$.  
     This means $x - 1$ is an eigenfunction and $2$ is the corresponding eigenvalue.

#### 3. Dilation applied to $f(x) = x^2 + x - 1$:
   - Substitution: Replace $x$ with $2x - 1$.
   - Computation:
     - For $x^2$:  
       $$(2x - 1)^2 = 4x^2 - 4x + 1$$
     - For $x$:  
       $$2x - 1$$
     - Final Result: Combine terms.
     $$
     D(x^2 + x - 1) = 4x^2 - 4x + 1 + 2x - 1 - 1 = 4x^2 - 2x - 1
     $$
   - **Linear Property Confirmation**:  
     Adding transformations separately or in combination produces the same result, showcasing the linearity of dilation.

---

### Observations on Dilation
1. **Linearity**:
   - Dilation is a **linear transformation**.
   - This means:
     - $D(f(x) + g(x)) = D(f(x)) + D(g(x))$
     - $D(c \cdot f(x)) = c \cdot D(f(x))$ for any constant $c$.

2. **Eigenvalues and Eigenfunctions**:
   - Identified eigenfunction: $f(x) = x - 1$ with eigenvalue $2$.
   - Finding additional eigenfunctions is challenging:
     - Trial and error is an option but lacks systematic robustness.
     - A robust algorithm is desirable for discovering eigenvalues and eigenfunctions systematically.

---

### The Need for a Robust Approach
- The goal is to develop a **robust theory of eigenvalues and eigenfunctions**:
  - Applicable to any transformation.
  - Systematic, allowing for easier determination of eigenvalues and eigenfunctions.
  - Analogous to how Gaussian elimination works to determine column relationships in linear systems.

### Conclusion
- Dilation serves as motivation to explore robust eigenvalue and eigenfunction discovery methods, emphasizing both its theoretical and practical importance in linear algebra.
```