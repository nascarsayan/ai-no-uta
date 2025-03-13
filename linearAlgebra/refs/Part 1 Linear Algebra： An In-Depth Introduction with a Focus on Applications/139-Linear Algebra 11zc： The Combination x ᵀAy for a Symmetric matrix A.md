## Verifying Symmetry in Triple Products

### Symmetric Matrix: Key Insight
If a matrix $A$ is **symmetric**, then in a triple product of the form:

$$
x^T A y
$$

the order of the vectors $x$ and $y$ does **not** matter. That is:

$$
x^T A y = y^T A x
$$

provided $A$ is symmetric.

---

### Importance of Symmetry
- **Necessity**: The symmetry of $A$ is **essential** for this identity to hold.
- If $A$ is not symmetric, the result will **vary** when switching the order of $x$ and $y$ in the product.

---

### Numerical Example Recap
- Consider a case where the middle matrix $A$ is **not symmetric**:
  - Original values: $x^T A y = 11$
  - Switching vectors: $y^T A x = 4$
  - **Result mismatch**: Clearly, asymmetry in $A$ invalidates the equality.

- When $A$ **is symmetric**, swapping $x$ and $y$ gives the same result in the triple product.

---

### Two Approaches to Validation

---

#### 1. **Entry-by-Entry Proof**
The triple product:

$$
x^T A y
$$

expands as a summation based on the entries of $A$, $x$, and $y$. 

#### Key Observation
- Each matrix entry $A_{ij}$ contributes a term $A_{ij} x_i y_j$.
- For **symmetric** $A$, $A_{ij} = A_{ji}$.

#### Behavior of:
1. **Diagonal Terms ($A_{ii}$)**:
   - These terms are unaffected when switching $x$ and $y$.
   - For instance: $A_{11} x_1 y_1$ remains the same as $A_{11} y_1 x_1$.

2. **Off-Diagonal Terms ($A_{ij}$, where $i \neq j$)**:
   - Switching $x$ and $y$ swaps $A_{ij} x_i y_j$ and $A_{ji} x_j y_i$.
   - For symmetric $A$, $A_{ij} = A_{ji}$ ensures that these terms are **equivalent**.

---

#### Final Entry-Based Conclusion
The **commutativity** of scalar multiplication combines the swapped terms, preserving the equality for symmetric $A$. Key idea:

$$
x^T A y = y^T A x
$$

---

#### 2. **Algebraic Proof Using Transposes**

#### Starting Observation
A triple product $x^T A y$ results in a **$1 \times 1$ matrix** (a scalar). For any scalar, the following holds:

$$
x^T A y = \left( x^T A y \right)^T
$$

#### Using Transpose Properties
The transpose of a triple product is expressed as:

$$
\left( x^T A y \right)^T = y^T A^T x
$$

#### Applying Symmetry of $A$
If $A$ is symmetric, then $A^T = A$. Substituting, we get:

$$
y^T A^T x = y^T A x
$$

Thus, 

$$
x^T A y = y^T A x
$$

---

### Insights from Both Approaches
- The **entry-based proof** shows equality term by term.
- The **algebraic proof** leverages symmetry and properties of transpose.

---

### Applications in Practice
- In practical applications, the middle matrix $A$ is **typically symmetric**, ensuring the order of $x$ and $y$ does not matter.
- This property is especially useful in optimizing computations involving symmetric matrices.

---

### Summary
If the middle matrix $A$ is symmetric, the order of vectors in the triple product does not matter:

$$
x^T A y = y^T A x
$$

Two proof techniques verify this: 
1. **Entry-by-entry analysis** highlights how symmetry ensures equivalence of terms.
2. **Algebraic proof** demonstrates the role of symmetry in matrix transposes.