## Example in $\mathbb{R}^n$

### Goal
- Evaluate a linear combination of two vectors in $\mathbb{R}^n$.

### Key Observations
1. **Format Confusion in $\mathbb{R}^n$**:
   - Vectors and their component space representations often have the same format (e.g., triplets of numbers). This can be confusing because it's not immediately clear whether you're looking at the vector itself or its components relative to a basis.

2. **Clarification Techniques**:
   - **Color Coding**: Use different colors for component spaces to differentiate them.
   - **Subscripts**: Write subscripts (e.g., $B$) to indicate components with respect to a basis.

3. **General 3-Step Process** (For Linear Combinations):
   1. Pick a basis and translate all elements of the problem into component space.
   2. Solve the problem in component space to get components of the result.
   3. Translate components back into the original space to get the final result.

---

### Example Walkthrough

#### Problem Setup
We are given two vectors $\mathbf{a}$ and $\mathbf{b}$, and a basis $B$.
- **Vector $\mathbf{a}$**: Directly aligns with the basis, making its components easy to find:
  - Components: $\begin{bmatrix} 0 \\ 1 \\ 0 \end{bmatrix}$.
- **Vector $\mathbf{b}$**: Scaled by 8, leading to components:
  - Components: $\begin{bmatrix} 0 \\ 8 \\ -8 \end{bmatrix}$.

#### Step 1: Translate to Component Space
- We express $\mathbf{a}$ and $\mathbf{b}$ in terms of their components relative to the given basis.

#### Step 2: Solve in Component Space
- The linear combination to compute is:

  $$
  3\mathbf{a} - \mathbf{b}
  $$

- Substituting components:
  - $\mathbf{a} = \begin{bmatrix} 0 \\ 1 \\ 0 \end{bmatrix}, \, \mathbf{b} = \begin{bmatrix} 0 \\ 8 \\ -8 \end{bmatrix}$.
  
  Compute:

  $$
  3\mathbf{a} - \mathbf{b} = 3\begin{bmatrix} 0 \\ 1 \\ 0 \end{bmatrix} - \begin{bmatrix} 0 \\ 8 \\ -8 \end{bmatrix}
  $$

  Result:
  $$
  = \begin{bmatrix} 0 \\ 3 \\ 0 \end{bmatrix} - \begin{bmatrix} 0 \\ 8 \\ -8 \end{bmatrix} = \begin{bmatrix} 0 \\ -5 \\ 8 \end{bmatrix}
  $$

#### Step 3: Translate Back to Original Space
- We now reconstruct the vector in the original space using the basis:
  
  If $\mathbf{v} = \begin{bmatrix} x \\ y \\ z \end{bmatrix}$ are the components, then in terms of the basis $B$, the corresponding vector is:

  $$
  \mathbf{v} = x \mathbf{b}_1 + y \mathbf{b}_2 + z \mathbf{b}_3
  $$

- Substituting $x = 0, y = -5, z = 8$:
  - $-5\mathbf{b}_2 + 8\mathbf{b}_3$ gives the final result.

---

### Final Verification
After solving and reconstruction, the computed answer matches the expected result. This confirms the process.

---

### Key Takeaways
1. Always distinguish between vectors and their component forms to avoid confusion.
2. The 3-step method (translate, solve, retranslate) provides a systematic way to handle computations in $\mathbb{R}^n$.
3. Component spaces are foundational for understanding linear transformations and vector addition.

Next up: **Component Spaces and Linear Transformations** – a richer and more important topic.