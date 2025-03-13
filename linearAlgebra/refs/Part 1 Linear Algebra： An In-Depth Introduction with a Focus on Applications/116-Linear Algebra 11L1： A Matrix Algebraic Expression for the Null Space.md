## Understanding the Null Space using Matrix Algebra

### Description of Null Space

- Null space can be described in the language of matrix algebra.
- To illustrate, consider two matrices, $A$ and $B$, with their product $C$:

### Matrix Multiplication Example

- Compute the resulting product matrix $C = AB$.
- In this particular case, the resulting matrix $C$ consists entirely of zeros.

### Key Concept

1. **Matrix Multiplication and Zeros**:
    - Unlike ordinary number multiplication, where a product is $0$ only when at least one multiplicand is $0$, matrix multiplication can give a zero matrix even if neither matrix is zero.
    - This happens when **The columns of one matrix belong to the null space of the other**.

### Null Space Perspective

- **Null Space**:
    - The null space of a matrix $A$ consists of all vectors $\mathbf{x}$ such that $A\mathbf{x} = \mathbf{0}$.
  
- **Observation in Example**:
    - The columns of matrix $B$ lie in the null space of $A$. This explains why $AB = \mathbf{0}$ (the zero matrix).

### Row Reduced Echelon Form (RREF) and Null Space

- Matrix $A$ in **Row Reduced Echelon Form** makes the null space easier to observe.
- By design, the columns of $B$ were chosen to belong to the null space of $A$, ensuring that their linear combinations also lie in the null space.

### Column Perspective on Matrix Multiplication

- The columns of matrix $B$ are linear combinations of the columns of matrix $A$:
    - The coefficients for these linear combinations come from the elements in matrix $B$.
    - If these coefficients belong to the null space of $A$, the resulting column contributions sum to $\mathbf{0}$.

### Matrix Representation of Null Space

1. Null space vectors can be combined into a matrix, $N$, representing the null space of a given matrix.

    $$
    N = 
    \begin{bmatrix}
    \mathbf{v}_1 & \mathbf{v}_2 & \cdots & \mathbf{v}_k
    \end{bmatrix}
    $$

    Where $\mathbf{v}_1, \mathbf{v}_2, \dots, \mathbf{v}_k$ are basis vectors for the null space.

2. **Conditions for $N$ to Represent the Null Space**:
    - The matrix $N$ must have as many columns as the dimension of the null space.
    - Its columns must be linearly independent.

### Compact Algebraic Expression

- A concise algebraic expression for the null space is:
    $$
    AN = \mathbf{0}
    $$
    Here, $N$ captures all the basis vectors of the null space.

### Dimensionality Considerations

- Important caveats for $N$:
    - It cannot have extra columns beyond the dimension of the null space.
    - Its columns must not be linearly dependent.

### Efficacy of Matrix Algebra

- Matrix algebra offers a compact and precise language to describe concepts like the null space:
    - Verbally: The null space is the set of all coefficients such that their linear combinations of matrix columns result in $\mathbf{0}$.
    - Algebraically: $AN = \mathbf{0}$.

### Summary

- The product of two non-zero matrices can yield the zero matrix if the columns of the second matrix lie in the null space of the first.
- Representing the null space with a matrix $N$ is a powerful and concise way to describe it algebraically.
- This showcases the potency of matrix algebra for clear and effective communication of linear algebra concepts.