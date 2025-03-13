## Proving Eigenvalue Identity of $A^\top A$ and $AA^\top$

### Objective:
To prove that the two matrices $A^\top A$ and $AA^\top$ have identical eigenvalues.

---

### Key Properties of $A^\top A$ and $AA^\top$:
1. Both matrices are **symmetric**.  
   This means:
   - They have real eigenvalues.
   - Their eigenvectors form an orthogonal basis.

2. The eigenvalues of both $A^\top A$ and $AA^\top$ are **non-negative**.

---

### Strategy for the Proof:
We rely on the **symmetry** of the matrices and a **decomposition** of the matrix $A$.

### Matrix Decomposition:
Assume:
- $A$ is expressed as $A = QS$,  
  where:
  - $Q$ is an orthogonal matrix ($Q^\top = Q^{-1}$),
  - $S$ is a symmetric matrix.

---

### Analysis of $A^\top A$:
The product $A^\top A$ is computed as:

\[
A^\top = S Q^\top
\]

\[
A^\top A = (S Q^\top)(QS) = S (Q^\top Q) S = S^2
\]

Since $Q^\top Q = I$ (orthogonality), the result simplifies to $S^2$.

---

### Analysis of $AA^\top$:
The product $AA^\top$ is computed as:

\[
AA^\top = (QS)(S Q^\top)
\]

Expanding:

\[
AA^\top = Q S^2 Q^\top
\]

---

### Insight:
While $A^\top A = S^2$ and $AA^\top = Q S^2 Q^\top$ are **different matrices**, they are **similar** matrices. 

---

### Similarity Transformation and Eigenvalues:
1. $AA^\top$ is related to $A^\top A$ through the similarity transformation:  
   \[
   AA^\top = Q (A^\top A) Q^\top
   \]

2. Key Property:
   - Matrices related by a similarity transformation have **identical eigenvalues**.
   - Hence, $A^\top A$ and $AA^\top$ share the same eigenvalues.

3. Eigenvectors of $AA^\top$ and $A^\top A$:
   - The eigenvectors of $AA^\top$ are related to those of $A^\top A$ by the orthogonal matrix $Q$.
   - This relationship implies a simple rotation or reflection between the two sets of eigenvectors.

---

### Conclusion:
1. The eigenvalues of $A^\top A$ and $AA^\top$ are identical due to their relationship via a similarity transformation.
2. The proof is complete as soon as this relationship is observed.