## Summary of Terms Encountered

### 1. Definition of a Vector
- A **vector** is an object that can:
  1. Be added to another object of the same kind, and
  2. Be multiplied by a real number (scalar), 
  - Resulting in another object of the same kind.

#### Examples:
1. **Geometric vectors** 
2. **Polynomials** 
3. **Functions**
4. **Elements of $\mathbb{R}^n$**
5. **Audio signals**

- In academia or professional applications, hundreds of other examples of vectors may be encountered.

---

### 2. Linear Combination
#### Definition:
- A **linear combination** involves:
  - A set of vectors and scalar coefficients.
  - Multiply each vector by the corresponding scalar, then add the results.
  - Example:
    Given vectors $\mathbf{u}$, $\mathbf{v}$, and scalars $a$, $b$:
    $$
    a\mathbf{u} + b\mathbf{v}
    $$

- **Decomposition**:
  - The reverse operation of a linear combination.
  - Given the vectors and the final result (right-hand side), determine the scalar coefficients.

---

### 3. Vector Spaces (or Linear Spaces)
- **Vector Space (Linear Space):**
  - The totality (set) of all objects of the same kind that:
    - Can be added together.
    - Can be multiplied by scalars to produce another object of the same kind.

#### Examples of Vector Spaces:
1. **Polynomials** form a vector space.
2. **Geometric vectors in a plane** form a vector space.
3. **Vectors in $\mathbb{R}^3$** form a vector space.
4. **Vectors in $\mathbb{R}^n$** (a generalization) form a vector space.

---

### 4. Subspaces
- Example: Polynomials of **degree 3 or less** form a subspace of the vector space of all polynomials.
- Important considerations:
  - Polynomials of degree **2 or less** form a vector space.
  - **Quadratic polynomials** _(e.g. $x^2 + x$ and $-x^2$)_ do NOT form a vector space because their sum is not necessarily quadratic.

---

### 5. Closure
#### Definition:
- **Closure** is a property of a vector space or linear space.
  - "Closed under addition": The sum of two objects of the space results in another object of the same kind.
  - "Closed under scalar multiplication": Multiplying an object of the space by a number results in another object of the same kind.

#### Geometric Intuition:
- Think of a vector space as:
  - A "closed island" or "room."
  - You cannot leave that space through addition or scalar multiplication.

#### Linear Combinations and Closure:
- **Closure under linear combinations**:
  - If a set of objects is closed under linear combinations, then it forms a vector space.

#### Example:
- Polynomials are closed under linear combinations, so they form a vector space.
