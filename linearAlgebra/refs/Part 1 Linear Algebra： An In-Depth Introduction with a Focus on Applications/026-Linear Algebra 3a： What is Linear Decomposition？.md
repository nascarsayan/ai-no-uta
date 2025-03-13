# Notes on Linear Decomposition

## 1. Importance of Linear Decomposition

- **Duration**: Linear decomposition is a central topic in linear algebra, comprising roughly one-third of the entire course.
- **Foundational Role**: All subsequent topics in linear algebra rely on decomposition.
- **Analogy**: Decomposition is the equivalent of **dribbling in basketball**:
  - It may not be the ultimate goal.
  - However, it's something you do most of the time.

---

## 2. Why is Decomposition Ubiquitous in Linear Algebra?

### Two Key Reasons:

1. **Applied Contexts**:
   - Many applied problems naturally arise as decomposition problems.
   - Example: Any linear system can be viewed as a decomposition problem.
   
2. **Breaking Down Complexity**:
   - Decomposition helps us understand complicated objects by breaking them into simpler components.
   - For any complex object, step one is to **decompose it into a sum of simple objects**, which is exactly what linear decomposition achieves.

---

## 3. What is Linear Decomposition?

- **Opposite of Evaluating Linear Combinations**: 
  - When evaluating linear combinations:
    - You are given vectors and the coefficients (scalars for combination).
    - Objective: Compute the result of the combination.
  - When performing decomposition:
    - You are given the result vector and the basis vectors.
    - Objective: Determine the coefficients that reconstruct the result.

---

## 4. Example: Understanding Flavor as Decomposition (Wine Tasting Analogy)

- The video showed people decomposing the **complex flavor of wine** into **simple characteristics** like:
  - Jammy red fruit,
  - Earthiness,
  - Vanilla or spices.
  
- Key Insight:
  - Decomposition is not about discovering **unknown ingredients from scratch**.
  - It's about quantifying **how much of each known component is present**.

---

## 5. Decomposition Within Linear Algebra

- In the geometric representation:
  - **Objective**: Represent a given vector $\mathbf{C}$ as a linear combination of known basis vectors $\mathbf{A}$ and $\mathbf{B}$:
    $$
    \mathbf{C} = x_1\mathbf{A} + x_2\mathbf{B}
    $$
  - **Task**: Determine the coefficients ($x_1$, $x_2$).

---

## 6. Decomposition vs. Combination: Schematic Difference

### Evaluating Linear Combinations:
- **Inputs**:
  - Vectors ($\mathbf{A}, \mathbf{B}$),
  - Coefficients ($x_1$, $x_2$).
- **Output**:
  - Resultant vector $\mathbf{C}$:
    $$
    \mathbf{C} = x_1\mathbf{A} + x_2\mathbf{B}
    $$

### Performing Decomposition:
- **Inputs**:
  - Resultant vector $\mathbf{C}$,
  - Basis vectors ($\mathbf{A}, \mathbf{B}$).
- **Output**:
  - Unknown coefficients ($x_1$, $x_2$).

---

## 7. Procedural Summary of Linear Decomposition

- **Given**:
  - Resultant vector $\mathbf{C}$.
  - Basis vectors ($\mathbf{A}, \mathbf{B}$).
- **Find**: The coefficients of the linear combination:
  $$
  \mathbf{C} = x_1\mathbf{A} + x_2\mathbf{B}
  $$

- **Importance**:
  - Decomposition allows you to express $\mathbf{C}$ in the **space of geometric vectors** defined by $\mathbf{A}$ and $\mathbf{B}$.
  - Without knowing the basis vectors ($\mathbf{A}, \mathbf{B}$), decomposition is **nonsensical**.

