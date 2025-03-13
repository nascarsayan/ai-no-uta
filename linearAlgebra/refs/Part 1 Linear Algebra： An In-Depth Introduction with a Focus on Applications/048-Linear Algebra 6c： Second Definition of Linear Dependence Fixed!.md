## Linear Dependence: Refining the Second Definition

### Definitions of Linear Dependence

1. **First Definition**:  
   A set of vectors is **linearly dependent** if **at least one vector** in the set is a **linear combination** of the rest.

2. **Second Definition** (initial form):  
   A set of vectors is **linearly dependent** if there exists a **linear combination** that equals **zero**.

---

### Issue with the Second Definition

- The second definition lacks precision because:
  - **Linear combination = 0** is always possible for any set of vectors (dependent or independent).
  - The **trivial linear combination** (all coefficients are zero) is unhelpful.
  - We must exclude the trivial case to make the definition meaningful.

---

### Trivial Linear Combination

Definition:  
A **trivial linear combination** occurs when **all coefficients are zero**.

Example:

$$
c_1 v_1 + c_2 v_2 + \dots + c_n v_n = 0
$$

where $c_1 = c_2 = \dots = c_n = 0$.  

This trivial case does **not** provide any information about the relationship between the vectors.

---

### Fixed Second Definition

A set of vectors is **linearly dependent** if there exists a **non-trivial linear combination** that equals **zero**.

Definition with Exclusion:  
A **non-trivial linear combination** is any combination where **at least one coefficient is not zero**.

Logical clarification:  
- If **trivial** is "all coefficients are zero," then **non-trivial** means "at least one coefficient is non-zero."

---

### Equivalence of Definitions

- The two definitions of **linear dependence** are, in fact, equivalent.
- This equivalence will be formally demonstrated in the next video.

