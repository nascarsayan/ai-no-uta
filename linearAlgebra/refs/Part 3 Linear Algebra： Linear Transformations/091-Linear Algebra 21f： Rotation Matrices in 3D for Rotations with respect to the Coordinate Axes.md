## Rotations in 3D - Elementary Rotation Matrices
This discussion revolves around rotation matrices in three dimensions with respect to a Cartesian basis. The end goal is to construct a matrix that represents an **arbitrary rotation**. However, breaking down arbitrary rotations into simpler, elementary rotations makes the process more manageable.

### 1. Elementary Rotations
Elementary rotations are simple rotations around one of the axes. We'll define three rotation matrices, each corresponding to a counterclockwise rotation about one of the x, y, or z axes, typically named as $R_x$, $R_y$, and $R_z$.

### 2. Rotation Matrix for $x$-Axis ($R_x$)
- Rotation occurs around the $x$-axis.
- The $x$ component remains unchanged while the $y$ and $z$ components undergo a planar rotation.

Rotation matrix:

$$
R_x(\theta) =
\begin{bmatrix}
1 & 0 & 0 \\
0 & \cos\theta & -\sin\theta \\
0 & \sin\theta & \cos\theta
\end{bmatrix}
$$

### 3. Rotation Matrix for $y$-Axis ($R_y$)
- Rotation occurs around the $y$-axis.
- The $y$ component remains unchanged while the $x$ and $z$ components undergo a planar rotation.

Rotation matrix:

$$
R_y(\theta) =
\begin{bmatrix}
\cos\theta & 0 & \sin\theta \\
0 & 1 & 0 \\
-\sin\theta & 0 & \cos\theta
\end{bmatrix}
$$

### 4. Rotation Matrix for $z$-Axis ($R_z$)
- Rotation occurs around the $z$-axis.
- The $z$ component remains unchanged while the $x$ and $y$ components undergo a planar rotation.

Rotation matrix:

$$
R_z(\theta) =
\begin{bmatrix}
\cos\theta & -\sin\theta & 0 \\
\sin\theta & \cos\theta & 0 \\
0 & 0 & 1
\end{bmatrix}
$$

### 5. Notations and Observations
- **Matrix Naming**: The rotations are typically written as $R_x(\theta)$, $R_y(\theta)$, and $R_z(\theta)$ to denote which axis the matrix corresponds to and the angle of rotation $\theta$.
- **Counterclockwise Specification**: The term "counterclockwise" is relative to the observer's perspective when looking down the axis in the positive direction.

### 6. Constructing Arbitrary Rotations
- Arbitrary rotations use combinations of these elementary rotation matrices.
- **Euler Angles**: In the next step, the construction of arbitrary rotation matrices using Euler angles (a combination of rotations about different axes) will be discussed.

### Key Points:
1. Rotation about a particular axis keeps that axis unchanged while the other two components undergo a 2D planar rotation.
2. The cosine and sine terms used in these matrices correspond to a standard 2D rotation transformation.
3. These three matrices form the foundation for more complex rotations in 3D space. 

In the next discussion, we will explore **Euler angles** to represent an arbitrary 3D rotation.