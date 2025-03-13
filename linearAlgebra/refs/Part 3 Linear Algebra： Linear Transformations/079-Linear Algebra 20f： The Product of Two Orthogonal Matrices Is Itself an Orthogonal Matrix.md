## The Product of Two Orthogonal Matrices

### Key Idea:
The product of two orthogonal matrices is itself an orthogonal matrix. 

Let us explore why this is true.

---

**Defining Orthogonal Matrices:**
- Consider two orthogonal matrices $Q_1$ and $Q_2$.
- By definition, a matrix $Q$ is orthogonal if:
  $$
  Q^{-1} = Q^\top
  $$

---

### Steps to Prove Orthogonality of the Product $Q = Q_1 Q_2$

1. **Finding the Inverse of $Q$:**
   - Recall the property of matrix inverses:
     $$
     (AB)^{-1} = B^{-1} A^{-1}
     $$
   - Applying this to the product $Q = Q_1 Q_2$, we have:
     $$
     Q^{-1} = Q_2^{-1} Q_1^{-1}
     $$

2. **Using Orthogonality of $Q_1$ and $Q_2$:**
   - Since $Q_1$ and $Q_2$ are orthogonal, their inverses are equal to their transposes:
     $$
     Q_1^{-1} = Q_1^\top \quad \text{and} \quad Q_2^{-1} = Q_2^\top
     $$
   - Substituting these into the inverse of $Q$, we obtain:
     $$
     Q^{-1} = Q_2^\top Q_1^\top
     $$

3. **Rewriting Using Transpose Properties:**
   - Recall that the transpose of a product is the product of the transposes in reverse order:
     $$
     (AB)^\top = B^\top A^\top
     $$
   - Applying this to $Q = Q_1 Q_2$, we find:
     $$
     Q^\top = (Q_1 Q_2)^\top = Q_2^\top Q_1^\top
     $$

4. **Conclusion:**
   - From the expressions for $Q^{-1}$ and $Q^\top$, we see that:
     $$
     Q^{-1} = Q^\top
     $$
   - Hence, $Q$ is orthogonal.

---

### Final Result:
The product of two orthogonal matrices $Q_1$ and $Q_2$ is itself an orthogonal matrix:
$$
Q = Q_1 Q_2 \quad \implies \quad Q^{-1} = Q^\top
$$

This completes the proof that the product of two orthogonal matrices is orthogonal, as stated.