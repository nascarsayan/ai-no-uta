## 15. Polynomials as Vectors

### Are Polynomials Multiples of Each Other?

- Polynomials can be considered as vectors. In this context, a natural question arises: 
  - *Is one polynomial a multiple of another?*
  
### Why the Answer is "No" in Linear Algebra:
- If we are working under the framework of **linear algebra**, the answer is **no**.
- Reason:
  - When treating polynomials as vectors, the only allowed operations are:
    1. **Addition** of polynomials.
    2. **Multiplication** of a polynomial by a scalar (a number).
  - The variable $x$, which appears in polynomials, is **not a scalar**. 
  - Therefore, $x$ itself cannot act as a multiplier in this vector space context.

### Example:
Suppose the polynomials are:
1. $p(x) = x$
2. $q(x) = 1$

- While $p(x) = x \cdot q(x)$ might seem valid algebraically, in **linear algebra**, this isn't permissible since $x$ is not a scalar.

### Contextual Differences:
- In **8th-grade algebra**, where the variable $x$ is treated mathematically and not as part of the linear algebra framework, the answer would have been **yes** — $p(x)$ is indeed a multiple of $q(x)$.
- In **linear algebra**, the answer is **no**, because:
  - There is **no scalar** $c$ such that $c \cdot q(x) = p(x)$.

### Key Takeaways:
1. **Polynomials as Vectors**:
   - When treating polynomials as vectors, only vector-space permitted actions matter:
     1. Adding polynomials.
     2. Multiplying polynomials by scalars.
   - Any operation outside these two, such as multiplication by $x$, is not valid.

2. **Linear Algebra vs Other Contexts**:
   - Linear algebra simplifies objects by focusing on their vector properties.
   - Any additional operations on the objects (like polynomial multiplication) are ignored for the purpose of studying them as vectors.

3. **Simplicity of Linear Algebra**:
   - Despite dealing with complex objects like polynomials, linear algebra remains "relatively uncomplicated."
   - We only consider **addition** and **scalar multiplication** and ignore other potential actions such as polynomial multiplication.

