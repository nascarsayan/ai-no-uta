# Notes: Algebraic Definition of Determinants

## 1. Introduction 
- **Goal:** Present and explain the direct algebraic definition of the determinant.  
- **Prerequisites:**
  - Understanding permutations.
  - Understanding permutation parity (even/odd).

## 2. Previous Context
- Previously derived expressions for determinants of small matrices:
  - 1×1, 2×2, 3×3, and 4×4 matrices.
- **Strategy:**
  - Postulate an algebraic definition based on observed patterns.  
  - Derive determinant properties using this definition.

---

## 3. General Setup: Denoting Matrix Entries
- A **3×3 matrix** with entries denoted using subscripts:
  
  $$
  \begin{bmatrix} 
  a_{11} & a_{12} & a_{13} \\ 
  a_{21} & a_{22} & a_{23} \\ 
  a_{31} & a_{32} & a_{33} 
  \end{bmatrix}
  $$
  
  - Subscript format $a_{ij}$:  
    - $i$: row index.  
    - $j$: column index.

---

## 4. Determinants for 3×3 Matrices
- **Pattern Summary:**
  - Determinant consists of **6 terms**, each a product of $3$ entries:
    - One entry from each row.
    - One entry from each column.

- **Key Observations:**
  - **Rows** in each term follow an ordered sequence: $1, 2, 3$.  
  - **Columns** are scrambled based on permutations.  
  - There are 6 possible permutations for a $3×3$ matrix   ($1, 2, 3$):  
    - $1, 2, 3$, $1, 3, 2$, $2, 1, 3$, $2, 3, 1$, $3, 1, 2$, $3, 2, 1$.

---

## 5. Permutations and Sign
- Determinant term signs depend on the **parity of the permutation**:
  - **Even permutations**: $+$.  
  - **Odd permutations**: $-$.

- **Example Analysis:**
  1. Permutation $1, 2, 3$:
     - Even (no swaps required).
     - Sign: $+$.
  2. Permutation $1, 3, 2$:
     - Odd (1 swap: $3↔2$).
     - Sign: $-$.
  3. Permutation $2, 3, 1$:
     - Even (2 swaps: $1↔3$, then $3↔2$).  
     - Sign: $+$.
  4. Continuing similarly for all 6 permutations...

---

## 6. General Formula for Determinants
- For an $n×n$ matrix, the determinant is defined as:

  $$
  \text{det}(A) = \sum_{\text{permutations } \sigma} \text{sgn}(\sigma) \prod_{i=1}^n a_{i, \sigma(i)}
  $$

  - $\sigma$: Permutation of column indices $\{1, 2, \dots, n\}$.  
  - $\text{sgn}(\sigma)$: Sign of permutation $\sigma$:
    - $+1$ for even.
    - $-1$ for odd.  
  - $\prod_{i=1}^n a_{i, \sigma(i)}$: Product of selected matrix entries.

---

## 7. Step-by-Step Illustration for 5×5 Matrices
- **Example:** Permutation $(2, 3, 5, 4, 1)$.  
  - Term: $a_{12} a_{23} a_{35} a_{44} a_{51}$.  
  - Compute parity:
    - Requires **5 swaps** to return to $(1, 2, 3, 4, 5)$.
    - Odd permutation, so sign is $-$.

---

## 8. Observations on Complexity
- Determinants grow factorially in terms of terms to evaluate:
  - For $n=5$ matrix, there are $5! = 120$ terms.
- Practical computation (e.g., row reduction methods) is preferred over brute force.

---

## 9. Final Remarks
- Direct algebraic definition:
  - Simultaneously **long** and **elegant**.  
  - Builds a strong foundation for understanding determinant properties.  
- The beauty lies in how permutations and matrix structure intertwine seamlessly.