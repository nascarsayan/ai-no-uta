## Linear Independence in Planes and Spaces

### Plane: At most 2 Linearly Independent Vectors
- In a plane, you can have a maximum of **two linearly independent vectors.**
- This conclusion arises by analyzing all possible configurations of three vectors in the plane:
  - Any such set of three vectors is **linearly dependent.**

### Space: At most 3 Linearly Independent Vectors
- In 3D space, the maximum number of **linearly independent vectors is three**:
  - This is why it’s called a **three-dimensional space.**

#### Visualizing 4 Vectors in Space
To understand why four vectors in 3D space are **always linearly dependent**, consider the following cases:
1. **One vector as a linear combination of others**:
   - Any one of the four vectors can be expressed as a linear combination of the other three.

2. **Some vectors dependent on others**:
   - For instance, three vectors lie in a plane, and the fourth vector may:
     - Lie within the same plane (making it dependent).
     - Not lie in the plane, but the dependency arises from other combinations.

3. **Zero vector in the set**:
   - A zero vector is always automatically a **linear combination of other vectors.**

4. **Parallel or collinear vectors**:
   - Two or more vectors could be **parallel**, reducing the effective dimensionality.

#### Mathematical Justification
Adding a fourth vector in 3D space introduces dependency because there are only three **degrees of freedom**:
$$
\text{Rank of the system (dimension)} = 3 \quad \rightarrow \quad \text{No room for a 4th independent vector.}
$$

### Summary
- **Plane (2D):** At most 2 linearly independent vectors.
- **Space (3D):** At most 3 linearly independent vectors.
- **Why?** Adding more vectors leads to one becoming a linear combination of others:
  - This results from the inherent dimensionality of the space or mathematical system.