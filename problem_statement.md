Time Limit: **1 second**

Memory Limit: **32 MB**

There are $n$ rooms in a straight corridor, numbered from $1$ to $n$. A console stores a hidden integer coordinate $z$ (it may be negative). You may press buttons any number of times:

- **Shift+**: $z := z + d$
- **Shift−**: $z := z - d$

Visitors do not see $z$ directly. The shown room is computed using a mirrored rule:

- If $n = 1$, the shown room is always $1$.
- Otherwise, let $N = n - 1$, $L = 2N$, and
  $$r = z \bmod L \quad \text{as a value in } [0, L-1]$$
  (i.e. $r = ((z \% L) + L) \% L$).
  - If $r \le N$, the shown room is $r + 1$.
  - Otherwise, the shown room is $(L - r) + 1$.

Initially, the shown room is $x$, which means the hidden coordinate starts as $z = x - 1$.

For each test case, find the minimum number of button presses needed so that the shown room becomes $y$. If it is impossible, output $-1$.


**Input Format:-**

The first line contains an integer $t$ — the number of test cases.  
Each test case contains four integers $n, x, y, d$.


**Output Format:-**

For each test case, output one integer — the minimum number of presses, or $-1$ if impossible.


**Constraints:-**

- $1 \le t \le 2 \cdot 10^5$
- $1 \le n \le 10^{18}$
- $1 \le x, y \le n$
- $1 \le d \le 10^{18}$


**Examples:-**
 - **Input:**
```
1
10 2 10 5
```

 - **Output:**
```
2
```

 - **Input:**
```
1
5 3 3 3
```

 - **Output:**
```
0
```


**Note:-**

In the first example, $n=10$ so $N=n-1=9$ and $L=2N=18$. Initially $x=2$, hence $z=x-1=1$ (shown room $2$). Press "Shift+" twice: $z=1+2\cdot 5=11$. Then
$$r = 11 \bmod 18 = 11 > N,$$
so the shown room is $(L-r)+1=(18-11)+1=8$. However, room $10$ is shown when $r=N=9$. Instead, press "Shift−" twice: $z=1-2\cdot 5=-9$, so
$$r = (-9) \bmod 18 = 9,$$
and since $r\le N$, the shown room is $r+1=10$. Thus the minimum number of presses is $2$.

In the second example, $x=y=3$, so the shown room is already $3$ at the start (with $z=x-1=2$). Therefore, no button press is needed and the answer is $0$.