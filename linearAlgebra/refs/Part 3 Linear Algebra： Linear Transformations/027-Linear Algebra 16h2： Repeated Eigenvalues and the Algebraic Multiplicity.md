## Repeated Eigenvalues and Their Multiplicities

### Geometric and Algebraic Multiplicities

- **Geometric Multiplicity**: Previously introduced in the context of repeated eigenvalues from a geometric point of view.
- **Algebraic Multiplicity**: This video explores repeated eigenvalues from the **algebraic point of view** using the standard algorithm.

### Transformation Represented by Matrix in $\mathbb{R}^3$

1. **Matrix setup**: A matrix transformation in $\mathbb{R}^3$.
2. **Characteristic Polynomial**:
   - Subtract $\lambda$ from the diagonal.
   - Evaluate the determinant of the resulting matrix.

### Construction of the Characteristic Polynomial

The determinant of the matrix simplifies into:

$$
(3 - \lambda) \cdot \text{det} \begin{bmatrix} 
    0 & 4 \\ 
    4 & 1 - \lambda 
\end{bmatrix}
$$

Expanding this determinant gives:

$$
(3 - \lambda) \cdot \left( \lambda^2 - 5\lambda + 6 \right)
$$

This is the characteristic polynomial of the matrix.

### Roots of the Polynomial

To solve the characteristic polynomial, observe:

1. **First root**:
   $$
   3 - \lambda = 0 \implies \lambda_1 = 3
   $$
   
2. **Remaining roots**:
   From $\lambda^2 - 5\lambda + 6 = 0$, two roots satisfy:
   - **Sum**: $2 + 3 = 5$
   - **Product**: $2 \cdot 3 = 6$
   
   Thus, $\lambda_2 = 2$ and $\lambda_3 = 3$.

### Properties of the Roots

- **Multiplicity**:
  - The eigenvalue $\lambda = 3$ appears *twice* in the characteristic polynomial (a **double root**).
  - Algebraic multiplicity is the **number of times** an eigenvalue occurs.
- **Eigenvalues**:
  - $2$, with **algebraic multiplicity of 1**.
  - $3$, with **algebraic multiplicity of 2** (repeated).

### Summary of Terms

1. **Geometric Multiplicity**: The **dimension** of the eigenspace associated with an eigenvalue.
2. **Algebraic Multiplicity**: The number of times an eigenvalue appears as a root of the characteristic polynomial.

### An Intriguing Question

- **Does Geometric Multiplicity Equal Algebraic Multiplicity**?
  - This question will be further explored in the next video using this example.