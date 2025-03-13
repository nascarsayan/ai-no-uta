## Problem Formulation and Geometric Intuition in Linear Systems

### 1. Motivation for the Study
- This discussion introduces a linear system to motivate future topics.
- Goal: Formulate a problem without an immediate solution and explore the underlying geometry.

---

### 2. The Linear System
- The system is analogous to a previously seen system.
- Key feature: **No easily obtainable solution**.

#### Observation:
- Values of $x$ and $y$ that satisfy the first two equations are $1$ and $1$.
- However, these values satisfy the third equation but **not the fourth equation**.
- Conclusion: The system has **no solution**.

#### Reason:
- The **right-hand side** of the equations is not in the **column space** of the matrix.
- This is equivalent to saying it is not in the **span** of the two column vectors.

---

### 3. Geometric Analogy
- **Key Question**: What does this mean geometrically?

#### Perspective:
- Solving the system is like attempting to **decompose a vector** (not in the plane) into a linear combination of two vectors within the plane.
- This is geometrically **impossible** because:
  - The two vectors span only the plane.
  - They cannot represent any vector outside the plane.

### 4. Closest Approximation
- Instead of solving the system exactly, we ask:
  - **How close can we get to matching the vector in question?**
  
#### Geometric Answer:
- Drop a **perpendicular line** from the given vector to the plane defined by the span of the two column vectors.
- The intersection point on the plane gives the **closest vector possible**.

---

### 5. Dissatisfaction and Approximation
- **Why is this unsatisfactory?**
  - We don't achieve the goal of exactly decomposing the vector.
  - But we find the best possible **approximate solution**.

#### Moving Forward:
- This introduces the idea of solving **decomposition problems** as accurately as possible.

---

### 6. Generalizing to $\mathbb{R}^n$
- Extending this analogy to $\mathbb{R}^n$ considers these questions:
  - Can we get close to the "target" vector, even if we can't match it exactly?
  
#### The Challenge:
- In $\mathbb{R}^n$, the notion of "closeness" is not as intuitive.
- Without geometric constructs, **proximity** between vectors in $\mathbb{R}^n$ needs formalization.

---

### 7. Defining Proximity in $\mathbb{R}^n$
- A possible measure of proximity for vectors $a$ and $b$ could be:
  
  $$
  \sqrt{(a_1 - b_1)^2 + (a_2 - b_2)^2 + \dots}
  $$

- This is the **Euclidean norm**, though it initially feels **arbitrary**.

#### Need for Generalization:
- We seek a systematic way to define **distance and proximity** for all types of vector spaces:
  - Beyond $\mathbb{R}^n$.
  - For objects like **polynomials** or **functions**.

---

### 8. Systematic Approach: Inner Product
- In **linear algebra**, the concept of **distance** arises from the **inner product**.
- **Inner Product**:
  - Generalizes notions of geometry to abstract vector spaces.
  - Allows systematic ways to solve approximate problems in over-defined systems.
  
---

### 9. Application and Next Steps
- Distance and inner products are vital tools with thousands of applications.
- This video introduces the motivation for:
  - Studying the **inner product**.
  - Understanding how it connects geometry and linear algebra.

