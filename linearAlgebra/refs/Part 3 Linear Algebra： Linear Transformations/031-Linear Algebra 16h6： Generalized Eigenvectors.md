# Defective Matrices and Generalized Eigenvectors

## Why Are Defective Matrices "Defective"?
- **Defective matrices** are described with a negative term despite not appearing "broken."
- They fail to provide a **basis consisting of eigenvectors**. 
  - This happens because there are **fewer eigenvectors than the dimension of the space**.
  - **Result:** Insufficient eigenvectors to construct a basis.

## Impact of Defective Matrices
- In many cases, defective matrices are just an inconvenience.
- They become a **stumbling block** in situations like solving **linear ordinary differential equations with constant coefficients**.
  
## Completing the Basis with Defective Matrices
- Defective matrices allow for a **natural way of completing the basis** using **generalized eigenvectors**.

---

## 1. Example: A Defective Matrix

Consider a matrix where the **characteristic polynomial** is:
$$
(3 - \lambda)^3
$$

### Properties:
- The eigenvalue $\lambda = 3$ has **algebraic multiplicity** 3.
- To find its **geometric multiplicity**, compute the null space of $A - 3I$:
  - The null space is **one-dimensional**.
  - **Geometric multiplicity** is 1.  
  - Therefore, the eigenvalue has a **defect** of $3 - 1 = 2$.

### Eigenvector for $\lambda = 3$:
- The eigenvector corresponding to $\lambda = 3$ is:
$$
\begin{bmatrix} 1 \\ 1 \\ 1 \end{bmatrix}
$$

### Missing Vectors:
- For a complete basis in $\mathbb{R}^3$, we need **3 linearly independent vectors**, but only have **1 eigenvector** so far.
- **Solution:** Use **generalized eigenvectors** to complete the basis.

---

## 2. Generalized Eigenvectors

### Special Property of Defective Matrices
- A **generalized eigenvector** is a vector that satisfies:
  $$ 
  (A - \lambda I)^k \mathbf{v} = 0 \quad \text{for some } k > 1.
  $$
- Generalized eigenvectors exist **because of a special property of defective matrices**:
  - The eigenvector is not just in the null space of $A - 3I$ but also in its **column space**.

### Step-by-Step Construction
1. **First Generalized Eigenvector**:
   - Solve the system:
     $$ 
     (A - 3I)\mathbf{v}_2 = \mathbf{v}_1, 
     $$
     where $\mathbf{v}_1 = \begin{bmatrix} 1 \\ 1 \\ 1 \end{bmatrix}$ is the eigenvector.
   - The solution is:
     $$ 
     \mathbf{v}_2 = \begin{bmatrix} 0 \\ 0 \\ 1 \end{bmatrix}.
     $$
   - $\mathbf{v}_2$ is linearly independent from $\mathbf{v}_1$.

2. **Second Generalized Eigenvector**:
   - Solve the system:
     $$
     (A - 3I)\mathbf{v}_3 = \mathbf{v}_2,
     $$
     where $\mathbf{v}_2 = \begin{bmatrix} 0 \\ 0 \\ 1 \end{bmatrix}$.
   - The solution is:
     $$ 
     \mathbf{v}_3 = \begin{bmatrix} 0 \\ -\frac{1}{2} \\ -\frac{1}{2} \end{bmatrix}.
     $$
   - $\mathbf{v}_3$ is linearly independent from both $\mathbf{v}_1$ and $\mathbf{v}_2$.

### Result:
The complete basis for $\mathbb{R}^3$ is:
$$
\begin{bmatrix}
\mathbf{v}_1 & \mathbf{v}_2 & \mathbf{v}_3
\end{bmatrix}
=
\begin{bmatrix}
1 & 0 & 0 \\
1 & 0 & -\frac{1}{2} \\
1 & 1 & -\frac{1}{2}
\end{bmatrix}.
$$

---

## 3. Terminology

- $\mathbf{v}_1$: Eigenvector (also called a **generalized vector of rank 1**).
- $\mathbf{v}_2$: Generalized eigenvector of **rank 2**.
- $\mathbf{v}_3$: Generalized eigenvector of **rank 3**.

### Summary of Roles:
- Generalized eigenvectors fill the gaps in the basis caused by the defect of the eigenvalue.
- Each generalized eigenvector is guaranteed to be linearly independent from the previous vectors.

---

## 4. Conclusion: Special Property of Defective Matrices
- Defective matrices inherently allow the existence of generalized eigenvectors.
- Generalized eigenvectors **always exist in sufficient numbers to complete the basis**.
- This special property ensures that systems involving defective matrices can still be solved effectively.