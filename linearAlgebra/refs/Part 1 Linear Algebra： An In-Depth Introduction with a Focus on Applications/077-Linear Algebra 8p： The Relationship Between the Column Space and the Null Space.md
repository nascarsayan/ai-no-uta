## 1. Column Space and Null Space Relationship

### Introduction
- **Key Question**: What is the relationship between the column space and the null space of a matrix? Specifically, what is the dimension of the null space?
- This lesson pulls together many foundational linear algebra concepts (e.g., column space, null space, linear independence).
- Column space and null space seem to live in "different worlds":
  - **Column Space**: Vectors are as tall as the height of the matrix (subspace of $\mathbb{R}^m$, where $m$ is the number of rows).
  - **Null Space**: Vectors have as many entries as the number of columns in the matrix (subspace of $\mathbb{R}^n$, where $n$ is the number of columns).
- **Key Idea**: Despite their differences, the column space and null space are connected via a relationship between their dimensions.

---

## 2. Exploring the Relationship via Matrix Construction

We build a matrix column by column and observe how the column space and null space are affected.

### Step 1: Matrix with One Column
Matrix:

$$
\begin{bmatrix} 
1 \\ 
2 \\ 
0 \\ 
0 
\end{bmatrix}
$$

- **Column Space**:
  - Contains all scalar multiples of the vector: $a \begin{bmatrix} 1 \\ 2 \\ 0 \\ 0 \end{bmatrix}$.
  - Captured as: $\{a \begin{bmatrix} 1 \\ 2 \\ 0 \\ 0 \end{bmatrix} : a \in \mathbb{R}\}$ or equivalently $a [1 \; 2 \; 0 \; 0]^T$. 

- **Null Space**:
  - Only the zero vector: $\{ \mathbf{0} \}$, where $\mathbf{0} = [0 \; 0]^T$.

---

### Step 2: Adding the Second Column ($[3, 6, 0, 0]^T$)
Matrix:

$$
\begin{bmatrix} 
1 & 3 \\ 
2 & 6 \\ 
0 & 0 \\ 
0 & 0 
\end{bmatrix}
$$

- **Column Space**:
  - The new column is a multiple of the first column ($[3, 6, 0, 0]^T = 3 \times [1, 2, 0, 0]^T$).
  - Therefore, the column space remains unchanged.

- **Null Space**:
  - A new relationship emerges: the second column is a multiple of the first. Hence, the null space now includes nontrivial solutions:
    - $\{ c_1 \begin{bmatrix} -3 \\ 1 \end{bmatrix} : c_1 \in \mathbb{R} \}$
    
---

### Step 3: Adding the Zero Column
Matrix:

$$
\begin{bmatrix} 
1 & 3 & 0 \\ 
2 & 6 & 0 \\ 
0 & 0 & 0 \\ 
0 & 0 & 0 
\end{bmatrix}
$$

- **Column Space**:
  - Unchanged because the zero column cannot augment the column space.

- **Null Space**:
  - The zero column introduces a new relationship, adding this vector to the null space:
    - $\{c_1 \begin{bmatrix} -3 \\ 1 \end{bmatrix} + c_2 \begin{bmatrix} 0 \\ 1 \end{bmatrix} : c_1, c_2 \in \mathbb{R}\}$.

---

### Step 4: Adding Another Independent Column ($[0, 0, 1, 0]^T$)
Matrix:

$$
\begin{bmatrix} 
1 & 3 & 0 & 0 \\ 
2 & 6 & 0 & 0 \\ 
0 & 0 & 0 & 1 \\ 
0 & 0 & 0 & 0 
\end{bmatrix}
$$

- **Column Space**:
  - The new column is linearly independent. It augments the column space, which now spans:
    - $\{ a \begin{bmatrix} 1 \\ 2 \\ 0 \\ 0 \end{bmatrix} + b \begin{bmatrix} 0 \\ 0 \\ 1 \\ 0 \end{bmatrix} : a, b \in \mathbb{R} \}$.

- **Null Space**:
  - Unchanged from Step 3.

---

### Step 5: Adding a Dependent Column ($[10, 20, 0, 37]^T$)
Matrix:

$$
\begin{bmatrix} 
1 & 3 & 0 & 0 & 10 \\ 
2 & 6 & 0 & 0 & 20 \\ 
0 & 0 & 0 & 1 & 0 \\ 
0 & 0 & 0 & 0 & 37 
\end{bmatrix}
$$

- **Column Space**:
  - Unchanged because the fifth column is a linear combination of previous columns:
    - $[10, 20, 0, 37]^T = 10 \times [1, 2, 0, 0]^T + 37 \times [0, 0, 1, 0]^T$. 

- **Null Space**:
  - Grows in dimension. A new vector is added based on the dependency relationship between the columns:
    - $\{c_1 \begin{bmatrix} -3 \\ 1 \end{bmatrix} + c_2 \begin{bmatrix} 0 \\ 1 \end{bmatrix} + c_3 \begin{bmatrix} 10 & \dots & -1 \end{bmatrix} : c_1, c_2, c_3 \in \mathbb{R}\}$.

---

## 3. Final Conclusion: Dimensions Relationship
We observe the following dynamic:
- Adding a column to a matrix:
  - **If the column is linearly independent**: It augments the dimension of the **column space**.
  - **If the column is linearly dependent**: It augments the dimension of the **null space**.

### Key Result
The sum of the dimensions of the column space and null space equals the number of columns in the matrix:

$$
\text{dim(Column Space)} + \text{dim(Null Space)} = \text{Number of Columns}
$$

This is often called the **Rank-Nullity Theorem**, where:
- The dimension of the column space is the **rank** of the matrix.
- The dimension of the null space is the **nullity** of the matrix.

### Insight
This relationship provides a powerful and simple tool for understanding the structure of a matrix and its associated spaces. It implies that the structural "freedom" captured in the matrix is distributed between its row space and null space.