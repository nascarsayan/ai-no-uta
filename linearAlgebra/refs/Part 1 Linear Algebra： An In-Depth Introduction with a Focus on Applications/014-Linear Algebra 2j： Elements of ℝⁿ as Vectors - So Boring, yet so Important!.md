## Introduction to $\mathbb{R}^n$

### Recap of Contexts
- We have previously discussed:
  - Geometric vectors.
  - Polynomials and functions.
- Now, the focus shifts to sets of $n$ numbers, specifically $\mathbb{R}^3$ (triplets of real numbers) in this instance.

### Remarkable Unification
- Despite their different natures, geometric vectors, polynomials, and numeric triplets are unified under the concept of linear algebra.
- What they share in common is the ability to:
  - **Add** these objects together.
  - **Multiply** them by scalars.
  - Produce another object of the same kind.

---

## 15. Properties and Importance of $\mathbb{R}^n$

1. **Practical Utility**  
   - Computers work with numbers. Representation of problems as numbers (elements of $\mathbb{R}^n$) leverages computational capabilities.

2. **Algorithmic Relevance**  
   - Algorithms in linear algebra are designed with $\mathbb{R}^n$ in mind.

3. **Equivalence of Vector Spaces**  
   - All vector spaces are effectively equivalent to some $\mathbb{R}^n$. By studying $\mathbb{R}^n$, we generalize insights to all vector spaces.

> Linear algebra abstracts operations like addition and scalar multiplication across vector spaces.

---

## 16. Operations in $\mathbb{R}^n$

### Addition
- Adding two vectors in $\mathbb{R}^n$ results in another vector in $\mathbb{R}^n$.  
  **Example:**

  $$
  \begin{bmatrix} 1 \\ 2 \\ 3 \end{bmatrix} +
  \begin{bmatrix} -2 \\ 7 \\ -6 \end{bmatrix} =
  \begin{bmatrix} -1 \\ 9 \\ -3 \end{bmatrix}
  $$

### Scalar Multiplication
- Multiplying a vector by a scalar scales each entry of the vector.  
  **Example:**

  $$
  7 \times \begin{bmatrix} 4 \\ 0 \\ 12 \end{bmatrix} =
  \begin{bmatrix} 28 \\ 0 \\ 84 \end{bmatrix}
  $$

### Key Properties Verified
- These operations satisfy the properties of:
  - Commutativity.
  - Associativity.
  - Distributivity.
- Thus, elements of $\mathbb{R}^n$ act as vectors in the linear algebraic sense.

---

## 17. Subspaces in $\mathbb{R}^3$

### Geometric Analogy
- In geometry, vectors in the same plane are "stuck" in that plane—adding or scaling these vectors won't take you out of it.

### Example in $\mathbb{R}^3$
- Consider vectors in $\mathbb{R}^3$ where the last entry is always three times the first entry:
  - $\begin{bmatrix} x \\ y \\ 3x \end{bmatrix}$
- This property is preserved under addition and scalar multiplication:
  - Adding $\begin{bmatrix} 1 \\ 2 \\ 3 \end{bmatrix}$ and $\begin{bmatrix} 4 \\ 5 \\ 12 \end{bmatrix}$:
    $$
    \begin{bmatrix} 1 \\ 2 \\ 3 \end{bmatrix} + \begin{bmatrix} 4 \\ 5 \\ 12 \end{bmatrix} =
    \begin{bmatrix} 5 \\ 7 \\ 15 \end{bmatrix}
    $$
    The third entry of the result is 3 times the first entry.
  - Scalar multiplication, e.g., $7 \times \begin{bmatrix} 4 \\ 0 \\ 12 \end{bmatrix}$:
    $$
    7 \times \begin{bmatrix} 4 \\ 0 \\ 12 \end{bmatrix} = \begin{bmatrix} 28 \\ 0 \\ 84 \end{bmatrix}
    $$
    This property still holds.

### Subspace Concept
- Such a set of vectors forms a **subspace** of $\mathbb{R}^3$.
- This parallels the geometric concept of a subspace, such as a plane being a subset of 3D space.

---

## 18. Importance of Abstraction
- Abandon geometric intuition for a more abstract view:
  - Think of vectors in $\mathbb{R}^n$ as abstract tuples of numbers, not spatial objects.
- Rebuilding geometric associations should come later, based on proper mathematical abstraction.

---

## 19. Spirit of Linear Algebra

### Parallel Discussions
- Linear algebra unifies seemingly diverse concepts:
  - Geometric vectors → Planes, lengths, angles.
  - Polynomials → Coefficients, roots, graphs.
  - $\mathbb{R}^n$ → Entries (numbers).
- Discussions respect the unique native contexts of these objects.

### Core Focus
- Linear algebra focuses on two universal operations:
  - **Addition**: Combining objects.
  - **Scalar Multiplication**: Scaling objects.

The central theme of linear algebra is finding the shared structure across different mathematical objects while interacting with these objects in their native terms.