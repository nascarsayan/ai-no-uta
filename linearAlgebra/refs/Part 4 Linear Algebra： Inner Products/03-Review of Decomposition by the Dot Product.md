# Notes: Linear Decomposition and Dot Product

## Introduction
- **Linear decomposition**: The task of representing a vector as a **linear combination** of basis vectors.
- This process becomes second nature with practice and is fundamental in mathematics and physics.

---

## Concept: Decomposition
### Decomposition with respect to an **orthonormal basis**
- Consider a 3D **Cartesian (orthonormal)** basis:
  - Basis vectors: $\mathbf{E_1}, \mathbf{E_2}, \mathbf{E_3}$
  - All vectors have unit length: $\|\mathbf{E_1}\| = \|\mathbf{E_2}\| = \|\mathbf{E_3}\| = 1$
  - All vectors are orthogonal to each other.

For a vector $\mathbf{v}$, decompose it into a linear combination of basis vectors:

$$
\mathbf{v} = \alpha_1 \mathbf{E_1} + \alpha_2 \mathbf{E_2} + \alpha_3 \mathbf{E_3}
$$

Where $\alpha_1$, $\alpha_2$, and $\alpha_3$ are **coefficients** to be determined.

---

## Dot Product and Its Use in Decomposition
### Dot Product Properties
1. **Commutative property**: $\mathbf{A} \cdot \mathbf{B} = \mathbf{B} \cdot \mathbf{A}$  
   - This arises because the dot product involves the cosine of the angle between vectors, and cosine is even.  
   - E.g., $\cos(\theta) = \cos(-\theta)$.

2. **Distributive property**:  
   For $\mathbf{A}, \mathbf{B}, \mathbf{C}$:
   $$
   (\mathbf{A} + \mathbf{B}) \cdot \mathbf{C} = \mathbf{A} \cdot \mathbf{C} + \mathbf{B} \cdot \mathbf{C}
   $$

3. If $\mathbf{A}$ is **orthogonal** to $\mathbf{B}$, then:  
   $$
   \mathbf{A} \cdot \mathbf{B} = 0
   $$

---

## Steps: Decomposing $\mathbf{v}$
1. Start with:  
   $$
   \mathbf{v} = \alpha_1 \mathbf{E_1} + \alpha_2 \mathbf{E_2} + \alpha_3 \mathbf{E_3}
   $$

2. Dot both sides with $\mathbf{E_1}$:
   $$
   \mathbf{v} \cdot \mathbf{E_1} = (\alpha_1 \mathbf{E_1} + \alpha_2 \mathbf{E_2} + \alpha_3 \mathbf{E_3}) \cdot \mathbf{E_1}
   $$

3. Apply distributive property:  
   $$
   \mathbf{v} \cdot \mathbf{E_1} = \alpha_1 (\mathbf{E_1} \cdot \mathbf{E_1}) + \alpha_2 (\mathbf{E_2} \cdot \mathbf{E_1}) + \alpha_3 (\mathbf{E_3} \cdot \mathbf{E_1})
   $$

4. Considering the properties of the orthonormal basis: 
   - $\mathbf{E_1} \cdot \mathbf{E_1} = 1$  
   - $\mathbf{E_2} \cdot \mathbf{E_1} = 0$, since they are orthogonal  
   - $\mathbf{E_3} \cdot \mathbf{E_1} = 0$, since they are orthogonal.

   This simplifies the equation to:  
   $$
   \mathbf{v} \cdot \mathbf{E_1} = \alpha_1
   $$

5. Similarly, dot with $\mathbf{E_2}$ and $\mathbf{E_3}$:
   $$
   \mathbf{v} \cdot \mathbf{E_2} = \alpha_2
   $$

   $$
   \mathbf{v} \cdot \mathbf{E_3} = \alpha_3
   $$

6. Result:  
   $$
   \alpha_i = \mathbf{v} \cdot \mathbf{E_i} \quad \text{for } i = 1, 2, 3
   $$

### Interpretation
- The coefficient $\alpha_i$ is the **projection** of $\mathbf{v}$ onto the basis vector $\mathbf{E_i}$, computed using the **dot product**.

---

## Generalization
### Non-orthonormal Basis
- If the basis vectors are **orthogonal** but not **normalized**:  
  - $\|\mathbf{E_i}\| \neq 1$, but $\mathbf{E_i} \cdot \mathbf{E_j} = 0 \quad \text{(for } i \neq j)$.

- Modify the coefficients:  
  $$
  \alpha_i = \frac{\mathbf{v} \cdot \mathbf{E_i}}{\mathbf{E_i} \cdot \mathbf{E_i}}
  $$

### Overlapping or Non-Orthogonal Basis
- If the basis vectors are not orthogonal, the calculation becomes more complex and involves solving a system of linear equations derived from the dot products of all combinations of basis vectors.

---

## Conclusion: Power of the Dot Product
1. Dot products enable decomposition **algebraically**, bypassing geometric intuition.
2. Geometric **concepts like orthogonality** and vector projection translate directly into **dot product calculations**.
3. Decomposition works for orthonormal, orthogonal, or even general bases but requires adjustments depending on the properties of the basis.

Exploration: Think about the implications when the basis is neither orthogonal nor normalized. How can we use a combination of dot products to retrieve coefficients systematically?