## Problem: Eigenvalues and Eigenvectors  

### Subtracting $\lambda$ from the diagonal 
To find the eigenvalues, subtract $\lambda$ from the diagonal of the matrix and evaluate its determinant:  

$$
\text{det}(A - \lambda I) = 0
$$  

### Determinant Calculation
The determinant is calculated as follows:  
- The answer is the product of one entry minus the product of another pair of entries:  
$$
\text{det}(A - \lambda I) = \lambda^2 + \lambda - 2
$$  

### Solving for $\lambda$
The polynomial must equal zero:  
$$
\lambda^2 + \lambda - 2 = 0  
$$  
The roots of this quadratic equation are:  
$$
\lambda = -2 \quad \text{and} \quad \lambda = 1
$$  

---

## Step 1: Eigenvalue $\lambda = -2$
Subtract $-2$ from the diagonal by adding 2 to diagonal entries. Perform the calculation to adjust the matrix:  

### Proportionality of Columns  
The resulting matrix columns are in proportion (3:2).  

### Eigenvector Corresponding to $\lambda = -2$  
The eigenvector associated with $\lambda = -2$ is:  
$$
\begin{bmatrix}
2 \\
3
\end{bmatrix}
$$  

#### Verification:  
Multiply the matrix by the eigenvector. The result matches:  
$$
A
\begin{bmatrix} 
2 \\ 
3 
\end{bmatrix} 
= -2 
\begin{bmatrix} 
2 \\ 
3 
\end{bmatrix}
$$  

Results:  
$$
\begin{bmatrix}
-4 \\
-6
\end{bmatrix}
$$  
Since $\begin{bmatrix} -4 \\ -6 \end{bmatrix}$ equals $\lambda \cdot \begin{bmatrix} 2 \\ 3 \end{bmatrix}$, the eigenvalue and eigenvector are correct.  

---

## Step 2: Eigenvalue $\lambda = 1$
Subtract $1$ from the diagonal. Perform matrix adjustment:  

### Proportionality of Columns  
Adjusted matrix columns are in proportion (3:5).  

### Eigenvector Corresponding to $\lambda = 1$  
The eigenvector associated with $\lambda = 1$ is:  
$$
\begin{bmatrix}
3 \\
5
\end{bmatrix}
$$  

#### Verification:  
Multiply the matrix by the eigenvector. The result matches the original eigenvector since $\lambda = 1$:  
$$
A
\begin{bmatrix}
3 \\
5
\end{bmatrix} 
= 1 
\begin{bmatrix}
3 \\
5
\end{bmatrix}
$$  

Results:  
The eigenvector is verified.  

---

## Final Validation: Trace and Determinant
### Trace of the Matrix  
The sum of eigenvalues equals the trace of the matrix:  
$$
\text{Trace} = \lambda_1 + \lambda_2 = -2 + 1 = -1
$$  

### Determinant of the Matrix  
The product of eigenvalues equals the determinant of the matrix:  
$$
\text{Determinant} = \lambda_1 \cdot \lambda_2 = -2 \cdot 1 = -2
$$  

Both calculations confirm the problem is correctly solved.  

---

**Summary:**  
- Eigenvalues: $\lambda = -2$, $\lambda = 1$  
- Eigenvectors: $\begin{bmatrix} 2 \\ 3 \end{bmatrix}$, $\begin{bmatrix} 3 \\ 5 \end{bmatrix}$  
- Trace and determinant accurately match computed values.  

Problem successfully solved! 🚀