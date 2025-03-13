## Similarity Transformation and Properties

### 1. Eigenvalues and Eigenvectors under Powers of a Matrix

- **Key Insight**:  
  The eigenvectors of $A^n$ are **the same** as the eigenvectors of $A$. The eigenvalues of $A^n$ are the eigenvalues of $A$ **raised to the $n$th power**.  

- **Works for All $n$**:  
  This rule holds for all integer powers of $n$ (positive and negative).

---

### 2. Similarity Transformation

#### Definition:
For a given invertible matrix $X$, the similarity transformation of a square matrix $A$ can be defined as:

$$
B = XAX^{-1}
$$

#### Properties of Similar Matrices:
- **Behavior**:  
  $A$ and $B$ are **not the same** matrix, but they are **similar** in many aspects.
- **Eigenvalues**:  
  $A$ and $B$ share the same eigenvalues.
- **Eigenvectors Relationship**:  
  The eigenvectors of $A$ and $B$ are related via the transformation matrix $X$.  

#### Reasoning:
Matrices generally do not commute, hence $X$ and $X^{-1}$ do not simply "cancel out" in $B = XAX^{-1}$.  

---

### 3. Analysis of $B$'s Eigenvalues and Eigenvectors

#### Setup:
- Let $\lambda$ be an eigenvalue of $A$, and let $\mathbf{v}$ be the corresponding eigenvector such that:
  $$
  A \mathbf{v} = \lambda \mathbf{v}.
  $$

#### Variable Substitution:
- Define $\mathbf{u}$ such that $\mathbf{u} = X \mathbf{v}$, implying $\mathbf{v} = X^{-1} \mathbf{u}$.

#### Computation:
- Using the expression for $B = XAX^{-1}$, consider:
  $$
  B \mathbf{u} = X A X^{-1} \mathbf{u}.
  $$
- Substitute $\mathbf{u} = X \mathbf{v}$ into $X^{-1} \mathbf{u} = \mathbf{v}$:
  $$
  B \mathbf{u} = X A \mathbf{v} = X (\lambda \mathbf{v}) = \lambda (X \mathbf{v}) = \lambda \mathbf{u}.
  $$

#### Conclusion:
- $B \mathbf{u} = \lambda \mathbf{u}$ shows that $\lambda$ is an eigenvalue of $B$, and $\mathbf{u}$ is the corresponding eigenvector.  

---

### 4. Summary of Similarity Transformations

**Important Results:**
1. Matrices $A$ and $B = XAX^{-1}$ have:
   - Identical eigenvalues.
   - Eigenvectors related via the transformation matrix $X$: $\mathbf{u} = X \mathbf{v}$.

2. **Terminology**:  
   - The process is called a **similarity transformation**.
   - Matrices related by similarity transformations are structurally tied together.

**Applications**:
Similarity transformations are pivotal in linear algebra, particularly in studying:
- **Eigenvalues and eigenvectors**.
- **Eigenvalue decomposition**.