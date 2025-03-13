## Definition and Examples of Spanning Sets

### 1. Definition of a Spanning Set
- A **spanning set** is any set of vectors whose **span** is the entire space.

### 2. Examples of Geometric Spanning Sets

#### Two Vectors in $\mathbb{R}^3$
- **Example**:
    - Suppose we have two vectors in $\mathbb{R}^3$ lying on the same plane. 
    - **Observation**:
        - The span of these two vectors only covers the plane they lie in.
        - Hence, **these two vectors do not form a spanning set** for $\mathbb{R}^3$.

#### Adding a Third Vector
- **Example**:
    - Add a third vector that does not lie on the same plane as the initial two vectors. 
    - **Observation**:
        - These three vectors can now generate all vectors in $\mathbb{R}^3$ via linear combinations.
        - Hence, **these three vectors form a spanning set** for $\mathbb{R}^3$.

#### Adding a Fourth Vector
- **Example**:
    - Add a fourth vector.
    - **Observation**:
        - The spanning property of the original set isn't removed by adding more vectors. The augmented set will still span $\mathbb{R}^3$.
        - **Conclusion**: A larger set of vectors can only improve the spanning property, but not remove it.

#### Four Vectors in a Plane
- **Example**:
    - All four vectors lie within the same plane.
    - **Observation**:
        - These vectors only span the plane and cannot span $\mathbb{R}^3$.
        - Hence, **these four vectors do not form a spanning set for $\mathbb{R}^3$**.

### 3. Key Insights on Spanning Sets
- To form a spanning set, the vectors must:
    1. Be **numerically sufficient**.
    2. Be **arranged properly** (not in the same plane, for instance).
- Spanning is **relative**:
    - Vectors might span a smaller subspace, even if they don’t span the larger space.

---

## Spanning Sets and Polynomial Spaces

### 4. Spanning Set for Quadratic Polynomials
- **Problem**: Do two particular quadratic polynomials span the space of all quadratic polynomials?

#### Geometric Analogy to Algebra
- **Observation**:
    - The space of quadratic polynomials is analogous to three-dimensional space $\mathbb{R}^3$ (both are three-dimensional spaces).
    - Two quadratic polynomials, regardless of arrangement, cannot span the entire space of quadratic polynomials.

#### Argument Based on Shared Properties
- **Property**:
    - The two quadratic polynomials share a property—**their coefficients add up to zero**.
    - Synonymously, both polynomials pass through zero at $x = 1$ and have a root at $x = 1$.

#### Why Two Polynomials Cannot Span the Space
- This shared property is **linear**:
    - Adding or scaling linear combinations of the two polynomials will preserve the property.
    - Hence, these two polynomials can only generate other polynomials that also share this property.
    - Polynomials that do not share this property cannot be generated.
- **Conclusion**: Two polynomials cannot span the entire space of quadratic polynomials.

#### Linear Algebra Insight
- **Linear Property**:
    - The shared property cannot be broken by linear combinations, making it a special invariant.

---

### 5. Subspaces and Spanning Sets
- **Subspace of Polynomials**:
    - Question: Can the two quadratic polynomials form a spanning set for the subspace of polynomials whose coefficients add up to zero?
    - Answer: This requires further evaluation but is distinct from spanning all quadratic polynomials.

---

## Extending to $\mathbb{R}^3$

### 6. Spanning Subspaces in $\mathbb{R}^3$
- **Example**:
    - Vectors in $\mathbb{R}^3$ with zero middle entry.
    - Observation: This subset is clearly not a spanning set for $\mathbb{R}^3$, as it only spans a subspace where the middle entry is zero.

#### Exploration Question
- **Challenge**:
    - Can you get all elements in $\mathbb{R}^3$ where the middle entry is zero using this subset? 
    - What is a spanning set for this subspace?

---

### Key Takeaways
1. Spanning sets are a central concept in Linear Algebra.
2. **Properties** such as linear invariance play a critical role in determining if vectors span a space.
3. The idea of spanning is **relative**—spanning a subspace can differ from spanning the overall space.
4. Logical arguments for impossibility (like shared properties) provide elegant ways to understand the limitations of a set of vectors.