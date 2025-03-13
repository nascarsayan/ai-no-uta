## 1. Proof of Orthogonal Matrix Consistency from Decomposition

### Key Observation
- **Fact Experimentally Discovered**: When decomposing a matrix as a product of:
  - An orthogonal matrix ($Q$) and a symmetric matrix ($S$), or  
  - A symmetric matrix followed by an orthogonal matrix,  
    **the resulting orthogonal matrices are the same.**
- **Surprising Insight**: This holds true even though matrix multiplication is not commutative (i.e., $AB \neq BA$ in general).

---

### Proof Based on Singular Value Decomposition (SVD)

#### Recall: Singular Value Decomposition
The singular value decomposition (SVD) of a matrix $A$ is given by:
$$
A = U \Sigma V^\top
$$
where:
- $U$ and $V$ are orthogonal matrices.
- $\Sigma$ is a diagonal matrix containing the singular values of $A$.

#### Conversion from SVD to $QS$ Decompositions
The SVD serves as a starting point for deriving:
1. Decomposition into $Q_1 S_1$ form.
2. Decomposition into $S_2 Q_2$ form.

---

#### **From SVD to $Q_1 S_1$**
1. Extract $V$ from $U \Sigma V^\top$ in $A$:
   $$ 
   A = Q_1 S_1 = (UV^\top)(V \Sigma V^\top)
   $$
   where:
   - $Q_1 = UV^\top$ (an orthogonal matrix),
   - $S_1 = V \Sigma V^\top$ (a symmetric matrix).

2. Key steps:
    - $V$ is re-grouped with $\Sigma$ and $V^\top$ to form $S_1$.

---

#### **From SVD to $S_2 Q_2$**
1. Extract $U$ instead of $V$:
   $$ 
   A = S_2 Q_2 = (U \Sigma U^\top)(UV^\top)
   $$
   where:
   - $S_2 = U \Sigma U^\top$ (a symmetric matrix),
   - $Q_2 = UV^\top$ (an orthogonal matrix).

2. Key steps:
    - The diagonal $\Sigma$ is grouped with $U$ to form $S_2$ while separating $Q_2$.

---

### Key Result: $Q_1 = Q_2$
- From both decomposition paths, the orthogonal matrix eventually resolves to the same $Q$:
  - $Q_1 = UV^\top$
  - $Q_2 = UV^\top$
- **Conclusion**: $Q_1 = Q_2$.

---

### Intuition Behind Symmetric Matrices
- The grouping naturally forms symmetric matrices:
  - Symmetric structure arises due to $X^\top X$ or $Y^\top Y$ terms.

---

### Verification of Decompositions
1. **Identity Matrix Approach**:
   $$ 
   IX = X^\top X \quad \text{or} \quad Y^\top Y = I
   $$
   - Inserting the identity matrix shows consistent factorization to $QS$ and $SQ$ forms equivalently.

---

### Conclusion
- The initial unexpected finding (experimental) turns out to align with theoretical properties derived from the SVD.
- The **singular value decomposition (SVD)** serves as the central tool for understanding the consistency between the two decompositions.
