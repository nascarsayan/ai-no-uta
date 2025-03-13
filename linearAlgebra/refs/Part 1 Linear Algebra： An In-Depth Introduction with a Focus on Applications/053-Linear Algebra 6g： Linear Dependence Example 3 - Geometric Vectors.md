## Linear Combinations and Relationships in Vectors

### Goal: Decompose $e$ as a Linear Combination
- The objective is to express $e$ as a linear combination of the vectors $a$, $b$, $c$, and $d$ in **all possible ways**.
- Capture all these combinations in a **single mathematical expression**.

---

### Key Concepts:
1. **Linear Dependence**  
   The linear dependence **among $a$, $b$, $c$**, and **$d$** plays a pivotal role in achieving the goal.

2. **Trivial vs. Non-Trivial Combinations**  
   - A **non-trivial linear combination** evaluates to **0**, revealing dependencies.  
   - This doesn't change the fact that the linear combination can still evaluate to $e$ but allows the exploration of all possible variations.

---

### Observed Dependencies and Relations Among Vectors:
#### 1. Dependency from **$b$ as a Linear Combination**:  
   - $b$ can be expressed as:

     $$
     b = a + c
     $$

   - Rearrange into:

     $$
     a - b + c = 0
     $$

   - This creates a **non-trivial zero**. Adding this to the linear combination of $e$ yields:  
     
     $$
     e = \alpha(a - b + c) + ...
     $$

#### 2. Dependency from **$d$ as a Linear Combination**:  
   - $d$ can be expressed as:

     $$
     d = c - a
     $$

   - Adding this new relationship introduces an additional term with a **new degree of freedom** $\beta$:

     $$
     e = \beta(-a + c + d) + ...
     $$

---

### Too Many Relationships?
1. **Average Relationship Dependency**  
   $c$ can also be written as the average of $d$ and $b$:

   $$
   c = \frac{b + d}{2}
   $$

   - Rearranging introduces:

     $$
     \frac{1}{2}b - c + \frac{1}{2}d = 0
     $$

   - However, **this relationship is not independent** of the previously captured dependencies.

2. **Why Stop at Two Terms?**  
   Adding the average relationship leads to **redundancy**:
   - You can deduce the average relationship (e.g., $c = \frac{b + d}{2}$) from the first two terms already.
   - **Including it unnecessarily complicates the expression without adding new information.**

---

### Uniqueness of Expression
- A "good" mathematical expression should:
  - **Uniquely capture all possible linear combinations** that produce $e$.  
  - Avoid multiple ways to represent the same combination.

#### Problem with Including Extra Terms:
- Consider $\alpha = 1$ and $\beta = 1$:
  $$
  e = 2a - b + 2c - d
  $$

- If we include the extra relationship (average dependency):
  - There are **infinitely many combinations** of $\alpha$, $\beta$, and new parameters yielding the **same result**, which defeats the goal of a unique representation.

---

### Future Discussion: Determining When to Stop
- **How many independent relationships** exist?
- **How to determine all independent pieces of information** among the vectors?
- This will prevent overcomplicating the decomposition while ensuring that all unique possibilities are included.

For now:  
- **Think about how to determine when you're done** (i.e., when no new independent relationships remain).  
- We'll revisit this question later with tools to formalize the process.

