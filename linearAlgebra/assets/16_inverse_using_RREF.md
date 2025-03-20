---
title: Matrix Inverse using RREF
font_size: 60
blocks:
  - name: "Matrix"
    position: [0, 0]
---

### Step 1

$$
\begin{bmatrix}
1 & 2 & 3 \\
4 & 5 & 6 \\
7 & 8 & 10
\end{bmatrix}
$$

### Step 2

$$
\begin{bmatrix}
1 & 2 & 3 & 1 & 0 & 0 \\
4 & 5 & 6 & 0 & 1 & 0 \\
7 & 8 & 10 & 0 & 0 & 1
\end{bmatrix}
$$

### Step 3

$$
\begin{bmatrix}
1 & 2 & 3 & 1 & 0 & 0 \\
0 & 3 & 6 & 4 & -1 & 0 \\
7 & 8 & 10 & 0 & 0 & 1
\end{bmatrix}
$$

### Step 4

$$
\begin{bmatrix}
1 & 2 & 3 & 1 & 0 & 0 \\
0 & 3 & 6 & 4 & -1 & 0 \\
0 & 6 & 11 & 7 & 0 & -1
\end{bmatrix}
$$

### Step 5

$$
\begin{bmatrix}
1 & 2 & 3 & 1 & 0 & 0 \\
0 & 3 & 6 & 4 & -1 & 0 \\
0 & 0 & 1 & 1 & -2 & 1
\end{bmatrix}
$$

### Step 6

$$
\begin{bmatrix}
1 & 2 & 3 & 1 & 0 & 0 \\
0 & 3 & 6 & 4 & -1 & 0 \\
0 & 0 & 1 & 1 & -2 & 1
\end{bmatrix}
$$

### Step 7

$$
\begin{bmatrix}
1 & 2 & 3 & 1 & 0 & 0 \\
0 & 3 & 0 & -2 & 11 & -6 \\
0 & 0 & 1 & 1 & -2 & 1
\end{bmatrix}
$$

### Step 8

$$
\begin{bmatrix}
1 & 2 & 0 & -2 & 6 & -3 \\
0 & 3 & 0 & -2 & 11 & -6 \\
0 & 0 & 1 & 1 & -2 & 1
\end{bmatrix}
$$

### Step 9

$$
\begin{bmatrix}
1 & 2 & 0 & -2 & 6 & -3 \\
0 & 1 & 0 & -2/3 & 11/3 & -2 \\
0 & 0 & 1 & 1 & -2 & 1
\end{bmatrix}
$$

### Step 10

$$
\begin{bmatrix}
1 & 0 & 0 & -2/3 & -4/3 & 1 \\
0 & 1 & 0 & -2/3 & 11/3 & -2 \\
0 & 0 & 1 & 1 & -2 & 1
\end{bmatrix}
$$
