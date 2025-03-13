## 1. Inner Products: Evaluating Through Real and Component Spaces

### Introduction
- The objective is to compare two approaches for evaluating inner products:
  1. Direct evaluation in **real space**.
  2. Evaluation in the corresponding **component space**.

---

### **Real Space vs. Component Space**
- **Real Space**: Treats objects as-is without referencing bases or components.
- **Component Space**: Uses a basis to represent objects in a structured form.

- Key distinction:
  - Real space is conceptually grounded in the natural interpretation of vectors or functions.
  - Component space reduces operations to matrix manipulations.

---

### **Direct Evaluation in Real Space**
1. **Inner Product Definition**:
   Evaluate the inner product directly in real space using the properties:
   - **Distributivity** and **commutativity (symmetry)** are sufficient for most cases.
   - Positive definiteness may not always be needed.

2. **Example**:
   Let's compute the inner product of two functions \( p(x) \) and \( q(x) \) represented by polynomials:
   - Multiply the two polynomials and integrate over the defined interval.
   - Result is purely analytical, involving no basis decomposition.

   Example Calculation:
   $$
   \text{Inner product: } p(x) = 1 + x, \; q(x) = 1 - x
   $$

   $$
   \langle p, q \rangle = \int_{0}^{1} (1 + x)(1 - x) \, dx = \int_{0}^{1} (1 - x^2) \, dx
   $$

   Solving:
   $$
   \int_{0}^{1} 1 \, dx - \int_{0}^{1} x^2 \, dx = \left[ x \right]_0^1 - \left[\frac{x^3}{3}\right]_0^1 = 1 - \frac{1}{3} = \frac{2}{3}
   $$

   - No basis or components are mentioned here.
   - Treats objects directly on their own terms.

---

### **Matrix Representation of Inner Products**
Switching from real space to **component space**:
1. Choose a basis, e.g., \( \{1, x, x^2 \} \), to represent the polynomials.
   - Example:
     - \( 1 + x \) in basis form: \( [1, 1, 0]^T \).
     - \( 1 - x \) in basis form: \( [1, -1, 0]^T \).

2. Compute the **Inner Product Matrix** \( M \) that encodes all pairwise inner products of basis vectors:
   $$
   M = 
   \begin{bmatrix}
   \langle 1, 1 \rangle & \langle 1, x \rangle & \langle 1, x^2 \rangle \\
   \langle x, 1 \rangle & \langle x, x \rangle & \langle x, x^2 \rangle \\
   \langle x^2, 1 \rangle & \langle x^2, x \rangle & \langle x^2, x^2 \rangle
   \end{bmatrix}
   $$

3. Matrix multiplication:
   Using:
   $$
   [1, 1, 0]^T M [1, -1, 0]
   $$
   Calculate the product that should reproduce the real-space result (invariant).

---

### Component Computation Example
1. **Basis Decomposition**:
   - \( 1 + x = [1, 1, 0]^T \)
   - \( 1 - x = [1, -1, 0]^T \)

2. **Matrix Multiplication**:
   $$
   [1, 1, 0]^T \begin{bmatrix}
   M_{11} & M_{12} & M_{13} \\
   M_{21} & M_{22} & M_{23} \\
   M_{31} & M_{32} & M_{33}
   \end{bmatrix}
   [1, -1, 0] = \frac{2}{3}
   $$

   - Ensures consistency with the real space result.

---

### **Invariant Properties**
1. The **result of the inner product** (e.g., \( \frac{2}{3} \)) is invariant under basis transformations.
2. The **inner product matrix** \( M \) and the vector components, however, vary with the choice of basis.

---

## 2. Variants, Invariants, and Tensor Calculus

### **Invariants vs. Variants**
- **Invariant**:
  - The scalar result (e.g., \( \frac{2}{3} \)).
  - Unchanged across transformations.

- **Variant**:
  - Matrix representations (e.g., \( M \)) and vector components.
  - Depend on the choice of basis or representation.

---

### Tensor Calculus Perspective
- **Inner product matrix** \( M \):
  - A doubly **covariant tensor**.
- **Vector components**:
  - Contravariant tensors.
- **Resulting scalar**:
  - Invariant under transformations.
- **Connecting the worlds**:
  - Tensor calculus formalizes the relationship between covariant and contravariant elements to yield invariants.

---

### General Utility
1. Real space representations: Useful for intuition, geometry, and direct computations.
2. Component space representations: Essential for computational efficiency and higher-dimensional problems.

- Clear visualization of the **parallel worlds**:
  - Real space: Grounded in natural vectors or polynomials.
  - Component space: Translated into matrices and vectors for manipulation. 

