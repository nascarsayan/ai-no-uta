## Transpose of a Product  

This lesson explores how the **transpose of a product** relates to the transposes of individual matrices, using matrix multiplication and examples.  

### Key Idea  

The transpose of a product works similarly to the inverse:  
- The **transpose of a product** is **equal to the product of individual transposes in the opposite order**, as will be shown mathematically below.  

---

### Multiplication Example  

Start with two compatible matrices:  

Matrix $A$ is $2 \times 3$:  
$$
A = \begin{bmatrix} 
1 & 2 & 3 \\ 
4 & 5 & 6 
\end{bmatrix}
$$  

Matrix $B$ is $3 \times 4$:  
$$
B = \begin{bmatrix} 
1 & 0 & 1 & -1 \\ 
0 & 1 & 0 & 1 \\ 
1 & 0 & 0 & 1 
\end{bmatrix}
$$  

**Matrix Product, $AB$:**

Multiply $A$ and $B$. The resulting matrix $AB$ is $2 \times 4$.  
Perform the multiplication:  

$$
AB = \begin{bmatrix} 
4 & 2 & 1 & 6 \\  
10 & 2 & 4 & 15 
\end{bmatrix}
$$  

---

### Transposes of $A$ and $B$  

#### Transpose of $B$:  
Transpose flips rows into columns:  
$$
B^T = \begin{bmatrix} 
1 & 0 & 1 \\  
0 & 1 & 0 \\  
1 & 0 & 0 \\  
-1 & 1 & 1 
\end{bmatrix}
$$  

#### Transpose of $A$:  
Transpose flips rows into columns:  
$$
A^T = \begin{bmatrix} 
1 & 4 \\  
2 & 5 \\  
3 & 6 
\end{bmatrix}
$$  

---

### Order to Multiply Transposes  

Now consider multiplying the transposes **in reverse order**:  

Multiply $B^T A^T$. First ensure compatibility:  
- $B^T$ is $4 \times 3$  
- $A^T$ is $3 \times 2$  
- Resulting matrix: $4 \times 2$.  

Perform the multiplication:  
$$
B^T A^T = \begin{bmatrix} 
4 & 10 \\  
2 & 5 \\  
1 & 4 \\  
6 & 15 
\end{bmatrix}
$$  

---

### Observations  

The product of $B^T A^T$ is identical to $(AB)^T$:  
$$
B^T A^T = (AB)^T
$$  

This demonstrates the property: **The transpose of the product is equal to the product of the transposes in reverse order**.  

---

### Conclusion  

#### General Formula for Transposes:  
$$
(A \cdot B)^T = B^T \cdot A^T
$$  

This property mirrors the behavior seen with inverses:  
1. The reverse order of operations applies to individual components.  
2. Analogous interpretation holds for inversion and transposition.