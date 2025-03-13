## Formula for the Inverse of a Matrix Product

### Introduction
- **Purpose**: Discover the formula for the inverse of a matrix product.
- **Highlights**:
  1. No visual matrices—only algebraic reasoning.
  2. Insights about linear algebra, mathematics, and life.
  3. Neat result deserving deeper exploration.

---

### Problem Setup
- Two invertible matrices: $A$ and $B$.
- Known inverses: $A^{-1}$ and $B^{-1}$.
- Task: Find the inverse of the product $AB$.
- **Approach**:
  - Avoiding Gaussian elimination, as it is time-consuming.
  - Utilize the known inverses $A^{-1}$ and $B^{-1}$.

---

### Initial Observation
- **False Formula**: $(AB)^{-1} \neq A^{-1} B^{-1}$.
- Reason: Matrix multiplication lacks **commutativity** ($AB \neq BA$). This complicates inverse calculations but makes them more interesting.

---

### Life Analogy: Actions and Their Inverses
- **Actions**:
  1. Take a step forward.
  2. Turn left.
- **Inverses**:
  - Step back (inverse of forward).
  - Turn right (inverse of left).

#### Sequence of Actions
1. Perform actions:
   - Step forward, then turn left.
2. Perform inverses:
   - Step back, then turn right.

#### Result:
- **Mismatch**: Actions performed in order cannot be undone by simply reversing the individual steps. They must be undone in **reverse order**.

---

### Formula Derivation
- **Correct Formula**:
  $$
  (AB)^{-1} = B^{-1}A^{-1}
  $$

- Explanation:
  - To reverse composite actions, reverse the order of individual inverses.
  - Undo $B$ first, then $A$.

---

### Formal Algebraic Proof
#### Idea:
- Show that multiplying $AB$ by $B^{-1}A^{-1}$ yields the identity matrix.

#### Proof:
$$
AB \cdot B^{-1}A^{-1} = (A \cdot B) \cdot (B^{-1} \cdot A^{-1})
$$

- **Step-by-step**:
  - $B \cdot B^{-1} = I$ (identity matrix).
  - $I \cdot A^{-1} = A^{-1}$.
  - $A \cdot A^{-1} = I$.

Thus:
$$
AB \cdot B^{-1}A^{-1} = I
$$

- Conclusion: $B^{-1}A^{-1}$ is indeed the inverse of $AB$.

---

### Generalization: Inverse of a Product of Multiple Matrices
#### Formula:
$$
(A \cdot B \cdot C)^{-1} = C^{-1}B^{-1}A^{-1}
$$

#### Explanation:
- Reverse the order of inverses: actions undone in the opposite sequence.

---

### Life Metaphor: Building and Demolishing
- **Construction**:
  1. Frame the wall.
  2. Install drywall.
  3. Mount blackboard.
- **Demolition**:
  - Reverse construction order.
  - Remove blackboard, then drywall, then frame.

#### Key Insight:
Order matters—actions are undoable only in reverse. Analogous to matrix products and their inverses.

---

### Fundamental Intuition
- **Reason**: Non-commutativity drives the need to reverse the sequence for inverses.
- **Visualization**: Matrices as actions—a highly intuitive perspective on algebra.