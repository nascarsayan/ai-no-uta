## 1. Linear Transformation with Respect to Standard Basis in $\mathbb{R}^3$

### Overview:
- This section discusses applying a linear transformation to vectors defined in the standard basis of $\mathbb{R}^3$.
- The goal is to compute the transformation and represent it in matrix form, following standard basis rules.

---

### Familiar Algorithm:
- Vectors involved: $S_1$, $S_2$, $S_3$
- Process:
  1. Apply the linear transformation $T$ to each vector ($S_1$, $S_2$, $S_3$).
  2. Decompose the resulting vectors into the standard basis components.
  3. Place corresponding components of transformed vectors as columns in the resulting matrix.

---

### Linear Transformation Rule:
Given a vector in $\mathbb{R}^3$:
- The new components are derived as:
  - **First entry**: Sum of the first two entries of the original vector.
  - **Second entry**: Difference of the first two entries of the original vector.
  - **Third entry**: The last entry of the original vector multiplied by 3.

---

### Applying $T$ to $S_1$:
- Let $S_1 = \begin{bmatrix} 1 \\ 1 \\ 0 \end{bmatrix}$.
- Applying $T$:
  - First component: $1 + 1 = 2$
  - Second component: $1 - 1 = 0$
  - Third component: $0 \times 3 = 0$
- Result: 
  $$
  T(S_1) = \begin{bmatrix} 2 \\ 0 \\ 0 \end{bmatrix}
  $$

- Decomposing $T(S_1)$ in terms of the standard basis:
  - Components are exactly the entries of the resulting vector because it's standard basis:
  - First column: $\begin{bmatrix} 2 \\ 0 \\ 0 \end{bmatrix}$

---

### Applying $T$ to $S_2$:
- Let $S_2 = \begin{bmatrix} 1 \\ -1 \\ 0 \end{bmatrix}$.
- Applying $T$:
  - First component: $1 + (-1) = 0$
  - Second component: $1 - (-1) = 2$
  - Third component: $0 \times 3 = 0$
- Result:
  $$
  T(S_2) = \begin{bmatrix} 0 \\ 2 \\ 0 \end{bmatrix}
  $$

- Decomposing $T(S_2)$ in terms of the standard basis:
  - Second column: $\begin{bmatrix} 0 \\ 2 \\ 0 \end{bmatrix}$

---

### Applying $T$ to $S_3$:
- Let $S_3 = \begin{bmatrix} 0 \\ 0 \\ 1 \end{bmatrix}$.
- Applying $T$:
  - First component: $0 + 0 = 0$
  - Second component: $0 - 0 = 0$
  - Third component: $1 \times 3 = 3$
- Result:
  $$
  T(S_3) = \begin{bmatrix} 0 \\ 0 \\ 3 \end{bmatrix}
  $$

- Decomposing $T(S_3)$ in terms of the standard basis:
  - Third column: $\begin{bmatrix} 0 \\ 0 \\ 3 \end{bmatrix}$

---

### Resulting Matrix:
By using the transformed components of $S_1$, $S_2$, and $S_3$:
$$
\text{Resulting Matrix} = 
\begin{bmatrix} 
2 & 0 & 0 \\ 
0 & 2 & 0 \\ 
0 & 0 & 3 
\end{bmatrix}
$$

---

### Observations:
- The resulting matrix is identical to the matrix defining the transformation itself, a unique property of the **standard basis**.
- In other bases, the resulting matrix can differ from the original transformation matrix.

---

### Special Features of Standard Basis:
- The basis ensures direct mapping of vectors' entries as components of the matrix.
- For linear transformations in the standard basis, the transformation matrix often reappears as the representation matrix.

---

### Next Steps:
- Explore even more special bases and their properties. This will lead to interesting discussions and insights into transformations.