## 3. Matrix with No Real Eigenvalues

### Problem Statement

The objective of this problem is to provide an example of a **matrix with no real eigenvalues**.

### Process

1. **Subtract $\lambda$ from the diagonal:**
   - Begin by forming the matrix $A - \lambda I$, which involves subtracting $\lambda$ from the diagonal entries of the matrix.

2. **Evaluate the determinant:**
   - Compute the determinant of $A - \lambda I$, which results in a characteristic equation (a quadratic equation in $\lambda$).

3. **Solve the quadratic equation:**
   - Attempt to solve the quadratic equation to find the eigenvalues.

4. **Discriminant Analysis:**
   - For a quadratic equation of the form $ax^2 + bx + c = 0$, the discriminant $\Delta$ is given by:
     $$
     \Delta = b^2 - 4ac
     $$
   - If $\Delta > 0$, the equation has two distinct real roots.
   - If $\Delta = 0$, the equation has exactly one real root (a repeated root).
   - If $\Delta < 0$, the equation has no real roots and only complex roots exist.

### Example Calculation

- Assume the quadratic equation derived from the determinant is of the form:
  $$
  \lambda^2 + 7\lambda + 22 = 0
  $$
- Calculate the discriminant:
  $$
  \Delta = 7^2 - 4(1)(22) = 49 - 88 = -39
  $$
- Since $\Delta < 0$, the discriminant is negative. Thus, the quadratic equation **does not have any real solutions**.

### Conclusion

- Since the quadratic equation has no real solutions, the matrix **does not have any real eigenvalues**.
- The matrix does, however, have **complex eigenvalues**. Further exploration of complex eigenvalues will be addressed later in the context of linear algebra with complex numbers.

### Notes

- Eigenvalues can be real or complex, depending on the discriminant of the characteristic equation.
- For now, we focus only on real values and defer studying complex eigenvalues to a later discussion.