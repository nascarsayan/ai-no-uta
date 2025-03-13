# Inner Products in $\mathbb{R}^n$

## 1. Introduction

- **Inner products** are a fundamental concept in linear algebra.
- **Positive definiteness** is a fascinating requirement of inner products.
- Determining whether an expression is positive definite can be complex.

---

## 2. Matrix Form and Distributive Property

- All operations in linear algebra, including inner products, can be expressed as **matrix products**.
- The distributive property ensures that terms satisfy specific constraints:
    - Individual terms contain one entry from vector $A$ and one entry from vector $B$.
    - No terms like $3A$ or omitted terms allowed, as they violate distributivity.
- **Matrix representation** simplifies operations by leveraging compactness.

### Example Matrix Form:
Given $A = [a_1\ a_2\ a_3]$ and $B = [b_1\ b_2\ b_3]$, the inner product can be written as:
$$
A^\top \cdot B = 
\begin{bmatrix}
a_1 & a_2 & a_3
\end{bmatrix}
\begin{bmatrix}
b_1 \\ b_2 \\ b_3
\end{bmatrix}
$$

---

## 3. Properties of Inner Products

1. **Distributivity**:
    - Essential for inner product properties.
    - Guarantees matrix form representation.

2. **Commutativity**:
    - Requires the matrix to be **symmetric**.
    - Symmetry implies:
        $$
        A^\top = A
        $$

3. **Positive Definiteness**:
    - Requires that for any non-zero vector $A$, the value $A^\top A$ is positive.

---

## 4. Bilinear Forms

- **Definition**: A bilinear form is a function of two vectors where:
    - Linear in both arguments.
    - Takes two vectors and returns a scalar.
- To qualify as an inner product:
    - The bilinear form must be **commutative** (matrix symmetry required).
    - Matrix expression must respect symmetry properties.

---

## 5. Example: Evaluating Positive Definiteness

### Consider the expression:
$$
F(A, B) = A^\top Q B
$$
Where $Q$ is a matrix, and $A, B$ are vectors.

#### Key Considerations:
1. **Matrix symmetry**:
    - $Q$ must satisfy $Q^\top = Q$.

2. **Positive definiteness**:
    - Must satisfy $F(A, A) > 0$ for any non-zero vector $A$.

---

## 6. Counterexample for Positive Definiteness

### Example Matrix:
$$
Q = 
\begin{bmatrix}
4 & -7 & 0 \\
-7 & 2 & 1 \\
0 & 1 & 3
\end{bmatrix}
$$

#### Evaluation of $F(A, A)$:
1. **For vector $A = [1\ 0\ 1]$**:
    - Calculate $F(A, A) = A^\top Q A$:
        - Contribution from diagonal entries: $4 + 3 = 7$.
        - Contribution from off-diagonal entries: $-7 \cdot 1 + 0 + 0 = -7$.
        - Total: $7 - 7 = 0$ (not positive).

2. **Conclusion**:
    - Matrix $Q$ lacks positive definiteness.

---

## 7. Subtle Scenarios in Positive Definiteness

- Positive definiteness problems become more interesting and challenging in higher dimensions or subtle cases.

---

## 8. Advantages of Matrix Notation

- **Compactness**:
    - Matrix representation organizes coefficients logically for better structure.
- Moving forward:
    - Inner products and bilinear forms will be exclusively discussed in **matrix notation** for clarity.

