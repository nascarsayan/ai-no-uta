## Rotations in the Plane

### Introduction
- Rotations in the plane are simple yet surprisingly interesting.
- This discussion will focus on the **geometric properties** of rotations, emphasizing intuition without introducing components or matrices yet. 
- Rotations will later be confirmed algebraically using matrices in future discussions.

---

### 1. Basic Setup
- We will **restrict** rotations to being about the **origin**:
  - Rotations about other points are not linear transformations.
  - Linear transformations are our current focus.
- **Rotations about the origin** ensure that the origin remains fixed.

---

### 2. Convention
- Rotations are a **one-parameter family**:
  - It takes a single number, the angle α, to describe a rotation.
  - **Positive angle**: Rotation is counterclockwise.
  - **Negative angle**: Rotation is clockwise.

Examples:
- Rotation by $\frac{\pi}{4}$:
  - Starting at some vector, rotate **counterclockwise** by $\frac{\pi}{4}$.
- Rotation by $-\frac{\pi}{4}$:
  - Starting at some vector, rotate **clockwise** by $\frac{\pi}{4}$.

---

### 3. Notation for Rotations
- Denote a rotation by angle α as $R_\alpha$.
- Understand $R_\alpha$ as a **function** that applies a rotation to vectors in the plane.

---

### 4. Key Properties of Rotations

#### Property 1: Composition of Rotations
1. **Consecutive Rotations Add**:
   - A rotation by angle $\alpha$, followed by a rotation by angle $\beta$, is equivalent to a **single rotation** by $\alpha + \beta$.
   - Mathematically:
     $$
     R_\alpha \circ R_\beta = R_{\alpha + \beta}
     $$
   - Example:
     Perform a $\frac{\pi}{3}$ rotation followed by a $\frac{\pi}{6}$ rotation:
     $$
     R_{\frac{\pi}{3}} \circ R_{\frac{\pi}{6}} = R_{\frac{\pi}{2}}
     $$
   
2. **Order of Rotations Doesn't Matter (Commutativity)**:
   - $R_\alpha \circ R_\beta = R_\beta \circ R_\alpha$
     - For example, $R_{\frac{\pi}{4}} \circ R_{\frac{\pi}{6}} = R_{\frac{\pi}{6}} \circ R_{\frac{\pi}{4}}$
   - Reason: Addition of angles is commutative ($\alpha + \beta = \beta + \alpha$).

---

#### Property 2: Inverses of Rotations
1. **Inverse of a Rotation**:
   - The inverse of a rotation by angle $\alpha$ is a rotation by $-\alpha$.
     - $$
     R_\alpha \circ R_{-\alpha} = R_0 = \text{Identity (Fixes every vector)}
     $$
   - Example:
     $$
     R_{\frac{\pi}{3}} \circ R_{-\frac{\pi}{3}} = R_0
     $$
2. **Notationally**:
   - The inverse of $R_\alpha$ is:
     $$
     R_\alpha^{-1} = R_{-\alpha}
     $$

---

#### Property 3: Eigenvalues and Eigenvectors
1. **General Behavior**:
   - Most rotations **do not have eigenvectors** in the plane because a vector is not scaled but rather rotated.
   
2. **Exceptions**:
   - Rotation by $\pi$:
     - Every vector becomes its **negative** (eigenvalue $-1$):
       $$
       R_\pi(\mathbf{v}) = -\mathbf{v}
       $$
     - Thus, every vector is an eigenvector.
   - Rotation by $2\pi$ (and multiples of $2\pi$):
     - Every vector remains unchanged (eigenvalue $1$):
       $$
       R_{2\pi}(\mathbf{v}) = \mathbf{v}
       $$
     - Thus, every vector is an eigenvector.

3. **Summary**:
   - Rotations **only have eigenvectors** when the angle is a **multiple of $\pi$**, i.e., $\alpha = n\pi$ for integer $n$.

---

### 5. Matrix Representation
- While this discussion avoided components and matrices, these properties will later translate directly into matrix operations:
  - Property 1 relates to **matrix multiplication** of rotation matrices.
  - Property 2 will directly translate to the **inverse of rotation matrices**.
  - Eigenvalue results will help identify decomposition when analyzing rotations algebraically.

---

### 6. Looking Ahead
- In the next discussion:
  - Rotations will be studied using **Cartesian coordinates** and **matrix representation**.
  - The geometric properties outlined here will be proven algebraically.