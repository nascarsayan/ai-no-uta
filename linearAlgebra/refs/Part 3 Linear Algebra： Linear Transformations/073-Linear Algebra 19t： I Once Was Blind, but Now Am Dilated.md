# Structured Notes: Transformation of Dilation and Eigen Analysis

## 1. Introduction  
- **Topic**: Analyze the dilation transformation.
- The transformation makes it difficult to guess eigenvalues and eigenvectors directly.
- Using component spaces simplifies finding eigenvalues and eigenvectors.

---

## 2. Basis Representation  
- **Goal**: Represent the linear transformation using a matrix with respect to chosen bases.
- Use the **standard basis** for the space of polynomials.

### Constructing the Matrix:
- Transformation involves plugging in a specific polynomial basis:  
   Transformation formula: Replace $x$ in the polynomial with $2x - 1$.

#### Example: Basis and Transformed Columns  
1. **Basis Element 1 (Constant Polynomial)**  
   $P_1(x) = 1$  
   Transformation of $P_1$:  
   $\text{Output} = 1$ (no $x$ term involved).  
   Decomposition with respect to basis: $[1, 0, 0]$.  
   First column of the matrix: $[1, 0, 0]$.

2. **Basis Element $x$**  
   $P_2(x) = x$  
   Transformation of $P_2$:  
   $\text{Output} = 2x - 1$.  
   Decomposition with respect to basis: $[-1, 2, 0]$.  
   Second column of the matrix: $[-1, 2, 0]$.

3. **Basis Element $x^2$**  
   $P_3(x) = x^2$  
   Transformation of $P_3$:  
   $\text{Output} = (2x - 1)^2 = 4x^2 - 4x + 1$.  
   Decomposition with respect to basis: $[1, -4, 4]$.  
   Third column of the matrix: $[1, -4, 4]$.  

### Resultant Matrix:
$$
\begin{bmatrix}
1 & -1 & 1 \\
0 & 2 & -4 \\
0 & 0 & 4
\end{bmatrix}
$$

---

## 3. Analysis of the Matrix  
- **Eigenvalue Algorithm**: Study the matrix to compute eigenvalues and eigenvectors.  
- Observations:  
  - Upper triangular matrix: Eigenvalues appear on the diagonal.  

### Eigenvalues:  
- $\lambda_1 = 1$, $\lambda_2 = 2$, $\lambda_3 = 4$

---

## 4. Eigenvectors (Component Space Analysis)
### Eigenvalues and their Eigenvectors:  
1. **Eigenvalue $\lambda_1 = 1$:**
   - Null space solution gives $V_1 = [1, 0, 0]$.  
   - **Corresponding Eigenvector**: Constant polynomial $P_1(x) = 1$.  

2. **Eigenvalue $\lambda_2 = 2$:**
   - Null space solution gives $V_2 = [1, -1, 0]$.  
   - **Corresponding Eigenvector**: Polynomial $P_2(x) = x - 1$.  

3. **Eigenvalue $\lambda_3 = 4$:**
   - Null space solution gives $V_3 = [1, -2, 1]$.  
   - **Corresponding Eigenvector**: Polynomial $P_3(x) = x^2 - 2x + 1$.  

---

## 5. Patterns in Eigenfunctions
- Each successive eigenfunction reflects powers of $(x - 1)$.
  - $\lambda_2$ → $P_2(x) = (x - 1)$  
  - $\lambda_3$ → $P_3(x) = (x - 1)^2$  
  - Extension: For higher orders, eigenfunctions become $(x - 1)^n$.

---

## 6. Higher-Order Transformation  
- For cubic polynomials, eigenvalues extend as powers of $2$:  
  $\lambda_4 = 8$, $\lambda_5 = 16$, $\dots$.  
- Eigenfunctions follow the pattern $(x - 1)^n$.

---

## 7. Conclusion  
- **Power of Component Spaces**:  
  - Facilitated finding eigenvalues and eigenvectors for the dilation transformation quickly.  
  - Helped reveal clear patterns in eigenfunctions.  
- Pattern: Eigenvalues correspond to powers of $2$, and eigenfunctions are $(x - 1)^n$ for polynomial basis elements.

---
