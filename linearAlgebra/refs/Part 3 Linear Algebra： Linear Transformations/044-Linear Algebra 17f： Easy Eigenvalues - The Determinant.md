## Trace, Determinant, $\lambda$ and $\mathbf{v}$ of Matrices

### Trace and Eigenvalues  
- **Trace** helps determine an eigenvalue $\lambda$ because:
    - The sum of all eigenvalues of the matrix equals the trace of the matrix.
    - Known $\lambda$ values can work with the trace to find the remaining $\lambda$.

### Determinant and Eigenvalues  
- **Determinant** relates to eigenvalues since:
    - The product of all eigenvalues equals the determinant.
    - Known $\lambda$ values can work with the determinant to find the remaining $\lambda$.

    Limitations:
    - Determinants are harder to compute than traces (trace = sum of diagonal entries).
    - If one $\lambda = 0$, the determinant becomes zero, offering no additional information.

### A Case Study: Combining Trace and Determinant  
- Both trace and determinant can be combined to find missing eigenvalues in certain situations.

#### Example Matrix:
The example matrix has the following structure:
$$
\begin{bmatrix} 
4 & -3 & 0 \\ 
-3 & 4 & 0 \\ 
0 & 0 & 4 
\end{bmatrix}
$$

- **Trace**: Sum of diagonal entries gives 4 + 4 + 4 = 12.
- **Determinant**: Computed from known methods for $3 \times 3$ matrices; here, it equals $-36$.  

#### Eigenvalue Computation:
1. One eigenvalue $\lambda = 4$ is known, with the eigenvector:
   $$
   \mathbf{v} = \begin{bmatrix} 0 \\ 1 \\ 0 \end{bmatrix}
   $$

2. Remaining eigenvalues:
    - Their sum is derived from the trace: $\lambda_1 + \lambda_2 + \lambda_3 = 12$, so $\lambda_2 + \lambda_3 = 8$.
    - Their product is derived from the determinant: $\lambda_1 \cdot \lambda_2 \cdot \lambda_3 = -36$, so $4 \cdot \lambda_2 \cdot \lambda_3 = -36$ implies $\lambda_2 \cdot \lambda_3 = -9$.

    - We solve the system:
        $$
        x + y = 8 \quad \text{and} \quad x \cdot y = -9.
        $$

        Using the quadratic relation $x^2 - 8x - 9 = 0$, the solutions are:
        $$
        \lambda_2 = 3, \quad \lambda_3 = -3.
        $$

#### Eigenvectors:
1. For $\lambda_2 = 3$, solve $\mathbf{A} - 3\mathbf{I}$:
    $$
    \begin{bmatrix} 4-3 & -3 & 0 \\ -3 & 4-3 & 0 \\ 0 & 0 & 4-3 \end{bmatrix}
    =
    \begin{bmatrix} 1 & -3 & 0 \\ -3 & 1 & 0 \\ 0 & 0 & 1 \end{bmatrix}
    $$

    Null space leads to eigenvector:
    $$
    \mathbf{v}_2 = \begin{bmatrix} 1 \\ 3 \\ 0 \end{bmatrix}.
    $$

2. For $\lambda_3 = -3$, solve $\mathbf{A} - (-3)\mathbf{I}$:
    $$
    \begin{bmatrix} 4+3 & -3 & 0 \\ -3 & 4+3 & 0 \\ 0 & 0 & 4+3 \end{bmatrix}
    =
    \begin{bmatrix} 7 & -3 & 0 \\ -3 & 7 & 0 \\ 0 & 0 & 7 \end{bmatrix}
    $$

    Null space leads to eigenvector:
    $$
    \mathbf{v}_3 = \begin{bmatrix} 1 \\ -3 \\ 0 \end{bmatrix}.
    $$

### Summary:
- Eigenvalues for the matrix are:
    $$
    \lambda_1 = 4, \quad \lambda_2 = 3, \quad \lambda_3 = -3.
    $$
- Eigenvectors are:
    $$
    \mathbf{v}_1 = \begin{bmatrix} 0 \\ 1 \\ 0 \end{bmatrix}, \quad 
    \mathbf{v}_2 = \begin{bmatrix} 1 \\ 3 \\ 0 \end{bmatrix}, \quad 
    \mathbf{v}_3 = \begin{bmatrix} 1 \\ -3 \\ 0 \end{bmatrix}.
    $$

### Conclusion:
- Trace and determinant together can break down eigenvalue-eigenvector problems effectively.
- Determinants are practically challenging to compute, but conceptually valuable in such situations.