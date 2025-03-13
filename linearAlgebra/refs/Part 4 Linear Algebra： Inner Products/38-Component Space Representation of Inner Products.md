## Inner Products and Component Spaces

### Basis and Inner Products

- Suppose we have:
  - A basis $B$.
  - An inner product with respect to which the basis elements are not necessarily orthogonal or normalized.
  - Two vectors $A$ and $B$ expressed in terms of basis $B$:
    - $A = \alpha_1 E_1 + \alpha_2 E_2 + \alpha_3 E_3$
    - $B = \beta_1 E_1 + \beta_2 E_2 + \beta_3 E_3$

### Expanding the Inner Product

#### Inner Product Definition:

The inner product of $A$ and $B$, $\langle A, B \rangle$, can be expanded as:

$$
\langle A, B \rangle =
\sum_{i=1}^{3} \sum_{j=1}^{3} \alpha_i \beta_j \langle E_i, E_j \rangle
$$

Here:
- $\langle E_i, E_j \rangle$ are the inner products of the basis vectors $E_i$ and $E_j$. 

#### Nine Terms:

- There are $3 \times 3 = 9$ terms resulting from expanding $\langle A, B \rangle$, such as:
  - $\alpha_1 \beta_1 \langle E_1, E_1 \rangle$
  - $\alpha_1 \beta_2 \langle E_1, E_2 \rangle$
  - $\alpha_1 \beta_3 \langle E_1, E_3 \rangle$
  - And so on...

### Matrix Representation

#### Inner Product Matrix:

Define a matrix $M$ where:
$$
M_{ij} = \langle E_i, E_j \rangle
$$

Then, the inner product $\langle A, B \rangle$ can be compactly represented as:
$$
\langle A, B \rangle = \alpha^T M \beta
$$
Where:
- $\alpha = \begin{bmatrix} \alpha_1 \\ \alpha_2 \\ \alpha_3 \end{bmatrix}$ (vector of coefficients of $A$ in component space).
- $\beta = \begin{bmatrix} \beta_1 \\ \beta_2 \\ \beta_3 \end{bmatrix}$ (vector of coefficients of $B$ in component space).

#### Explanation of the Matrix $M$:
- $M$ encapsulates all the information about the inner product and the basis choice.
- Once $M$ is computed, all inner products can be calculated using matrix-vector multiplication without directly evaluating $\langle E_i, E_j \rangle$ each time.

### Positive Definiteness of the Matrix $M$

#### Definition Link:

For any vector $A$:
$$
\langle A, A \rangle = \alpha^T M \alpha
$$

#### Explanation:

- $\langle A, A \rangle$ is the inner product of $A$ with itself.
- By definition of an inner product, $\langle A, A \rangle > 0$ for all non-zero $A$.
- Therefore, $M$ is a positive definite matrix.

#### Generalization for Higher Dimensions:

In $n$-dimensional space:
$$
\langle A, A \rangle = \alpha^T M \alpha > 0
$$
for any non-zero $\alpha \in \mathbb{R}^n$.

### Symmetry and Formula Recap

#### Symmetry of $M$:

- If the inner product is symmetric, then $M_{ij} = M_{ji}$, making $M$ a symmetric matrix.

#### Inner Product Matrix Recap:

$$
\langle A, B \rangle = \alpha^T M \beta
$$
Where $M$ depends on the inner product and the choice of basis.

### Importance of Matrix Representation in Linear Algebra

#### Component Spaces:

- Inner products in component spaces are represented by matrix products.
- This is analogous to how linear transformations are represented by matrices.

#### Universality of Matrix Representation:

- Matrix representations appear naturally in linear algebra calculations (e.g., inner products, linear transformations).
- Matrix multiplication serves as a powerful formalism to encode relationships in component spaces.

### Observations on Matrix Multiplication

- Matrix multiplication may initially seem awkward, but its structure naturally arises in linear algebra computations.
- The need for the **transpose** in inner product formulas ensures compatibility with matrix multiplication but introduces aesthetic asymmetry.

#### Summary of Key Points:

- An inner product matrix $M$ captures the relationship between basis elements and is essential for computing inner products efficiently.
- Positive definiteness and symmetry make $M$ a particularly special matrix in inner product theory.
- Matrix operations concisely express computations in component spaces across various applications in linear algebra.