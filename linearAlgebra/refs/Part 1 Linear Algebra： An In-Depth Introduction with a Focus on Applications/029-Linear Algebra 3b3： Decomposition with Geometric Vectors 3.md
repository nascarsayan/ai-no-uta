## Decomposing a Vector as a Linear Combination

### Introduction to the Problem
- The exercise involves decomposing the **vector C** as a linear combination of two other vectors, **A** and **B**.
- Given conditions include:
  - All vectors in the problem are unit vectors.
  - The angle between **A** and **B** is $90^\circ$.
  - The angle between **C** and **A** is $45^\circ$.

### Why This Exercise Matters
1. **Skill Development:**
   - Trains the brain to handle complex vector exercises.
2. **Understanding Geometric Vectors:**
   - Helps in reasoning about vectors without relying on a coordinate system.
3. **Accuracy and Speed:**
   - Improves the ability to solve vector-related problems, which is useful for advanced topics.

### Decomposition Strategy
1. **Step 1: Analyze Vector Relationships**
   - Notice that **A** is related to $C - B$.
   - However, $|C - B| \neq |A|$; instead, $|C - B| = \sqrt{2}$ (by the Pythagorean theorem for a $90^\circ$ isosceles triangle).

2. **Step 2: Rescale the Vector**
   - To align the magnitudes, scale $C - B$ by a factor of $\frac{1}{\sqrt{2}}$.
   - This gives:
     $$
     A = \frac{1}{\sqrt{2}} (C - B)
     $$
   - Simplifying:
     $$
     A = \frac{1}{\sqrt{2}}C - \frac{1}{\sqrt{2}}B
     $$

3. **Step 3: Solve for Vector C**
   - Rearrange to express **C** in terms of **A** and **B**:
     $$
     C = \sqrt{2}A + B
     $$

### Summary of the Decomposition
- Final decomposition of **C**:
  $$
  C = \sqrt{2}A + B
  $$
- This illustrates a systematic approach to decompose **C** into a linear combination of **A** and **B**.

### Generalization
- The above example relies on the special arrangement of vectors. If the arrangement is arbitrary:
  - A **systematic and robust method** is needed to compute the coefficients for combining **A** and **B** into **C**.
  - This general method will be discussed in the next topic.