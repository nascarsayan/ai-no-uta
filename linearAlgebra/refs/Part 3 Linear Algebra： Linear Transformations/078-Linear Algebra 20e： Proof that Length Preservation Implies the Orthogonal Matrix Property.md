## Proof of Orthogonality: $\mathbf{Q^\top Q = I}$

### Introduction
- This video justifies the earlier statement that:
  - If the identity $(Q \alpha)^\top (Q \alpha) = \alpha^\top \alpha$ holds for all vectors $\alpha$,  
  - Then $\mathbf{Q^\top Q = I}$ (where $\mathbf{I}$ is the identity matrix).  
  - This implies $\mathbf{Q}$ represents a length-preserving linear transformation and is **orthogonal**.  

### Review of Concepts
- For understanding the proof, familiarity with matrix transposes and their products is essential. 
- Both $\mathbf{Q^\top Q}$ and $\mathbf{I}$ are **symmetric matrices**.  
  - $\mathbf{I}$ is symmetric by definition.  
  - $\mathbf{Q^\top Q}$ is symmetric because $\mathbf{A^\top A}$ is symmetric for any matrix $\mathbf{A}$.  

### Generalization of the Statement
- Instead of proving for $\mathbf{Q^\top Q}$ and $\mathbf{I}$, a more general case will be proven:  
  - For two symmetric matrices $\mathbf{A}$ and $\mathbf{B}$: if  
    $$  
    (\alpha^\top \mathbf{A} \alpha) = (\alpha^\top \mathbf{B} \alpha)  
    $$  
    for **all vectors $\alpha$**,  
    - Then $\mathbf{A = B}$ (both matrices must be the same).  

---

## Proof

### Step 1: Symmetry Assumption
- Symmetry is essential for the proof. Without it, there could exist **different matrices** $\mathbf{A}$ and $\mathbf{B}$ such that below still holds:  
  $$  
  (\alpha^\top \mathbf{A} \alpha) = (\alpha^\top \mathbf{B} \alpha)  
  $$  
  for all $\alpha$.  
- Example with non-symmetric matrices shows how constraints break if matrices aren't symmetric.

---

### Step 2: Proof Strategy
1. Assume $\mathbf{A}$ and $\mathbf{B}$ are **different symmetric matrices**.  
2. Show that this assumption leads to a contradiction:
   - Find a vector $\alpha$ such that:  
     $$  
     \alpha^\top \mathbf{A} \alpha \neq \alpha^\top \mathbf{B} \alpha  
     $$
   - Separate proof into two cases:  
     - Differences in **diagonal elements**.  
     - Differences in **off-diagonal elements**.  

---

### Case 1: Diagonal Element Differences  

#### Example
- Assume $\mathbf{A}$ and $\mathbf{B}$ differ only in a diagonal entry, e.g.,  
  $$  
  \mathbf{A}_{11} = 3 \quad \text{and} \quad \mathbf{B}_{11} = 4.  
  $$

#### Alpha Selection
- Choose a vector $\alpha$ that isolates this discrepancy:  
  $$  
  \alpha = \begin{bmatrix} 1 \\ 0 \\ 0 \end{bmatrix}.  
  $$

#### Resulting Products
- Compute $\alpha^\top \mathbf{A} \alpha$:  
  $$  
  \alpha^\top \mathbf{A} \alpha = 1 \cdot 3 \cdot 1 = 3.  
  $$  
- Compute $\alpha^\top \mathbf{B} \alpha$:  
  $$  
  \alpha^\top \mathbf{B} \alpha = 1 \cdot 4 \cdot 1 = 4.  
  $$

#### Contradiction
- $\alpha^\top \mathbf{A} \alpha \neq \alpha^\top \mathbf{B} \alpha$: contradiction.  
- Therefore, diagonal entries of $\mathbf{A}$ and $\mathbf{B}$ **must match**.  

---

### Case 2: Off-Diagonal Element Differences  

#### Example
- Assume $\mathbf{A}$ and $\mathbf{B}$ differ in off-diagonal entries, e.g.,  
  $$  
  \mathbf{A}_{12} = 7, \mathbf{A}_{21} = 7 \quad \text{and} \quad \mathbf{B}_{12} = 8, \mathbf{B}_{21} = 8.  
  $$

#### Alpha Selection
- Choose a vector $\alpha$ to isolate the discrepancy:  
  $$  
  \alpha = \begin{bmatrix} 1 \\ 1 \\ 0 \end{bmatrix}.  
  $$

#### Resulting Products
- Compute $\alpha^\top \mathbf{A} \alpha$:  
  $$  
  \alpha^\top \mathbf{A} \alpha = (1 \cdot 7 \cdot 1) + (1 \cdot 7 \cdot 1) = 14.  
  $$  
- Compute $\alpha^\top \mathbf{B} \alpha$:  
  $$  
  \alpha^\top \mathbf{B} \alpha = (1 \cdot 8 \cdot 1) + (1 \cdot 8 \cdot 1) = 16.  
  $$

#### Contradiction
- $\alpha^\top \mathbf{A} \alpha \neq \alpha^\top \mathbf{B} \alpha$: contradiction.  
- Therefore, off-diagonal entries of $\mathbf{A}$ and $\mathbf{B}$ **must match**.  

---

### Final Conclusion
- As diagonal and off-diagonal elements of $\mathbf{A}$ and $\mathbf{B}$ match,  
  $$  
  \mathbf{A = B}.  
  $$  

---

## Implication for $\mathbf{Q^\top Q = I}$
- Substituting $\mathbf{A = Q^\top Q}$ and $\mathbf{B = I}$:  
  - The derived generalization proves that $\mathbf{Q^\top Q = I}$.  
  - By definition, $\mathbf{Q}$ is **orthogonal**.  

### Essential Note on Symmetry
- Requirement for symmetry was crucial; without it, the proof would fail.  
- For non-symmetric matrices, $\alpha^\top \mathbf{A} \alpha = \alpha^\top \mathbf{B} \alpha$ could hold even if $\mathbf{A} \neq \mathbf{B}$.  

---

## Generalization & Final Remarks
- The argument holds for matrices of any dimension.  
- Symmetry of matrices and arbitrariness of vector $\alpha$ were heavily utilized throughout the proof.  
- Thus:  
  $$  
  \mathbf{Q^\top Q = I} \implies \mathbf{Q} \text{ is orthogonal}.  
  $$