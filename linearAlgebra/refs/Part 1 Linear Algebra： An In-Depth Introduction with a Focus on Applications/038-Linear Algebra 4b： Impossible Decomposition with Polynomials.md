## Impossible Decomposition Problems with Quadratic Polynomials

### Purpose:
1. Illustrate the general idea behind why certain polynomials cannot be decomposed.
2. Emphasize practicing polynomials as vector spaces on their terms.

---

### 1. First Impossible Problem - Missing Constant Term

#### Problem:
Why is it not possible to express $x^2 + 1$ as a linear combination of three given decomposition polynomials?

#### Reasoning:
- The decomposition polynomials lack constant terms.
- Linear combinations of these polynomials will only produce other polynomials with zero free terms.

#### Conclusion:
Since the target polynomial $x^2 + 1$ has a free term (constant) of 1, it cannot belong to the span of the given decomposition polynomials.

---

### 2. Second Impossible Problem - Coefficients Add to Zero

#### Problem:
Why is it not possible to express $x^2 + 1$ as a linear combination of polynomials whose coefficients sum to zero?

#### Key Property:
- Given polynomials have the property: their coefficients add up to zero.

#### Proof:
- Addition: If you add two polynomials with this property, the resultant polynomial also has coefficients that add up to zero.
- Scalar multiplication: Multiplying a polynomial with this property by any scalar retains the property.

#### Observation:
- Target polynomial $x^2 + 1$ has coefficients that sum to two.
- Hence, $x^2 + 1$ does not share the property of the span defined by these decomposition polynomials.

---

### 3. Third Impossible Problem - Root at $x = 2$

#### Problem:
Why can’t $x^2 + 1$ be decomposed using polynomials that have $x = 2$ as a root?

#### Key Property:
- All given polynomials satisfy $f(2) = 0$, meaning $x = 2$ is their root.

#### Graphical/Factual Basis:
- Sum of two such polynomials retains this root property: $f(2) = 0$.
- Scalar multiplication retains the root property.
- Linear combinations of these polynomials will always yield polynomials with $x = 2$ as a root.

#### Target Polynomial:
- $x^2 + 1$ does not pass through zero at $x = 2$ ($f(2) = 5$).
- Therefore, it cannot belong to the subspace defined by these polynomials.

---

### Analogy to Geometric Vectors:
- Ineffectiveness of decomposition in polynomials aligns with geometric vector analogies:
    - Two vectors in the same line fail to span a third one lying outside the line.
    - Two vectors in arbitrary directions may fail to span a third vector outside their plane.

---

### Subspace Differences:
1. **Coefficients Add to Zero:** Equivalent to having a root at $x = 1$.  
2. **Root at $x = 2:** Subspace of polynomials that pass through zero at $x = 2$.  

### Conclusion:
Each subspace has distinct properties for decomposition and ensures specific constraints on the resultant polynomials.

---

### Next Topic:
Vectors from $\mathbb{R}^n$