## Special Cases: Eigenvalues and Eigenvectors

In this discussion, we explore situations in which the eigenvalues (and sometimes the eigenvectors) of a matrix are straightforward to determine without using the eigenvalue algorithm. These are insightful examples that improve understanding and have practical applications.

---

### Diagonal Matrices

#### Eigenvalues:
The eigenvalues of a diagonal matrix appear directly on the diagonal of the matrix. E.g., for the diagonal matrix:

$$
A =
\begin{bmatrix}
3 & 0 & 0 \\
0 & 7 & 0 \\
0 & 0 & 8
\end{bmatrix}
$$

The eigenvalues are:
$$
\lambda_1 = 3, \, \lambda_2 = 7, \, \lambda_3 = 8
$$

#### Eigenvectors:
The eigenvectors corresponding to these eigenvalues are straightforward:
- For $\lambda = 3$, the eigenvector is:
  $$
  v_1 = \begin{bmatrix} 1 \\ 0 \\ 0 \end{bmatrix}
  $$
  Explanation: When multiplying $A$ by $v_1$, the result is:
  $$
  A v_1 = \begin{bmatrix} 3 \\ 0 \\ 0 \end{bmatrix} = 3 v_1
  $$

- For $\lambda = 7$, the eigenvector is:
  $$
  v_2 = \begin{bmatrix} 0 \\ 1 \\ 0 \end{bmatrix}
  $$

- For $\lambda = 8$, the eigenvector is:
  $$
  v_3 = \begin{bmatrix} 0 \\ 0 \\ 1 \end{bmatrix}
  $$

Thus, for diagonal matrices:
- The eigenvalues are located on the diagonal.
- Eigenvectors correspond to the standard basis vectors (or "pivot columns") in $\mathbb{R}^n$.

---

### A Question on Diagonal Matrix Order

If the diagonal matrix entries are reordered, such as:

$$
B = 
\begin{bmatrix}
7 & 0 & 0 \\
0 & 8 & 0 \\
0 & 0 & 3
\end{bmatrix}
$$

Do $A$ and $B$ have the same eigenvalues and eigenvectors?

#### Observation:
- Eigenvalues remain the same ($\{3, 7, 8\}$), but the correspondence to eigenvectors changes.
  - In $B$, the eigenvector $\begin{bmatrix} 1 \\ 0 \\ 0 \end{bmatrix}$ now corresponds to $\lambda = 7$, rather than $\lambda = 3$.

#### Conclusion:
While $A$ and $B$ share the same eigenvalues and eigenvectors **individually**, the eigenvalue-eigenvector pairs **differ**. Thus, their "spectra" are considered different.

---

### Spectra and Correspondence

The concept of the "spectrum" of a matrix refers to the collection of eigenvalue-eigenvector pairs. For two matrices to have identical spectra:
1. They must have the same eigenvalues.
2. Corresponding eigenvectors must match their respective eigenvalues in the same way.

In the above example, $A$ and $B$ do not share the same spectrum due to mismatched correspondences.

---

### Outstanding Questions

1. **Identical Spectra:**
   - Is it possible for two distinct matrices to share the same eigenvalues and eigenvectors (i.e., identical spectra)? 
   - This question remains unresolved but will be revisited in the eigenvalue decomposition topic.

2. **Constructing Matrices:**
   - Diagonal matrices simplify the construction of matrices with given eigenvalues and eigenvectors. This insight will serve as a foundation for future studies.