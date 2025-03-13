## 1. Two Miracles of Linear Algebra

### First Miracle: Column Rank Equals Row Rank
- For **any matrix**, the number of linearly independent columns (*column rank*) always equals the number of linearly independent rows (*row rank*).

---

### Second Miracle: Single Well-Defined Matrix Inverse
#### Statement:
- For any matrix with an inverse, multiplying by the inverse from the **left** or the **right** results in the **identity matrix**.

$$
A^{-1} A = I, \quad A A^{-1} = I
$$

#### Implications:
- There is no need to consider separate left and right inverses; every matrix with an inverse has **one single well-defined inverse**.
- This property simplifies matrix algebra significantly.

#### Key Takeaway:
- Every matrix that has an inverse has a **single well-defined inverse**, and multiplication (left or right) results in the **identity matrix**.

---

## 2. Surprises in Matrix Multiplication

### Non-Commutativity of Matrix Multiplication:
- **Rule**: Matrix multiplication is generally **non-commutative**, meaning:
$$
AB \neq BA \quad \text{(in general)}
$$

#### Exception 1: Multiplication by Identity Matrix
- Multiplying a matrix by the **identity** on either side yields the matrix itself:
$$
AI = IA = A
$$

#### Exception 2: Multiplication by an Inverse Matrix
- When two matrices are inverses of each other, their product (in either order) equals the identity matrix:
$$
A^{-1} A = AA^{-1} = I
$$

---

### Unexpected Symmetry of Inverses:
- Despite non-commutative matrix multiplication, inverses behave symmetrically:
  - Multiplying the inverse on the **left** or **right** produces the **same result (identity matrix)**.
- This result is **unexpected** and seems **miraculous** in the context of matrix mechanics.

---

## 3. Dot Product Perspective: Why this Holds

The calculation for individual entries in the resulting identity matrix involves a dot product. Here's an example:

### Entry Calculation:
#### First Zero Entry:
$$
- \frac{2}{3} \times 1 + \frac{11}{3} \times 4 - 2 \times 7 = 0
$$

#### Second Zero Entry (from identity matrix):
$$
- \frac{4}{3} \times 4 + \frac{11}{3} \times 5 - 2 \times 6 = 0
$$

- **Observation**: Although the numbers and positions are completely different, the interaction of these values leads to **consistent results** across all entries.

---

### Deeper Perspective:
- Simple mechanical arguments fail to adequately explain the symmetry of inverses in matrix multiplication.
- A more profound explanation comes from a **bird's-eye view** on matrix multiplication (to be presented in another video).

---

## 4. Summary of Matrix Multiplication Rules and Exceptions

### Rule:
Matrix multiplication is **non-commutative**:
$$
AB \neq BA \quad \text{(typically)}
$$

### Exceptions:
1. **Identity Matrix**:
   $$
   AI = IA = A \quad \text{(identity property)}
   $$

2. **Inverse Matrices**:
   $$
   A^{-1} A = AA^{-1} = I \quad \text{(inverse symmetry)}
   $$

---

## 5. Key Takeaways

- Matrix multiplication is **non-commutative**, but there are two notable exceptions:
  1. Multiplication involving the **identity matrix**.
  2. Multiplication involving **inverse matrices**.
- The symmetry of inverse matrices is an unexpected phenomenon, showcasing the **miraculous nature of linear algebra**.