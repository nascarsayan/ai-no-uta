## Dot Product in Component Space Representation

### Introduction
- **Objective**: Discuss the component space representation of the dot product, with respect to a Cartesian basis.
- The main formula:
  $$
  \mathbf{v} \cdot \mathbf{w} = \|\mathbf{v}\| \|\mathbf{w}\| \cos \theta
  $$

### Setup
- Consider vectors $\mathbf{v}$ and $\mathbf{w}$:
    - $\mathbf{v}$ has components $\alpha_1, \alpha_2$ (organized as a vector $\alpha$ in $\mathbb{R}^2$).
    - $\mathbf{w}$ has components $\beta_1, \beta_2$ (organized as a vector $\beta$ in $\mathbb{R}^2$).
- Represent $\mathbf{v}$ and $\mathbf{w}$ as $2 \times 1$ matrices:
    - $\alpha = \begin{bmatrix} \alpha_1 \\ \alpha_2 \end{bmatrix}$, 
    - $\beta = \begin{bmatrix} \beta_1 \\ \beta_2 \end{bmatrix}$.

### Dot Product Expression in Component Form
- Geometrically:
  $$
  \mathbf{v} \cdot \mathbf{w} = \|\mathbf{v}\| \|\mathbf{w}\| \cos \theta
  $$
- In component space with respect to a basis:
  $$
  \mathbf{v} \cdot \mathbf{w} = \alpha_1 \beta_1 + \alpha_2 \beta_2
  $$
- Generalizing to $\mathbb{R}^3$, an additional term $\alpha_3 \beta_3$ is added:
  $$
  \mathbf{v} \cdot \mathbf{w} = \alpha_1 \beta_1 + \alpha_2 \beta_2 + \alpha_3 \beta_3
  $$

### Matrix Representation of the Dot Product
- In matrix terms:
  $$
  \mathbf{v} \cdot \mathbf{w} = \alpha^T \beta
  $$
  Which simplifies to:
  $$
  \alpha_1 \beta_1 + \alpha_2 \beta_2
  $$
- Alternatively, written as:
  $$
  \beta^T \alpha
  $$

### Orthogonality
- **Orthogonal Vectors**:
  - Two vectors are orthogonal if and only if their dot product is zero:
    $$
    \mathbf{v} \cdot \mathbf{w} = 0 \implies \cos 90^\circ = 0
    $$
  - This works both ways: 
    - If $\mathbf{v} \cdot \mathbf{w} = 0$, the angle between vectors is $90^\circ$.
- **Example**:
  - Given $\mathbf{v} = \begin{bmatrix} 3 \\ 4 \end{bmatrix}$, find a vector orthogonal to it.
    - Solution: Switch the entries and change the sign of one:
      $$
      \mathbf{w} = \begin{bmatrix} -4 \\ 3 \end{bmatrix}
      $$
      Verify:
      $$
      \mathbf{v} \cdot \mathbf{w} = 3 \cdot (-4) + 4 \cdot 3 = -12 + 12 = 0
      $$

### Generalization to Higher Dimensions
- The principles of orthogonality and dot products generalize neatly to $\mathbb{R}^n$:
    $$
    \mathbf{v} \cdot \mathbf{w} = \sum_{i=1}^n \alpha_i \beta_i
    $$

---

## Relation Between Dot Product and Angles
- The cosine of the angle $\theta$ between two vectors:
  $$
  \cos \theta = \frac{\mathbf{v} \cdot \mathbf{w}}{\|\mathbf{v}\| \|\mathbf{w}\|}
  $$
- Using components:
  $$
  \mathbf{v} \cdot \mathbf{w} = \alpha_1 \beta_1 + \alpha_2 \beta_2
  $$
  $$
  \|\mathbf{v}\| = \sqrt{\alpha_1^2 + \alpha_2^2}, \quad \|\mathbf{w}\| = \sqrt{\beta_1^2 + \beta_2^2}
  $$
  Substituting:
  $$
  \cos \theta = \frac{\alpha_1 \beta_1 + \alpha_2 \beta_2}{\sqrt{\alpha_1^2 + \alpha_2^2} \sqrt{\beta_1^2 + \beta_2^2}}
  $$

---

## Length of a Vector
- The length squared of a vector $\mathbf{v}$ is consistent with the dot product:
  $$
  \|\mathbf{v}\|^2 = \mathbf{v} \cdot \mathbf{v} = \alpha_1^2 + \alpha_2^2
  $$
- Matrix representation:
  $$
  \|\mathbf{v}\|^2 = \alpha^T \alpha
  $$

---

## Implications for Matrix Multiplication
- Dot product ties directly to the way matrices are multiplied (row and column operations):
  - Example:
    $$
    \text{Row vector} \cdot \text{Column vector}
    $$

