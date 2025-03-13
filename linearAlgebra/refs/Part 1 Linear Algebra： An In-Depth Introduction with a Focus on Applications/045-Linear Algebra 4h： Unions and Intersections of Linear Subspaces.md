# Notes on Unions and Intersections of Subspaces

## Introduction

- The discussion focuses on two logical questions about linear subspaces:
  1. Is the **union** of two linear subspaces itself a linear subspace?
  2. Is the **intersection** of two linear subspaces itself a linear subspace?

- **Set theory perspective** provides the foundation of the analysis:
  - Union (\*) represents combining elements from two sets.
  - Intersection (\&) represents the common elements between two sets.

---

## 1. **Union of Two Subspaces**

### Definition:
The **union** of two subspaces includes **all vectors in either one subspace or the other** (or both). 

#### Venn Diagram Representation:
The union is visually represented as the shaded area covering both sets in the diagram.

### Properties of Union in General:

1. **Inclusive**: A vector only needs to belong to one of the sets to be in the union.
   - Logical keyword: **OR**.
    
2. **Not Closed Under Addition**:
    - If a vector is in one subspace and a second vector is in the other, their **sum may not lie in the union**.
    - Example: Adding non-collinear vectors on two distinct lines results in a vector not on either line.

3. **Closed Under Scalar Multiplication**:
    - Any scalar multiple of a vector from the subspaces will still lie in the union because it will remain on the same line.

### Conclusion:
- The **union** of subspaces is **not a linear subspace** because it fails the closure property under addition.

---

## 2. **Intersection of Two Subspaces**

### Definition:
The **intersection** of two subspaces includes **all vectors common to both subspaces**.

#### Venn Diagram Representation:
The intersection is visually represented by the overlapping region of the two sets.

### Properties of Intersection in General:

1. **Exclusive**: A vector must satisfy the conditions of **both subspaces simultaneously** to be in the intersection.
   - Logical keyword: **AND**.

2. **Closed Under Addition**:
    - If \(v_1, v_2 \in S_1 \cap S_2\):
      - \(v_1 + v_2 \in S_1\) because \(S_1\) is closed under addition.
      - \(v_1 + v_2 \in S_2\) because \(S_2\) is closed under addition.
      - Hence, \(v_1 + v_2 \in S_1 \cap S_2\).

3. **Closed Under Scalar Multiplication**:
    - If \(v \in S_1 \cap S_2\) and \(k\) is a scalar:
      - \(kv \in S_1\) because \(S_1\) is closed under scalar multiplication.
      - \(kv \in S_2\) because \(S_2\) is closed under scalar multiplication.
      - Hence, \(kv \in S_1 \cap S_2\).

### Examples:
1. **Zero Vector**: The intersection of two subspaces can include only the zero vector, which forms a trivial subspace.

2. **Planes in 3D**:
   - Consider two planes intersecting at the origin:
     - Their **intersection** is a **line through the origin**, which is a valid subspace.

### Conclusion:
- The **intersection** of subspaces is **always a linear subspace** because it satisfies closure under both addition and scalar multiplication.

---

## 3. **Union vs Intersection: Key Differences**

| **Property**            | **Union**     | **Intersection** |
|--------------------------|---------------|-------------------|
| **Closure under addition** | Not satisfied | Satisfied         |
| **Closure under scalar multiplication** | Satisfied     | Satisfied         |
| **Terminology**          | OR            | AND               |
| **Represents**           | Combination of vectors in either subspace | Common vectors shared by both subspaces |
| **Subspace?**            | No            | Yes               |

---

## 4. Applying Concepts to Linear Subspaces

### Defining a Linear Subspace via Properties:

- A subspace can be characterized using **linear properties** that its elements satisfy.
  
**Example:**
- Subspace in \(\mathbb{R}^3\) defined by:
  - Second component \(= 0\): \(b = 0\),
  - Third component \( = 3 \times \text{first component}\): \(c = 3a\).

### Subspaces and Logical Operations:

1. **Intersection of Linear Properties**:
   - If vectors satisfy property \(P_1\) **AND** \(P_2\), they belong to the subspace defined by the intersection of properties.
   - Multiple conditions combine via logical **AND** (intersection).

2. **Union of Linear Properties**:
   - If vectors satisfy \(P_1\) **OR** \(P_2\), the resulting set does **not** define a subspace because addition isn’t preserved.

---

## 5. Summary

- **Union** of two subspaces is generally **not a linear subspace** because it lacks closure under addition.
- **Intersection** of two subspaces is always a valid linear subspace because it satisfies closure under both addition and scalar multiplication.
- Logical keywords:
  - **OR** leads to unions – typically not subspaces.
  - **AND** leads to intersections – always subspaces.
  
These conclusions about unions and intersections are fundamental to understanding the structure of linear algebra and vector spaces. Further exploration can connect this discussion to subspace dimensions and additional algebraic contexts.