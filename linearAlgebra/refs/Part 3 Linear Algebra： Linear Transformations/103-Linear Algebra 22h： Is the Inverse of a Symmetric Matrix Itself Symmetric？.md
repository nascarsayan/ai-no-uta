## Symmetric and Invertible Matrices

### Question
If the matrix $S$ is symmetric and invertible, is its inverse necessarily symmetric as well?

### Answer
**Yes**, the inverse of a symmetric matrix is also symmetric. The key to this result lies in the eigenvalue decomposition.

---

### Eigenvalue Decomposition of a Symmetric Matrix

For a symmetric matrix $S$, we can write its eigenvalue decomposition as:

$$
S = X \Lambda X^\top
$$

where:
- $X$ is the matrix of eigenvectors (orthogonal and can be chosen orthonormal),
- $\Lambda$ is the diagonal matrix of eigenvalues,
- $X^\top$ is the transpose of $X$ (since $X$ is orthogonal, $X^{-1} = X^\top$).

---

### Inverse of a Symmetric Matrix

The inverse of $S$ can be expressed as:

$$
S^{-1} = X \Lambda^{-1} X^\top
$$

where $\Lambda^{-1}$ is the diagonal matrix with the reciprocals of the eigenvalues of $S$.

---

### Symmetry of the Inverse

To check if $S^{-1}$ is symmetric, we compute its transpose:

$$
(S^{-1})^\top = \left(X \Lambda^{-1} X^\top \right)^\top
$$

Using the property of transpose, the order of the terms is reversed, and each term is transposed:

$$
(S^{-1})^\top = X^\top ( \Lambda^{-1} )^\top X
$$

- $X^\top$ transposed is $X$ (since $X$ is orthogonal),
- $\Lambda^{-1}$ is a diagonal matrix, so its transpose is itself.

Thus:

$$
(S^{-1})^\top = X \Lambda^{-1} X^\top = S^{-1}
$$

Since $(S^{-1})^\top = S^{-1}$, the inverse of $S$ is symmetric.

---

### Key Takeaways
1. Eigenvalue decomposition for symmetric matrices allows us to express $S = X \Lambda X^\top$.
2. The eigenvectors form an orthogonal matrix $X$, with $X^{-1} = X^\top$.
3. The inverse of a symmetric matrix is symmetric because transposing the decomposition returns the original form of $S^{-1}$.

Hence, **the inverse of a symmetric matrix is necessarily symmetric.**