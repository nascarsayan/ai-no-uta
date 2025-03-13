## Rotation Around an Arbitrary Axis

### Problem Description
- In this video, we explore a technique frequently used in computer graphics for **rotating a body about an axis that points in an arbitrary direction.**
- The direction of the axis is described using the angles $\theta$ and $\phi$, and the body is rotated by an angle $\alpha$.

---

### Objective
- Represent this rotation as the product of **elementary rotation matrices** with respect to the coordinate axes.

### Key Insight
- While a rotation about the $x$, $y$, or $z$ axis can be represented by a single elementary rotation matrix, the rotation about an **arbitrarily oriented axis** cannot—it must be decomposed into multiple transformations.

---

### Strategy for Rotation
The approach can be broken down into **three main steps**:

1. **Align the Axis with the z-Axis**:
   - Use rotations to align the arbitrary axis with the $z$-axis.
   
2. **Perform the Rotation**:
   - Rotate around the $z$-axis using an elementary rotation matrix for the given angle $\alpha$.

3. **Bring Back to the Original Orientation**:
   - Reverse the transformations used in Step 1 to restore the axis to its original position.

---

### Implementation: Five Elementary Steps

#### Step Breakdown
1. **Un-Swing the Axis**:
   - Rotate the axis about the $z$-axis by an angle $-\phi$ to eliminate azimuth.

2. **Un-Lean the Axis**:
   - Rotate the axis about the $y$-axis by an angle $-\theta$ to align it with the $z$-axis.

3. **Perform the Main Rotation**:
   - Rotate the body about the $z$-axis by the desired angle $\alpha$.

4. **Lean the Axis Back**:
   - Rotate about the $y$-axis by $\theta$ to tilt the axis back.

5. **Swing the Axis Back**:
   - Rotate about the $z$-axis by $\phi$ to return to the original azimuth.

#### Combined Transformation
The total transformation can be represented algebraically:

$$
M = R_z(\phi) \cdot R_y(\theta) \cdot R_z(\alpha) \cdot R_y(-\theta) \cdot R_z(-\phi)
$$

---

### Geometric Interpretation
- The **first two steps** (un-lean and un-swing) move the axis to align with the $z$-axis.
- The **main rotation** is then performed about the $z$-axis.
- The **last two steps** (lean and swing) reverse the initial transformation, restoring the axis to its original arbitrary direction.

---

### Observations
1. **Transformations are Applied to the Body**:
   - The matrix transformations are essentially applied to the 3D body or object, with the axis serving as an imaginary guide.

2. **Non-Commutativity of Matrices**:
   - Matrix multiplication is **non-commutative**, which is crucial for these transformations to work. For example:
     - $R_y(-\theta)$ does not "cancel out" $R_y(\theta)$ when applied in a sequence, as their context differs.

3. **Why Are These Steps Needed?**:
   - The intermediate steps (un-lean, un-swing, etc.) help set up the geometry such that the desired rotation can be completed accurately.

---

### Applications in Computer Graphics
- This idea of **decomposing rotations** into elementary matrix transformations is ubiquitous in computer graphics.
- It is also generalized in implementing **translations** using matrix products, which will be explored in future discussions.

---

### Conclusion
- The described method may seem like a roundabout way to achieve a simple goal, but it is a structured, effective approach due to the constraints of linear algebra and matrix operations.
- This process illuminates the **power of matrix compositions** in solving complex geometric problems systematically.