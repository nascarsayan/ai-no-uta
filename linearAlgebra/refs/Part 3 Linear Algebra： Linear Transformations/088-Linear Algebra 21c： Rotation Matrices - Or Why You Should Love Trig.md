## Rotations in the Plane with Cartesian Basis

### Overview
In this video, we analyze rotations in the plane with respect to a Cartesian basis and derive the famous **rotation matrices**. Along the way, we confirm that these matrices satisfy the **four basic properties** of rotations in linear algebra.

---

### 1. The Rotation Matrix
A rotation in the plane can be represented using a transformation matrix. By applying a rotation of angle $\alpha$ to the standard basis vectors $\mathbf{e}_1$ and $\mathbf{e}_2$, we derive the rotation matrix:

#### Basis Vector Rotations:
1. **First column (rotating $\mathbf{e}_1$ by $\alpha$):**
    - Resulting vector: $\begin{bmatrix} \cos \alpha \\ \sin \alpha \end{bmatrix}$  
    - First column = $\begin{bmatrix} \cos \alpha \\ \sin \alpha \end{bmatrix}$  

2. **Second column (rotating $\mathbf{e}_2$ by $\alpha$):**
    - Resulting vector: $\begin{bmatrix} -\sin \alpha \\ \cos \alpha \end{bmatrix}$  
    - Second column = $\begin{bmatrix} -\sin \alpha \\ \cos \alpha \end{bmatrix}$  

#### Final Rotation Matrix:
$$
R_\alpha =
\begin{bmatrix}
\cos \alpha & -\sin \alpha \\
\sin \alpha & \cos \alpha
\end{bmatrix}
$$

This matrix has properties we will explore further.

---

### 2. Key Properties of the Rotation Matrix
The rotation matrix exhibits several fundamental properties that hold under a Cartesian basis. These properties are tied to the geometric and algebraic nature of rotations.

#### Property 1: Composition of Rotations
The composition of two rotations by angles $\alpha$ and $\beta$ corresponds to a single rotation by the sum of the angles $\alpha + \beta$. Mathematically:
$$
R_\beta R_\alpha = R_{\alpha + \beta}
$$

#### Trigonometric Identity Verification:
Using the entries of the rotation matrices:
- $(1,1)$ entry: $\cos \alpha \cos \beta - \sin \alpha \sin \beta = \cos(\alpha + \beta)$  
- $(2,1)$ entry: $-\sin \alpha \cos \beta - \cos \alpha \sin \beta = -\sin(\alpha + \beta)$  

These align with trigonometric sum formulas.

#### Property 2: Length Preservation
Rotations preserve the Euclidean length of vectors. For any vector $\mathbf{v} \in \mathbb{R}^2$:
$$
\| R_\alpha \mathbf{v} \| = \| \mathbf{v} \|
$$

#### Property 3: Orthogonal Matrix (Transpose is the Inverse)
The rotation matrix is orthogonal:
$$
R_\alpha^{-1} = R_\alpha^\top
$$

- This follows from the fact that rotation transformations are length-preserving.
- Inverting $R_\alpha$ is equivalent to reversing the rotation angle:
$$
R_\alpha^{-1} =
R_{-\alpha} =
\begin{bmatrix}
\cos(-\alpha) & -\sin(-\alpha) \\
\sin(-\alpha) & \cos(-\alpha)
\end{bmatrix}
=
\begin{bmatrix}
\cos \alpha & \sin \alpha \\
-\sin \alpha & \cos \alpha
\end{bmatrix}
$$

#### Property 4: Determinant
The determinant of the rotation matrix is always $1$:
$$
\det R_\alpha = (\cos \alpha)^2 + (\sin \alpha)^2 = 1
$$

This reflects the fact that rotations preserve area.

#### Property 5: No Real Eigenvalues (Except for Specific Cases)
- The eigenvalues of $R_\alpha$ are generally complex unless $\alpha$ is a multiple of $\pi$.
- For $\alpha = k\pi$, the matrix has real eigenvalues:
  - $\alpha = 0$ gives eigenvalue $1$ (identity matrix).
  - $\alpha = \pi$ gives eigenvalue $-1$ (reflection matrix).

---

### 3. Derivation of Rotation Composition
To verify that $R_\beta R_\alpha = R_{\alpha+\beta}$, multiply the two rotation matrices:
$$
R_\beta =
\begin{bmatrix}
\cos \beta & -\sin \beta \\
\sin \beta & \cos \beta
\end{bmatrix},
\quad
R_\alpha =
\begin{bmatrix}
\cos \alpha & -\sin \alpha \\
\sin \alpha & \cos \alpha
\end{bmatrix}
$$

Result:
$$
R_\beta R_\alpha =
\begin{bmatrix}
(\cos \beta \cos \alpha - \sin \beta \sin \alpha) & (-\cos \beta \sin \alpha - \sin \beta \cos \alpha) \\
(\sin \beta \cos \alpha + \cos \beta \sin \alpha) & (-\sin \beta \sin \alpha + \cos \beta \cos \alpha)
\end{bmatrix}
=
\begin{bmatrix}
\cos(\alpha + \beta) & -\sin(\alpha + \beta) \\
\sin(\alpha + \beta) & \cos(\alpha + \beta)
\end{bmatrix}
$$

This confirms the composition property.

---

### 4. Properties of Eigenvalues
#### Case Analysis:
1. For $\alpha = k\pi$:
   - If $k$ is even: $R_\alpha = I$ with eigenvalue $1$.
   - If $k$ is odd: $R_\alpha = -I$ with eigenvalue $-1$.

2. For $\alpha \neq k\pi$:
   - Eigenvalues are complex: $\lambda = e^{i\alpha}, \lambda = e^{-i\alpha}$ (on the unit circle in the complex plane).

### 5. Orthogonality and Transpose
Rotations preserve both:
- **Lengths:** $\| R_\alpha \mathbf{v} \| = \| \mathbf{v} \|$
- **Dot products:** $\langle R_\alpha \mathbf{u}, R_\alpha \mathbf{v} \rangle = \langle \mathbf{u}, \mathbf{v} \rangle$

As a result, $R_\alpha$ satisfies:
$$
R_\alpha^\top R_\alpha = I
$$

Hence:
$$
R_\alpha^{-1} = R_\alpha^\top
$$

---

### 6. General Observations
1. **Invariant Properties:** The four core rotation properties are intrinsic to the transformation itself, independent of the coordinate system.
2. **Cartesian-Specific Properties:**
   - Determinant = $1$
   - Orthogonality ($R_\alpha^{-1} = R_\alpha^\top$) is tied to the Cartesian basis.

Switching away from Cartesian bases may lead to loss of these additional properties.

---

### 7. Next Steps
- Future topics will explore rotations under **non-Cartesian bases**, where certain properties (like orthogonality of the matrix or determinant = $1$) might no longer hold.
- Examine higher-dimensional rotations ($\mathbb{R}^3$ and beyond). 

😅 Mistakes are part of learning! Always revisit core derivations for clarity! 🚀