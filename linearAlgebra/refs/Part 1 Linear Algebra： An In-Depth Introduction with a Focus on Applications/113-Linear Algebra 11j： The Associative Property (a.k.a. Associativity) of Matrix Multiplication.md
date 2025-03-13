## Associativity in Matrix Multiplication

### Overview of Associativity

- The **associative property** of multiplication states that in a triple product, the order of grouping does not matter.
- For ordinary numbers, the result of $13 \times (25 \times 4)$ is the same as $(13 \times 25) \times 4$:
    1. $25 \times 4 = 100$
    2. $13 \times 100 = 1300$
    - Both groupings produce the same result.

### Representation Using Parentheses

- Parentheses are used to indicate precedence in operations. For example:
    - $(AB)C$ means multiply $A$ and $B$ first, then multiply the result with $C$.
    - $A(BC)$ means multiply $B$ and $C$ first, then multiply the result with $A$.
- Associativity can be formally written as:
    $$
    (AB)C = A(BC)
    $$
- Since the results are the same regardless of grouping, parentheses can often be omitted.

---

### Associative Property in Matrix Multiplication

- Matrix multiplication is **also associative**. This property can be illustrated by considering the dimensions of matrices:
    - Example setup:
        - $A$: $2 \times 3$ matrix
        - $B$: $3 \times 2$ matrix
        - $C$: $2 \times 4$ matrix
    - Both groupings are compatible:
        1. $(AB)C$: $A \cdot B$ produces a $2 \times 2$ matrix, which can then multiply $C$ ($2 \times 4$).
        2. $A(BC)$: $B \cdot C$ produces a $3 \times 4$ matrix, which can then multiply $A$ ($2 \times 3$).

---

### Verification of Associativity Through Example

#### Intermediate Results
1. **First grouping: $(AB)C$**
    - Compute $AB$:
        - Output: $2 \times 2$ matrix.
    - Multiply the result with $C$:
        - Final output: $2 \times 4$ matrix.

2. **Second grouping: $A(BC)$**
    - Compute $BC$:
        - Output: $3 \times 4$ matrix.
    - Multiply the result with $A$:
        - Final output: $2 \times 4$ matrix.

#### Observation
- Both groupings result in the same $2 \times 4$ matrix, confirming that the matrix product is associative.

---

### Importance of Associativity

1. **Flexibility in Computations:**
    - Allows for choosing the most computationally efficient grouping while ensuring the result remains the same.
    - Example:
        - Multiplying $4 \times 4$ matrices followed by a $4 \times 1$ vector:
            - Grouping $(A \cdot B) \cdot C$: Compute larger, intermediate results, requiring more operations.
            - Grouping $A \cdot (B \cdot C)$: Compute smaller, intermediate results, reducing operations.

2. **Efficiency Considerations:**
    - Multiplying intermediate results (like producing vectors early) can significantly reduce computational effort.

---

### Proof Strategies for Associativity

- **Experimental Approach:**
    - Work through multiple triple-product examples and verify that the same result is obtained for both groupings.
- **General Proof:**
    - Use algebraic operations with the dimensions of matrices to show that associativity holds universally.
- **Computational Illustration:**
    - Use a computational system to evaluate products in both groupings and verify that results align.

---

### Taking Advantage of Associativity

- Due to associativity:
    - Systems can evaluate matrix products in different orders for efficiency.
    - Parentheses can often be dropped when writing expressions, e.g.,
        $$
        ABC \quad \text{instead of} \quad (AB)C \text{ or } A(BC)
        $$
- The associative property ensures that regardless of the order of grouping, the results remain consistent.

---

### Summary

- Associativity is a critical property of matrix multiplication and makes it similar to multiplication of ordinary numbers.
- It provides the freedom to group operations in a way that minimizes computational complexity.
- Associativity is formally expressed as:
    $$
    (AB)C = A(BC)
    $$
- Example calculations and computational proof confirm this property.
  
Next topic: **Commutativity** – where matrix multiplication differs from ordinary multiplication.