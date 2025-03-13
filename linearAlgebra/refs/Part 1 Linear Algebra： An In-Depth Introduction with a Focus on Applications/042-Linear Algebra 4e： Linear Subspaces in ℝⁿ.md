## Common Template for Linear Properties in $\mathbb{R}^n$

### Introduction
- Linear properties can be described using a **common template**.
- Linear properties are synonymous with **linear subspaces**.
- A **linear property** characterizes vectors that form a subspace due to closure under addition and scalar multiplication.

### Examples of Linear Properties
#### 1. Middle Entry Equals Zero
- Let a vector be $\begin{bmatrix} a \\ b \\ c \end{bmatrix}$.
- Property: Second entry is zero.
  $$
  b = 0
  $$
- Algebraically, this is represented as one linear equation.

#### 2. Second Entry is 5 Times the First
- Property: The second entry is 5 times the first.
  $$
  b = 5a
  $$
- Can be rewritten as:
  $$
  5a - b = 0
  $$

#### 3. Middle Entry is the Average of First and Third
- Property: The middle entry is the average of the first and third.
  $$
  b = \frac{a + c}{2}
  $$
- Can be rewritten as:
  $$
  \frac{1}{2}a - b + \frac{1}{2}c = 0
  $$

### Common Template for Linear Properties
- All these linear properties can be expressed as:
  - **A linear combination of coefficients equals zero**, e.g.,:
    $$
    \alpha a + \beta b + \gamma c = 0
    $$
- This template captures the fundamental structure of all linear properties.

### Non-Linear Properties as Counterexamples
1. **First Entry Equals One**
   - $a = 1$ does **not** fit the template $\text{linear combination} = 0$.
   - It represents a condition, not a linear subspace.

2. **Second Entry is One Greater Than the First**
   - $b = a + 1$ does **not** fit the form $\text{linear combination} = 0$.

3. **All Entries are Even**
   - This is not expressible as a linear combination of coefficients equaling zero.

### Intersection of Linear Properties
- Combining multiple linear properties results in another linear property.
- Example:
  - First property: $b = 0 \implies b = 0$.
  - Second property: $c = 3a \implies 3a - c = 0$.
  - Combined system:
    $$
    \begin{cases} 
    b = 0 \\
    3a - c = 0
    \end{cases}
    $$
  - Represents an intersection of two subspaces, which is also a subspace.

### Significance of the Template
1. Every linear property in $\mathbb{R}^n$ adheres to the form **linear combination of coefficients equals zero**.
2. This simplifies the characterization of linear subspaces in higher dimensions.
3. Even for richer vector spaces like **functions** and **polynomials**, similar templates often exist for subspaces.

### Next Steps
- Moving to polynomial spaces and function spaces, we will see similar templates.
- Polynomials and functions provide a **richer set of examples** to explore the concept of linear properties.