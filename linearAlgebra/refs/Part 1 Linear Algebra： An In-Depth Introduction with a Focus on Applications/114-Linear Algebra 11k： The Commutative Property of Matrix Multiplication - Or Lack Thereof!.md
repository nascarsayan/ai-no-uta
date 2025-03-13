## Commutativity in Matrix Multiplication

### Comparing Commutativity and Associativity
- The **associative property** of matrix multiplication deals with the *order of operations*, i.e., how the grouping of terms changes.
- The **commutative property**, on the other hand, deals with the *order of the multiplicative terms themselves*.

#### Associativity Example:
Given matrices $A$, $B$, and $C$:
- Left-hand side: $(AB)C$
- Right-hand side: $A(BC)$
- In both cases, the order of terms is the same ($A$, $B$, $C$), but the grouping of operations differs.

#### Commutativity Example:
If commutativity held:
$$
AB = BA
$$
However, **this is not true for matrices.**

---

### Key Observation: Commutativity Fails for Matrices
1. Unlike multiplication of real numbers (e.g., $14 \times 25 = 25 \times 14$), the **product of matrices is not commutative**.
2. Switching the order of matrix multiplication leads to fundamentally different results.

#### Example of Non-Commutativity
Given two matrices:
$$
A = \begin{bmatrix} 1 & 4 \\ 4 & 7 \end{bmatrix}, \, B = \begin{bmatrix} 2 & 5 \\ 8 & 1 \end{bmatrix}
$$
If we compute $AB$ versus $BA$:
- **Resulting matrices will differ**.

#### Key Insights:
- Matrix multiplication is dependent on actions. 
- When a matrix acts on another (via multiplication), it modifies it in a particular way.

---

### Actions and Lack of Commutativity
- View **matrix multiplication as an operation or action**:
  - When $A$ acts on $B$ as $AB$, the action could be interpreted as, for example, switching columns.
  - Conversely, $BA$ would represent $B$ acting on $A$ and might switch rows instead.
- The lack of commutativity reflects real-world actions:
  - If you take a step forward and then turn left, the result is different from turning left first and then stepping forward.

---

### Illustrative Examples of Actions (Real Life)
1. **"Shoot first, ask questions later" vs. "Ask questions first, shoot later"**
   - The order in which actions are performed matters!

2. **Movement Example**:
   - Action 1: Step forward.
   - Action 2: Turn left.
   - Result is different if the actions are performed in the reverse order.

---

### The Structure Behind Lack of Commutativity
While commutativity fails, there is a **predictable structure** to what happens:
1. When one matrix is on the right, it might act by switching columns.
2. When it appears on the left, it might act by switching rows.

---

### Final Thoughts
- Commutativity does not hold for matrix multiplication; this is a **crucial difference** from the multiplication of real numbers.
- The lack of commutativity might initially appear as a complication, but **it actually reflects natural actions in the real world**, where order matters.