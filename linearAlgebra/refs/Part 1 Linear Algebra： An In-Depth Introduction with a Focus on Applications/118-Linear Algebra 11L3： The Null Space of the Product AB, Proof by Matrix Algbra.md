## Null Space Inclusion via Matrix Algebra

### Key Concept:
In an earlier discussion, it was established that if $C$ is the product $AB$ ($C = AB$), the null space of $C$ contains the null space of $B$. This video offers a purely algebraic proof using matrix manipulation.

---

### Methodology

- **Step 1**: Multiply the matrix $C$ by the matrix representing the null space of $B$.
  
$$
C \cdot N_B
$$

This product is crucial because it provides a means to verify null space containment.

---

- **Step 2**: Substitute $C = AB$ into the expression:

$$
C \cdot N_B = AB \cdot N_B
$$

This substitution allows direct examination of the product using $A$ and $B$.

---

- **Step 3**: Recognize that $B \cdot N_B = 0$ by definition (the null space property of $B$):

$$
AB \cdot N_B = A \cdot (B \cdot N_B) = A \cdot 0
$$

Where $B \cdot N_B = 0$ produces the zero matrix as output.

---

### Result
Finally, the expression simplifies:

$$
A \cdot 0 = 0
$$

Thus, $C \cdot N_B = 0$, meaning every element of the null space of $B$ is also a part of the null space of $C$. The result is the purely algebraic confirmation that:

### Conclusion
The null space of $C$ includes the null space of $B$. Unlike previous geometric approaches, this proof relied entirely on matrix algebra, showcasing the elegance of symbol manipulation.