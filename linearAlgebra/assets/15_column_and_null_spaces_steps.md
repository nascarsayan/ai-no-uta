---
font_size: 40
blocks:
  - name: "Matrix"
    position: [2.2, -3.5]
  - name: "ColumnSpace"
    position: [-1, -5]
  - name: "NullSpace"
    position: [-1, 1.5]
---

### Step 1

$$
\begin{bmatrix}
1 \\\ 2 \\\ 0 \\\ 0
\end{bmatrix}
$$

$$
\mathbf{R} =
\begin{bmatrix}
a \\\ 2a \\\ 0 \\\ 0
\end{bmatrix}
$$

$$
\mathbf{N} =
\{\begin{bmatrix}
0
\end{bmatrix}
\}
$$

### Step 2

$$
\begin{bmatrix}
1 & 3\\
2 & 6\\
0 & 0\\
0 & 0
\end{bmatrix}
$$

$$
\mathbf{R} =
\begin{bmatrix}
a \\\ 2a \\\ 0 \\\ 0
\end{bmatrix}
$$

$$
\mathbf{N} =
\alpha
\begin{bmatrix}
3 \\\ -1
\end{bmatrix}
$$

### Step 3

$$
\begin{bmatrix}
1 & 3 & 0\\
2 & 6 & 0\\
0 & 0 & 0\\
0 & 0 & 0
\end{bmatrix}
$$

$$
\mathbf{R} =
\begin{bmatrix}
a \\\ 2a \\\ 0 \\\ 0
\end{bmatrix}
$$

$$
\mathbf{N} =
\alpha
\begin{bmatrix}
3 \\\ -1 \\\ 0
\end{bmatrix} +
\beta
\begin{bmatrix}
0 \\\ 0 \\\ 1
\end{bmatrix}
$$

### Step 4

$$
\begin{bmatrix}
1 & 3 & 0 & 0\\
2 & 6 & 0 & 0\\
0 & 0 & 0 & 1\\
0 & 0 & 0 & 0
\end{bmatrix}
$$

$$
\mathbf{R} =
\begin{bmatrix}
a \\\ 2a \\\ b \\\ 0
\end{bmatrix}
$$

$$
\mathbf{N} =
\alpha
\begin{bmatrix}
3 \\\ -1 \\\ 0 \\\ 0
\end{bmatrix} +
\beta
\begin{bmatrix}
0 \\\ 0 \\\ 1 \\\ 0
\end{bmatrix}
$$

### Step 5

$$
\begin{bmatrix}
1 & 3 & 0 & 0 & 10\\
2 & 6 & 0 & 0 & 20\\
0 & 0 & 0 & 1 & 37\\
0 & 0 & 0 & 0 & 0
\end{bmatrix}
$$

$$
\mathbf{R} =
\begin{bmatrix}
a \\\ 2a \\\ b \\\ 0
\end{bmatrix}
$$

$$
\mathbf{N} =
\alpha
\begin{bmatrix}
3 \\\ -1 \\\ 0 \\\ 0 \\\ 0
\end{bmatrix} +
\beta
\begin{bmatrix}
0 \\\ 0 \\\ 1 \\\ 0 \\\ 0
\end{bmatrix} +
\gamma
\begin{bmatrix}
10 \\\ 0 \\\ 0 \\\ 37 \\\ 0
\end{bmatrix}
$$

### Step 6

$$
\begin{bmatrix}
1 & 3 & 0 & 0 & 10 & 1\\
2 & 6 & 0 & 0 & 20 & 0\\
0 & 0 & 0 & 1 & 37 & 0\\
0 & 0 & 0 & 0 & 0 & 0
\end{bmatrix}
$$

$$
\mathbf{R} =
\begin{bmatrix}
a \\\ b \\\ c \\\ 0
\end{bmatrix}
$$

$$
\mathbf{N} =
\alpha
\begin{bmatrix}
3 \\\ -1 \\\ 0 \\\ 0 \\\ 0 \\\ 0
\end{bmatrix} +
\beta
\begin{bmatrix}
0 \\\ 0 \\\ 1 \\\ 0 \\\ 0 \\\ 0
\end{bmatrix} +
\gamma
\begin{bmatrix}
10 \\\ 0 \\\ 0 \\\ 37 \\\ 0 \\\ 0
\end{bmatrix}
$$

### Step 7

$$
\begin{bmatrix}
1 & 3 & 0 & 0 & 10 & 1 & 3\\
2 & 6 & 0 & 0 & 20 & 0 & 64\\
0 & 0 & 0 & 1 & 37 & 0 & -73\\
0 & 0 & 0 & 0 & 0 & 0 & 0
\end{bmatrix}
$$

$$
\mathbf{R} =
\begin{bmatrix}
a \\\ b \\\ c \\\ 0
\end{bmatrix}
$$

$$
\mathbf{N} =
\alpha
\begin{bmatrix}
3 \\\ -1 \\\ 0 \\\ 0 \\\ 0 \\\ 0 \\\ 0
\end{bmatrix} +
\beta
\begin{bmatrix}
0 \\\ 0 \\\ 1 \\\ 0 \\\ 0 \\\ 0 \\\ 0
\end{bmatrix} +
\gamma
\begin{bmatrix}
10 \\\ 0 \\\ 0 \\\ 37 \\\ 0 \\\ 0 \\\ 0
\end{bmatrix} +
\delta
\begin{bmatrix}
32 \\\ 0 \\\ 0 \\\ -73 \\\ 0 \\\ -29 \\\ -1
\end{bmatrix}
$$

### Step 8

$$
\begin{bmatrix}
1 & 3 & 0 & 0 & 10 & 1 & 3 & 2 \\
2 & 6 & 0 & 0 & 20 & 0 & 64 & 3 \\
0 & 0 & 0 & 1 & 37 & 0 & -73 & 4 \\
0 & 0 & 0 & 0 & 0 & 0 & 0 & 5
\end{bmatrix}
$$

$$
\begin{aligned}
\mathbf{R} &=
\begin{bmatrix}
a \\\ b \\\ c \\\ d
\end{bmatrix} \\
&= \mathbb{R}^4
\end{aligned}
$$

$$
\mathbf{N} =
\alpha
\begin{bmatrix}
3 \\\ -1 \\\ 0 \\\ 0 \\\ 0 \\\ 0 \\\ 0 \\\ 0
\end{bmatrix} +
\beta
\begin{bmatrix}
0 \\\ 0 \\\ 1 \\\ 0 \\\ 0 \\\ 0 \\\ 0 \\\ 0
\end{bmatrix} +
\gamma
\begin{bmatrix}
10 \\\ 0 \\\ 0 \\\ 37 \\\ 0 \\\ 0 \\\ 0 \\\ 0
\end{bmatrix} +
\delta
\begin{bmatrix}
32 \\\ 0 \\\ 0 \\\ -73 \\\ 0 \\\ -29 \\\ -1 \\\ 0
\end{bmatrix}
$$

