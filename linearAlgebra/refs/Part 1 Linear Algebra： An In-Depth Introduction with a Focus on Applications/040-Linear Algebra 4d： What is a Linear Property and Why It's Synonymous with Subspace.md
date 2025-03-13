## Linear Properties and Decomposition Problems in Vector Spaces

### 1. Introduction
- **Topic:** Decomposition problems with no solutions.
- **Key observation:** Special properties shared by decomposition vectors but not satisfied by the target vector determine the impossibility of decomposition.
- **Focus:** Understanding the required conditions for valid arguments in decomposition problems.

---

### 2. Linear Properties
- A property is **linear** if it is preserved under linear combinations of vectors.

#### Definition of a Linear Property:
- **Addition:** If two vectors satisfy the property, their sum also satisfies the property.
- **Scalar Multiplication:** Multiplying a vector satisfying the property by a scalar preserves the property.

#### Formal Statement:
- A property is linear if **any linear combination** of vectors that satisfy the property **also satisfies the property**.

---

### 3. Incorrect Arguments for Impossibility of Decomposition
#### Example 1:
- **Claim:** All decomposition vectors have 1 as their first entry, but the target vector has a 3 as its first entry.
- **Flaw:** The property of "having 1 as the first entry" is **not linear**, as addition and scalar multiplication break this property.
  - $$ 
  \begin{bmatrix} 1 \\ 2 \\ 3 \end{bmatrix} + 
  \begin{bmatrix} 1 \\ 4 \\ 2 \end{bmatrix} =
  \begin{bmatrix} 2 \\ 6 \\ 5 \end{bmatrix}
  $$ 
    (**Result:** First entry becomes 2, not preserved.)
  - $$ 
  10 \times \begin{bmatrix} 1 \\ 2 \\ 3 \end{bmatrix} =
  \begin{bmatrix} 10 \\ 20 \\ 30 \end{bmatrix}
  $$
    (**Result:** First entry becomes 10, not preserved.)
- **Conclusion:** The decomposition problem is possible because the property is irrelevant (non-linear).

---

#### Example 2:
- **Claim:** Second entry is always one greater than the first entry in decomposition vectors, but the target vector does not satisfy this.
- **Flaw:** The "second entry being one greater than the first" does **not survive linear combinations or scalar multiplication**.
  - **Addition:**
    $$ 
    \begin{bmatrix} 1 \\ 2 \\ 0 \end{bmatrix} +
    \begin{bmatrix} 1 \\ 2 \\ 3 \end{bmatrix} =
    \begin{bmatrix} 2 \\ 4 \\ 3 \end{bmatrix}
    $$
    (**Result:** Second entry no longer one greater than the first.)
  - **Scalar Multiplication:**
    $$ 
    2 \times \begin{bmatrix} 1 \\ 2 \\ 3 \end{bmatrix} =
    \begin{bmatrix} 2 \\ 4 \\ 6 \end{bmatrix}
    $$
    (**Result:** Property not preserved.)
- **Conclusion:** Argument is invalid as the property is irrelevant (non-linear).

---

#### Example 3:
- **Claim:** Decomposition vectors have even entries, but some target vector entries are odd.
- **Flaw:** "Being even" does **not survive linear combinations or scalar multiplication**:
  - $$ 
  \begin{bmatrix} 2 \\ 4 \\ 6 \end{bmatrix} \times \frac{1}{2} =
  \begin{bmatrix} 1 \\ 2 \\ 3 \end{bmatrix}
  $$
    (**Result:** Entries are no longer even.)
- **Conclusion:** The property is completely irrelevant, and the decomposition remains feasible.

---

### 4. Linear Property and Subspaces
- **Definition of a Subspace:**
  A Subspace is:
  - Closed under addition: Sum of any two vectors in the subspace remains in the subspace.
  - Closed under scalar multiplication: Scaling a vector by a scalar keeps it in the subspace.
  
#### Connection:
- **Linear Properties = Subspaces**
  - Vectors satisfying a linear property form a **subspace** of the vector space.
  - **Key Criterion:** Closure under linear combinations (sum & scalar multiplication).

---

### 5. Closure Under Linear Combinations
#### Subspaces:
- **Example:**
  - Add two vectors in the subspace:
    $$ 
    \begin{bmatrix} 1 \\ 3 \\ 5 \end{bmatrix} +
    \begin{bmatrix} -2 \\ -6 \\ -8 \end{bmatrix} =
    \begin{bmatrix} -1 \\ -3 \\ -3 \end{bmatrix}
    $$ 
    (**Result:** Still has the linear defining property.)
  - Multiply a vector in the subspace by a scalar:
    $$ 
    2 \times \begin{bmatrix} 1 \\ 2 \\ 3 \end{bmatrix} =
    \begin{bmatrix} 2 \\ 4 \\ 6 \end{bmatrix}
    $$ 
    (**Result:** Still in the subspace.)

---

### 6. Key Takeaways
- A property is **linear** if it survives linear combinations.
- Linear properties extract **subspaces** from a vector space.
- Non-linear properties (e.g., integer-based or specific entry-based) do not lead to valid impossibility arguments for decomposition problems.
- Subspaces are subsets of vector spaces that preserve vector operations (closure under addition and scalar multiplication).

---

### 7. Next Steps
- **Upcoming Video:** Formal characterization of all linear properties.
- Anticipation of common structure and patterns among linear properties, simplifying identification in vector spaces.