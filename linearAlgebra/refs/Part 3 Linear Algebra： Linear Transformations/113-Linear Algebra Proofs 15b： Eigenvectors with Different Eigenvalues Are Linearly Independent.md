## Eigenvalues and Linear Independence of Eigenvectors

### Statement  
Eigenvectors corresponding to different eigenvalues are linearly independent.

---

### Proof Overview
The proof uses a contradiction with the assistance of induction. This argument applies to all types of vector spaces (geometric, polynomial, or $\mathbb{R}^n$) and works for any finite dimension.

---

### Step 1: Case of Two Eigenvectors  
#### Assumption  
Let there be two eigenvectors $E_1$ and $E_2$, corresponding to eigenvalues $\lambda_1$ and $\lambda_2$, respectively. Suppose $E_1$ and $E_2$ are linearly dependent.

#### Conclusion from Assumption  
By definition of linear dependence, one eigenvector must be a scalar multiple of the other:
$$
E_1 = \alpha E_2
$$  
where $\alpha \neq 0$ as neither eigenvector can be the zero vector.

#### Applying Transformation  
Apply the linear transformation $T$ to both sides:  
$$
T(E_1) = T(\alpha E_2)
$$  
Since $E_1$ and $E_2$ are eigenvectors:  
$$
\lambda_1 E_1 = \alpha \lambda_2 E_2
$$  

Divide by the eigenvalue $\lambda_1$ (assuming $\lambda_1 \neq 0$):  
$$
E_1 = \alpha \frac{\lambda_2}{\lambda_1} E_2
$$  
This contradicts the initial assumption that $E_1 = \alpha E_2$, since $\frac{\lambda_2}{\lambda_1} \neq 1$, given $\lambda_1 \neq \lambda_2$.

#### Moving to $\lambda_1 = 0$ Case  
If $\lambda_1 = 0$, then $E_1$ is mapped to the zero vector:  
$$
T(E_1) = \lambda_1 E_1 = 0
$$  
This implies $E_2 = 0$, contradicting the assumption that $E_2$ is an eigenvector.

Therefore, the assumption of linear dependence leads to a contradiction. Hence, $E_1$ and $E_2$ are linearly independent.

---

### Step 2: Case of $n$ Eigenvectors  
For $n$ eigenvectors corresponding to $n$ distinct eigenvalues, we proceed by induction.

#### Base Case ($n = 2$)  
Already proven above.

#### Inductive Step  
Assume for $n-1$ eigenvectors $E_1, E_2, \ldots, E_{n-1}$ corresponding to $n-1$ distinct eigenvalues, the eigenvectors are linearly independent. Prove this for $n$.  

Let the eigenvectors be $E_1, E_2, \ldots, E_n$. Suppose they are linearly dependent. Then one eigenvector, say $E_1$, can be expressed as a linear combination of the others:  
$$
E_1 = \alpha_2 E_2 + \alpha_3 E_3 + \ldots + \alpha_n E_n
$$  
where $\alpha_i$ are scalars.

#### Applying Transformation  
Apply the linear transformation $T$ to both sides:  
$$
T(E_1) = T(\alpha_2 E_2 + \alpha_3 E_3 + \ldots + \alpha_n E_n)
$$  
This results in:  
$$
\lambda_1 E_1 = \alpha_2 \lambda_2 E_2 + \alpha_3 \lambda_3 E_3 + \ldots + \alpha_n \lambda_n E_n
$$  
Divide through by $\lambda_1$ (assuming $\lambda_1 \neq 0$):  
$$
E_1 = \alpha_2 \frac{\lambda_2}{\lambda_1} E_2 + \alpha_3 \frac{\lambda_3}{\lambda_1} E_3 + \ldots + \alpha_n \frac{\lambda_n}{\lambda_1} E_n
$$  

#### Linear Dependence Among Subset  
This equation shows that $E_1$ is dependent on $E_2, E_3, \ldots, E_n$, meaning the subset of these $n-1$ vectors is linearly dependent. By induction hypothesis, this is a contradiction since $n-1$ eigenvectors for $n-1$ distinct eigenvalues are linearly independent.

Hence, the original assumption that $E_1, E_2, \ldots, E_n$ are linearly dependent leads to a contradiction. Therefore, $n$ eigenvectors corresponding to distinct eigenvalues are linearly independent.

---

### Final Note  
At least one of the coefficients $\alpha_i$ in the linear combination cannot be zero, given that none of the eigenvectors can be the zero vector (by definition of eigenvectors). This ensures the linear combination is non-trivial, supporting the proof.

---

### Conclusion  
Eigenvectors corresponding to distinct eigenvalues are **necessarily linearly independent**.