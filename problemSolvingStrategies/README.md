## Problem Solving Strategies - Arthur Engel

Insights while solving problems from the book.

### 1. The Invariance Principle

- E2. $1, 2, ...2n$.
  - We have another invariant:
    - The number of odd numbers is odd.
    - Odd number count disappear in pairs, i.e.:
      + $|O - E|$, $|E - O|$ gives $O$
      + $|O - O|$, $|E - E|$ gives $E$
    - Since there are odd number of odd numbers, there will be at least one odd number left.

- E3. Circle divided into 6 sectors with $1, 0, 1, 0, 0, 0$
  - If the number of sectors is odd, all the numbers can be equalized.
  - If the number of sectors is even, it can never be done, by the invariant.

- E4. Parliament - Each member having at most 3 enemies. We can partition into 2 groups each member having at most 1.
  - Worst case scenaio: There are groups of 4, everyone the enemy of each other. We can take any 2 and put into the other group. This is simply bipartite problem.

- E5. $(a, b, c, d) \to (a-b, b-c, c-d, d-a)$ Good one.
  - Can we always have equality in $(a_n^2 + b_n^2 + c_n^2 + d_n^2) \geq 2^{n-1}(a_1^2 + b_1^2 + c_1^2 + d_1^2)$?
    + Yes, when $a+c = b+c = 0$, i.e., when seq is $a, b, -a, -b$
    + Then $a-b, a+b, -(a-b), -(a+b)$ is the next seq, which has the same property, $S_1+S_3 = 0, S_2+S_4 = 0$.

