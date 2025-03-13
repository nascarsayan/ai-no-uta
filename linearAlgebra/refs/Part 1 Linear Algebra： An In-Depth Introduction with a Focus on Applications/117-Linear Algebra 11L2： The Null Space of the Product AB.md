## Null Spaces in Matrix Multiplication

### Problem Context

Given that matrix $C$ is the product of matrices $A$ and $B$, the key question is:

> How is the null space of $C$ related to the null spaces of $A$ and $B$?

To investigate this, consider a matrix product where:
- $A$ is a matrix,
- $B$ is a matrix, and
- $C = AB$.

### Observations

#### Key Insight:
The null space of $C$ is:
- **Related to the null space of $B$.**
- **Unrelated to the null space of $A$.**

#### Dimensions Analysis:
- $B$ has the same number of columns as $C$.
- The null spaces of both $B$ and $C$ inhabit the same space, $R^n$.

#### Relation Between Null Spaces:
- Any linear relationships present among the columns of $B$ will also exist among the columns of $C$.
- Specifically:
    - If the $j$-th column of $B$ is a linear combination of other columns in $B$, then the $j$-th column of $C$ will also exhibit the same linear combination property.

---

### Column-Wise Perspective 

When viewing matrix multiplication column-wise:
- **Columns of $B$:** Represent coefficients for linear combinations of the columns of $A$.
- **Columns of $C$:** Result from applying the same coefficient patterns (from $B$) to linear combinations of columns of $A$.

#### Example:
- If the third column of $B$ is the sum of the first two columns, i.e:
  $$
  b^3 = b^1 + b^2
  $$
  then the third column of $C$ must also satisfy:
  $$
  c^3 = c^1 + c^2
  $$

This property generalizes to all linear relationships among the columns of $B$.

---

### Null Space Containment

#### Observations:
- The null space of $B$ is always a **subspace** of the null space of $C$.
- If $v \in \text{null}(B)$, then $v \in \text{null}(C)$.

#### Cases:
1. **Equal Null Spaces:**  
   If the null spaces of $B$ and $C$ coincide, then:  
   $$
   \text{null}(B) = \text{null}(C)
   $$

2. **Proper Subspace:**  
   The null space of $B$ can be a proper subspace of the null space of $C$.

---

### Extreme Example: Zero Matrix
If $A = 0$, then:
- $C = AB = 0$, and
- $\text{null}(C)$ becomes all of $R^n$.  
In this case, $\text{null}(B) \subseteq \text{null}(C)$ and $\text{null}(C)$ is much larger.

Thus, generally:
- $\text{null}(B) \subseteq \text{null}(C)$,
- Equality may hold in some cases, but in others, $\text{null}(C)$ can be larger.

---

### Conclusion

The null space of $B$:
1. Is always a **subspace** of the null space of $C$.
2. Can be:
   - Equal to $\text{null}(C)$ in some cases (e.g., specific properties of $A$ and $B$).
   - A proper subspace of $\text{null}(C)$ in other situations (e.g., $A$ contributes additional nullity).