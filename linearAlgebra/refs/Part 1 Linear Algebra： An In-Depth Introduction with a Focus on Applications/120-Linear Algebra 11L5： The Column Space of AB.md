## Column Space of the Product $AB$

### Objective:

In this video, the goal is to explore how the column space of the product $AB$ (denoted as matrix $C$) relates to the column spaces of $A$ and $B$. Previously, we considered the null space of $C$ and found that:

1. The null space of $C$ is always the same or larger than the null space of $B$.
2. The null space of $B$ is a subspace of the null space of $C$.

In this video, we aim to relate the **column space of $C$** to the column spaces of $A$ and $B$.

---

### Key Observations:

#### Column Space of $C$ Relates to $A$:
- The columns of $C$ must necessarily reside in the same space as the columns of $A$. 
- This is because, by the definition of matrix multiplication, the columns of $C$ are **linear combinations of the columns of $A$**.

---

### Decomposing Columns of $C$ Using $A$:

#### General Method:
For each column of $C$, we seek a set of coefficients such that **a linear combination of the columns of $A$ results in the corresponding column of $C$**. This involves solving decomposition problems column by column.

#### Example 1: Decomposition of the First Column of $C$
- The first column of $C$ matches the first column of $A$.
- Therefore, the linear combination to represent it is:
  $$
  \text{Coefficients: } \begin{bmatrix} 1 \\ 0 \\ 0 \\ 0 \end{bmatrix}
  $$
- This solution is not unique because:
  - The columns of $A$ are linearly dependent (4 columns in $\mathbb{R}^3$), which guarantees the existence of a non-trivial null space.
  - There are infinitely many possible coefficient sets.

#### Example 2: Decomposition of the Second Column of $C$
- The second column of $B$ is the sum of the first two columns of $A$.
- The coefficients for the linear combination are:
  $$
  \text{Coefficients: } \begin{bmatrix} 1 \\ 1 \\ 0 \\ 0 \end{bmatrix}
  $$

#### Example 3: Decomposition of the Last Column of $C$
- The last column of $C$ does not belong to the column space of $A$.
- This is clear because the last column violates a fundamental property of the column space of $A$:
  - In $A$, the last entry of each column is the sum of the first two entries.
  - In this case, the column in question does not satisfy this property.

---

### Implications and Conclusions:

#### Properties of $C$:
- If $C$ is the product of $A$ and $B$ ($C = AB$), then **all columns of $C$ must be in the column space of $A$**. This is a direct consequence of the definition of matrix multiplication:
  - Each column of $C$ is a linear combination of the columns of $A$.

#### Column Space Relation:
- The column space of $C$ is a **subspace of the column space of $A$**.

#### Further Notes:
- The column space of $C$ can:
  1. Be **smaller** than the column space of $A$.
    - Example: If $B$ is the zero matrix, $C$ becomes the zero matrix, and the column space of $C$ is the trivial space (only the zero vector).
  2. Be **the same** as the column space of $A$.
    - This occurs when $B$ has enough linearly independent columns to fully span the column space of $A$.

---

### Summary:
The column space of $C$ is related to the column space of $A$ such that:
- $\text{Column space of } C \subseteq \text{Column space of } A$.
- The column space of $C$ is always **the same or smaller than** the column space of $A$.