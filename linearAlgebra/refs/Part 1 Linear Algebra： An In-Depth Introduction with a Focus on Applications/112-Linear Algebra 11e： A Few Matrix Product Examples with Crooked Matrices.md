## Matrix Multiplication Examples

### 1. Example with a $5 \times 2$ Matrix and $2 \times 1$ Matrix  

#### Dimensions Compatibility:

- A $5 \times 2$ matrix is multiplied by a $2 \times 1$ matrix.  
- The inner dimensions (columns of the first matrix and rows of the second) match, so the product is valid.  
- The resulting matrix will have dimensions $5 \times 1$.  

#### Calculating Entries:

- Compute each entry by taking linear combinations of the columns:  
  $$
  \begin{aligned}
  \text{Entry 1} &= 3 \times 1 + 1 \times 3 = 6, \\
  \text{Entry 2} &= 3 \times 3 - 1 \times 1 = 8, \\
  \text{Entry 3} &= 21 - 2 = 19, \\
  \text{Entry 4} &= 12 - 1 = 11, \\
  \text{Entry 5} &= 3 + 4 = 7.  
  \end{aligned}
  $$

#### Resulting Matrix:

$$
\begin{bmatrix} 
6 \\ 
8 \\ 
19 \\ 
11 \\ 
7 
\end{bmatrix}
$$  

---

### 2. Example with a $3 \times 1$ Matrix and $1 \times 1$ Matrix  

#### Dimensions Compatibility:

- A $3 \times 1$ matrix is multiplied by a $1 \times 1$ matrix.  
- The inner dimension matches, so the product is valid.  
- The resulting matrix will have dimensions $3 \times 1$.  

#### Calculating Entries:

- Multiply each entry of the first matrix by the single value in the second matrix (say $4$):  
  $$
  4 \times  
  \begin{bmatrix} 
  1 \\ 
  2 \\ 
  3 
  \end{bmatrix} =  
  \begin{bmatrix} 
  4 \\ 
  8 \\ 
  12 
  \end{bmatrix}
  $$  

---

### 3. Example with a $1 \times 4$ Matrix and $4 \times 1$ Matrix  

#### Dimensions Compatibility:

- A $1 \times 4$ matrix is multiplied by a $4 \times 1$ matrix.  
- The inner dimensions match (columns of the first, rows of the second), so the product is valid.  
- The resulting matrix will have dimensions $1 \times 1$ (just a scalar).  

#### Calculating the Result:

- Perform the dot product of the two matrices:  
  $$
  \begin{bmatrix} 1 & 2 & 3 & 4 \end{bmatrix} \times  
  \begin{bmatrix} 4 \\ 6 \\ 6 \\ 4 \end{bmatrix} = 1 \times 4 + 2 \times 6 + 3 \times 6 + 4 \times 4 = 20
  $$  

#### Resulting Matrix:

$$
\begin{bmatrix} 20 \end{bmatrix}
$$  

---

### Key Insights:

1. Matrix multiplication requires inner dimensions to match.  
   - If matrix $A$ is $m \times n$, and matrix $B$ is $n \times p$, the resulting matrix will be $m \times p$.  

2. Entries are computed using linear combinations of columns (or rows).  

3. The dimensions of the output can be determined without full computation, by observing the "outer dimensions."  

4. Crooked matrices (non-square matrices) are simply less uniform but follow the same rules.  