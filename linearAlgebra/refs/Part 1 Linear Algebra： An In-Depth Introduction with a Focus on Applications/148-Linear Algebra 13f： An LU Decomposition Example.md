## LU Decomposition of a Symmetric Matrix

### Symmetric Matrix Properties

- A symmetric matrix is a square matrix whose rows are the same as its columns.  
- This characteristic provides a "nice surprise" during LU decomposition, as the **L** matrix turns out to be the transpose of the **U** matrix.

---

### Gaussian Elimination for LU Decomposition

#### Goal
To calculate the LU decomposition of a $4 \times 4$ symmetric matrix.

#### Steps:

1. **Gaussian Elimination with Record Inversion**  
   - Start with the identity matrix and perform Gaussian elimination on the given symmetric matrix.
   - Simultaneously record the inverse steps for later construction of the **L** matrix.

---

### Step-by-Step Gaussian Elimination

#### Step 1: Subtract $2$ of Row 1 from Row 2  

- Operation changes:
  $$
  \begin{pmatrix} 2 & 5 & 2 & 5 \end{pmatrix} \rightarrow \begin{pmatrix} 0 & 1 & -2 & 1 \end{pmatrix}
  $$

---

#### Step 2: Subtract $2$ of Row 1 from Row 3  

- Operation changes:
  $$
  \begin{pmatrix} 2 & 2 & 9 & 1 \end{pmatrix} \rightarrow \begin{pmatrix} 0 & -2 & 5 & -3 \end{pmatrix}
  $$

---

#### Step 3: Subtract $2$ of Row 1 from Row 4  

- Operation changes:
  $$
  \begin{pmatrix} 2 & 1 & -3 & 3 \end{pmatrix} \rightarrow \begin{pmatrix} 0 & -3 & 1 & 3 \end{pmatrix}
  $$

---

#### Step 4: Add $2$ of Row 2 to Row 3  

- Operation changes:
  $$
  \begin{pmatrix} 0 & -2 & 5 & -3 \end{pmatrix} \rightarrow \begin{pmatrix} 0 & 0 & 1 & -1 \end{pmatrix}
  $$

---

#### Step 5: Subtract Row 2 from Row 4  

- Operation changes:
  $$
  \begin{pmatrix} 0 & -3 & 1 & 3 \end{pmatrix} \rightarrow \begin{pmatrix} 0 & 0 & -1 & 2 \end{pmatrix}
  $$

---

#### Step 6: Add Row 3 to Row 4  

- Operation changes:
  $$
  \begin{pmatrix} 0 & 0 & -1 & 2 \end{pmatrix} \rightarrow \begin{pmatrix} 0 & 0 & 0 & 1 \end{pmatrix}
  $$

---

### Result of Gaussian Elimination:

- Matrix $U$:
  ```
  U = \text{transformed matrix after Gaussian elimination.}
  ```

---

### Constructing the **L** Matrix

- Combine the recorded inverse steps from Gaussian elimination into **L**.
  - Since the original matrix is symmetric, **L** is simply the transpose of **U**.

---

### Observation: Symmetric Matrix Implication

- For symmetric matrices, the **L** matrix is always the transpose of the **U** matrix.
- This property will be further explored later in the course when discussing inner products.

---

### Final Result:

- Matrix $A$ can be expressed as:
  $$
  A = L \cdot U
  $$

#### Verification:
- Multiply matrices **L** and **U** to verify $\mathbf{A = L \cdot U}$.

---

### Key Takeaway:

- LU decomposition is straightforward for symmetric matrices due to the relationship between **L** and **U**:
  $$
  L = U^\top
  $$

