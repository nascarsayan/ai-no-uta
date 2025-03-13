## Determinants of $2 \times 2$ Matrices

### 1. Formula for Determinants
In an earlier video, we derived the determinant formula for a $2 \times 2$ matrix of the form:

$$
\begin{bmatrix}
a & b \\
c & d 
\end{bmatrix}
$$

The determinant is calculated as:

$$
\text{det} = ad - bc
$$

This is often referred to as the "criss-cross" pattern.

---

### 2. Example 1: Simple Matrix

Given the matrix:

$$
\begin{bmatrix}
2 & 1 \\
3 & 4
\end{bmatrix},
$$

the determinant is:

$$
\text{det} = (2)(4) - (1)(3) = 8 - 3 = 5
$$

- Since $\text{det} \neq 0$, the **columns are linearly independent**.
- The determinant confirms what we already know.

---

### 3. Example 2: Proportional Columns

Given the matrix:

$$
\begin{bmatrix}
5 & -15 \\
12 & -36
\end{bmatrix},
$$

the determinant is:

$$
\text{det} = (5)(-36) - (-15)(12) = -180 + 180 = 0
$$

- Since $\text{det} = 0$, the **columns are linearly dependent**.
- Upon closer inspection:
  - The second column is $-3$ times the first column:
    $$ -3 \cdot \begin{bmatrix} 5 \\ 12 \end{bmatrix} = \begin{bmatrix} -15 \\ -36 \end{bmatrix} $$
  - Determinants help us identify such relationships.

---

### 4. Example 3: Unexpected Dependence

Given the matrix:

$$
\begin{bmatrix}
3 & 3\sqrt{2} \\
1 & \sqrt{2}
\end{bmatrix},
$$

the determinant is:

$$
\text{det} = (3)(\sqrt{2}) - (3\sqrt{2})(1) = 3\sqrt{2} - 3\sqrt{2} = 0
$$

- At first glance, the columns do not appear proportional, but the determinant confirms they are **linearly dependent**.
- Further inspection reveals the relationship:
  - The second column is $\sqrt{2}$ times the first column:
    $$ \sqrt{2} \cdot \begin{bmatrix} 3 \\ 1 \end{bmatrix} = \begin{bmatrix} 3\sqrt{2} \\ \sqrt{2} \end{bmatrix} $$

---

### 5. Example 4: The Trigonometric Matrix

Consider a matrix with trigonometric entries:

$$
\begin{bmatrix}
\cos(\alpha) & -\sin(\alpha) \\
\sin(\alpha) & \cos(\alpha)
\end{bmatrix}.
$$

The determinant is:

$$
\text{det} = \cos^2(\alpha) + \sin^2(\alpha)
$$

Using the Pythagorean identity:

$$
\cos^2(\alpha) + \sin^2(\alpha) = 1
$$

Thus, $\text{det} = 1$ for all values of $\alpha$, which tells us:

- The columns are always **linearly independent**, regardless of the value of $\alpha$.
- This is interesting because intuition would not easily reveal this result.

---

### 6. Insights from Determinants

- Determinants help us answer important questions like whether the columns of a matrix are linearly independent or dependent. 
- Even simple $2 \times 2$ matrices can offer non-obvious insights into such relationships.
- Determinants also show the importance of mathematical tools when visual intuition fails us.