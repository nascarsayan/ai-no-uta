## Eigenvalues and Eigenvectors for Powers and Inverses of a Matrix

### Key Question:
Given the eigenvalues and eigenvectors of matrix $A$, determine:
- The eigenvalues and eigenvectors of $A^k$ (for powers of $A$).
- The eigenvalues and eigenvectors of $A^{-1}$ (for the inverse of $A$).

---

### The Eigenvalue Equation:

The eigenvalue equation for a matrix $A$ is given by:

$$
A v = \lambda v
$$

Here:
- $v$ is the eigenvector.
- $\lambda$ is the eigenvalue.

---

### 1. Eigenvalues and Eigenvectors of $A^2$

Starting with the eigenvalue equation:

$$
A v = \lambda v
$$

Multiply both sides by $A$:

$$
A (A v) = A (\lambda v)
$$

The left-hand side becomes:

$$
A^2 v
$$

The right-hand side becomes:

$$
\lambda (A v) = \lambda (\lambda v) = \lambda^2 v
$$

Thus, we have:

$$
A^2 v = \lambda^2 v
$$

#### Interpretation:
- $v$ remains an eigenvector of $A^2$.
- The corresponding eigenvalues of $A^2$ are the squares of the eigenvalues of $A$.

---

### 2. Eigenvalues and Eigenvectors of $A^{-1}$

To explore $A^{-1}$, assume $A$ is invertible (i.e., no eigenvalues are zero).

Start with the eigenvalue equation:

$$
A v = \lambda v
$$

Multiply both sides by $A^{-1}$:

$$
A^{-1} (A v) = A^{-1} (\lambda v)
$$

The left-hand side becomes:

$$
A^{-1} A v = I v = v
$$

The right-hand side simplifies to:

$$
\lambda (A^{-1} v)
$$

Switch sides and divide through by $\lambda$:

$$
A^{-1} v = \frac{1}{\lambda} v
$$

#### Interpretation:
- $v$ remains an eigenvector of $A^{-1}$.
- The eigenvalues of $A^{-1}$ are the reciprocals of the eigenvalues of $A$, assuming $\lambda \neq 0$.

---

### 3. Generalization to $A^k$ ($k$ as any integer)

The eigenvalue equation for $A$ is:

$$
A v = \lambda v
$$

Raise both sides to the $k$th power:

$$
A^k v = \lambda^k v
$$

#### Interpretation:
- $v$ remains an eigenvector of $A^k$ for all integer powers of $k$.
- The eigenvalues of $A^k$ are $\lambda^k$, where $\lambda$ are the eigenvalues of $A$.

This holds for:
- Positive powers ($k > 0$).
- Negative powers ($k < 0$), such as $A^{-k}$, where the eigenvalues are $(1/\lambda)^k$.

---

### Applying to Any Integer Power $k$

1. For $k = 2$, the eigenvalues become $\lambda^2$.
2. For $k = -1$, the eigenvalues become $1/\lambda$.
3. For $k = -5$ (example):
   - The matrix is $A^{-5} = (A^{-1})^5$.
   - The eigenvalues are $(1/\lambda)^5 = \lambda^{-5}$.

---

### Key Observations:
1. The eigenvectors of $A^k$ (or its inverse) are the same as the eigenvectors of $A$.
2. The eigenvalues of $A^k$ are $\lambda^k$, and for negative powers, they are $\lambda^{-k}$.
3. This relationship works for all integer powers of $A$.
4. Matrix powers ($A^k$) obey similar rules to powers of scalars in terms of eigenvalues and eigenvectors. 

---

### Recap of Rules:
- If $A v = \lambda v$, then $A^k v = \lambda^k v$.
- If $A$ is invertible, $A^{-1} v = \frac{1}{\lambda} v$.
- The eigenvalues of $A^k$ are $\lambda^k$, and the eigenvectors are unchanged.