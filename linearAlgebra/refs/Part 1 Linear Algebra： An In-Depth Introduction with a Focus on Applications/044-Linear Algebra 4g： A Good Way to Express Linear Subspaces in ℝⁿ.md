## Linear Subspaces in $\mathbb{R}^n$

### 1. Introduction
- This video introduces a direct and explicit way to express linear subspaces in $\mathbb{R}^n$.
- Explicit representations are useful when testing for subspaces or working in the context of decomposition.

---

### 2. Expressing Linear Properties in Subspaces

#### Example 1: Subspace in $\mathbb{R}^3$ (Middle Entry = 0)
- **Verbal Description**:
  - Consider all vectors in $\mathbb{R}^3$ where the middle entry equals zero.
  - Example application: Testing whether a target vector belongs to this subspace involves checking if its middle entry equals zero.
- **Algebraic Representation (Traditional)**:  
  Represent the vector as $\begin{bmatrix} a \\ b \\ c \end{bmatrix}$, with the condition $b = 0$.
- **Direct Algebraic Form**:
  $$ 
  \begin{bmatrix} 
  \alpha \\ 
  0 \\ 
  \beta 
  \end{bmatrix}, 
  \quad \alpha, \beta \in \mathbb{R}. 
  $$
  - The explicit inclusion of the zero makes the condition clear: the middle entry is always zero.
  - This form translates naturally into words: the middle entry is zero, while the first and third entries can take on any values.

---

#### Example 2: Subspace in $\mathbb{R}^3$ (Second Entry Equals Five Times the First)
- **Condition**:
  - The second entry equals five times the first entry ($b = 5a$).
- **Direct Algebraic Representation**:
  $$ 
  \begin{bmatrix} 
  \alpha \\ 
  5\alpha \\ 
  \beta 
  \end{bmatrix}, 
  \quad \alpha, \beta \in \mathbb{R}.
  $$
  - Interpretation: The first entry, $\alpha$, determines the second entry as $5\alpha$, while the third entry can be anything.
- **Alternate Forms**:
  - The same subspace can be expressed as:
    $$ 
    \begin{bmatrix} 
    \alpha \\ 
    \frac{\alpha}{5} \\ 
    \gamma 
    \end{bmatrix}, \quad \alpha, \gamma \in \mathbb{R}.
    $$
  - Both forms describe the same subspace, as mathematical expressions for subspaces are not unique.

---

#### Example 3: Subspace in $\mathbb{R}^3$ (Middle Entry = Average of Other Two)
- **Condition**:
  - The middle entry is the average of the first and third entries ($b = \frac{a + c}{2}$).
- **Direct Algebraic Representation**:
  $$ 
  \begin{bmatrix} 
  \alpha \\ 
  \frac{\alpha + \beta}{2} \\ 
  \beta 
  \end{bmatrix}, 
  \quad \alpha, \beta \in \mathbb{R}.
  $$
  - Interpretation: The middle entry is explicitly identified as the average of the first and third entries.

#### Testing Membership of a Vector:
- **Example**:
  Consider the vector $\begin{bmatrix} 11 \\ 15 \\ 19 \end{bmatrix}$.
  - Let $\alpha = 11$ and $\beta = 19$.
  - Check the middle value: $\frac{11 + 19}{2} = 15$.
  - The vector belongs to this subspace.

---

### 3. Combining Multiple Properties

#### Example 4: Subspace in $\mathbb{R}^3$ (Multiple Conditions)
- **Conditions**:
  1. Middle entry equals zero ($b = 0$).
  2. Last entry equals four times the first entry ($c = 4a$).
- **Direct Algebraic Representation**:
  $$ 
  \begin{bmatrix} 
  \alpha \\ 
  0 \\ 
  4\alpha 
  \end{bmatrix}, 
  \quad \alpha \in \mathbb{R}.
  $$
  - Interpretation: The first entry, $\alpha$, determines the remaining entries under the given constraints.

---

### 4. Summary

- While traditional algebraic forms for subspaces (e.g., defining conditions like $b=0$) are valid, direct representations (e.g., $\begin{bmatrix} \alpha \\ 0 \\ \beta \end{bmatrix}$) provide clearer insights.
- Explicit representations:
  1. Encode all conditions directly into the vector.
  2. Simplify testing for vector membership in subspaces.
  3. Are more intuitive for decomposition problems.
  
- **Key Takeaway**: Expressing subspaces explicitly balances compactness with clarity, and it is particularly effective for understanding and solving decomposition problems.