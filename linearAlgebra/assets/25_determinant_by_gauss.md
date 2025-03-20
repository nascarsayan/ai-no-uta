---
title: Determinant by Gaussian Elimination
font_size: 60
blocks:
  - name: "Matrix"
    position: [0, 0]
---

## Step 0

$$
\begin{vmatrix}
1 & 1 & 4 & 1 \\
2 & 2 & 10 & 6 \\
3 & 9 & 21 & 17 \\
5 & 11 & 29 & 23
\end{vmatrix}
$$

## Step 1

$$
\begin{vmatrix}
1 & 1 & 4 & 1 \\
0 & 0 & 2 & 4 \\
3 & 9 & 21 & 17 \\
5 & 11 & 29 & 23
\end{vmatrix}
$$

## Step 2

$$
\begin{vmatrix}
1 & 1 & 4 & 1 \\
0 & 0 & 2 & 4 \\
0 & 6 & 9 & 14 \\
5 & 11 & 29 & 23
\end{vmatrix}
$$

## Step 3

$$
\begin{vmatrix}
1 & 1 & 4 & 1 \\
0 & 0 & 2 & 4 \\
0 & 6 & 9 & 14 \\
0 & 6 & 9 & 18
\end{vmatrix}
$$

## Step 4

$$
-\begin{vmatrix}
1 & 1 & 4 & 1 \\
0 & 6 & 9 & 14 \\
0 & 0 & 2 & 4 \\
0 & 6 & 9 & 18
\end{vmatrix}
$$

## Step 5

$$
-\begin{vmatrix}
1 & 1 & 4 & 1 \\
0 & 6 & 9 & 14 \\
0 & 0 & 2 & 4 \\
0 & 0 & 0 & 4
\end{vmatrix}
$$

## Step 6

$$
-(1 \times 6 \times 2 \times 4) = -48
$$
