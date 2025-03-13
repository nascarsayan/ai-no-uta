## Introduction to Determinants

### Key Properties of Determinants
1. Determinant of the identity matrix equals 1.
2. Alternating property: When two columns are identical, the determinant becomes 0.
3. Linear property: Allows column decomposition and scalar multiplication.

These three properties can be used to **define the determinant**, and all formulas for determinants follow logically from this definition.

---

## Approach 1: 2x2 Determinants

### Formula for Determinant of a 2x2 Matrix:
If the matrix is:

$$
\begin{bmatrix}
a & b \\
c & d
\end{bmatrix}
$$

The determinant is calculated as:

$$
\text{det} =
a \cdot d - b \cdot c
$$

Example: 

$$
\text{det} =
2 \cdot 5 - 4 \cdot 3 = -2
$$

---

### Using Linear Property for Decomposition:
1. Decompose each column into a sum of vectors, e.g., first column as $\begin{bmatrix} 2 \\ 0 \end{bmatrix} + \begin{bmatrix} 0 \\ 4 \end{bmatrix}$.
2. Apply the linear property to represent the determinant as a sum of smaller determinants.

For the second column (example: $\begin{bmatrix} 3 \\ 0 \end{bmatrix} + \begin{bmatrix} 0 \\ 5 \end{bmatrix}$):
- Each determinant splits further using the linear property.

#### Final Decomposition:
The determinant gets split into individual terms, each weighted by scalar factors derived from the columns.

---

## Approach 2: Larger Matrices (e.g., 3x3, $n \times n$)

### Column Decomposition:
1. For an $n \times n$ matrix:
   - The first column is decomposed into the sum of $n$ vectors, each having a single nonzero entry.
   - The determinant is expressed as a sum of $n$ sub-determinants.

2. This process repeats for subsequent columns:
   - Second column = sum of $n$ vectors $\rightarrow$ $n^2$ determinants.
   - Third column $\rightarrow$ $n^3$ determinants.
   - Continue until $n^n$ determinants (total possible terms).

---

### Elimination of Determinants via Alternating Property:
- Determinants with two identical columns are eliminated (value becomes 0).
- Remaining determinants correspond to permutations of the entries and are weighted by their sign.

#### Surviving Determinants:
- **Number of surviving terms**: $n!$ (corresponding to permutations of rows/columns).

---

### Factorization
1. Factor out nonzero entries from columns.
2. Remaining determinants consist of matrices with entries of 1 and 0, ensuring row and column consistency.

---

### Signs of Determinants:
- Signs are determined by the number of row swaps required to transform the matrix into the identity matrix.
   - **Even number of swaps** $\rightarrow$ determinant is positive (+1).
   - **Odd number of swaps** $\rightarrow$ determinant is negative (-1).

---

## General Formula for $n \times n$ Matrices:
The determinant formula arises naturally from the properties:
1. **Alternating Property**: Zero determinant for identical columns.
2. **Linear Property**: Scalar factors and decomposition.
3. Permutations of rows/columns determine the surviving terms.

---

## Conclusion
There are **two approaches** to defining determinants:
1. Start with the algebraic formula and derive the properties.
2. Begin with the properties and deduce the formula.

Both approaches are equivalent, and the choice depends on the context or preference.

