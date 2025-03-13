# Component Space Analysis of Rotations in the Plane (Non-Cartesian Basis)

### Overview
- This video explores rotations in the plane using a **non-Cartesian basis**. 
- The basis:
  - Is **orthogonal** (vectors are perpendicular).
  - One vector has length 1, the other has length 2.
- The goal: Derive the **rotation matrix** for this non-Cartesian basis and analyze its properties.

---

## 1. Procedure for Deriving the Matrix

1. Apply the transformation (rotation by $\alpha$) to each basis vector:  
   - Decompose the result into components with respect to the new basis.

2. **Example for the first basis vector ($e_1$):**
   - Rotation transforms $e_1$ to a new position, maintaining its length.
   - Components of the transformed $e_1$:
     - Along $e_1$: $\cos(\alpha)$ (no scaling needed for this basis direction).
     - Along $e_2$: $2 \sin(\alpha)$ (scaled by 2 due to the length of $e_2$).
   - First column of the matrix: $\begin{bmatrix} \cos(\alpha) \\ 2\sin(\alpha) \end{bmatrix}$.

3. **Example for the second basis vector ($e_2$):**
   - Rotate $e_2$ by $\alpha$.
   - Components of the rotated $e_2$:
     - Along $e_1$: $-\frac{1}{2}\sin(\alpha)$ (scaled down by $\frac{1}{2}$ due to $e_1$ being half the length).
     - Along $e_2$: $\cos(\alpha)$.
   - Second column of the matrix: $\begin{bmatrix} -\frac{1}{2}\sin(\alpha) \\ \cos(\alpha) \end{bmatrix}$.

4. **Final Matrix:**
   $$
   R_\alpha = 
   \begin{bmatrix} 
   \cos(\alpha) & -\frac{1}{2}\sin(\alpha) \\ 
   2\sin(\alpha) & \cos(\alpha) 
   \end{bmatrix}
   $$

---

## 2. Key Properties of the Rotation Matrix

### a. **Preservation of Relationships**
- Although the entries of the matrix differ from the Cartesian case, **trigonometric relationships hold true**.
- When multiplying two rotation matrices $R_\alpha$ and $R_\beta$, the result is the matrix for rotation by $\alpha + \beta$:
  $$
  R_\alpha \cdot R_\beta = R_{\alpha + \beta}.
  $$
- **Example Justification:**
  - The entry in the first row, first column:
    - $\cos(\alpha)\cos(\beta) - \left(-\frac{1}{2}\sin(\alpha)\right)(2\sin(\beta))$
    - Simplifies to $\cos(\alpha + \beta)$.

### b. **Commutativity**
- Rotation matrices for different angles **commute**:
  $$
  R_\alpha \cdot R_\beta = R_\beta \cdot R_\alpha.
  $$

### c. **Inverse of the Rotation Matrix**
- The inverse of the rotation matrix $R_\alpha$ is:
  $$
  R_\alpha^{-1} = R_{-\alpha}.
  $$
- Replace $\alpha$ with $-\alpha$, flipping the signs of sine terms.

### d. **Determinant and Trace**
- Determinant of $R_\alpha$:  
  $$
  \text{det}(R_\alpha) = \cos^2(\alpha) + 2 \cdot \frac{1}{2} \sin^2(\alpha) = 1.
  $$  
  This confirms length preservation (rotations do not stretch or shrink vectors).
  
- Trace of $R_\alpha$ (sum of diagonal elements):
  $$
  \text{tr}(R_\alpha) = 2\cos(\alpha).
  $$

---

## 3. Rotations and Preservation of Key Properties

### a. Rotations in a Non-Cartesian Basis
- Rotations **preserve geometric transformations** regardless of the chosen orthogonal basis.  
- This is because the properties arise from the **linear transformation itself**, not the specific matrix representation.

### b. Changes in Basis-Specific Properties
- In the non-Cartesian basis:
  - The transpose of $R_\alpha$ is **not** equal to $R_\alpha^{-1}$.
  - This is because the orthogonality property of the matrix depends on the Cartesian nature of the basis.

---

## 4. Conclusion

- The component space analysis of rotations in the plane for a non-Cartesian basis shows:
  - Expected mathematical relationships (e.g., additive angles, matrix commutativity) **still hold true**.
  - Basis-specific properties (e.g., transpose equals inverse, orthogonality) **depend on the Cartesian structure** of the basis.

- This process unfolded like a **well-written TV show**:  
  - All components worked together in perfect harmony to reach the expected result! 😄