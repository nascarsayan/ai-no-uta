## Adding a Multiple of One Row or Column to Another Leaves the Determinant Unchanged

### Key Properties of the Determinant
1. The **determinant remains unchanged** when adding a multiple of one row or column to another. 
2. This fact, combined with:
   - The **alternating property** (which explains how the determinant changes when two rows are swapped).
   - The **linearity property** (which explains how the determinant behaves under scalar multiplication).
3. Together, these properties allow us to calculate determinants using **Gaussian elimination**.

---

### Proof that Adding a Multiple of One Row/Column Leaves the Determinant Unchanged

1. **Setup**:
   - Let $A$ be a square matrix.
   - Add a multiple $\alpha$ of the first row to the third row.
   
2. **Applying Linearity**:
   - By the linearity property, the determinant can be expressed as the sum of two determinants:
     - The first determinant contains the original third row.
     - The second determinant contains the added multiple of the first row.

   $$
   \text{det}(A) = \text{det}\left(\begin{bmatrix}
   \text{Row 1} \\
   \text{Row 2} \\
   \text{Original Row 3}
   \end{bmatrix}\right)
   + \text{det}\left(\begin{bmatrix}
   \text{Row 1} \\
   \text{Row 2} \\
   \alpha \cdot \text{Row 1}
   \end{bmatrix}\right)
   $$

3. **Factoring Out $\alpha$**:
   - In the second determinant, $\alpha$ (the scalar multiplier) can be factored out:
     
     $$
     \text{det}\left(\begin{bmatrix}
     \text{Row 1} \\
     \text{Row 2} \\
     \alpha \cdot \text{Row 1}
     \end{bmatrix}\right) = 
     \alpha \cdot \text{det}\left(\begin{bmatrix}
     \text{Row 1} \\
     \text{Row 2} \\
     \text{Row 1 (again)}
     \end{bmatrix}\right)
     $$

4. **Result of Two Identical Rows**:
   - In the second term, the determinant contains two identical rows (Row 1 appears twice). 
   - By the **alternating property**, the determinant of any matrix with two identical rows is zero:
     
     $$
     \text{det}\left(\begin{bmatrix}
     \text{Row 1} \\
     \text{Row 2} \\
     \text{Row 1}
     \end{bmatrix}\right) = 0
     $$

5. **Conclusion**:
   - The only term left is the determinant of the original matrix:
     
     $$
     \text{det}(A) = \text{det}\left(\begin{bmatrix}
     \text{Row 1} \\
     \text{Row 2} \\
     \text{Original Row 3}
     \end{bmatrix}\right)
     $$
   - Hence, adding a multiple of one row to another does not change the determinant.

---

### Implications for Gaussian Elimination
- With this property, combined with the alternating and linearity properties, we can:
  1. Row reduce a matrix to a simpler form.
  2. Use the result to compute the determinant efficiently.

