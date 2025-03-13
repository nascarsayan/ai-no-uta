# Structured Notes: Determinants

## Overview

This session provides a grand overview of the determinant and its properties. Key areas covered include:
- Algebraic definition of the determinant.
- Navigation from the definition to its properties.
- Determinant implications in transformations and geometry.
- Practical calculation methods like Gaussian elimination.

---

## 1. Algebraic Definition of the Determinant

The determinant of an $n \times n$ matrix is defined as a sum of $n!$ terms, where:
- Each term is a product of $n$ entries from the matrix.
- The entries are chosen such that:
  - **One entry per row and column**.
  - Columns are aligned according to a permutation $\epsilon$.

### Formula:

$$
\det(A) = \sum_{\epsilon} \text{sign}(\epsilon) \prod_{i=1}^n a_{i, \epsilon(i)}.
$$

Where $\text{sign}(\epsilon)$ determines if $\epsilon$ is an even (+1) or odd (-1) permutation.

---

## 2. Key Properties of Determinants

### **Property 1:** Determinant of Transpose
$$
\det(A^T) = \det(A).
$$
- Enables interchangeability in examining rows versus columns.

---

### **Property 2:** Determinant of Triangular Matrix
For triangular matrices (upper or lower triangular):
$$
\det(A) = \prod_{i=1}^n a_{ii}.
$$
- Only diagonal entries affect the determinant.
- Used frequently in Gaussian elimination for efficiency.

---

### **Property 3:** Determinant of Identity Matrix
$$
\det(I) = 1.
$$
- Serves as a foundational reference.

---

### **Property 4:** Swapping Columns and Rows
Swapping two columns (or rows) changes the sign of the determinant:
$$
\det(A') = -\det(A).
$$

Implications:
- If two columns (or rows) are equal, $\det(A) = 0$.

---

### **Property 5:** Determinant Linearity
The determinant is **linear with respect to individual columns (or rows)**.

#### (a) Scalar Multiplication:
Multiplying a column by a scalar $k$ scales the determinant:
$$
\det(A') = k \cdot \det(A).
$$

#### (b) Column Addition:
The determinant of a matrix where one column is the sum of two vectors is:
$$
\det(A + B) = \det(A) + \det(B).
$$

Note: Applies **individually** to columns, not entire matrices. This property is referred to as **multi-linearity**.

---

### **Property 6:** Zero Column/Row
If a matrix contains a zero column or row:
$$
\det(A) = 0.
$$

---

### **Property 7:** Gaussian Elimination Behavior
The determinant remains unchanged when:
- Adding a multiple of one column/row to another.
  
The determinant's value under other Gaussian elimination operations:
- **Swapping rows:** Determinant changes sign.
- **Scaling rows:** Determinant scales proportionally.

---

### **Property 8:** Singular Matrices
A matrix is **singular** if and only if:
$$
\det(A) = 0.
$$
Equivalent conditions:
- Matrix has linearly dependent columns.
- Transformation collapses space (e.g., zero volume).

---

## 3. Geometric Interpretation of Determinants

### **In 2D (Area)**
For a $2 \times 2$ matrix:
$$
\det(A) = \text{Area of parallelogram formed by column vectors}.
$$

- **Positive Area:** Counterclockwise orientation.
- **Negative Area:** Clockwise orientation.

---

### **In 3D (Volume)**
For a $3 \times 3$ matrix:
$$
\det(A) = \text{Volume of parallelepiped formed by column vectors}.
$$

Orientation determined by the **right-hand rule**.

---

### **Higher Dimensions**
In dimensions greater than three:
- Geometry **does not extend**.
- Determinants **define volume** algebraically, inspired by 2D/3D intuition.

---

## 4. Practical Calculation: Gaussian Elimination

### Steps:
1. Apply Gaussian elimination to the matrix to obtain an upper triangular form.
2. Keep track of:
   - Row swaps (change sign).
   - Scaling (scale determinant).
3. Compute the determinant by multiplying the diagonal entries.

$$
\det(A) = \prod_{i=1}^n a_{ii} \text{ (after Gaussian elimination)}.
$$

---

## 5. Surprising Properties of Determinant

### **Product Rule**
The determinant of the product of two matrices equals the product of their determinants:
$$
\det(AB) = \det(A) \cdot \det(B).
$$

### **Geometric Intuition**
Matrices as space transformations:
- A matrix stretches areas/volumes by a factor determined by its determinant.

For transformation matrices $A$ and $B$:
- $A$ stretches areas by factor $x$, $B$ by factor $y$.
- Combined transformation stretches by $x \cdot y$.

---

## 6. Proof Sketch: Geometric Connection in 2D

Using geometric arguments, signed area satisfies all determinant properties:
1. **Identity matrix** corresponds to unit square (area = 1).
2. **Swapping vectors** reverses orientation (negative determinant).
3. Scaling vectors stretches area proportionally.
4. Linearity holds for combined and split parallelograms.

Thus:
$$
\text{Signed Area} = \det(A).
$$

In higher dimensions, the connection to signed volume under transformations is extended algebraically.

---

## 7. Significance of Determinants in Applied Mathematics

Determinants:
- Offer tools for **space transformation** analysis, including stretching and collapsing.
- Are extensively used in **linear algebra**, **geometry**, and **multidimensional spaces**.

Geometric and algebraic interpretations unify intuitive and computational aspects of determinants.

---

This session concludes the overview of determinant properties. Subsequent discussions will dive deeper into individual aspects on the board.