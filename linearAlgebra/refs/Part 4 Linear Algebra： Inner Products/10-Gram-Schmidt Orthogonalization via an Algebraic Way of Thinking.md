### Notes: Gram-Schmidt Orthogonalization Process

#### Algebraic Derivation of Orthogonality

- The derivation of this formula uses basic **algebraic properties**:
  - **Commutative Property**
  - **Distributive Property**
  - The ability to divide by a non-zero scalar.

#### Modifying Vectors for Orthogonality
To make a vector orthogonal to another:
1. Subtract a scalar multiple of one vector from the other.
2. Choose the scalar multiple such that the resulting vector satisfies the orthogonality condition.

#### The Process

1. **Orthogonal Vector Definition**:
   - For two vectors $a$ and $B_1$, being orthogonal means:
     $$
     a \cdot B_1 = 0
     $$

2. **Creating the Orthogonal Vector**:
   - Start with $B$, subtract $\alpha a$ to modify $B$. The orthogonality condition leads us to:
     $$
     B_1 = B - \alpha a
     $$

3. **Finding $\alpha$**:
   - Using the definition of orthogonality:
     $$
     a \cdot B_1 = a \cdot B - \alpha a \cdot a = 0
     $$
     Rearranging gives:
     $$
     \alpha = \frac{a \cdot B}{a \cdot a}
     $$

4. **Resulting Formula for $B_1$**:
   - Substitute $\alpha$ back:
     $$
     B_1 = B - \frac{a \cdot B}{a \cdot a} a
     $$

#### Geometric Interpretation vs Algebraic View
- While geometric intuition is helpful, this process works purely through algebra without relying on visual representations.
- Orthogonality in algebra refers to **dot product results** being zero, or more generally, **inner product results** being zero.

#### Inner Product Generalization
- The argument can extend to any **inner product space**, not just geometric vectors. The formula remains valid as long as inner products are well-defined.

#### Verifying Orthogonality
1. Postulate $B_1$:
   $$
   B_1 = B - \frac{a \cdot B}{a \cdot a} a
   $$

2. Dot $B_1$ with $a$:
   - Apply distributive laws:
     $$
     a \cdot B_1 = a \cdot B - \frac{a \cdot B}{a \cdot a}(a \cdot a)
     $$
     - The second term cancels out: $\frac{a \cdot B}{a \cdot a}(a \cdot a) = a \cdot B$.
   - Final result:
     $$
     a \cdot B_1 = 0
     $$

#### Summary of Gram-Schmidt Step
- **Key Result**:
  $$
  B_1 = B - \frac{a \cdot B}{a \cdot a} a
  $$
- This formula creates a vector $B_1$ that is **orthogonal** to $a$ while maintaining the span of the original vectors.

#### Practice with Notation
- Be familiar with alternate representations like:
  - Dot product for geometric and algebraic calculations.
  - `Inner product` notation in more general vector spaces.
  
#### Gram-Schmidt Orthogonalization
- Fundamental step for creating **orthogonal** and **linearly independent** vectors from a given basis in linear algebra.

