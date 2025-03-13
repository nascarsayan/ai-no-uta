## Symmetric Matrices and LDU Decomposition

### Symmetry in LDU Decomposition

1. **Introduction**:  
   - Symmetric matrices have special properties with respect to LDU decomposition.
   - Symmetric matrices are more valuable than general matrices in LDU decomposition, especially when compared to eigenvalue decomposition.

2. **Gaussian Elimination Insight**:  
   - Matrix $U$ is obtained by Gaussian elimination on matrix $A$.  
   - Matrix $L$ contains the inverses of the Gaussian elimination steps, usually with 1's on its diagonal.

### Factoring Pivots in LDU Decomposition

1. **Pivot Factorization**:  
   - If pivots are factored so $U$ has 1's on the diagonal, the process leads to **LDU decomposition**:
     
     $$
     A = LDU
     $$

   - Here:
     - $L$: Lower triangular matrix with ones on the diagonal.
     - $D$: Diagonal matrix containing the pivots.
     - $U$: Upper triangular matrix with ones on the diagonal.

2. **Constructing $U$**:  
   - Rows of $U$ are derived by dividing rows from the original matrix $U$ by the pivots (diagonal values).  

#### Example Adjustment:
Let matrix $U$ be adjusted row by row:  
   - Divide row 1 by pivot, row 2 by its pivot, etc., to ensure 1's on the diagonal.

### Symmetry Observation

1. **Special Relation**:  
   - For symmetric matrices:  

     $$
     U = L^\top
     $$

2. **Reason for Symmetry**:  
   - Symmetry arises because the transpose of $LDU$ matches its original form:
     
     $$
     A = LDL^\top
     $$

   - This is typical for symmetric matrices.

---

## Comparing LDU and Eigenvalue Decomposition

1. **Similarity in Form**:
   - Both decompositions share structural similarity:
     
     $$
     A = LDL^\top
     \quad \text{and} \quad
     A = X \Lambda X^\top
     $$

   - Both involve:
     - A factor matrix ($L$ or $X$).
     - A diagonal matrix ($D$ or $\Lambda$).
     - A transpose of the factor matrix.

2. **Key Differences**:  
   - **LDU Decomposition**:
     - $L$: Lower triangular matrix.
     - $U$: Upper triangular matrix as the transpose of $L$.
   - **Eigenvalue Decomposition**:
     - $X$: Orthogonal matrix (eigenvectors).
     - $X^{-1} = X^\top$ (orthogonal matrices inverse equal transpose).

---

## Computational Perspective

1. **Ease of Computation**:
   - Pivots (from LDU) are computationally simpler to obtain, even for large matrices.  
   - Eigenvalues (from eigenvalue decomposition) are computationally intensive.

2. **Unrelated in Practice**:  
   - LDU and eigenvalue decompositions are fundamentally disconnected:
     - Diagonal entries in $D$ (pivots) differ from $\Lambda$ (eigenvalues).  
     - A relation would imply a computational shortcut to eigenvalues—impossible due to theoretical limitations.

### Sylvester Inertia Theorem

1. **Diagonal Entry Consistency**:
   - Positive, negative, and zero counts on the diagonal of $D$ in LDU decomposition match the counts on $\Lambda$ in eigenvalue decomposition.

2. **Insight**:  
   - Despite differences, they share the same **inertia quantities**:
     
     - Count of positive eigenvalues/pivots.
     - Count of negative eigenvalues/pivots.
     - Count of zero eigenvalues/pivots.

3. **Theorem Name**:  
   - **Sylvester's Inertia Theorem**.

---

## Future Directions

1. **Focusing on Positive Pivots**:  
   - Next, consider matrices where all pivots are positive.
   - Leads to **Cholesky Decomposition**:
     
     $$
     A = L\sqrt{D} \cdot \sqrt{D}L^\top
     $$

2. **Utility of Cholesky Decomposition**:  
   - Useful for symmetric positive-definite matrices, widely used in numerical computing.

