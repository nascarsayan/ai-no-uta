## Inner Product Properties and Examples

### Definition of Inner Product
- The concept of the inner product was introduced in the context of linear algebra. In this discussion:
  - We'll define two polynomials, $p$ and $q$.
  - The inner product of $p$ and $q$ involves evaluating the integral (as shown on the board in the earlier lecture).
  
---

### Evaluating an Integral to Interpret Dot Products
#### Example 1: Dotting $x$ with $x$
1. Suppose we compute the dot product of $x$ with $x$ using the inner product definition:
   $$
   \int_{-1}^{1} x \cdot x \, dx = \int_{-1}^{1} x^2 \, dx
   $$
2. By symmetry and basic calculus:
   - The area under $x^2$ from 0 to 1 is $\frac{1}{3}$.
   - Doubling it for both sides gives:
     $$
     \int_{-1}^{1} x^2 \, dx = \frac{2}{3}
     $$
3. This confirms the result is positive:
   - **Key Check**: If the result were negative, the operation couldn't qualify as an inner product.

#### Takeaway: Positive inner product values play a critical role in validating the operation.

---

### Odd Functions and Orthogonality
#### Example 2: Dotting $1$ with $x$
1. Compute the inner product of 1 and $x$:
   $$
   \int_{-1}^{1} 1 \cdot x \, dx
   $$
2. Since $x$ is an odd function, the integral over $[-1, 1]$ cancels out:
   - The result:
     $$
     \int_{-1}^{1} 1 \cdot x \, dx = 0
     $$
3. **Interpretation**:
   - The value being 0 indicates that $1$ and $x$ are **orthogonal** with respect to this inner product.

#### Understanding Orthogonality
- Orthogonality in this context generalizes the geometric concept of perpendicularity.
- Two functions (or vectors) are orthogonal if their inner product is zero.

---

### Length of Vectors
1. The length (or norm) of a vector is determined by:
   $$
   \sqrt{\text{Inner Product of the vector with itself}}
   $$
2. **Example**: Compute the length of $x$:
   - From earlier, the inner product of $x$ with itself is $\frac{2}{3}$.
   - Hence:
     $$
     \text{Length of } x = \sqrt{\frac{2}{3}}
     $$

#### Example with Scaled Vectors
- If $k \cdot x$ is scaled by a factor $k$, its length would involve scaling the resulting inner product.

---

### Unit Vectors
1. A unit vector has a length of 1. **Example**:
   - Consider $\sqrt{\frac{3}{2}} \cdot x$.
   - Compute the inner product:
     $$
     \int_{-1}^{1} \left(\sqrt{\frac{3}{2}} \cdot x \right)^2 \, dx
     $$
   - This results in 1, verifying that $\sqrt{\frac{3}{2}} \cdot x$ is a unit vector.

---

### Inner Products and Complex Numbers
1. If we extend the inner product definition for **complex numbers**, it requires changes:
   - Swapping operands introduces a **complex conjugate**.
   - Many properties remain consistent, but this marks one of the significant departures from real-number treatments in linear algebra.

---

### Orthogonality and Changes in Inner Product Definition
1. **Orthogonality is relative**:
   - Functions or vectors are orthogonal with respect to the **chosen inner product**.
   - Changing the inner product might remove the orthogonality property for a given pair of vectors.

---

### Limitations of Function Definitions in Real Numbers
1. For example, attempting to compute:
   $$
   \int_{-1}^{1} \sqrt{x} \cdot \sqrt{x} \, dx
   $$
   - This fails as $\sqrt{x}$ is not defined for negative real numbers.
   - Thus, such functions cannot be used in the context of this inner product.

---

### Summary
1. Definition: Two vectors (functions) are **orthogonal** when their inner product is zero.
2. Length (norm) interpretation:
   $$
   \text{Length} = \sqrt{\text{Inner Product with itself}}
   $$
3. Inner products can change based on context (e.g., complex vs. real numbers), affecting key properties like symmetry and orthogonality.
4. Positive values are crucial for inner products to satisfy the axioms (e.g., ensuring inner product consistency).

