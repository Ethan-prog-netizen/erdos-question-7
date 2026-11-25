# No distinct covering system with moduli supported on 3, 5, and 7

Every finite family of residue classes with distinct moduli \(m>1\) supported on \(\{3,5,7\}\) misses more than \(5/48\) of a period. The smallest period passing the necessary reciprocal-sum test is \(945\), but even there at least \(179\) of the \(945\) residues are missed. The proof is finite and uniform in all three exponents; the accompanying Python checks are not used to infer the theorem.

## Scope and setup

The unrestricted [Erdős–Selfridge problem](https://www.erdosproblems.com/7) asks whether distinct odd moduli can cover the integers. Qualitative noncoverage for the present subcase already follows from the classical Berger–Felzenbaum–Fraenkel necessary condition, stated without any squarefreeness assumption in [Guo and Sun’s introduction](https://arxiv.org/html/math/0412217): for the set \(P\) of prime divisors of the lcm of the moduli, a cover requires
\[
\prod_{p\in P}\frac{p-1}{p-2}-\sum_{p\in P}\frac1{p-2}>2.
\]
For \(P=\{3,5,7\}\) the left side is \(2(4/3)(6/5)-(1+1/3+1/5)=16/5-23/15=5/3\). Deleting a prime cannot increase it: writing \(t_p=1/(p-2)\), the expression is \(1+\sum_{J\subseteq P,\,|J|\ge2}\prod_{p\in J}t_p\). The proof below instead gives a quantitative bound by elementary conditioning; it does not require the full [distortion method of Balister, Bollobás, Morris, Sahasrabudhe and Tiba](https://link.springer.com/10.1007/s10474-020-01048-z).

Fix any common multiple \(N=3^A5^B7^C\) of the moduli. Every class is periodic modulo \(N\), so it suffices to count residues in \(\mathbb Z/N\mathbb Z\). By CRT a uniform residue is a tuple of independent uniform coordinates in \(\mathbb Z/3^A\mathbb Z\), \(\mathbb Z/5^B\mathbb Z\), and \(\mathbb Z/7^C\mathbb Z\). An exponent of zero gives a one-point coordinate. A class modulo \(m=3^a5^b7^c\mid N\) restricts exactly the coordinates with positive exponent, and its uniform density is \(1/m\).

Write \(E_3=A,E_5=B,E_7=C\), and set
\[
s_p=\sum_{j=1}^{E_p}p^{-j}=\frac{1-p^{-E_p}}{p-1},\qquad
q_p=1-s_p,\qquad t_p=\frac{s_p}{q_p}.
\]
Indeed, multiplying the sum by \(p-1\) gives the telescoping sum \(\sum_{j=1}^{E_p}(p^{1-j}-p^{-j})=1-p^{-E_p}\). Abbreviate \(x=s_3,y=s_5,z=s_7\). The sum \(S(N)\) of the reciprocals of all nontrivial divisors is
\[
S(N)=(1+x)(1+y)(1+z)-1=x+y+z+xy+xz+yz+xyz.
\]
As all three exponents grow, the sum increases to
\[
\frac32\frac54\frac76-1=\frac{105}{48}-1=\frac{19}{16}.
\]
Thus a hypothetical finite cover could spend strictly less than \(19/16-1=3/16=9/48\) on overlap. One may add an arbitrary class for each omitted nontrivial divisor of \(N\): this preserves distinctness and can only reduce the uncovered set. This observation will justify applying overlap tests to the full divisor family, even if the original family omitted a prime modulus.

## Prime-by-prime conditional proof

### Pure prime powers and the exact first stage

In the \(p\)-coordinate, let \(H_p\) be the complement of the chosen pure \(p\)-power classes. A class modulo \(p^j\) contains \(p^{E_p-j}\) of the \(p^{E_p}\) residues. There is at most one such class per \(j\), so the union bound gives \(\Pr(H_p)\ge 1-s_p=q_p\). Equality is attainable: for every \(1\le j\le E_p\), choose \(p^{j-1}\bmod p^j\). For \(j<k\), the class prescribed at level \(k\) is \(0\bmod p^j\), whereas the one at level \(j\) is not. Thus the classes are disjoint.

In particular, the minimum uncovered fraction after the \(3\)-stage and the maximum corresponding conditioning factor are exactly
\[
\min\Pr(H_3)=q_3=\frac{1+3^{-A}}2,\qquad
\max\frac{1}{\Pr(H_3)}=\frac{2}{1+3^{-A}}.
\]
This includes \(A=0\). The extremum is over all possible residue choices, not a random-choice estimate.

### Restricted-coordinate counting lemma

Let \(\nu_p\) be uniform measure conditioned on \(H_p\). For a class \(D\) modulo \(p^j\), \(j\ge1\),
\[
\nu_p(D)=\frac{\Pr(D\cap H_p)}{\Pr(H_p)}
 \le \frac{p^{-j}}{q_p}.
\]
Introduce these conditioned coordinates in the order \(3,5,7\), retaining their product measure. A mixed class with prime support \(J\) and exponents \(e_p\ge1\) has product-measure mass at most \(\prod_{p\in J}(p^{-e_p}/q_p)\): each restricted coordinate contributes its own factor, and an unrestricted coordinate contributes exactly \(1\). Distinctness gives at most one class per exponent tuple. Summing and factoring the finite sums gives the following bound for the entire block with support exactly \(J\):
\[
\sum_{\substack{\text{chosen classes}\\\text{with support }J}}\nu(\text{class})
\le\prod_{p\in J}\left(\sum_{e=1}^{E_p}\frac{p^{-e}}{q_p}\right)
=\prod_{p\in J}t_p.
\]
Since \(0\le s_p<1/(p-1)\), \(q_p>1-1/(p-1)>0\). It follows that \(t_p\le 1/(p-2)\), and hence \(t_3\le1,\ t_5\le1/3,\ t_7\le1/5\). Only the pure-coordinate conditioning events are treated as independent; the mixed classes are handled by a union bound.

### Introducing 5

In \(H_3\times H_5\), all pure classes have been avoided. The only remaining block at this stage is \(3^a5^b\) with \(a,b\ge1\); it removes at most \(t_3t_5\le1/3\) of the conditioned product. Multiplying the nonnegative conditional lower bound by the density of the product set gives the uniform uncovered fraction
\[
u_{35}\ \ge\ q_3q_5(1-t_3t_5)
=(1-x)(1-y)-xy=1-x-y>\frac14.
\]
The final strict inequality follows from \(x<1/2\) and \(y<1/4\).

In fact \(1-x-y\) is the exact finite minimum at this stage. For both \(p=3\) and \(p=5\), use \(P_{p,j}=p^{j-1}\bmod p^j\) for each pure class and reserve \(D_{p,j}=2p^{j-1}\bmod p^j\) for mixed classes. Within either coordinate all the \(P\)'s and \(D\)'s are mutually disjoint: different levels have different positions of the first nonzero base-\(p\) digit, and at the same level the digits are \(1\) and \(2\). For modulus \(3^a5^b\), choose the CRT class \(D_{3,a}\times D_{5,b}\). These rectangles are disjoint from the pure classes and from one another. They remove exactly \(\sum_{a,b\ge1}3^{-a}5^{-b}=xy\) in the indicated finite ranges, after the pure classes have left exactly \(q_3q_5\).

### Introducing 7

Extend to \(H_3\times H_5\times H_7\). The relative mass charged to the old \(\{3,5\}\) block does not change because it imposes no condition on the new coordinate. The new mixed supports are \(\{3,7\},\{5,7\},\{3,5,7\}\); their combined relative mass is at most
\[
t_3t_7+t_5t_7+t_3t_5t_7
\le \frac15+\frac1{15}+\frac1{15}=\frac13.
\]
Consequently all mixed classes together remove at most \(1/3+1/3=2/3\) of this product. Equivalently, if one renormalizes on the survivors of the old mixed block, the new mixed blocks can remove at most \((1/3)/(2/3)=1/2\) of those survivors. If \(U_N\) is the set missed by the full family, the uniform uncovered fraction satisfies
\[
\frac{|U_N|}{N}
\ge q_3q_5q_7\left(1-\frac23\right)
\;>\;\frac12\frac34\frac56\frac13=\boxed{\frac5{48}}.
\]
Strictness holds for every finite exponent triple because each \(q_p>(p-2)/(p-1)\). Thus no finite distinct covering system of the specified kind exists.

Keeping the finite coefficients gives a stronger bound for each \(N\). The bracket in the first line below is at least \(1/3\), so replacing the actual pure-product density by its lower bound does not reverse any inequality:
\[
\begin{aligned}
\frac{|U_N|}{N}
&\ge q_3q_5q_7(1-t_3t_5-t_3t_7-t_5t_7-t_3t_5t_7)\\
&=(1-x)(1-y)(1-z)-xy(1-z)-xz(1-y)-yz(1-x)-xyz\\
&=[1-x-y-z+xy+xz+yz-xyz]\\
&\quad-[xy+xz+yz-3xyz]-xyz\\
&=\boxed{\,1-x-y-z+xyz\,}.
\end{aligned}
\]
Neither this three-prime bound nor \(5/48\) is asserted to be the optimal uncovered density for arbitrary exponents. The first- and second-stage minima, by contrast, have explicit attaining constructions.

## Exact reciprocal-sum threshold

Let \(G_p(E)=1+s_p\). The condition \(S(N)\ge1\) is exactly \(G_3(A)G_5(B)G_7(C)\ge2\), and this product is increasing in each coordinate. The following bounds restrict all feasible triples, without any finite search cutoff.

- **The exponent of 3:** If \(A\le1\), the full product is at most \((4/3)(5/4)(7/6)=35/18<2\). Hence \(A\ge2\).
- **The exponent of 5:** If \(B=0\), the product is at most \((3/2)(7/6)=7/4<2\). Hence \(B\ge1\).
- **The exponent of 7:** If \(C=0\), the product is at most \((3/2)(5/4)=15/8<2\). Hence \(C\ge1\).

At the resulting floor \((2,1,1)\), \(S=(13/9)(6/5)(8/7)-1=208/105-1=103/105<1\). Each of its three immediate coordinate successors passes:

| \((A,B,C)\) | \(N\) | Product \(1+S(N)\) | \(S(N)\) |
|---|---:|---:|---:|
| \((3,1,1)\) | \(945\) | \((40/27)(6/5)(8/7)=1920/945\) | \(65/63\) |
| \((2,2,1)\) | \(1575\) | \((13/9)(31/25)(8/7)=3224/1575\) | \(1649/1575\) |
| \((2,1,2)\) | \(2205\) | \((13/9)(6/5)(57/49)=4446/2205\) | \(249/245\) |

Every feasible triple dominates the floor and differs from it in at least one coordinate. It therefore dominates at least one of these three successors; conversely any triple dominating a successor passes by monotonicity. The successors are incomparable, proving that the table is the complete list of coordinatewise-minimal triples. Its smallest period, \(945\), is the smallest feasible \(N\), since increasing an exponent increases \(N\).

## Exact coprime overlap and pruning

For a family of classes, define its waste to be the sum of the individual densities minus the density of their union. Adding a class \(D\) to an existing union \(V\) increases waste by \(\Pr(D)-\Pr(D\setminus V)=\Pr(D\cap V)\ge0\). For any subfamily with pairwise-coprime moduli \(T\), CRT gives an exact value, independent of residue choices:
\[
W(T)=\sum_{d\in T}\frac1d-\left(1-\prod_{d\in T}(1-1/d)\right).
\]
Indeed, the residues on these moduli are independent and uniform, as their product divides \(N\). For \(T=\{3,5,7\}\) the value is
\[
W(T)=\frac1{15}+\frac1{21}+\frac1{35}-\frac1{105}
=\frac{7+5+3-1}{105}=\frac2{15}.
\]
The subtraction is essential: summing pair intersections without correcting for the triple intersection overstates the forced waste. This is exact for the coprime subfamily, not an assertion of equality for the entire family.

In fact the available primes maximize \(W(T)\) over all single pairwise-coprime subfamilies of divisors of \(N\). If one density increases from \(u\) to \(v\), the waste increases by \((v-u)(1-\prod_{j\ne i}(1-u_j))\ge0\), where \(u_j\) are the other densities. Each \(d\in T\) can be replaced by a prime dividing it; these primes are distinct since the \(d\)'s are coprime, and the densities only increase. Adding any remaining prime divisors of \(N\) also only increases waste, by increasing a density from zero. Thus \(2/15\), when all three primes divide \(N\), cannot be improved just by picking a different pairwise-coprime \(T\).

After adjoining omitted divisor classes, the uncovered density is therefore at least the signed gap \(1-S(N)+W(T)\). A positive gap rules out a cover; a zero or negative gap from this test alone is inconclusive. The last column applies the stronger conditional bound proved above.

| \((A,B,C)\) | \(N\) | Prime-only gap \(1-S(N)+2/15\) | Residues missed, prime-only test | Residues missed, conditional test |
|---|---:|---:|---:|---:|
| \((3,1,1)\) | \(945\) | \(32/315\) | at least \(96\) | at least \(179\) |
| \((2,2,1)\) | \(1575\) | \(136/1575\) | at least \(136\) | at least \(296\) |
| \((2,1,2)\) | \(2205\) | \(86/735\) | at least \(258\) | at least \(456\) |
| \((3,2,2)\) | \(33075\) | \(-8/2205\) | inconclusive | at least \(4436\) |

There is also an exact minimum waste for the subfamily of all available pure prime powers. Its total individual density is \(x+y+z\); independence across the coordinates and the one-coordinate lemma show that its maximum possible union density is \(1-(1-x)(1-y)(1-z)\). The disjoint choices \(P_{p,j}\) attain that maximum simultaneously. Therefore
\[
W_{\rm pure}^{\min}=x+y+z-1+(1-x)(1-y)(1-z)=xy+xz+yz-xyz.
\]
This gives a second, shorter proof of noncoverage even if all mixed classes are granted their full raw densities. For the saturated divisor family, and hence as an uncovered-density lower bound for any subfamily,
\[
\begin{aligned}
1-S(N)+W_{\rm pure}^{\min}
&=1-[x+y+z+xy+xz+yz+xyz]+[xy+xz+yz-xyz]\\
&=1-x-y-z-2xyz\\
&>1-\tfrac12-\tfrac14-\tfrac16-2(\tfrac12)(\tfrac14)(\tfrac16)
=\tfrac1{24}.
\end{aligned}
\]
At the infinite-budget endpoint the forced pure-power waste is \(1/8+1/12+1/24-1/48=11/48\), larger than the allowed \(9/48\). The finite identity, rather than a comparison of limits alone, justifies the exclusion for every triple.

## Integer certificate for Lean 4

Set \(n_p=p^{E_p}\), \(k_p=\sum_{j=1}^{E_p}p^{E_p-j}=(n_p-1)/(p-1)\), and \(\ell_p=n_p-k_p\). The pure complement \(H_p\) has at least \(\ell_p\) elements, so choose any subset \(R_p\subseteq H_p\) of exactly that size. This permits a formalization with finite sets and natural-number cardinalities, with no probability measure or infinite series.

In \(R_3\times R_5\times R_7\), a class with support \(\{3,5\}\) contributes at most \(3^{A-a}5^{B-b}\ell_7\) elements. Summing gives \(k_3k_5\ell_7\); the analogous bounds for the other pairs are \(k_3k_7\ell_5\) and \(k_5k_7\ell_3\). The three-prime block contributes at most \(k_3k_5k_7\). Counting the union of these blocks and the globally uncovered residues yields
\[
|U_N|+k_3k_5\ell_7+k_3k_7\ell_5+k_5k_7\ell_3+k_3k_5k_7
\ \ge\ \ell_3\ell_5\ell_7.
\]
Using \(n_p=k_p+\ell_p\), distributivity gives the equivalent subtraction-free target
\[
\boxed{|U_N|+k_3n_5n_7+n_3k_5n_7+n_3n_5k_7
\ \ge\ N+k_3k_5k_7.}
\]
Dividing by \(N\) recovers \(1-x-y-z+xyz\), since \(s_p=k_p/n_p\). These are mathematical lemmas prepared for formalization, not a claim that a Lean proof has been kernel-checked.

## Running the verifier

The companion file `smooth_cover_check.py` requires only Python 3.10 or newer and uses `fractions.Fraction` for every density. The default command proves the completeness of the exponent list by the floor-and-successors certificate, not by extrapolating from a scan.

```bash
python3 smooth_cover_check.py
python3 smooth_cover_check.py --self-test --triple 3 2 2
python3 smooth_cover_check.py --coprime 9 25 7
python3 smooth_cover_check.py --scan 4 2 2
```

The self-test compares the factored divisor sums with direct enumeration on \(0\le A,B,C\le3\), verifies the rational identities, and independently exhausts all residue choices for \(N=105\) up to translation. In the last check exactly \(35\) missed residues is attainable and no assignment does better; it checks a finite instance, not the universal conclusion.
