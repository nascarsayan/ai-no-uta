## Proofs of the Dot Product Formula

### The Statement
We aim to prove that the formula for the dot product of vectors $\mathbf{v}$ and $\mathbf{w}$ in terms of their components, expressed as:

$$
\mathbf{v} \cdot \mathbf{w} = \|\mathbf{v}\| \|\mathbf{w}\| \cos(\theta),
$$

where $\|\mathbf{v}\|$ and $\|\mathbf{w}\|$ are the magnitudes of $\mathbf{v}$ and $\mathbf{w}$, and $\theta$ is the angle between them, is valid.

---

### 1. **Proof Using Trigonometry**

#### Key Idea:
Utilize basic trigonometric identities, with reliance on geometric representations of the vectors.

#### Special Case – Unit Vectors:
Assume $\mathbf{v}$ and $\mathbf{w}$ are unit vectors:
  - Let the components of $\mathbf{v}$ be $\alpha_1$ and $\alpha_2$, and those of $\mathbf{w}$ be $\beta_1$ and $\beta_2$.

For unit vectors:
  - $\|\mathbf{v}\| = \|\mathbf{w}\| = 1$
  - $\alpha_1 = \cos(\nu)$, $\alpha_2 = \sin(\nu)$ (angles $\nu$ and $\omega$ are with respect to basis $\mathbf{e}_1$)
  - $\beta_1 = \cos(\omega)$, $\beta_2 = \sin(\omega)$ 

From the dot product formula:

$$
\mathbf{v} \cdot \mathbf{w} = \alpha_1 \beta_1 + \alpha_2 \beta_2,
$$
which simplifies to:

$$
\mathbf{v} \cdot \mathbf{w} = \cos(\nu)\cos(\omega) + \sin(\nu)\sin(\omega).
$$

Using the cosine angle addition formula, this becomes:

$$
\mathbf{v} \cdot \mathbf{w} = \cos(\nu - \omega).
$$

Here, $\nu - \omega$ is the angle $\theta$ between the vectors $\mathbf{v}$ and $\mathbf{w}$. Thus:

$$
\mathbf{v} \cdot \mathbf{w} = \|\mathbf{v}\| \|\mathbf{w}\| \cos(\theta),
$$

proven for unit vectors.


#### General Case:
If vectors $\mathbf{v}$ and $\mathbf{w}$ are not unit vectors:
- Scale the components of $\mathbf{v}$ and $\mathbf{w}$ by their lengths ($\|\mathbf{v}\|$ and $\|\mathbf{w}\|$):

$$
\mathbf{v} \cdot \mathbf{w} = \|\mathbf{v}\| \|\mathbf{w}\| \Bigg( \frac{\alpha_1}{\|\mathbf{v}\|}\frac{\beta_1}{\|\mathbf{w}\|} + \frac{\alpha_2}{\|\mathbf{v}\|}\frac{\beta_2}{\|\mathbf{w}\|} \Bigg).
$$

Recognize the normalized components as unit vectors; from the special case, this reduces to:

$$
\mathbf{v} \cdot \mathbf{w} = \|\mathbf{v}\| \|\mathbf{w}\| \cos(\theta).
$$

The general case is thus proven.

---

### 2. **Proof Using Algebra**

#### Key Idea:
Expand the dot product in terms of components and use the orthogonality of the basis vectors.

#### Represent the Vectors:
Let:

$$
\mathbf{v} = \alpha_1 \mathbf{e}_1 + \alpha_2 \mathbf{e}_2, \quad \mathbf{w} = \beta_1 \mathbf{e}_1 + \beta_2 \mathbf{e}_2,
$$

where $\mathbf{e}_1$ and $\mathbf{e}_2$ are orthonormal basis vectors.

#### Expand Using Distributive Law:
The dot product:

$$
\mathbf{v} \cdot \mathbf{w} = (\alpha_1 \mathbf{e}_1 + \alpha_2 \mathbf{e}_2) \cdot (\beta_1 \mathbf{e}_1 + \beta_2 \mathbf{e}_2),
$$

expands to:

$$
\mathbf{v} \cdot \mathbf{w} = \alpha_1 \beta_1 (\mathbf{e}_1 \cdot \mathbf{e}_1) + \alpha_1 \beta_2 (\mathbf{e}_1 \cdot \mathbf{e}_2) + \alpha_2 \beta_1 (\mathbf{e}_2 \cdot \mathbf{e}_1) + \alpha_2 \beta_2 (\mathbf{e}_2 \cdot \mathbf{e}_2).
$$

#### Simplify Using Orthogonality:
- $\mathbf{e}_1 \cdot \mathbf{e}_1 = \mathbf{e}_2 \cdot \mathbf{e}_2 = 1$ (basis vectors are unit length)
- $\mathbf{e}_1 \cdot \mathbf{e}_2 = \mathbf{e}_2 \cdot \mathbf{e}_1 = 0$ (basis vectors are orthogonal)

Thus:

$$
\mathbf{v} \cdot \mathbf{w} = \alpha_1 \beta_1 + \alpha_2 \beta_2.
$$

This is exactly the component-wise definition of the dot product.

#### Relating to the Trigonometric Definition:
The result matches the formula $\mathbf{v} \cdot \mathbf{w} = \|\mathbf{v}\| \|\mathbf{w}\| \cos(\theta)$ after substituting $\alpha_1$ and $\alpha_2$ in terms of $\cos(\nu)$ and $\sin(\nu)$ (or $\|\mathbf{v}\|$ and angles, if desired).

---

### Summary
- **Proof 1** derived the dot product formula assuming unit vectors and extended the result to general cases using scaling.
- **Proof 2** proved the component-wise formula directly via distributive law and orthogonality.

These proofs verify the equivalence of the geometric and algebraic definitions of the dot product.