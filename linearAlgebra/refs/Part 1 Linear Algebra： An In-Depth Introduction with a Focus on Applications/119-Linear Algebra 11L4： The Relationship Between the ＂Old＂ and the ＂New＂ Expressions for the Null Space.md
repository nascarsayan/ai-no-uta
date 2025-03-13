## Expressing Null Spaces with Matrices

### Null Spaces and Basis Representation
- A new way of expressing null spaces of matrices involves combining the elements of a basis into a matrix.
- Example: Given a matrix \( A \), its null space can be compactly represented by a matrix \( N \), satisfying:
  $$
  A N = 0
  $$
- This approach captures the relationship between the matrices \( A \) and \( N \) through a compact algebraic identity.

### Null Space as a Column Space
- It's important to note that the null space is fundamentally a **space**, i.e., a collection of vectors.
- The matrix \( N \) **represents** the null space.
  - Specifically, the null space is the **column space** of the matrix \( N \), which is the set of all possible linear combinations of its columns.
  - Thus, elements of the null space are:
    $$
    \text{Linear combinations of the basis elements (columns of } N\text{)}.
    $$

### Comparing Representations
- The traditional way expresses the null space as a collection of vectors formed by combinations of basis elements involving parameters like \( \alpha, \beta, \dots \):
  $$
  \text{Null space as vectors: } \alpha v_1 + \beta v_2 + \dots
  $$
- The matrix representation provides a compact algebraic formulation:
  $$
  A N = 0 \quad \text{and} \quad \text{Null space} = \text{Column space of } N.
  $$
- Both approaches are equivalent but differ in perspective:
  - **Traditional representation** is more direct in geometric terms.
  - **Matrix form** leverages the tools of linear algebra to encode relationships succinctly.

### Reconciling Both Representations
- To reconcile the algebraic representation with the traditional vector formulation:
  1. Combine the parameters \( \alpha, \beta \) into a column vector.
  2. Multiply this vector with \( N \) to generate the null space vectors:
     $$
     n(\alpha, \beta) = N \begin{bmatrix} \alpha \\ \beta \end{bmatrix}.
     $$

### Choosing Matrix Dimensions and Product Order
- Through trial and error, the appropriate setup is to:
  - Combine parameters (e.g., \( \alpha, \beta \)) into a **column vector**.
  - Multiply this **from the right** of the matrix \( N \):
    $$
    n = N \begin{bmatrix} \alpha \\ \beta \end{bmatrix}.
    $$

### Verifying the Approach
- To verify this representation:
  - Perform the matrix multiplication:
    $$
    N \begin{bmatrix} \alpha \\ \beta \end{bmatrix} = \alpha n_1 + \beta n_2,
    $$
    where \( n_1, n_2 \) are columns of \( N \) (basis vectors of the null space).
  - The result matches the traditional combination of basis elements.

### Conclusion
- Matrix algebra provides a versatile and compact tool to represent and manipulate null spaces.
- The elegant identity \( A N = 0 \) encapsulates the null space while preserving its geometric significance as the column space of \( N \).