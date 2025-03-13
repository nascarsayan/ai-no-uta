## 1. Calculating the Inverse of a Matrix

### Introduction:
- This video introduces an **algorithm** to calculate the inverse of a matrix without explaining why it works.
- Later videos will provide **three different explanations** for why the algorithm works.

### Why Linear Algebra is Fascinating:
- It combines **geometry** and **algebra** through concepts like matrix algebra.
- Linear algebra has evolved into being all about **algorithms**.
- Plenty of reasons to love linear algebra!

---

### The Algorithm:

1. **Start with the matrix** and the 3x3 **identity matrix**:
   - Combine them into a **3x6 matrix**.

   Example:
   $$
   \text{Matrix to invert | Identity matrix}
   $$

   - Left side: Matrix to invert.
   - Right side: Identity matrix.

2. **Perform Gaussian Elimination**:
   - Reduce the combined matrix to **row-reduced echelon form (RREF)**.

3. In RREF:
   - **Left side** will become the **identity matrix**.
   - **Right side** will become the **inverse** of the original matrix.

---

### Guarantee of Results:
- The inverse exists only for matrices with **linearly independent columns**.
- In RREF, the columns align with pivot positions and form an identity matrix on the left.

---

### Recap of the Steps:
1. Put the matrix and identity matrix **side-by-side** carefully.
2. Perform **Gaussian elimination** to reach RREF.
3. **Left side → identity matrix; Right side → inverse matrix**.

### Example Execution:
- An example 3x3 matrix is reduced to find its inverse using the outlined technique.
- The result matches the previously calculated inverse from earlier videos.

---

### Summary:
- **Deceptively Simple Algorithm**:
  - Position identity matrix and target matrix together.
  - Use Gaussian elimination.
  - Capture the result on the right as the inverse.

---

### Next Steps:
- Upcoming videos:
  - **Two explanations** for why this algorithm works.
- Later, a **third explanation** will be introduced.