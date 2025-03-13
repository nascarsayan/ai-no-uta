## Defective Matrices Overview

Defective matrices are matrices where the algebraic multiplicity of an eigenvalue exceeds its geometric multiplicity. These matrices are also called **non-diagonalizable matrices**.

### Key Characteristics of Defective Matrices

1. **Algebraic vs Geometric Multiplicity**:
   - **Algebraic multiplicity**: The number of times an eigenvalue appears as a root of the characteristic polynomial.
   - **Geometric multiplicity**: The dimension of the eigenspace corresponding to the eigenvalue.
   - For defective matrices: 
     $$
     \text{Algebraic multiplicity} > \text{Geometric multiplicity}.
     $$

2. **Structure**:
   - Typically upper or lower triangular.
   - Repeat eigenvalues on the diagonal (e.g., multiple 3's) and non-zero values on the subdiagonal.

---

### Why Defective Matrices are Interesting
- Crucial in understanding the broader theory of eigenvalues and eigenvectors.
- They occur infrequently in applications but have unique algebraic and geometric properties.
- Essential when studying diagonalization, eigenvalue decomposition, and system behaviors.

---

### Example of a Defective Matrix

#### Matrix Example:
The matrix  
$A = \begin{bmatrix} 3 & 1 \\ 0 & 3 \end{bmatrix}$  
is defective because it has:
1. **Algebraic multiplicity** = 2 (eigenvalue 3 appears twice).
2. **Geometric multiplicity** = 1 (eigenspace of dimension 1).

#### Characteristic Polynomial:
The characteristic polynomial of $A$:
$$
\text{det}(A - \lambda I) = (3 - \lambda)^2.
$$

#### Eigenvector and Eigenspace:
Subtracting $3$ from the diagonal:
$$
A - 3I = \begin{bmatrix} 0 & 1 \\ 0 & 0 \end{bmatrix}.
$$

Null space of $(A - 3I)$ is:
$$
\text{Null}(A - 3I) = \text{span}\left(\begin{bmatrix} 1 \\ 0 \end{bmatrix} \right).
$$

Eigenspace dimension = 1 (geometric multiplicity).

---

### Defect of a Matrix

- The **defect** is the difference between the algebraic and geometric multiplicities of an eigenvalue.
  $$
  \text{Defect} = \text{Algebraic multiplicity} - \text{Geometric multiplicity}.
  $$
- Example:
   - For $A = \begin{bmatrix} 3 & 1 \\ 0 & 3 \end{bmatrix}$:
     $$
     \text{Defect} = 2 - 1 = 1.
     $$

#### Can the Defect be Greater than 1?
Yes. For a matrix with a triple eigenvalue (algebraic multiplicity = 3) and an eigenspace of dimension 1 (geometric multiplicity = 1), the defect is 2.

---

### Fragility of Defective Matrices

1. **Sensitivity to Perturbations**:
   - Even a tiny change in a matrix's entries can make it **non-defective**.
   - Example:
     - Changing one diagonal element slightly can split a repeated eigenvalue into distinct values.

2. **Comparison with Symmetric Matrices**:
   - Symmetric matrices are more stable under perturbations:
     - They remain symmetric even after small changes (e.g., $A^T A$ remains symmetric after changes to $A$).
   - Eigenvalue perturbations in symmetric matrices are proportional to matrix entry changes, unlike defective matrices where eigenvalue changes can be disproportionally large.

---

### Random Matrices and Defectiveness
- Probability of a random matrix being defective is essentially **zero**.
- Defective matrices are rare and arise due to specific structural properties.

---

### Practical Usage of Defective Matrices
- While uncommon in applications, they are critical to theoretical understanding and necessary to create a complete eigenvalue framework.

