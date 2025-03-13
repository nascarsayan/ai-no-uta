## Example: Calculating Determinant by Gaussian Elimination

This example demonstrates how to calculate the determinant of a matrix using Gaussian elimination. Throughout the process, row switching, subtraction, and triangular matrix formation are explained.

---

### Steps:

#### Initial Subtraction:
The first step in Gaussian elimination is to modify rows. Here, subtracting two times the first row from the second row produces:

$$
\begin{bmatrix}
0 & 0 & 2 & 4
\end{bmatrix}
$$

#### Temporary Zero Pivot:
At this stage, a temporary zero pivot is encountered. To proceed, we'll eventually need to switch rows.

#### Subtracting Higher Rows:
1. Subtract 3 times the first row from the third row:
    $$
    \begin{bmatrix}
    0 & 6 & 9 & 14
    \end{bmatrix}
    $$

2. Subtract 5 times the first row from the fourth row:
    $$
    \begin{bmatrix}
    0 & 6 & 9 & 18
    \end{bmatrix}
    $$

#### Row Switching for Non-Zero Pivot:
To ensure a nonzero pivot in the second row position, switch rows 2 and 3. However, this row switching affects the determinant due to the _alternating property_:
- **Effect:** The determinant is multiplied by $-1$. 
- We record this by factoring out $-1$.

#### Continuing Gaussian Elimination:
Proceeding with Gaussian elimination:
1. Subtract one time the second row from the fourth row:
    $$
    \begin{bmatrix}
    0 & 0 & 0 & 4
    \end{bmatrix}
    $$

#### Final Form:
The matrix is now in upper triangular form. The determinant of an upper triangular matrix is the product of its diagonal entries.

#### Determinant:
Product of diagonal entries: $48$  
Incorporate the $-1$ factor from row switching:  
**Determinant:** $-48$

---

### Summary:
The determinant of the original matrix is:

$$
\text{Determinant} = -48
$$

This concludes the example of calculating a determinant using Gaussian elimination!