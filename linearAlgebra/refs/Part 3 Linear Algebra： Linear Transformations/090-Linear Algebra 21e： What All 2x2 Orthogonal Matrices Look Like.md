## 2x2 Orthogonal Matrices

In this lecture, we will determine the structure of all 2x2 orthogonal matrices. The main goal is to show that these can either be classified as standard rotation matrices or rotation matrices with a reflection. Let’s break this process down.

---

### **Definition and Properties of Orthogonal Matrices**

Given an orthogonal matrix $Q$, its definition implies:  

- The **columns of $Q$ are orthonormal**, that is:
  - Their dot products satisfy orthogonality.
  - Each column is a unit vector (magnitude = 1).

- $Q^\top Q = I$, where $Q^\top$ denotes the transpose of $Q$, and $I$ is the identity matrix.

We will decompose the general form of a 2x2 orthogonal matrix and examine the constraints placed on its entries.

---

### **General Form of a 2x2 Orthogonal Matrix**

Let $Q$ be a 2x2 matrix with entries $a, b, c, d$:
$$
Q = \begin{bmatrix} 
a & b \\ 
c & d 
\end{bmatrix}
$$
and its transpose:
$$
Q^\top = \begin{bmatrix} 
a & c \\ 
b & d 
\end{bmatrix}.
$$

The orthogonality condition states:
$$
Q^\top Q = I.
$$

#### **Condition 1: Column Norms**

The diagonal terms of $Q^\top Q = I$ yield:
1. The first column is a unit vector:
   $$
   a^2 + c^2 = 1.
   $$

2. The second column is also a unit vector:
   $$
   b^2 + d^2 = 1.
   $$

#### **Condition 2: Orthogonality Between Columns**

The off-diagonal terms of $Q^\top Q = I$ give:
$$
ab + cd = 0.
$$

This means the dot product of the two columns is zero, confirming their orthogonality.

---

### **Relationship Between Entries**

From the conditions, we observe the following:
- The first column satisfies $a^2 + c^2 = 1$. This corresponds to the trigonometric identity:
  $$
  \cos^2(\alpha) + \sin^2(\alpha) = 1.
  $$
  Choose an angle $\alpha$ such that:
  $$
  a = \cos(\alpha), \quad c = \sin(\alpha).
  $$

- The second column satisfies $b^2 + d^2 = 1$. Let the entries be parametrized as:
  $$
  b = \cos(\beta), \quad d = \sin(\beta).
  $$

- To satisfy $ab + cd = 0$, special constraints exist between $\alpha$ and $\beta$.

---

### **Constructing the Second Column**

To guarantee orthogonality to the first column:
1. Swap the entries of the first column.
2. Introduce a minus sign in one of the swapped terms:
   $$
   \text{Second column: } \begin{bmatrix} -\sin(\alpha) \\ \cos(\alpha) \end{bmatrix}.
   $$

Thus, the matrix takes the form:
$$
Q = \begin{bmatrix} 
\cos(\alpha) & -\sin(\alpha) \\ 
\sin(\alpha) & \cos(\alpha) 
\end{bmatrix}.
$$

This is the **standard rotation matrix** for angle $\alpha$.

---

### **Alternative Configuration: Reflection**

If the negative sign is placed in the other position of the second column:
$$
Q = \begin{bmatrix} 
\cos(\alpha) & \sin(\alpha) \\ 
\sin(\alpha) & -\cos(\alpha) 
\end{bmatrix}.
$$

This transformation describes a **rotation followed by a reflection**, as the determinant of this matrix is $-1$:
$$
\det(Q) = \cos^2(\alpha) - \sin^2(\alpha) = -1.
$$

---

### **Understanding Determinants**
- **Rotation Matrices**: Determinant = 1
- **Reflection Matrices**: Determinant = -1

---

### **Decomposition of General 2x2 Orthogonal Matrices**

An orthogonal matrix can always be expressed as either:
1. A **rotation** matrix:
   $$
   Q = \begin{bmatrix} 
   \cos(\alpha) & -\sin(\alpha) \\ 
   \sin(\alpha) & \cos(\alpha) 
   \end{bmatrix}.
   $$
2. A **rotation combined with reflection**:
   $$
   Q = \begin{bmatrix} 
   \cos(\alpha) & \sin(\alpha) \\ 
   \sin(\alpha) & -\cos(\alpha) 
   \end{bmatrix}.
   $$

---

### **Key Takeaways**
- All 2x2 orthogonal matrices either represent **rotations** or **compositions of rotations and reflections**.
- The determinant distinguishes between the two:
  - $\det(Q) = 1$: Pure rotation.
  - $\det(Q) = -1$: Rotation + reflection.

