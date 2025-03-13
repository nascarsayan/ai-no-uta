## Eigenvalues and Eigenvectors Analysis

### Eigenvalues of the Matrix:
- The sum of each row of the matrix equals $5$, indicating an eigenvalue:
  - $\lambda_1 = 5$
- The eigenvector corresponding to this eigenvalue:
  - $\mathbf{v}_1 = \begin{bmatrix} 1 \\ 1 \\ 1 \end{bmatrix}$
  - Normalization:
    - $$ \mathbf{v}_1^\text{normalized} = \frac{\begin{bmatrix} 1 \\ 1 \\ 1 \end{bmatrix}}{\sqrt{3}} $$

- The second eigenvalue ($\lambda_2$) arises due to the repetition of columns in the matrix:
  - $\lambda_2 = 0$
- The eigenvector corresponding to $\lambda_2$:
  - $\mathbf{v}_2 = \begin{bmatrix} 0 \\ 1 \\ -1 \end{bmatrix}$
  
- The third eigenvalue ($\lambda_3$):
  - Using the trace of the matrix:
    $$
    \text{Sum of eigenvalues} = \text{Trace of the matrix}
    $$
    $\lambda_3 = 2$
- Finding the third eigenvector:
  - Orthogonal to both $\mathbf{v}_1$ and $\mathbf{v}_2$
  - Trick: Determinant method or cross-product trick.

### Finding the Third Eigenvector:
- Orthogonality condition:
  - The eigenvector corresponding to $\lambda_3$ must be orthogonal to $\mathbf{v}_1$ and $\mathbf{v}_2$.
- Third eigenvector derived as:
  - $\mathbf{v}_3 = \begin{bmatrix} 2 \\ -1 \\ -1 \end{bmatrix}$
- Normalization involves computing the length:
  - Length: 
    $$
    \|\mathbf{v}_3\| = \sqrt{2^2 + (-1)^2 + (-1)^2} = \sqrt{6}
    $$
  - Normalized eigenvector:
    $$ \mathbf{v}_3^\text{normalized} = \frac{\begin{bmatrix} 2 \\ -1 \\ -1 \end{bmatrix}}{\sqrt{6}} $$

### Observations and Takeaways:
- This method demonstrates the ability to find eigenvectors (like $\mathbf{v}_3$) without solving for the null space of the matrix explicitly.
- Key tricks include using:
  - Orthogonality conditions among eigenvectors.
  - Determinants or cross-products to simplify derivations.

### Insights from Linear Algebra:
- Linear algebra reveals simple structures hidden in seemingly complicated problems.
- The decomposition into eigenvalues and eigenvectors illustrates the matrix's inherent simplicity.
  - Without this insight, identifying eigenvalues and eigenvectors would seem like an overwhelmingly difficult problem.
  - Equipped with the right tools and perspective, it becomes straightforward and intuitive.