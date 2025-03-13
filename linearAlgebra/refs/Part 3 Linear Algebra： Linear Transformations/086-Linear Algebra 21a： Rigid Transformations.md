# Rigid Transformations

## 1. Introduction to Rigid Transformations

- Rigid transformations preserve the distance between any two points.
- Inspired by the concept of **rigid bodies**, which retain their shape regardless of applied forces or transformations.

### Key Characterization:

- **Distance Preservation**: Distances between points remain unchanged under rigid transformations.
- **Physical Analogy**: A rigid body is considered to not undergo bending, twisting, or deformation.

## 2. Types of Rigid Transformations

Rigid transformations can be classified into **simpler, more elementary transformations**:
1. **Rotation**
2. **Translation**
3. **Reflection**

---

### 2.1 Rotations

#### Definition:
- A rigid transformation where one **fixed point** (the center of rotation) remains stationary while other points rotate around it.

#### Key Properties:
1. Tremendous complexity, yet every rotation can be captured with **3 parameters**:
   - The axis of rotation (requires 2 parameters: longitude and latitude).
   - The **angle of rotation**.

#### Representation:
- Any rotation is equivalent to a simple rotation about a fixed axis.

#### Key Notes:
- If the rotation is not about the **origin**, the **zero vector** will transform into a **nonzero vector**, making the transformation **nonlinear**.

---

### 2.2 Translations

#### Definition:
- Every point in the space moves by the **same vector**.

#### Key Properties:
1. **Nonlinear Transformation**: 
   - Translations move the **origin**, and nonlinear transformations fail to send the zero vector to the zero vector, breaking linearity.
2. **Representation**:
   - Cannot be directly captured via matrix multiplication in the original space.
   - Requires augmentation (e.g., switching to homogeneous coordinates) to capture translations.

#### Mathematical Representation:
If translation is denoted by $T$, and the translation vector is $\mathbf{C}$:
$$ 
T(\mathbf{v}) = \mathbf{v} + \mathbf{C}
$$

Where:
- $\mathbf{v}$ is the original vector.
- $\mathbf{C}$ is the constant translation vector.

#### Visualization:
- **Origin**: Under translation by $\mathbf{C}$, becomes $\mathbf{C}$ itself:
  $$ 
  T(\mathbf{0}) = \mathbf{C}
  $$

#### Strict Definition:
- Translations involve parallel shifts. Any additional rotation during the shift introduces **nonlinearity** (e.g., combined rotation and translation).

---

### 2.3 Reflections

#### Definition:
- A rigid transformation where a body appears as if it were reflected in a **plane (3D)** or a **line (2D)**.

#### Key Observations:
- Reflective transformations **flip** orientations (e.g., left becomes right in a mirror).
- Usually **linear** when the plane of reflection passes through the origin.

---

## 3. General Notes on Transformations

### 3.1 Transforming Space:
- Transformations apply not just to rigid bodies but to the **entire space**.
- Rigid transformations modify the **vectors** (not individual points) while preserving certain properties like distance.

### 3.2 Nonlinear Transformations:
- **Translations**, **rotations** not about the origin, and **reflections** not through the origin are **nonlinear** due to their effects on the zero vector.

#### Example:
For translations:
- Adding a constant vector $\mathbf{C}$ shifts the zero vector:
  $$ 
  T(\mathbf{0}) = \mathbf{C}
  $$
- Violates the rule that linear transformations must map $\mathbf{0} \to \mathbf{0}$.

For rotations not about the origin:
- Similar to translations, the zero vector is shifted, making the transformation **nonlinear**.

---

## 4. Combining Rigid Transformations

To handle nonlinear rigid transformations such as **rotations about a point not at the origin**:
- Translate the **center of rotation** to the origin.
- Perform the rotation.
- Translate the point back.

### Sequence:
1. Translation to origin.
2. Rotation about the origin.
3. Translation back.

This method captures the transformation within the same framework while respecting its nonlinear nature.

---

## 5. Reflections: A Closer Look

- Reflections introduce an **interesting symmetry**.
- Common paradox: Mirrors flip **front-back**, but we perceive it as **left-right**.
  - See video explanation by Richard Feynman for further insights!

---

## 6. Moving Forward

- **Next topic**: Rotations in detail, including their **mathematical properties** and **representation in component spaces**.
- Goal: Gain deeper understanding of the structure of transformations without immediately invoking representation via component spaces.