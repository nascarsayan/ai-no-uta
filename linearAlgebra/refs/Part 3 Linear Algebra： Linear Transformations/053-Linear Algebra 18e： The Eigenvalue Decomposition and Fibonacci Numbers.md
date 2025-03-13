## Fibonacci Numbers and Linear Algebra

### Introduction
- Fibonacci numbers are a beautiful and vast topic.
- Extensive literature exists on Fibonacci numbers, including their applications and connections to linear algebra, particularly eigenvalue decomposition.

---

### 1. Fibonacci Numbers Basics
- The Fibonacci sequence starts with two numbers, e.g., `0` and `1`.
- Every subsequent number is the **sum of the two preceding numbers**:
  $$
  \text{Example: } 1 = 0 + 1, \, 2 = 1 + 1, \, 3 = 1 + 2, \, 5 = 2 + 3, \, 8 = 3 + 5, \, \ldots
  $$
- This sequence produces familiar numbers such as: `0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55...`.

---

### 2. The Golden Ratio $\phi$
- Fibonacci numbers have a deep connection to the **Golden Ratio**:
  $$
  \phi = \frac{1 + \sqrt{5}}{2} \approx 1.618
  $$
- Successive ratios of Fibonacci numbers, $F_{n+1} / F_n$, converge to $\phi$ as $n \to \infty$.

---

### 3. Properties and Relationships of Fibonacci Numbers
#### Property 1: Successive Ratios
- Ratios $F_{n+1} / F_n$ converge to $\phi$:
  $$
  2 / 1, \, 3 / 2, \, 5 / 3, \, 8 / 5, \, \ldots \to \phi
  $$

#### Property 2: Closed-Form Expression for $F_n$ ("Binet's Formula")
- The closed-form expression for the $n$th Fibonacci number:
  $$
  F_n = \frac{\phi^n - (-\phi)^{-n}}{\sqrt{5}}
  $$

#### Property 3: Sum of Squares
- The sum of squares of two consecutive Fibonacci numbers is another Fibonacci number:
  $$
  F_n^2 + F_{n+1}^2 = F_{2n+1}
  $$

---

### 4. Matrix Representation of Fibonacci Numbers
- The Fibonacci sequence can be represented using **linear algebra**.
  
#### Matrix Representation:
\[
\begin{bmatrix} F_n \\ F_{n+1} \end{bmatrix} =
\begin{bmatrix} 0 & 1 \\ 1 & 1 \end{bmatrix}
\begin{bmatrix} F_{n-1} \\ F_n \end{bmatrix}
\]

#### Powers of the Matrix:
- To compute $F_n$, raise the matrix to the $(n-1)$th power:
  $$
  \begin{bmatrix} F_n \\ F_{n+1} \end{bmatrix} =
  \begin{bmatrix} 0 & 1 \\ 1 & 1 \end{bmatrix}^{n-1}
  \begin{bmatrix} 0 \\ 1 \end{bmatrix}
  $$

#### From Recurrence to Linear Algebra:
- The rule $F_{n+2} = F_{n+1} + F_n$ allows expressing the sequence in terms of matrix multiplication:
  \[
  \begin{bmatrix} F_{n+1} \\ F_{n+2} \end{bmatrix} =
  \begin{bmatrix} 0 & 1 \\ 1 & 1 \end{bmatrix}
  \begin{bmatrix} F_{n} \\ F_{n+1} \end{bmatrix}.
  \]

---

### 5. Eigenvalue Decomposition and Fibonacci Numbers
#### The Transition Matrix:
- Consider the matrix 
  $$
  A = \begin{bmatrix} 0 & 1 \\ 1 & 1 \end{bmatrix}.
  $$
- The eigenvalues of $A$ are $\lambda_1 = \phi$ (Golden Ratio) and $\lambda_2 = -1/\phi$.

#### Eigendecomposition:
- Perform an eigendecomposition of $A$:
  $$
  A = PDP^{-1},
  $$
  where:
  - $P$ contains eigenvectors of $A$.
  - $D = \text{diag}(\phi, -1/\phi)$.

#### Matrix Power Simplification:
- To compute $A^{n-1}$:
  $$
  A^{n-1} = P D^{n-1} P^{-1}.
  $$

---

### 6. Derivation of the Closed-Form Formula
1. Start with:
   $$
   F_n = \begin{bmatrix} 1 & 0 \end{bmatrix}
   \begin{bmatrix} 0 & 1 \\ 1 & 1 \end{bmatrix}^{n-1}
   \begin{bmatrix} 0 \\ 1 \end{bmatrix}.
   $$

2. Employ eigenvalue decomposition:
   $$
   F_n = \begin{bmatrix} 1 & 0 \end{bmatrix} P D^{n-1} P^{-1} \begin{bmatrix} 0 \\ 1 \end{bmatrix}.
   $$

3. Substituting eigenvalues and simplifying:
   $$
   F_n = \frac{\phi^n - (-1/\phi)^n}{\sqrt{5}}.
   $$

---

### 7. Applications and Observations
#### General Applications:
- The eigenvalue decomposition method can simplify the computation of:
  - Fibonacci-like sequences.
  - Linear recurrence relations.

#### Observations:
1. Despite involving square roots, $F_n$ is always an integer.
2. The elegance of the formula highlights the surprising interplay between linear algebra and number theory.

#### Confirmation of Properties:
- Properties like sums and ratios of Fibonacci numbers can be easily verified using the closed-form formula.

---

### 8. Closing Remarks
- Fibonacci numbers are a prime example of how abstract mathematical fields (like linear algebra) can provide deep insights.
- The eigenvalue decomposition not only simplifies computation but also reveals hidden connections between numbers, algebra, and geometry.