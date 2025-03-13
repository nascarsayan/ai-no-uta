# Structured Markdown Notes

## 1. Orthogonal and Orthonormal Bases

### Decomposing a Vector  
- Suppose we have an **orthonormal basis** or an **orthogonal basis**, denoted as $B$, not restricted to any specific vector space:
  - This vector space could represent geometric vectors, polynomials, audio signals, etc.
  - The discussion is abstract, encompassing all possible spaces.

### Task: Decompose a vector $\vec{v}$ relative to this basis.  
This involves expressing $\vec{v}$ as a linear combination of the basis elements.

### Setting Context  
- Inner product availability determines how the decomposition is carried out:
    - Without an inner product: Different strategies must be employed (system of equations, geometry, or "crafty" methods).
    - With an inner product: A fundamental algebraic trick involving dot products can be applied.

---

## 2. Using Inner Products to Find Decomposition Coefficients  
### Key Idea:  
- Dot product each side of $\vec{v}$'s expression with one of the basis elements.

1. **Orthonormal Case**  
    - By definition of orthonormality, the inner product eliminates terms where indices don’t match:
      $$
      \vec{v} = \sum_{i=1}^{n} \alpha_i \vec{e}_i
      $$
      Dotting both sides with $\vec{e}_1$ gives:
      $$
      \vec{e}_1 \cdot \vec{v} = \alpha_1
      $$
      - To find $\alpha_i$: Dot $\vec{v}$ with $\vec{e}_i$.
      - Simple rule for orthonormal bases:  
        $\alpha_i = \vec{e}_i \cdot \vec{v}$.

2. **Orthogonal Case**  
    - For orthogonal bases, the inner product is not necessarily 1:
      $$
      \lVert \vec{e}_i \rVert = \sqrt{\vec{e}_i \cdot \vec{e}_i}
      $$
      $\alpha_i$: Divide by $\lVert \vec{e}_i \rVert^2$.

3. **Non-Orthogonal Basis**  
    - Basis elements being neither orthogonal nor orthonormal results in a system of equations:
      - Dot product each side with $\vec{e}_1, \vec{e}_2, \dots$ to generate equations.
      - Solve the resulting system (matrix form: $A\vec{\alpha} = \vec{b}$).

---

## 3. Matrix Representation for Non-Orthogonal Bases  

### General Procedure  
1. Form the matrix $A$ using **pairwise inner products** of the basis elements:
   $$
   A[i, j] = \vec{e}_i \cdot \vec{e}_j
   $$
   Example for $n = 3$:
   $$
   A = 
   \begin{bmatrix}
   \vec{e}_1 \cdot \vec{e}_1 & \vec{e}_1 \cdot \vec{e}_2 & \vec{e}_1 \cdot \vec{e}_3 \\
   \vec{e}_2 \cdot \vec{e}_1 & \vec{e}_2 \cdot \vec{e}_2 & \vec{e}_2 \cdot \vec{e}_3 \\
   \vec{e}_3 \cdot \vec{e}_1 & \vec{e}_3 \cdot \vec{e}_2 & \vec{e}_3 \cdot \vec{e}_3
   \end{bmatrix}
   $$

2. Represent the decomposition as:
   $$
   A\vec{\alpha} = \vec{b}
   $$
   - $\vec{\alpha} = [\alpha_1, \alpha_2, \alpha_3]^\top$ (unknown coefficients),
   - $\vec{b} = [\vec{v} \cdot \vec{e}_1, \vec{v} \cdot \vec{e}_2, \vec{v} \cdot \vec{e}_3]^\top$.

### Remarks  
- Matrix $A$:
  - Symmetric: Owing to the commutative property of the dot product.
  - Positive definite: By the definition of inner products.
- The system can be solved via Gaussian elimination or other numerical techniques.

---

## 4. Metric Matrix and Names  
- **Matrix $A$** is central to linear algebra and inner product formulation.  
- Names:
  - **Metric**: Borrowed from tensor calculus, as it relates to measuring distances.
  - **Inner Product Matrix**: Descriptive of its use.
  - **Gram Matrix**: A common terminology.

---

## 5. Positive Definiteness of the Matrix  
- Regardless of basis choice or inner product:
  - The matrix $A$ is **positive definite**.
  - This property ensures solvability of the system $A\vec{\alpha} = \vec{b}$, guaranteeing a unique decomposition.

### Summary: Applicability of the Technique  
- The method of using inner products and solving the resulting system works in all cases:
  - Orthogonal bases (simplest case).
  - Arbitrary bases (requires solving $A\vec{\alpha} = \vec{b}$).
- The beauty lies in reducing decomposition to arithmetic and linear algebra.