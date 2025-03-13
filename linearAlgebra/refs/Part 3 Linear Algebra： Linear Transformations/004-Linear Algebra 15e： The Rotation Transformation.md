# Rotation as a Linear Transformation

Rotation by an angle $\alpha$ is a linear transformation denoted by $R_\alpha$. Below are the key aspects of this transformation, including its properties, evaluation of linearity, eigenvalues, and eigenvectors.

---

## 1. Definition of Rotation Transformation

Given a vector $\mathbf{u}$ and an angle $\alpha$, the rotation transformation $R_\alpha$ rotates $\mathbf{u}$ counterclockwise by the angle $\alpha$. 

- **Counterclockwise rotation:** The convention is to rotate counterclockwise. To rotate clockwise, use a negative value for $\alpha$.
- **Invariant length:** The length of the vector remains unchanged, only its direction is modified.

For example, consider $\alpha = \frac{\pi}{4}$ (45 degrees). Rotating a vector by $\frac{\pi}{4}$ counterclockwise transforms it to $R_{\pi/4}(\mathbf{u})$.

---

## 2. Is Rotation a Linear Transformation?

To verify linearity, we check two key conditions for a transformation $T$:
1. **Preservation of addition:** $T(\mathbf{u} + \mathbf{v}) = T(\mathbf{u}) + T(\mathbf{v})$
2. **Preservation of scalar multiplication:** $T(c\mathbf{u}) = cT(\mathbf{u})$, where $c$ is a scalar.

### (a) Addition Test

Given vectors $\mathbf{u}$ and $\mathbf{v}$:

1. Compute the result of adding $\mathbf{u}$ and $\mathbf{v}$ first, then apply the rotation:
   $$
   R_\alpha(\mathbf{u} + \mathbf{v})
   $$

2. Compare it to applying the rotation to each vector individually, then adding the results:
   $$
   R_\alpha(\mathbf{u}) + R_\alpha(\mathbf{v})
   $$

Using the parallelogram rule for vector addition, both approaches yield the same rotated result. Hence, rotation preserves addition.

### (b) Scalar Multiplication Test

For a scalar $c$ and a vector $\mathbf{u}$:

1. Apply scalar multiplication first, then rotate:
   $$
   R_\alpha(c\mathbf{u})
   $$

2. Compare it to rotating the vector first and then applying scalar multiplication:
   $$
   cR_\alpha(\mathbf{u})
   $$

Both approaches yield the same result. Hence, rotation preserves scalar multiplication.

#### Conclusion:
Since both tests are satisfied, **rotation is a linear transformation**.

---

## 3. Eigenvalues and Eigenvectors of Rotation

An eigenvector $\mathbf{v}$ of a transformation satisfies:
$$
R_\alpha(\mathbf{v}) = \lambda \mathbf{v}
$$
where $\lambda$ is the eigenvalue.

### (a) General Case

Rotation transformations usually do **not** have real eigenvalues or eigenvectors for arbitrary values of $\alpha$.

- When $\alpha$ is not a multiple of $\pi$, **no vector remains a scaled version of itself** (except $\mathbf{0}$, which is trivial and not considered an eigenvector). Every vector rotates to a new position.

### (b) Special Cases

For specific angles, rotation may have real eigenvalues and eigenvectors:
1. $\alpha = \pi$ (180 degrees):
   - All vectors become their negatives.
   - Eigenvalue $\lambda = -1$, and every vector in the plane is an eigenvector (eigenspace is the entire plane).

2. $\alpha = 2\pi$ (360 degrees):
   - All vectors remain unchanged.
   - Eigenvalue $\lambda = 1$, and every vector in the plane is an eigenvector.

---

## 4. Algebraic Properties of Rotation

### (a) Composition of Rotations

If a rotation by $\alpha$ is followed by a rotation by $\beta$, the result is equivalent to a rotation by $\alpha + \beta$:
$$
R_\alpha \circ R_\beta = R_{\alpha + \beta}
$$

### (b) Repeated Rotations

- Rotating by $\frac{\pi}{4}$ four times results in a rotation by $\pi$ (180 degrees):
  $$
  R_{\pi/4}^4 = -I
  $$
  Here, $I$ is the identity transformation, and $-I$ negates every vector.

---

## 5. Algebraic Implications for Eigenvalues

For rotations, the algebraic equation resembles:
$$
x^4 = -1
$$

This equation has **no real roots** (no real eigenvalues). However, it does have complex roots, which are relevant when considering rotations in the context of complex numbers.

---

## 6. Summary

- **Linearity:** Rotation is a linear transformation.
- **Eigenvalues/eigenvectors:**
  - In general, there are no real eigenvalues or eigenvectors, except for special cases ($\alpha = \pi$ or $2\pi$).
  - Complex eigenvalues arise when extending the discussion to complex numbers.
- **Properties:**
  - Rotations preserve length.
  - Composition of rotations adds angles: $R_\alpha \circ R_\beta = R_{\alpha + \beta}$.
  - Repeated rotations can have special effects (e.g., $R_{\pi/4}^4 = -I$).

Rotation provides a rich example of linear transformations with both geometric and algebraic perspectives!