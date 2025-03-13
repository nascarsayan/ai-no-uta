## Matrix Algebra: The Cayley-Hamilton Theorem

### Introduction
- **Theorem**: Every matrix satisfies its own characteristic equation.
- **Relevance**:
  - The theorem has conceptual significance despite limited practical application in engineering.
  - Widely regarded for its sheer beauty in linear algebra.

---

### Characteristic Polynomial
1. **Definition**:
   - The characteristic polynomial of a matrix $A$ is defined as:  
     $$\text{det}(A - \lambda I)$$
     where $\lambda$ represents an eigenvalue.

2. **Alternative Definition**:
   - To avoid a leading negative sign in odd-dimension matrices, we can define it as:  
     $$\text{det}(\lambda I - A).$$

3. **Implication**:
   - Both definitions produce equivalent results because multiplying the equation by $-1$ does not alter the roots.

---

### Statement of the Theorem
1. **For a given 3x3 matrix $A$,**  
   - Plugging $A$ into its characteristic polynomial yields the zero matrix.  
   - Formally:  
     $$A^3 + 6A^2 + 11A + 6I = 0,$$  
     where $I$ is the identity matrix.

2. **What it means**:
   - This matrix relation (derived from the characteristic polynomial) evaluates to the zero matrix when substituted.

---

### Proof Outline (Case: Matrices with Real Eigenvalues)

#### Assumptions:
- Matrix $A$ has a **complete set** of eigenvalues and linearly independent eigenvectors.
- Eigenvectors form a basis of the space.
  
#### Proof Steps:
1. **Property of Eigenvectors**:
   - For an eigenvector $v_1$ corresponding to eigenvalue $\lambda_1$:  
     $$A^k v_1 = \lambda_1^k v_1,$$  
     for any positive integer $k$.

2. **Expanding the Polynomial**:
   - Substituting $A^k v_1$ into the polynomial representation:  
     $$p(A)v_1 = (\lambda_1^3 + 6\lambda_1^2 + 11\lambda_1 + 6)v_1.$$

3. **Eigenvalue Condition**:
   - By definition, $\lambda_1$ is a root of the characteristic polynomial $p(\lambda)$:  
     $$\lambda_1^3 + 6\lambda_1^2 + 11\lambda_1 + 6 = 0.$$

4. **Conclusion**:
   - Thus, $p(A)v_1 = 0$, and since eigenvectors span the space, $p(A)$ is the zero matrix.

---

### Special Cases & Examples

#### Defective Matrices
- Matrices lacking a full set of linearly independent eigenvectors still satisfy the theorem:
  - Example: A matrix with repeated eigenvalues $\lambda_1 = 2$, characteristic polynomial:  
    $$\lambda^2 - 4\lambda + 4.$$
  - Compute powers of $A$ and verify:  
    $$A^2 - 4A + 4I = 0.$$

#### Complex Eigenvalues
- Matrices with no real eigenvalues also satisfy the theorem.
  - Example:
    - Matrix with characteristic polynomial:  
      $$\lambda^2 - 7\lambda + 22.$$
    - Compute powers of $A$ and verify:  
      $$A^2 - 7A + 22I = 0.$$

---

### Partial Proofs Summary
1. **Full Set of Real Eigenvalues**:
   - Proof provided using eigenvector basis.

2. **Defective Matrices and Complex Eigenvalues**:
   - Verified through computational examples.
   - Complete formal proofs saved for later discussion.

---

### Insights
- **Key Idea**:
  - If $p(A)v = 0$ for eigenvectors $v$ spanning the space, then $p(A)$ must be the zero matrix.
- **Broader Implications**:
  - The Cayley-Hamilton theorem holds universally for all matrices, regardless of real or complex eigenvalues, or defectiveness.