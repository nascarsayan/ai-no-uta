## Determinant of Triangular Matrices

### Key Property:
- The determinant of a triangular matrix (whether lower or upper triangular) is the product of its diagonal entries.

### Implications:
1. **Diagonal Matrix:**
   - Since diagonal matrices are triangular (both upper and lower triangular), their determinant is also the product of their diagonal entries.

2. **Identity Matrix:**
   - Being a diagonal matrix with ones on the diagonal, the determinant of the identity matrix is simply 1.

### Proof:
1. Focus on **lower triangular matrices** (the proof for upper triangular matrices will follow using the **transpose property**).
    - If the property holds for lower triangular matrices, it holds for upper triangular matrices due to symmetry.

2. **General Form of an $n \times n$ Lower Triangular Matrix:**
    - Consider how terms contribute to the determinant.
    - Many terms in the determinant expression will naturally evaluate to zero because of zero entries in the matrix.

3. Nonzero Terms:
    - The nonzero terms arise from selecting diagonal entries $a_{11}, a_{22}, ..., a_{nn}$.
    - For every row:
        - Row 1 → $a_{11}$ is mandatory since other entries in the row are zero.
        - Row 2 → $a_{22}$ is chosen as all other entries are zero, except those already used in earlier rows.
        - This pattern continues for all rows.

4. **Final Term:**
    - After exhausting all rows, the only surviving term in the determinant calculation is:
      $$
      a_{11} \cdot a_{22} \cdot \ldots \cdot a_{nn}
      $$
    - This term corresponds to the **zero permutation** (identity permutation), which always has even parity (hence a positive sign).

### Example:
Consider a specific matrix:

$$
\begin{bmatrix}
-3 & 0 & 0 \\
1 & 6 & 0 \\
5 & 2 & -6
\end{bmatrix}
$$

The determinant is calculated as:

$$
\text{Determinant} = (-3) \cdot (6) \cdot (-6) = -36
$$

### Conclusion:
- This simple calculation confirms the general property that the determinant of triangular matrices is the product of their diagonal entries.