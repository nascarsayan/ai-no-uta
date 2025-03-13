# Capturing Translations and Rotations via Matrix Multiplication

## 1. Problem Overview: Non-linear Transformations
- **Goal:** Represent translations and rotations with respect to arbitrary points/axes using matrix multiplication.
- **Challenge:** Translations and rotations that are not through the origin are **non-linear**, meaning they cannot be directly expressed as matrix products in the component space.

### Linear Transformation Property
- Hallmark property: Any linear transformation applied to the **zero vector** produces the **zero vector**.
- Non-linear transformations break this property:
    - Translation: $T(v) = v + a$, where $a$ is constant for all inputs $v$.
        - Applying $a$ to $v = 0$ gives $T(0) = a \neq 0$.
    - Rotation about points other than the origin similarly violates the linear property.

---

## 2. Augmented Component Space Trick
- **Solution:** Rescue matrix representation by augmenting component spaces with an additional "tail" entry.

### Example Translation Setup
#### Vector and Translation Definition:
Let $v = \begin{bmatrix} v_1 \\ v_2 \\ v_3 \end{bmatrix}, a = \begin{bmatrix} a_1 \\ a_2 \\ a_3 \end{bmatrix}$.  
To augment the space:
$$
v \to \begin{bmatrix} v_1 \\ v_2 \\ v_3 \\ 1 \end{bmatrix}, \quad a \to \begin{bmatrix} a_1 \\ a_2 \\ a_3 \\ 0 \end{bmatrix}.
$$

#### Translation Matrix Representation:
For translation by $a$, use the following matrix:
$$
T = 
\begin{bmatrix}
1 & 0 & 0 & a_1 \\
0 & 1 & 0 & a_2 \\
0 & 0 & 1 & a_3 \\
0 & 0 & 0 & 1
\end{bmatrix}.
$$

#### Applying Translation:
$$
T \begin{bmatrix} v_1 \\ v_2 \\ v_3 \\ 1 \end{bmatrix} = \begin{bmatrix} v_1 + a_1 \\ v_2 + a_2 \\ v_3 + a_3 \\ 1 \end{bmatrix}.
$$

---

## 3. Rotations in Augmented Space
- **Rotations about origin** work as linear transformations (e.g., a $3 \times 3$ matrix $R$).
- To express **rotations about arbitrary points**:
  1. **Translate the point of rotation to the origin** (subtract $a$ via translation).
  2. Apply the rotation matrix $R$.
  3. **Translate the origin back to the original point** (add $a$ via translation).

---

### Composite Rotation Matrix
Given the rotation matrix $R$, and translation vector $a = \begin{bmatrix} a_1 \\ a_2 \\ a_3 \end{bmatrix}$:

#### Sequence:
1. **Translate to origin**: $T_{-\mathbf{a}}$
   $$
   T_{-\mathbf{a}} = \begin{bmatrix}
   1 & 0 & 0 & -a_1 \\
   0 & 1 & 0 & -a_2 \\
   0 & 0 & 1 & -a_3 \\
   0 & 0 & 0 & 1
   \end{bmatrix}.
   $$
2. **Apply rotation**: $R$
   $$
   R = \begin{bmatrix}
   r_{11} & r_{12} & r_{13} & 0 \\
   r_{21} & r_{22} & r_{23} & 0 \\
   r_{31} & r_{32} & r_{33} & 0 \\
   0 & 0 & 0 & 1
   \end{bmatrix}.
   $$

3. **Translate back**: $T_{\mathbf{a}}$
   $$
   T_{\mathbf{a}} = \begin{bmatrix}
   1 & 0 & 0 & a_1 \\
   0 & 1 & 0 & a_2 \\
   0 & 0 & 1 & a_3 \\
   0 & 0 & 0 & 1
   \end{bmatrix}.
   $$

#### Composite Matrix Representation:
The overall composite transformation matrix is:
$$
T_{\mathbf{a}} R T_{-\mathbf{a}}.
$$

---

## 4. Augmented Vector Space Trade-offs
- **Advantages**:
  - Unified representation for translations and rotations.
  - Compatible with matrix algebra and computational frameworks.
- **Disadvantages**:
  - Non-standard vector space: requires redefining operations like addition and scalar multiplication.
    - Augmented vectors have a "tail" $1$ that remains unchanged during operations.
  - Increased storage and computation cost (extra zeros and ones).

---

## 5. Applications in Computer Graphics
- Translations and rotations are essential tools in graphics.
- Augmented matrix representation allows for uniform and efficient computations.

---

## 6. Conclusion
- Matrix algebra has been successfully extended to represent translations and arbitrary rotations using augmented component spaces.
- Despite trade-offs in complexity and storage, this formulation maintains a uniform language for expressing transformations, preserving the beauty and utility of matrix operations.