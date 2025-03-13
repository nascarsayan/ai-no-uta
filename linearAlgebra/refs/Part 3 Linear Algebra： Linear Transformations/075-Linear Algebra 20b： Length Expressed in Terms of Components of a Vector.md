### Cartesian Basis and Length of Vectors

---

#### Key Concepts:
1. **Cartesian Basis**:
   - Contains orthogonal vectors, each of unit length.
   - For any dimension:
     - **2D Basis**: Two orthogonal vectors.
     - **3D Basis**: Three orthogonal vectors.

2. **Rotations in Cartesian Basis**:
   - Basis can be rotated, retaining orthogonality and unit lengths.
   - Rotated bases are still Cartesian.

   > **Example**: Rotating a basis in 2D results in different orientations, but the orthogonal and unit-length properties remain.

3. **Versatility of Cartesian Basis**:
   - Different bases (rotated, flipped) retain computations like vector length.
   - Orthogonality and unit vector properties are essential for deriving formulas.

---

#### Formula for Length of a Vector in a Cartesian Basis

**Setup**:  
- Represent vector $v$ in terms of components $\alpha_1$ and $\alpha_2$ with respect to a Cartesian basis.

---

**Pythagorean Theorem Approach**:

1. **Decomposing $v$**:
   - Components of $v$ are projections:
     - $\alpha_1$: Projection along unit vector $E_1$ in the horizontal direction.
     - $\alpha_2$: Projection along unit vector $E_2$ in the vertical direction.

2. **Length Formula**:
   - Use Pythagorean theorem for the hypotenuse:
   $$
   ||v|| = \sqrt{\alpha_1^2 + \alpha_2^2}
   $$

3. **Square Length for Simplicity**:
   To simplify computation:
   $$
   ||v||^2 = \alpha_1^2 + \alpha_2^2
   $$

---

#### Matrix Representation for Length Formula

1. **Vector Representation**:
   - Represent vector components as a matrix:
     $$
     \alpha = \begin{bmatrix} \alpha_1 \\ \alpha_2 \end{bmatrix}
     $$

2. **Matrix Expression**:
   - Combine components using matrix multiplication. The length squared of $v$ can be expressed as:
     $$
     ||v||^2 = \alpha^\top \alpha
     $$
     **Explanation**:
     - $\alpha^\top$: Transpose of $\alpha:$ $[\alpha_1 \, \alpha_2]$ (row vector).
     - Matrix multiplication results in a scalar $\alpha_1^2 + \alpha_2^2$.

3. **Advantages**:
   - The formula avoids explicit references to $\alpha_1$, $\alpha_2$.
   - Simplifies operations using block matrix representation.

---

#### Changing Bases:
1. **Rotated/Modified Cartesian Basis**:
   - Components of $v$ ($\alpha_1, \alpha_2$) change.
   - Using the new components under the same formula ($\sqrt{\alpha_1^2 + \alpha_2^2}$), the computed length remains unchanged.

2. **Non-Cartesian Basis**:
   - Vectors are orthogonal but not unit length.
   - The formula adjusts to include scaling factors derived from vector lengths.

---

### Extending the Framework: Angles Between Vectors

**Problem**:
Given vectors $v = (\alpha_1, \alpha_2)$ and $w = (\beta_1, \beta_2)$, derive an expression for the angle $\theta$ between them using their components $\alpha_1, \alpha_2, \beta_1, \beta_2$.

---
#### Next Steps:
1. **Idea**: Express cosine of $\theta$ using the dot product and vector norms:
   $$
   \cos\theta = \frac{v \cdot w}{||v|| \, ||w||}
   $$

2. **Convert to Matrix Form**:
   - Represent dot product and norms in matrix operations.

---

**Future Topics**:
- Discussion of dot products (combination of lengths and angles).
- Exploring the role of transpose operation in dot products and vector projections.