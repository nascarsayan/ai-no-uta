## Inner Products for Polynomials

### Polynomial Example of an Inner Product
To explore inner products in the context of polynomials, consider the following example:

- Let $P$ and $Q$ be polynomials. Define their "dot product" as:
  $$
  P \cdot Q = P(0) \times Q(0)
  $$

  - **Observation**: This dot product evaluates at a specific point, $x = 0$, for simplicity.

---

### Key Properties of an Inner Product
To qualify as a **valid inner product**, a function must satisfy the following properties:

1. **Commutativity**  
   $P \cdot Q = Q \cdot P$  
   - This property holds naturally in the given example.

2. **Distributive Property**  
   $(P + Q) \cdot R = P \cdot R + Q \cdot R$  
   - This can be verified by directly computing both sides.

3. **Positive Definiteness**  
   $P \cdot P > 0 \quad \text{if } P \neq 0$  
   - However, in this case, **positive definiteness fails**. For example:
     - If $P(x) = x$, then $P(0) \cdot P(0) = 0 \times 0 = 0$, which violates the strict positivity condition.

---

### Counterexample to Positive Definiteness
Consider a specific polynomial example:
- Let $P(x) = x$
  $$
  P(0) = 0 \quad \implies \quad P \cdot P = P(0) \cdot P(0) = 0
  $$
  - Since $P(x) \neq 0$ but $P \cdot P = 0$, positive definiteness is violated.

---

### General Observations
1. **Quadratic Polynomial Space**  
   - When restricted to quadratic polynomials (degree $\leq 2$), definitions like the above may sometimes act as valid inner products within specific subspaces.  
   - For example, extending this dot product naively to cubic polynomials would allow $P(x)$ to intersect three zeros **and fail positive definiteness**.

2. **Wider Polynomial Space**  
   - In the generalized space of all polynomials, it becomes impossible to "fix" the failure of positive definiteness when using point evaluations like $P(0)$.

---

### Connection Between Discrete Summation and Integrals
The failure of evaluating a polynomial "dot product" at only one point can be connected to integrals:

- Intuitively, summing polynomial products $P(x) \cdot Q(x)$ at **infinitely many points** approaches the behavior of an **integral**. For example:
  $$
  \int_{a}^{b} P(x) Q(x) \, dx
  $$
  satisfies positive definiteness (under suitable conditions).

---

### Insights into the Integral as an Inner Product
- **Integral Definition**  
  The integral acts like an inner product because it sums products $P(x) Q(x)$ over a continuous interval.  
  - Example:
    $$
    \int_{0}^{2} P(x) Q(x) \, dx
    $$
    restores positive definiteness when $P(x)$ and $Q(x)$ are reasonably continuous functions.
  
---

### Summary
- Point evaluations like $P(0) \cdot Q(0)$ fail as a general definition of an inner product because they lack positive definiteness in the broader polynomial space.
- Integrals, which generalize the summation concept over a continuous domain, naturally satisfy the inner product properties (especially positive definiteness for suitable spaces).