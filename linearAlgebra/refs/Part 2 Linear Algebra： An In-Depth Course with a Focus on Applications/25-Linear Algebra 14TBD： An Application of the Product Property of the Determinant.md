## 1. Determinant of Matrix Products

### Goal:
To prove the property:  
$\text{det}(AB) = \text{det}(A) \cdot \text{det}(B)$  

#### Geometric Intuition:
1. **Interpretation of matrices**:
    - Matrices can be interpreted as transformations of space.
    - The determinant expresses how areas are scaled under these transformations.
2. **Scaling areas**:
    - If two transformations (matrices) are applied one after another:  
      - The net scaling factor (determinant of the product) equals the product of individual scaling factors.
    - Example:
        - Transformation 1: Stretch by $5$.
        - Transformation 2: Stretch further by $7$.
        - Net stretch = $5 \times 7 = 35$.  

#### Insights:
- The property is not surprising geometrically but needs algebraic proof.
- Proof based on **elementary matrices** and **row operations** will provide further insights.

---

## 2. Row Operations and Determinant Effects

### Adding a Multiple of One Row to Another:
1. Representation:
    - Adding a multiple of one row to another can be expressed using an **elementary matrix**.
2. Determinant Effect:
    - Determinant of the resulting matrix equals the product of:
      - Determinant of the elementary matrix (which is $1$ for this operation).
      - Determinant of the original matrix.
    - Conclusion:
        - **Adding a multiple of one row to another leaves the determinant unchanged**.

---

### Switching Two Rows:
1. Representation:
    - Switching rows in a matrix can be expressed using an **elementary matrix**.
2. Determinant Effect:
    - Determinant of the elementary matrix = $-1$ (since it's one row swap away from identity).
    - Determinant of the new matrix:
        $$
        \text{det}(\text{new matrix}) = -\text{det}(B)
        $$
    - Conclusion:
        - **Switching rows changes the sign of the determinant**.

---

### Multiplying a Row by a Scalar:
1. Representation:
    - Multiplying a row by a scalar is expressed using an **elementary matrix**.
2. Determinant Effect:
    - Determinant of the elementary matrix:
        - For diagonal entries, determinant = product of diagonal elements.  
      Example:
      $$
      \text{diag}([1, 7, 1]) \rightarrow \text{det} = 7
      $$
    - Determinant of the new matrix:
        $$
        \text{det}(\text{new matrix}) = 7 \times \text{det}(B)
        $$
    - Conclusion:
        - **Multiplying a row by a scalar multiplies the determinant by the same scalar**.

---

## 3. Summary of Determinant Row Operation Effects:
- **Add a multiple of a row to another:** Determinant **unchanged**.
- **Switch rows:** Determinant changes **sign**.
- **Multiply row by scalar:** Determinant scaled by the scalar.

---

## 4. Proof Strategy:
### Current Video:
- Explore effects of row operations using property $\text{det}(AB) = \text{det}(A) \cdot \text{det}(B)$.

### Subsequent Videos:
1. Reverse the logic:
    - Start from row operation effects and derive $\text{det}(AB) = \text{det}(A) \cdot \text{det}(B)$.
2. Proof steps:
    - Establish the identity for **elementary matrices**.
    - Extend proof to **all matrices**.

