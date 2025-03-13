## Example: Rank of a Matrix and Linear Dependence

### Concept Overview
This example explores the *rank of a matrix* and its connection to the linear dependence of its columns and rows.

### Problem Statement
Are the columns of the following matrix linearly dependent?

### Key Insight
Linear dependence can be determined via the rank:
- If the rank is less than the number of columns, the columns are linearly dependent.
  
Additionally:
- The relationship between the rows can also sometimes be used to infer column dependency, as we'll see below.

---

### Matrix Analysis

Consider the matrix below:

$$
\begin{bmatrix}
a_{11} & a_{12} & a_{13} \\
a_{21} & a_{22} & a_{23} \\
a_{31} & a_{32} & a_{33} \\
\end{bmatrix}
$$

#### Row Dependency
The rows are linearly dependent because:

$$
10 \cdot \text{row}_1 + \text{row}_2 = \text{row}_3
$$

This implies that any row can be expressed as a combination of others.

#### Column Dependency
Since the rows are linearly dependent, the rank of the row space is:

$$
\text{Rank of row space} = 2
$$

In linear algebra, the rank of the column space matches the rank of the row space. Thus:

$$
\text{Rank of column space} = 2
$$

Given that there are *3 columns* in the matrix, while the rank (dimension of the column space) is *2*, **the columns must be linearly dependent**.

---

### Linear Combination
The dependency among columns means there exists a non-trivial linear combination of the columns that equals zero. Specifically, if:

$$
c_1 \textbf{v}_1 + c_2 \textbf{v}_2 + c_3 \textbf{v}_3 = 0
$$

Where \( \textbf{v}_i \) are column vectors, at least one \( c_i \neq 0 \).

Important:
- The coefficients of the relationship can be determined using methods like Gaussian elimination, but their mere existence is implied by the rank analysis.

---

### Final Remarks
This example highlights the **power** of linear algebra:
- By understanding the rank, we can make insights about the relationships within a matrix without performing time-consuming row reduction steps (e.g., Gaussian elimination).

#### Key Takeaways:
- **Rank** provides an instant insight into linear dependence.
- **Row dependence** implies column dependence (and vice-versa).
- Linear algebra enables concise and powerful arguments about matrix structure.

