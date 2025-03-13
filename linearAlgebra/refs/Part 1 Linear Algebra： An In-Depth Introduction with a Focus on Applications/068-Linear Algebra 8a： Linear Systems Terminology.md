## Chapter Overview: Linear Systems

### Introduction
- **Goal**: Solve various linear systems (e.g., Ax = b).
- **Approach**: 
  - No Gaussian Elimination; simple systems where solutions can be determined by visual inspection.
  - Focus is on understanding the **structure** of solutions rather than number manipulation.

### Key Insights:
1. Knowing the structure of the solution is more important than the computation method.
2. Simple systems are used in this chapter to familiarize with solution structures.
   
---

## Terminology and Concepts

### 1. Column Space
- **Definition**: The column space of a matrix is the **span** of its column vectors.
- **Notation**:
  - Column space is denoted by $R$ (stands for "range").
- **Explanation**: 
  - A system has a solution if the right-hand side vector is in the column space of the matrix (i.e., it can be expressed as a linear combination of the column vectors).

### Example:
In a linear system of the form:
$$
A \cdot \vec{x} = \vec{b}
$$
- The column space represents all possible values of $\vec{b}$ achievable by multiplying $A$ with some $\vec{x}$.

---

### 2. Null Space
- **Definition**: The null space of a matrix consists of all vectors $\vec{x}$ that satisfy:
  $$
  A \cdot \vec{x} = \vec{0}
  $$
- **Properties**:
  - The null space is a subspace of $\mathbb{R}^n$.
  - It comprises all linear combinations of vectors that map to the zero vector under the transformation $A$.
- **Notation**: Denoted by $N$.

### Null Space and Context:
- Similar to the concept of spans but focuses on solutions mapping to zero.
- If unfamiliar with null spaces, review prior lessons on this.

---

## Bread and Butter of Linear Systems
- **Column Space** and **Null Space** are foundational concepts.
- Represent solution conditions and properties of the system.

---

## Matrix Form for Linear Systems

### Transition to Matrix Notation
- Traditional form:
  $$
  a_{11}x_1 + a_{12}x_2 + \ldots + a_{1n}x_n = b_1
  $$
  becomes:
  $$
  A \cdot \vec{x} = \vec{b}
  $$
  where:
  - $A$ is the coefficient matrix.
  - $\vec{x}$ is the column vector of variables.
  - $\vec{b}$ is the result vector.

### Advantages:
1. Simplifies representation by condensing information into a matrix.
2. Facilitates operations like matrix multiplication (introduced in future chapters).

### Visualizing the Structure:
- Coefficients $A$ are organized into a matrix.
- Variables $\vec{x}$ are written as a vertical column vector.
- Right-hand side $\vec{b}$ appears as before.

---

## Matrix Multiplication (Teaser)
- Eventually, the notation $A \cdot \vec{x} = \vec{b}$ will be interpreted using **matrix multiplication**.
- **Excitement Ahead**:
  - Matrix multiplication allows for easier manipulation and computation of solutions.
  - This concept will be explored in detail in future chapters.

---

## Summary
1. Focus this chapter: Understanding **structures** of solutions for simple linear systems.
2. Key terms:
   - **Column Space ($R$)**: Span of column vectors; determines if the system has a solution.
   - **Null Space ($N$)**: Set of all solutions that map to the zero vector ($\vec{0}$).
3. Transition to matrix form simplifies representation:
   $$
   A \cdot \vec{x} = \vec{b}
   $$
   where matrix multiplication will play a key role in future concepts.

- Let's dive into solving linear systems! 🚀