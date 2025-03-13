## Understanding $X^\top A Y$

### Definition:
We are considering the following combination:

$$
X^\top A Y
$$

where:
- $X$ and $Y$ are vectors in $\mathbb{R}^n$, represented as single column matrices.
- $A$ is a matrix.

This product is crucial, and we will encounter it frequently later in the course.

---

### Example 1: Numeric Calculation

#### Given:
Let 
$$
X = \begin{bmatrix} 1 \\ 2 \end{bmatrix}, \quad
A = \begin{bmatrix} 1 & 2 \\ 3 & 4 \end{bmatrix}, \quad
Y = \begin{bmatrix} 1 \\ 1 \end{bmatrix}.
$$

#### Step-by-Step Solution:
1. Compute $A Y$ (matrix-vector multiplication):
   $$
   A Y = \begin{bmatrix} 1 & 2 \\ 3 & 4 \end{bmatrix} \begin{bmatrix} 1 \\ 1 \end{bmatrix} =
   \begin{bmatrix} 1 \cdot 1 + 2 \cdot 1 \\ 3 \cdot 1 + 4 \cdot 1 \end{bmatrix} =
   \begin{bmatrix} 3 \\ 7 \end{bmatrix}.
   $$

2. Compute $X^\top (A Y)$:
   $$
   X^\top A Y = \begin{bmatrix} 1 & 2 \end{bmatrix} \begin{bmatrix} 3 \\ 7 \end{bmatrix} =
   1 \cdot 3 + 2 \cdot 7 = 3 + 14 = 17.
   $$

#### Result:
The result is a **single number**, $17$. While technically a $1 \times 1$ matrix, we often interpret it as just a number.

---

### Example 2: General Case with Symbols

Let $X$, $A$, and $Y$ be given as general matrices:
$$
X = \begin{bmatrix} x_1 \\ x_2 \end{bmatrix}, \quad
A = \begin{bmatrix} a_{11} & a_{12} \\ a_{21} & a_{22} \end{bmatrix}, \quad
Y = \begin{bmatrix} y_1 \\ y_2 \end{bmatrix}.
$$

#### Step-by-Step Solution:
1. Compute $A Y$:
   $$
   A Y = \begin{bmatrix} a_{11} & a_{12} \\ a_{21} & a_{22} \end{bmatrix} 
         \begin{bmatrix} y_1 \\ y_2 \end{bmatrix} =
         \begin{bmatrix} a_{11}y_1 + a_{12}y_2 \\ a_{21}y_1 + a_{22}y_2 \end{bmatrix}.
   $$

2. Compute $X^\top (A Y)$:
   $$
   X^\top A Y = \begin{bmatrix} x_1 & x_2 \end{bmatrix} 
                \begin{bmatrix} a_{11}y_1 + a_{12}y_2 \\ a_{21}y_1 + a_{22}y_2 \end{bmatrix}.
   $$
   Expanding:
   $$
   X^\top A Y = x_1(a_{11}y_1 + a_{12}y_2) + x_2(a_{21}y_1 + a_{22}y_2).
   $$

3. Organizing terms:
   $$
   X^\top A Y = a_{11}x_1y_1 + a_{12}x_1y_2 + a_{21}x_2y_1 + a_{22}x_2y_2.
   $$

#### Interpretation:
The result is a **sum of terms**, where:
- Each term corresponds to an entry in the matrix $A$.
- Each term involves one component from $X$ and one from $Y$.

---

### General Structure and Insight:

#### Observations:
1. For any $m \times n$ matrix $A$, the result of $X^\top A Y$ is:
   - A **single scalar value** (technically a $1 \times 1$ matrix).
   - The scalar is the **sum of as many terms as there are entries in $A$**.
2. Each term in the sum is of the form $a_{ij} x_i y_j$, where:
   - $a_{ij}$ is the $(i, j)$ entry of $A$.
   - $x_i$ is the $i$th component of $X$.
   - $y_j$ is the $j$th component of $Y$.

#### Summary:
The result of $X^\top A Y$ is computed as:
$$
X^\top A Y = \sum_{i=1}^m \sum_{j=1}^n a_{ij} x_i y_j.
$$

#### Practical Notes:
- The **row index $i$** of $A$ corresponds to the $x_i$ entry from $X$.
- The **column index $j$** of $A$ corresponds to the $y_j$ entry from $Y$.

---

### Key Takeaway:
This combination $X^\top A Y$ will appear frequently in applications, and its structured interpretation is essential to understanding matrix-vector relationships in linear algebra and beyond.