## Matrix Decomposition: Orthogonal and Symmetric Matrices

### 1. Representation with Orthogonal and Symmetric Matrices
- Any matrix $A$ can be represented as a product of:
  - An **orthogonal matrix** $Q$, and 
  - A **symmetric matrix** $S$ such that:

    $$
    A = QS
    $$
  
- Question: Can $A$ also be represented in the reverse order as:

    $$
    A = SQ
    $$

  Where $S$ is the symmetric matrix, and $Q$ is the orthogonal matrix?  
  **Answer**: Yes!

### 2. Approach to Reverse Representation
- To derive the matrices $S$ and $Q$ for the $A = SQ$ decomposition:
  - Repeat the logic originally used to find $Q$ and $S$ in $A = QS$.

- **Key Observations**:
  - The matrices $S$ and $Q$ in this form will likely differ from the ones in $A = QS$.
  - Exploit orthogonality: $Q^\top Q = I$.

### 3. From Transpose Products to Solution
- Use **$A^\top A$** or **$AA^\top$** to analyze $A$:
  - $A^\top A$ previously led to $A = QS$, where $S = \sqrt{A^\top A}$.
  - Now leverage $AA^\top$ to find $A = SQ$.

- For $A = SQ$, compute:

    $$
    A A^\top = S Q Q^\top S^\top
    $$

  Since $Q^\top Q = I$:
    $$
    A A^\top = S S^\top
    $$
  
  **S** can therefore be obtained as the square root of $AA^\top$.

### 4. Properties of $AA^\top$
- $AA^\top$ shares similar properties with $A^\top A$:
  - Symmetric.
  - All eigenvalues are real and positive.
  - Allows clean computation of $S$ through square root operation.

- $S$ will take the form:

    $$
    S = \sqrt{AA^\top}
    $$

### 5. Completing the Decomposition
- Once $S$ is computed:
  - Calculate $Q$ as:

    $$
    Q = S^{-1} A
    $$

- **Key Findings**:
  - Surprisingly, the orthogonal matrix $Q$ remains unchanged between the two decompositions:
    - $A = QS$ (orthogonal $\times$ symmetric).
    - $A = SQ$ (symmetric $\times$ orthogonal).

### 6. Uniqueness of $S$ and $Q$
- While $Q$ is consistent across both decompositions, the symmetric matrix $S$ is different in each case.

### 7. Connection to Singular Value Decomposition (SVD)
- **Next Steps**:
  - Explore how these decompositions relate to the **Singular Value Decomposition (SVD)**.
