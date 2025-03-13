## Component Spaces and Eigen Values/Vectors

### Overview
- This series of videos focuses on using **component spaces** to calculate the **eigenvalues** and **eigenvectors** of linear transformations.
- The approach involves understanding reflection and dilation transformations and leveraging matrix representations for analysis.

---

### Reflection Transformation: Eigenvalues and Eigenvectors

#### Reflection Operator
- The reflection operator is a linear transformation for which the **spectrum** (eigenvalues) is already known.
  - It will be revisited to confirm results and showcase calculations using **component spaces**.
  
#### Eigenvalues of Reflection
- **Eigenvalue +1** corresponds to the line of reflection:
  - The eigenvector for $\lambda = 1$ lies on the line of reflection and remains **unchanged**.
  - Denote this eigenvector as $\mathbf{v}_1$.

- **Eigenvalue -1** corresponds to orthogonal directions to the line of reflection:
  - The eigenvector for $\lambda = -1$ lies orthogonal to the line of reflection and gets **flipped** by the reflection.
  - Denote this eigenvector as $\mathbf{v}_2$.

---

#### Matrix Representation in Component Space
- Construct the matrix that represents the reflection transformation in **component space**.
- Eigenvalues are found along the diagonal because the matrix is upper triangular.

#### Calculation of Eigenvalues and Eigenvectors
1. **Eigenvalue $\lambda = 1$:**
   - Diagonal element and corresponding eigenvector derived straightforwardly.

   **Eigenvector**:
   $$
   \mathbf{v}_1 = \begin{bmatrix} 1 \\ 0 \end{bmatrix}
   $$

2. **Eigenvalue $\lambda = -1$:**
   - Subtract $\lambda = -1$ from diagonal elements to calculate eigenvectors. Solve the resulting null space problem.

   **Eigenvector**:
   $$
   \mathbf{v}_2 = \begin{bmatrix} 1 \\ -1 \end{bmatrix}
   $$

---

### Translation from Component Space to Real Eigenvectors
After obtaining eigenvectors in **component representation**, translate them back to the original basis:
1. First eigenvector $\mathbf{v}_1$:
   - Take **1 unit** of $\mathbf{e}_1$ and **0 units** of $\mathbf{e}_2$.
   - Resulting vector:
   $$
   \mathbf{v}_1 = \mathbf{e}_1
   $$

2. Second eigenvector $\mathbf{v}_2$:
   - Combine **1 unit** of $\mathbf{e}_1$ minus **1 unit** of $\mathbf{e}_2$.
   - Resulting vector:
   $$
   \mathbf{v}_2 = \mathbf{e}_1 - \mathbf{e}_2
   $$

---

### Matrix Representation in Different Bases
- When changing to a new basis (e.g., $\mathbf{F}_1, \mathbf{F}_2$), the matrix representation of the linear transformation also changes.
- However, the eigenvalues ($\lambda_1 = 1$ and $\lambda_2 = -1$) remain the same.
  
#### Example of Basis Transformation
- **New basis $\mathbf{F}_1, \mathbf{F}_2$:**
  - $\mathbf{F}_1$ is different, but $\mathbf{F}_2$ coincides with $\mathbf{E}_2$.
  - The transformed matrix becomes symmetric, but the diagonal retains eigenvalues.

---

### Eigenvalues and Eigenvectors for Matrix Representation
#### Diagonal Matrix in Eigenbasis
- Choose eigenbasis $\{\mathbf{v}_1, \mathbf{v}_2\}$ as the new basis representation:
  - The matrix becomes **diagonal** in this eigenbasis.
  - Eigenvalues appear directly along the diagonal.

#### Advantages of Diagonalization
- Easier to compute eigenvalues and eigenvectors.
- Eigenvectors become unit standard vectors in $\mathbb{R}^n$.

**Exercise:** Diagonalize the reflection matrix in the eigenbasis.
1. Verify that eigenvalues are along the diagonal.
2. Ensure the eigenvectors correspond to the standard basis vectors in $\mathbb{R}^2$. 

---

### Summary of Key Results
- Eigenvalues of reflection:
  - $\lambda_1 = +1$
  - $\lambda_2 = -1$

- Eigenvectors for reflection:
  - $\mathbf{v}_1 = \mathbf{e}_1$
  - $\mathbf{v}_2 = \mathbf{e}_1 - \mathbf{e}_2$

- Matrix properties in component space:
  - Component spaces retain the same eigenvalues but represent eigenvectors differently depending on the chosen basis.

---

### Next Topic: Dilation Transformation
- In the next video, the **dilation transformation** on the space of polynomials will be analyzed.
- **Component spaces** will be essential to determine its eigenvalues and eigenvectors.