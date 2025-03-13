# Systems of Linear Equations as Decomposition Problems

## 1. Motivation

- The video introduces the concept that **systems of linear equations** can be thought of as **decomposition problems**.
- It aims to justify prior discussions because of the undeniable importance of linear systems.
- Linear systems and decomposition problems are equivalent:
  - Solving a linear system provides the same solutions as solving a decomposition problem.
- **Applications:** Decomposition problems appear in areas like **signal processing**.

---

## 2. Traditional Approach to Linear Systems

- **Old Perspective:** Linear systems were traditionally treated as a collection of individual equations.
    - **Operations:** 
        - Adding a multiple of one equation to another.
        - Multiplying an equation by a scalar.
        - Switching the order of equations.
    - This perspective aligns with **Gaussian elimination**.

---

## 3. New Perspective: Linear Systems as Decomposition Problems

- The video introduces a new dominant perspective: **linear systems are decomposition problems**.

### Example:
- **System of Linear Equations:**
    $$
    \begin{aligned}
    1x + 2y + 3z + 3t &= 12, \\
    2x + 4y + 6z + 6t &= 18, \\
    3x + 6y + 9z + 9t &= 24.
    \end{aligned}
    $$
- The equations above are reinterpreted as a **decomposition problem**:
    - Decomposition problem involves finding coefficients (\(x, y, z, t\)) for a **target vector** formed using **basis vectors**.

#### Transformation into Decomposition Problem

- Target vector:
    $$
    \begin{bmatrix} 12 \\ 18 \\ 24 \end{bmatrix}
    $$
- Coefficient vectors correspond to variables:
    $$
    x \begin{bmatrix} 1 \\ 2 \\ 3 \end{bmatrix} + 
    y \begin{bmatrix} 2 \\ 4 \\ 6 \end{bmatrix} +
    z \begin{bmatrix} 3 \\ 6 \\ 9 \end{bmatrix} +
    t \begin{bmatrix} 3 \\ 6 \\ 9 \end{bmatrix} =
    \begin{bmatrix} 12 \\ 18 \\ 24 \end{bmatrix}
    $$

---

## 4. Equivalence of the Two Approaches

- Solving the linear system is equivalent to solving the decomposition problem.
- **Similarities:**
  - Both involve finding the same sets of numbers (\(x, y, z, t\)):
      - Linear systems are solved by simultaneously satisfying the three equations.
      - Decomposition problems involve matching the entries of the linear combination to the target vector.

#### Example Condition:
For the first entry:
$$
12 = x \cdot 1 + y \cdot 2 + z \cdot 3 + t \cdot 3.
$$
This condition is equivalent to the first equation in the system.

---

## 5. Types of Solutions in Linear Systems and Decomposition Problems

- **Nice Case:** Problems with unique solutions.
- **What Can Go Wrong?**
  1. **No solutions:** The system or target vector cannot be satisfied.  
  2. **Infinitely many solutions:** When there is more than one solution, there are infinitely many.

---

## 6. Addressing Non-Nice Scenarios

1. **No Solutions:**
   - Requires understanding when no solution exists for the system or decomposition problem.

2. **Infinite Solutions:**
   - When infinite solutions exist:
     - Represent the solutions compactly using mathematical expressions.
     - Explore the idea that there are **infinitely many solutions** once more than one solution exists.

---

## 7. Fundamental Concepts

- The exploration of these "non-nice" cases leads to foundational ideas in **linear algebra**:
    - **Linear dependence**
    - **Dimension**
    - **Basis**
- These concepts form the **beauty and power of linear algebra**.

---

## 8. Moving Forward in the Course

- Upcoming chapters focus on:
    - **No solutions** scenarios.
    - **Infinitely many solutions** scenarios.
    - Deeper insights into linear dependencies, dimensions, and bases, which are key to understanding linear systems in the real world.

