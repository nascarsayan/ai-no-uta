# Notes on Null Space and Linear Transformations

## 1. Introduction to Null Space and Inverse of Linear Transformations
- Transitioning from the study of eigenvalues and eigenvectors to understanding **null space** and **inverse of a linear transformation**.
- These are two closely related and important concepts.

---

## 2. Null Space of a Set of Vectors
- Definition: The **null space** consists of all linear combinations of a set of vectors that result in the **zero vector**.
- Properties:
  1. The null space is a **vector space**.
  2. It is **closed under addition** and **multiplication by scalars**:
    - $v_1, v_2 \in \text{null space} \implies v_1 + v_2 \in \text{null space}$.
    - $\alpha v \in \text{null space}$ for any scalar $\alpha$.
  3. The null space's **dimension** depends on the number of **linear dependencies** among the vectors:
     - Linearly independent vectors $\implies$ trivial null space (only **zero vector** exists).
     - More dependencies $\implies$ larger null space dimension.

---

## 3. Null Space of a Linear Transformation
- **Definition**: For a linear transformation $T$, the null space is the set of all vectors $v$ such that $T(v) = 0$.  
  That is:  
  $$
  \text{Null Space} = \{ v \ | \ T(v) = 0 \}
  $$
- **Why is the null space a vector space?**
  1. The **zero vector** always satisfies $T(0) = 0$.
  2. The space is closed under addition and scalar multiplication (proven using linearity of $T$):
     $$
     T(v_1 + v_2) = T(v_1) + T(v_2) = 0 + 0 = 0.
     $$  
     $$
     T(\alpha v) = \alpha T(v) = \alpha \cdot 0 = 0.
     $$
- **Connection**: Null space relates to linear independence and spans of vectors.

---

## 4. Examples of Null Spaces
### 4.1 Reflection
- **Description**: Reflection about a line or axis.  
- **Null Space**: Only the **zero vector** is sent to 0 (trivial null space).

### 4.2 Projection
- **Description**: Project a vector onto a line.  
- **Null Space**: All vectors **perpendicular** to the projection line are in the null space.

### 4.3 Rotation by an Angle
- **Description**: Rotate vectors by an arbitrary angle.  
- **Null Space**: No vectors, except the zero vector, are sent to zero. Null space is trivial.

### 4.4 Translation
- **Description**: Shift vectors by a fixed amount.  
- **Null Space**: Not applicable, as translation is **not a linear transformation**.

### 4.5 Derivative Operator
- **First Derivative**:
  - The null space is the set of **constant functions**.
  - Example: $f'(x) = 0 \implies f(x) = c$.
- **Second Derivative**:
  - The null space is the set of **linear functions**.
  - Example: $f''(x) = 0 \implies f(x) = ax + b$.

### 4.6 Dilation
- **Description**: Scaling vectors (expansion or contraction).  
- **Null Space**: Trivial null space (only the zero vector is sent to zero).

---

## 5. Connection to Eigenvalues
- The **null space** can be viewed as the **eigenspace** corresponding to the **zero eigenvalue**.  
  This reveals a deeper relationship between eigenvectors and null space.

---

## 6. Null Space of a Matrix
- **Linear Transformations in $\mathbb{R}^n$**: Represented as matrix-vector products.
- Finding the null space of a transformation corresponds to solving the system:  
  $$
  A \mathbf{x} = 0,
  $$
  where $A$ is a matrix, and $\mathbf{x}$ is the vector.  
- **Existing Perspectives**:
  1. The null space can be thought of as solving for combinations of columns that result in the zero vector:
     $$
     \mathbf{x}_1 \cdot \text{col}_1 + \mathbf{x}_2 \cdot \text{col}_2 + \dots + \mathbf{x}_n \cdot \text{col}_n = \mathbf{0}.
     $$
  2. Alternatively, it connects to broader notions of linear transformations.

---

## 7. Summary
- The null space explains relationships within a linear system or transformation.
- Key properties:
  - It is always a **vector space**.
  - Its size and dimension are linked with dependencies and degrees of freedom in the system.
- When analyzing matrices, the null space bridges two perspectives:
  1. Classical linear systems ($A \mathbf{x} = 0$ as a system of equations).
  2. Linear transformations as actions on vector spaces.

---

## 8. Preview of Next Concepts
- **Inverse of Linear Transformations**:
  - The next step is to discuss the **inverse** of a matrix or transformation.
  - This concept directly connects to null space and broader ideas of linear algebra.