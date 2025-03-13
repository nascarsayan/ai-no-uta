# Orthogonalization and Gram-Schmidt Process

## 1. Overview
When given a set of three vectors, the goal is to make them orthogonal. This can be accomplished using the **Gram-Schmidt process**, divided into the following steps:
1. Pick the first vector as the starting vector (**A**).
2. Adjust the second vector (**B**) to be orthogonal to the starting vector.
3. Adjust the third vector (**C**) to be orthogonal to both the first and second adjusted vectors.

### Key Concepts
- An **orthogonal set of vectors** means any pair of vectors in the set are perpendicular (dot product equals 0).
- If vectors are orthogonal, calculations like projections and decompositions become simpler and more reliable.

---

## 2. Step-by-Step Gram-Schmidt Process

### Step 1: Leave the first vector unchanged
- Let the first vector be:
    $$
    A_1 = A
    $$

### Step 2: Adjust the second vector
To make **B** orthogonal to **A_1**, subtract the projection of **B** onto **A_1**:
$$
B_1 = B - \text{proj}_{A_1}(B)
$$
Where the projection formula is:
$$
\text{proj}_{A_1}(B) = \frac{B \cdot A_1}{A_1 \cdot A_1}A_1
$$

### Step 3: Adjust the third vector
To make **C** orthogonal to **A_1** and **B_1**:
1. Subtract the projection of **C** onto **A_1**:
    $$
    C - \text{proj}_{A_1}(C)
    $$
2. Subtract the projection of **C** onto **B_1**:
    $$
    C_1 = \left(C - \text{proj}_{A_1}(C)\right) - \text{proj}_{B_1}(C)
    $$
3. The order of subtraction is crucial for maintaining orthogonality within the set.

---

## 3. Generalization and Intuition

### Intuition of Orthogonality
1. **Incremental Adjustments**: Each vector is adjusted using the most recently computed orthogonal vectors in sequence (e.g., **A_1**, then **B_1**) to ensure all vectors remain orthogonal.
2. **Orthogonality in Planes**: Once orthogonality is established with one vector, any further adjustments (e.g., making a vector orthogonal to another) occur in the subspace orthogonal to the first vector, preserving the orthogonal property.

### Process for Higher Dimensions
This approach generalizes easily to more vectors. For each vector, subtract the projections onto all previously computed orthogonal vectors.

---

## 4. Discussion and Possible Challenges

### Critical Observations
1. For this process to work:
   - The original set of vectors must be **linearly independent**.
   - Adjustments using projections will yield non-zero orthogonal components.

2. If the vectors are co-planar (linearly dependent), the process fails, since one vector will have no "new" direction.

### Potential Danger
- When adjusting a vector to make it orthogonal to others:
  - It’s important to check that previously established orthogonality (e.g., to **A_1**) is not inadvertently broken.
  - This doesn't occur because the adjustments happen in a subspace already orthogonal to the earlier vectors.

**Verification**: After adjustments, verify results by taking dot products:
- Check that $A_1 \cdot B_1 = 0$, $A_1 \cdot C_1 = 0$, and $B_1 \cdot C_1 = 0$.

### Matrix Representation
The process has a **triangular structure** when represented in matrix form, where each new row/vector involves progressively more subtractions.

---

## 5. Benefits of Orthogonal Sets
1. **Simplicity of Decomposition**:
   - Orthogonal vectors allow easier projections and representations of arbitrary vectors within the space.
   
2. **Stability in Computation**:
   - Computational methods like solving systems and performing transformations are numerically more stable with orthogonal (or orthonormal) bases.

3. **Efficiency**:
   - Calculations such as dot products for orthogonality checks and projections are simplified due to zero cross-terms in orthogonal bases.

