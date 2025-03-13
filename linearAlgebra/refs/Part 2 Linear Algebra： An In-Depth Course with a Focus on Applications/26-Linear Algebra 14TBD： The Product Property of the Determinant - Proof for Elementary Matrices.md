## Determinant Property for Elementary Matrices

### Overview

- **Objective**: To prove an important determinant property for elementary matrices.
- **Approach**: Start with elementary matrices and extend to general matrices in a subsequent discussion.

---

### 1. Elementary Matrix: Triangular Matrix with Ones on the Diagonal

#### Determinant Calculation:
- Consider a triangular matrix with ones on the diagonal and a single nonzero entry off the diagonal.
  
#### Property Explanation:
- The determinant of the product is equal to the determinant of $B$, as such a matrix adds a multiple of one row to another, leaving the determinant unchanged.

#### Identity:
On the left-hand side, the determinant of the product equals:
$$
\det(A \cdot B) = \det(B)
$$

On the right-hand side:
$$
\det(A) \cdot \det(B) = 1 \cdot \det(B) = \det(B)
$$

#### Conclusion:
- The identity holds as both sides equal $\det(B)$.

---

### 2. Elementary Matrix: Single Row Switch

#### Determinant Calculation:
- This matrix switches two rows, changing the sign of the determinant.

#### Property Explanation:
- On the left-hand side, the determinant of the product equals:
$$
\det(A \cdot B) = -\det(B)
$$

On the right-hand side:
$$
\det(A) \cdot \det(B) = (-1) \cdot \det(B) = -\det(B)
$$

#### Conclusion:
- The identity holds as both sides equal $-\det(B)$.

---

### 3. Elementary Matrix: Diagonal Scaling

#### Determinant Calculation:
- This matrix equals the identity matrix, except one entry on the diagonal is not $1$.

#### Property Explanation:
- On the left-hand side, the determinant of the product equals:
$$
\det(A \cdot B) = k \cdot \det(B)
$$
where $k$ corresponds to the scaled diagonal entry.

On the right-hand side:
$$
\det(A) \cdot \det(B) = k \cdot \det(B)
$$

#### Conclusion:
- The identity holds as both sides equal $k \cdot \det(B)$.

---

### General Conclusions

1. **Elementary Matrices**:
   - The determinant property holds for all kinds of elementary matrices.

2. **Extension to General Matrices**:
   - In the next discussion, we will prove that **any matrix can be represented as a product of elementary matrices**.
   - Using this representation, the determinant property is extended to arbitrary matrices.

---