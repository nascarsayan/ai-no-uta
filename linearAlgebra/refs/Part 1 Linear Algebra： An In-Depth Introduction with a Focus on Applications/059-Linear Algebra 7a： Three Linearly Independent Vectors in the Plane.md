# Notes: Linearly Independent Vectors in the Plane

## 1. The Challenge: 3 Linearly Independent Vectors in the Plane
- The video begins with a challenge:
  - **Find three linearly independent vectors in the plane**.
- Key insight:
  - **3 linearly independent vectors in a plane is not possible**.
  - “The magic number” for a plane is **2** (maximal number of linearly independent vectors).

---

## 2. Definitions and Key Concepts

### Linear Dependence:
- A set of vectors is **linearly dependent** if **at least one vector** in the set can be written as a **linear combination** of the other vectors.

### Linear Independence:
- A set of vectors is **linearly independent** when **no** vector in the set can be expressed as a **linear combination** of the others.

---

## 3. Example Attempts and Counterexamples

### Example 1: Two Parallel Vectors + One Non-parallel
- Hypothesis: Two parallel vectors and a third not parallel might work.
- Reasoning: The third vector is not a combination of the parallel ones.
- **Flaw:** 
  - The two parallel vectors themselves are linearly dependent.
  - Thus, the whole set of three is linearly dependent.

---

### Example 2: Two Non-parallel Vectors + Zero Vector
- Hypothesis: Add the zero vector to two non-parallel vectors.
- **Flaw:** 
  - The zero vector is trivially a **linear combination of any set** (0 times any vector).
  - Thus, the set is automatically linearly dependent.

---

### Example 3: Two Non-parallel Vectors and One Vaguely Aligned Vector
- Arrangement:
  1. Two vectors are slightly off alignment (almost in the same line).
  2. A third vector points in a completely different direction.
- **Observation**:
  - While decomposition is complex, the three vectors remain linearly dependent.
  - Any two non-parallel vectors already span the plane, making the third vector redundant.

---

### Example 4: Three Arbitrary Directions in the Plane
- Hypothesis: Three vectors in different directions (e.g., nonnegative cases).
- Reality:
  - **Result:** One vector in the system can always be expressed as a linear combination of the other two.
  - The reasoning holds whether using positive, negative, or other scalar values.
  - **Reason:** The plane itself is a 2-dimensional subspace.

---

### Counterexamples Involving Zero Vectors
- Any set containing at least one zero vector is **automatically linearly dependent**:
  - The zero vector can always be expressed as $0 \cdot v_1 + 0 \cdot v_2 + \dots + 0 \cdot v_n$ for any $v_1, v_2, \dots$.

---

## 4. Core Observations for the Plane
- The **plane is two-dimensional**, meaning:
  - At most **2 linearly independent vectors** exist in the plane.
  - Adding a third vector always results in dependence.
- Generalized insight:
  - **Linear independence matches the dimensionality of the space**.

### Intuition Behind Higher Dimensions:
- For $\mathbb{R}^n$:
  - Maximal set of linearly independent vectors = $n$.
  - Examples:
    - $\mathbb{R}^2$ supports up to 2 vectors.
    - $\mathbb{R}^3$ supports up to 3 vectors, etc.

---

### Implications for Linear Algebra:
- Any **two non-parallel vectors span the plane**.
- Linear combinations allow full expression of the vector space.

---

## 5. Larger Takeaway and Future Exploration
- Importance of extending these ideas:
  - Beyond geometric vectors to **functions**, **audio signals**, **polynomials**, etc.
- The concept of independence is foundational to **linear algebra**:
  - Provides a framework for spanning sets, basis, and dimensionality.