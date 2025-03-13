# Linear Dependence and Linear Combinations

## 1. Recap from Previous Video:
- The vector **D** can be expressed as a linear combination of **A**, **B**, and **C** in infinitely many ways.
- This introduced the **first definition** of linear dependence.

---

## 2. Goal:
- To represent **all linear combinations** of **A**, **B**, and **C** that yield **D** using a **single mathematical expression**.

---

## 3. Key Idea: Substituting Relationships
- In the previous video:
    - **C** was expressed as:  
      $C = A + B$  
    - Using this, substitutions like "remove 1 unit of A and 1 unit of B, and replace them with 1 unit of C" could keep the expression for **D** unchanged.

### Generalization using a Parameter ($\alpha$):
- Take any value $\alpha$ to adjust contributions of **A**, **B**, and **C**:
    $$
    (2 + \alpha)A + (1 + \alpha)B - \alpha C = D
    $$

---

## 4. Rewriting for Insight:
- Group terms involving $\alpha$:
    $$
    D = 2A + B + \alpha(A + B - C)
    $$
- **Key Takeaway**:  
  The term $(A + B - C)$ represents the adjustment and can be scaled by $\alpha$, without changing the value of **D**.

---

## 5. Why Does This Work?  
- **Linear Dependence**:  
  The key property making this possible is that **C** can be written as a linear combination of **A** and **B**:  
  $C = A + B$  

- **Degree of Freedom**:  
  The parameter $\alpha$ allows us to generate infinitely many valid linear combinations of **A**, **B**, and **C** that yield the same vector **D**.

    - Example Linear Combination for $\alpha = 0$:  
      $2A + B = D$  
    - Example Linear Combination for $\alpha = 1$:  
      $3A + 2B - C = D$  

---

## 6. The "Fancy Zero":
- The term $(A + B - C)$ evaluates to the **zero vector**, as:
    $$
    A + B - C = 0
    $$

- Adding scalars of this **"fancy zero"**:
    - Does **not** change the value of the combination.  
    - But changes the **appearance** of the linear combination, creating infinitely many representations.

    **Conclusion**: Adding a "fancy zero" enables capturing all `infinitely possible combinations` while maintaining the result.  

---

## 7. Alternative Definition of Linear Dependence:
- A set of vectors (**A**, **B**, and **C**) is **linearly dependent** if there exists a **nontrivial** linear combination that equals the zero vector:
    $$
    \alpha_1 A + \alpha_2 B + \alpha_3 C = 0
    $$

- **Important Notes**:
   - "Nontrivial" means at least one of the coefficients $\alpha_1, \alpha_2, \alpha_3$ is not zero.
   - This definition captures the same linear dependence introduced earlier.

---

## 8. Implications of Linear Dependence:
- **Lack of Uniqueness**:  
  If vectors are linearly dependent, any decomposition of a vector like **D** (into **A**, **B**, and **C**) will have infinitely many solutions.

    - Example:  
      Adding/subtracting multiples of the "fancy zero" $(A + B - C)$ to any valid decomposition of **D** produces new solutions.

- **Why It Matters**:  
  This has critical implications when solving linear systems, as it highlights the need to account for all possible solutions.

---

### Summary:
- The existence of the zero vector in a linear combination is central to understanding linear dependence.
- Linear dependence introduces freedom to modify linear combinations without changing the result, but it precludes uniqueness in decomposition.