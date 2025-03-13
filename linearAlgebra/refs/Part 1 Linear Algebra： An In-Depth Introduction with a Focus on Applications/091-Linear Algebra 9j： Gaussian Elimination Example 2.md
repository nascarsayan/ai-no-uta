## Problem 2: Flipped Matrix and Gaussian Elimination

### Overview

1. The matrix in this problem is a flipped version of the matrix in Problem 1.
   - Rows of the matrix in Problem 1 have been turned into columns in Problem 2.
   - The right-hand side has also been redefined for this problem.

2. **Key Observations:**
   - We are working with vectors in $\mathbb{R}^5$.
   - There are only 2 vectors, and they are linearly independent since neither is a scalar multiple of the other.
   - The two vectors span a 2-dimensional subspace of $\mathbb{R}^5$.

3. **Solution Existence:**
   - A solution exists **only if** the right-hand side vector lies in the column space of the matrix.
   - Gaussian elimination will reveal if this condition is met.

---

### Expectation from the Solution

- Since the null space is trivial (contains only the zero vector), **any solution will be unique.**
- The challenge lies in determining:
  1. If a solution exists.
  2. If the right-hand side is in the column space.

---

### Gaussian Elimination Process

1. **First Pivot:**
   - Identify the first pivot and use it to eliminate numbers below it.
   - Example row operations:
     - Subtract 2 of Row 1 from Row 2, eliminating the $2$ in Row 2.
     - Subtract 3 of Row 1 from Row 3, turning $3$ into $1$.
     - Subtract 4 of Row 1 from Row 4, turning $13$ into $1$.
     - Subtract 5 of Row 1 from Row 5, turning $16$ into $1$.

2. **Second Pivot:**
   - Identify the second pivot and eliminate all entries below it.
   - Example row operations:
     - Subtract Row 2 from Row 3, turning a $1$ into $0$.
     - Subtract Row 2 from Row 4, getting a $0$.
     - Subtract Row 2 from Row 5, eliminating $1$.

3. **Continue with successive pivots**, repeating the process, until all entries below the pivots are eliminated.

---

### Back Substitution using Jordan Elimination

1. Use back substitution to simplify the rows above the pivots and finalize the solution.
   - For example, subtract 3 of Row 2 from Row 1 to eliminate the $3$ above the pivot.
   - Apply similar steps on the right-hand side to ensure consistency.

---

### Final Solution 

- After completing Gaussian elimination and back substitution, compute the solution vector.
- Example:
  - Solution is determined to be **unique** since the null space is trivial.
  - Verify correctness by checking that operations on rows return consistent results for the right-hand side.

---

### Key Results

1. The solution is **unique** because the null space contains only the zero vector.
2. Gaussian elimination facilitates the verification of whether the solution exists (by checking if the right-hand side lies in the column space). 
3. The process ensures both consistency and completeness in solving the system.

