# Sharp three-prime covering densities and the obstruction modulo 9

The infimum of the uncovered fraction for distinct \(\{3,5,7\}\)-smooth moduli is \(53/432\), not \(5/48\). Every finite family misses strictly more; explicit families approach the infimum. This limiting constant and sharp counts at 315 and 945 are also recorded in the [TrureTuring research report, CM1–CM11](https://github.com/the-omega-institute/trureturing-experiments/blob/main/docs/reports/erdos7-odd-covering/problem-details/02-current-bounds-and-comparisons.md). The argument below gives a finite-height identity for every \(\{3,p,q\}\) with \(5\le p<q\), a matching CRT construction, and a two-level test that still gives a positive quantitative bound for the five smallest odd primes. No priority claim is made.

## Exact finite-height theorem

Let \(5\le p<q\) be odd primes. In a period \(N=3^A p^B q^C\) choose at most one class for every divisor \(m>1\). Write \(u_{\min}(N)\) for the smallest fraction missed over all assignments, and set
\[
x=\frac{1-3^{-A}}2,\qquad
y=\frac{1-p^{-B}}{p-1},\qquad
z=\frac{1-q^{-C}}{q-1}.
\]
These are the finite sums of the reciprocals of the positive powers in their respective coordinates. Modulus \(1\) is never allowed. Omitting moduli cannot improve coverage, so for the minimum one may assign a class to every nonunit divisor.

**Theorem.** For every \(A,B,C\ge0\),
\[
\boxed{u_{\min}(N)=1-x-y-z+(x+\kappa_A)yz,\qquad
\kappa_A=
\begin{cases}
0 & A=0,1,\\
1/3 & A=2,\\
4/9 & A\ge3 .
\end{cases}}
\]
In particular, the exact infimum over all heights for this prime set is
\[
\frac12-\frac1{p-1}-\frac1{q-1}
  +\frac{17}{18(p-1)(q-1)}.
\]
For \(p=5,q=7\) this is \(5/48+(4/9)(1/4)(1/6)=53/432\). Some finite controls are \(35\) missed out of \(105\), \(74\) out of \(315\), \(191\) out of \(945\), and \(5012\) out of \(33075\); these are minima, not just counts for one assignment.

There is an equivalent exact statement about waste when all nonunit divisors are used. Their total mass is \((1+x)(1+y)(1+z)-1=x+y+z+xy+xz+yz+xyz\); their maximum union mass is \(1-u_{\min}=x+y+z-xyz-\kappa_Ayz\). Subtraction gives minimum waste \(xy+xz+yz+2xyz+\kappa_Ayz\). For \(3,5,7\) its limit is \(1/8+1/12+1/24+1/24+1/54=67/216\). This exceeds the limiting allowed waste \(19/16-1=3/16\) by exactly \(67/216-3/16=53/432\). The waste identity is not asserted for subfamilies that omit moduli.

### What the small moduli force

- **Distinctness:** For fixed ternary depth \(a\), the classes \(3^a p^b\), \(b\ge1\), have total available \(p\)-coordinate mass at most \(y\). Two classes of the same modulus would invalidate this accounting.
- **The classes modulo 3 and 9:** The \(9\)-class either lies inside the \(3\)-class and adds nothing, or removes a full one of the three mod-\(9\) children of another mod-\(3\) residue. Similarly, the \(15\)- and \(21\)-classes intersect in one class modulo \(105\) if their mod-\(3\) residues agree, and are disjoint otherwise. When both avoid the pure \(3\)-class and occupy different branches, a nonnested \(9\)-class meets one of them in a class modulo \(45\) or \(63\).
- **The classes modulo 5, 7, and 35:** At period \(105\), translate the three prime residues to zero. The \(15,21,35\) classes can have CRT coordinates \((1,1,*),(2,*,1),(*,2,2)\), respectively. Outside the prime classes these remove \(6,4,2\) disjoint points; a \(105\)-class removes one more. Thus \(48-6-4-2-1=35\) points remain, attaining the old bound at this height. One must not charge a collision between these mixed classes just because their moduli share a prime.
- **Parity:** There is no independent even/odd loss for these moduli. Translation by the odd period exchanges the two parities in a doubled period and preserves all the classes. The obstruction is the limited space in the ternary coordinate, not parity of the integers being covered.

### Proof of the lower bound

Use unconditional counting on the CRT product. In each coordinate the pure classes have union of density at most the corresponding sum \(x,y,z\). Enlarge these unions within their own coordinates to exactly these densities. This is possible because, for example, \(3^Ax\) is an integer. Write \(R_3,R_p,R_q\) for the complements, of densities \(1-x,1-y,1-z\).

In \(R_3\times R_p\times R_q\) charge each mixed class at most its raw density times the survivor densities in the coordinates it does not restrict. By the union bound this gives
\[
F_0=(1-x)(1-y)(1-z)
-xy(1-z)-xz(1-y)-yz(1-x)-xyz
=1-x-y-z+xyz .
\]
If \(A\le1\) or \(yz=0\), this is the asserted lower bound. Assume henceforth \(A\ge2\), \(yz>0\). Improve the charge for just two groups: \(3^a p^b\) and \(3^a q^c\) with \(a=1,2\) and \(b,c\ge1\). All other charges are left unchanged.

Fix a ternary coordinate \(v\in R_3\). The first group's \(p\)-coordinate union inside \(R_p\) has density at most
\[
f(v)=\sum_{a=1}^2\sum_{b=1}^B p^{-b}\,\mathbf1_{I_{ab}}(v),
\]
where \(I_{ab}\) is the ternary cylinder chosen for that modulus. Define \(g(v)\) analogously for the second group. The bound on the combined two-dimensional section is
\[
f(v)(1-z)+g(v)(1-y)-f(v)g(v).
\]
Indeed, for the actual projected union sizes this is the exact row-plus-column union formula. It increases in both arguments up to the displayed majorants, since \(f\le 2y\le1-y\) and \(g\le2z\le1-z\). All section sizes are absolute coordinate densities; they are summed over \(R_3\), not renormalized.

For fixed \(R_3\) and fixed \(q\)-placements, the integral of this expression is linear in the \(p^{-b}\)-weights assigned to the ternary cells at each of the two depths. Moving each depth's whole weight \(y\) to a single maximizing cell cannot decrease the upper bound. The same operation then works for the \(q\)-weights. Thus it suffices to consider one coarse cell modulo 3 and one fine cell modulo 9 for each of \(p,q\). They may be placed outside the blocked pure \(3\)-class, since moving a weight out of a blocked cell cannot decrease this monotone bound.

Set \(U=(1-z)/z\), \(V=(1-y)/y\). We have \(U\ge V\ge3\): \(V\le p-1\), whereas \(U\ge q-2\ge p\). On an available mod-\(9\) cell let \(n_p,n_q\in\{0,1,2\}\) count its two possible incidences for each group. In units of \(yz\) its score is
\[
U n_p+V n_q-n_p n_q .
\]
Measure ternary lengths in units of one mod-\(9\) cell. The six cells outside the blocked coarse branch contain \(R_3\), of total length
\[
9(1-x)=4+\theta,\qquad
\theta=\frac12+\frac{9}{2\cdot3^A}.
\]
Before charging any collision the score was \(4(U+V)\): one coarse cell of length 3 and one fine cell of length 1 for each group. The following two cases bound its true value on \(R_3\).

- **Same coarse branch:** Its three cells each start at \(U+V-1\). An outside cell can never exceed that score, even with both fine placements, so the maximum can be evaluated by including all three coarse cells. Placing both fine cells inside adds at most \(U+V-2\); placing one inside and one outside, or both on the same outside cell, adds at most \(U+V-1\). Placing them on distinct outside cells adds at most \(U+\theta V\), because only \(1+\theta\) outside cell units remain. The score is therefore at most \(3(U+V-1)+\max(U+V-1,U+\theta V)\).
- **Different coarse branches:** The total starting score on all six cells is \(3U+3V\), and \(2-\theta\) cell units of score at least \(V\) must be omitted. The two fine placements add at most \(U+V\). The score is therefore at most \(4(U+V)-(2-\theta)V\).

For \(A\ge3\), \(\theta\le2/3\), so \((1-\theta)V\ge1\) and \((2-\theta)V\ge4\). Both cases lose at least \(4\) score units. For \(A=2\), \(\theta=1\): the first case loses at least \(3\) units and the second loses at least \(V\ge3\). A score unit contributes unconditional density \(yz/9\). The extra loss relative to \(F_0\) is therefore at least \(\kappa_A yz\), as claimed.

### Construction attaining the finite bound

For a prime \(s\), write \([k]_{s,j}=k s^{j-1}\pmod {s^j}\), \(1\le k<s\). In a fixed coordinate, these classes are disjoint for different \((k,j)\): the first nonzero digit has position \(j\) and value \(k\). Call \(k\) its color. Use color \(1\) for all pure classes. Write \(T_a=[2]_{3,a}\).

Choose the mixed classes by the following table. An asterisk is an unrestricted coordinate. Within each row, use every exponent in range and the unique class specified by CRT.

| Modulus | 3-coordinate | \(p\)-coordinate | \(q\)-coordinate |
|---|---|---|---|
| \(3^a p^b\) | \(I_a\) | \([k_a]_{p,b}\) | \(*\) |
| \(3^a q^c\) | \(J_a\) | \(*\) | \([l_a]_{q,c}\) |
| \(p^b q^c\) | \(*\) | \([4]_{p,b}\) | \([4]_{q,c}\) |
| \(3^a p^b q^c\) | \(T_a\) | \([4]_{p,b}\) | \([5]_{q,c}\) |

Take \(k_a=2\), except that \(k_2=3\) when \(A\ge3\). Take \(l_a=2\) for \(a\le2\) and \(l_a=3\) for \(a\ge3\). The ternary choices are:

- **\(A=0,1\):** At \(A=0\) the ternary rows are empty. At \(A=1\), take \(I_1=T_1\) and \(J_1=0\bmod3\); they are disjoint and avoid the pure class \(1\bmod3\).
- **\(A=2\):** Take \(I_1=J_1=T_1\), \(I_2=0\bmod9\), and \(J_2=6\bmod9\). Only \(I_1,J_1\) intersect across the two rows.
- **\(A\ge3\):** Take \(I_1=J_1=T_1\), \(I_2=2\bmod9\), and \(J_2=T_2=6\bmod9\). For \(a\ge3\), take \(I_a=T_a\) and \(J_a=6+3^{a-1}\bmod 3^a\). The latter cells are mutually disjoint inside \(T_2\). Across the two rows the only intersections are \(I_1\cap J_1=T_1\) and \(I_2\cap J_1=I_2\).

All constrained coordinates avoid their own pure classes, so every individual charge in \(F_0\) is attained inside the pure-survivor product. Within a row, a ternary nesting is separated by different \(p\)- or \(q\)-colors. The last two rows avoid the first two by their colors, and avoid each other by their \(q\)-colors. The only duplicate charges are consequently the listed cross-row overlaps, of total mass \(0\), \(yz/3\), or \((1/3+1/9)yz\). In the last case the two intersections are disjoint because they use different \(p\)-colors. This proves equality, including when an exponent range is empty.

The minimum is nonincreasing when heights increase: old assignments are still available. Taking a cofinal sequence of heights tending to infinity therefore gives the claimed infimum. It is unattained by any finite family: it is positive, and one can add a fresh smooth multiple of the period with its class entirely inside a missed residue, decreasing the uncovered density strictly.

As a contrast, for three distinct primes all at least \(5\), the uncorrected formula \(F_0\) is already sharp. Give each support containing a fixed prime its own color in that coordinate; there are only four such supports and at least four colors. Any two mixed supports share a coordinate and have different colors there, so no mixed overlap inside the pure-survivor product is necessary.

## Four primes and the general test

For a finite odd support \(S\), put \(x_s=1/(s-1)\), \(q_s=1-x_s\), \(t_s=x_s/q_s=1/(s-2)\), \(Q=\prod_{s\in S}q_s\). These endpoint capacities give a bound independent of exponents. For finite-height versions use \(x_s=\sum_{j=1}^{E_s}s^{-j}\) instead. To realize endpoint padding using only finite unconditional counting, adjoin an independent uniform dummy coordinate of size \(s-1\) to each prime coordinate. Then a pure union can be enlarged to density exactly \(x_s\) without changing any actual class probability; the surviving set \(R_s\) has density \(q_s\).

Charging a mixed support \(J\) by its full raw density gives the lower bound \(G_{\rm raw}=Q-[\prod(1+x_s)-1-\sum x_s]\). Charging only what enters the survivor product gives
\[
G_0=Q\left[1-\sum_{|J|\ge2}\prod_{s\in J}t_s\right]
=Q\left[2+\sum_s t_s-\prod_s(1+t_s)\right].
\]
Indeed, the unconditional charge for a support \(J\) is \(\prod_{s\in J}x_s\prod_{s\notin J}q_s\). The endpoint sign criterion is the classical Berger–Felzenbaum–Fraenkel obstruction as stated in [Guo and Sun’s introduction](https://arxiv.org/html/math/0412217).

| Prime support | Pure CRT, mixed at raw density | Pure CRT, mixed restricted to survivor product | Two-level ternary test |
|---|---:|---:|---:|
| \(3,5,7\) | \(1/24\) | \(5/48\) | \(53/432\), sharp infimum |
| \(3,5,7,11\) | \(-13/120\) | \(1/40\) | \(59/1080\) |
| \(3,5,7,11,13\) | \(-239/960\) | \(-71/1920\) | \(13/12960\) |
| \(3,5,7,11,13,17\) | \(-2807/7680\) | \(-83/1024\) | \(-6217/165888\) |

Negative entries are signed estimates, not evidence of a cover. Before using CRT at all, the ordinary reciprocal sum is at most \((3/2)(5/4)-1=7/8\) for two odd primes, but reaches a supremum of \(19/16\) for the first three. The uncut mixed test first fails on the fourth smallest prime; the product-restricted test first fails on the fifth. More precisely, appending a prime \(r\) to \(3,5,7,11\) changes the bracket in \(G_0\) to \(4/45-23/[9(r-2)]\). Thus that elementary bound still works for \(r\ge31\), but not for \(r=13,17,19,23,29\). Noncoverage for support size at most five is already a classical consequence of [Berger, Felzenbaum and Fraenkel, Part II](https://geodesic.mathdoc.fr/articles/10.4064/aa-48-1-73-79/); see the [six-prime corollary and its provenance](https://erdosproblems.ai/wiki/library/covering_systems/berger_1987_necessary_condition_odd_covering_systems_ii).

### Two-level lemma for several satellite primes

Suppose \(S=\{3\}\cup T\) with every \(s\in T\) at least 5. Consider only the classes \(3^a s^b\), \(a=1,2\), \(b\ge1\), and keep the old charges on everything else. Normalize the blocked mod-\(3\) residue to 0, adjoining its class first if necessary; one may lift to a common period divisible by 9 without changing densities. For each \(s\), give its two levels one coarse cell \(i_s\in\{1,2\}\) and one fine cell \(j_s\in C=\{1,2,4,5,7,8\}\). Define
\[
n_s(r)=\mathbf1_{r\equiv i_s\ (3)}+\mathbf1_{r=j_s},\quad
D=\prod_{s\in T}(s-2),\quad
h(r)=D-\prod_{s\in T}(s-2-n_s(r)).
\]
Sort the six scores as \(h_1\ge\cdots\ge h_6\). Let \(M_T\) be the maximum of \(2(h_1+h_2+h_3+h_4)+h_5\) over the \(12^{|T|}\) placements. With \(Q_T=\prod_{s\in T}q_s\), the resulting unconditional bound is
\[
\boxed{G_2=G_0+Q_T\left(\frac49\sum_{s\in T}t_s-\frac{M_T}{18D}\right).}
\]

To prove it, fix a ternary point. Each satellite group's classes restrict just its own remaining coordinate. If their actual projected sizes are \(f_s\), their union section has size \(Q_T[1-\prod_s(1-f_s/q_s)]\). Replacing \(f_s\) by the sum of its active \(s^{-b}\)-weights only increases this expression, because \(2t_s\le 2/3\). It is affine in one satellite's allocations when the rest are fixed. Just as in the two-group proof, concentrate each depth on one maximizing cell, giving \(f_s=x_s n_s(r)\) in the bound. Only \(4.5\) mod-\(9\) cell units can belong to \(R_3\), so the largest integral is bounded by the top four cells and half the fifth. The old charge for these groups was \(Q_T(4/9)\sum t_s\); replacing it proves the lemma.

For \(T=(5,7),(5,7,11),(5,7,11,13),(5,7,11,13,17)\), the respective pairs \((D,M_T)\) are \((15,56),(135,568),(1485,6767),(22275,106775)\). For the five-prime case the improvement is \(1969/51840\), exceeding the previous shortfall \(71/1920=1917/51840\) by exactly \(13/12960\). Here is the entire finite integer calculation for these auxiliary maxima. The coverage result is uniform in all exponents because the lemma, not an exponent cutoff, reduces the calculation to these cells.

```python
from itertools import product
from math import prod

def score(T):
    C = (1, 2, 4, 5, 7, 8)
    rows = [tuple(int(r % 3 == i) + int(r == j) for r in C)
            for i, j in product((1, 2), C)]
    D, best = prod(s-2 for s in T), 0
    for layout in product(rows, repeat=len(T)):
        h = sorted((D - prod(s-2-n for s, n in zip(T, column))
                    for column in zip(*layout)), reverse=True)
        best = max(best, 2*sum(h[:4]) + h[4])
    return D, best
```

This also yields noncoverage for every set of at most five odd primes. When 3 is present, the total upper charge divided by \(Q\) is increasing in each satellite \(t_s\): the nonselected terms are nonnegative monomials (for remaining \(3^a s^b\), \(a\ge3\), the coefficient is \(t_s/9\)), and each selected section \(1-\prod_s(1-n_s t_s)\) is increasing. The worst four satellites are therefore \(5,7,11,13\); missing satellites may be appended. When 3 is absent the worst five primes \(5,7,11,13,17\) already leave \(1415/9216\) by the ordinary reciprocal sum alone. This is a quantitative derivation, not a claim to improve the published prime-count restriction.

### Further gains from disjoint supports at four and five primes

For \(S=\{3,5,7,11\}\), improve the two-level estimate to \(239/4320\). For each satellite \(s\), pair the as-yet-uncombined \(3^a s^b\) block with \(a\ge3\) with the block supported exactly on the other two primes \(v,w\). These two events involve disjoint coordinates; the three pairings use disjoint lists of moduli, none already jointly charged by the two-level test.

Here is the correction without any pairwise-overlap overcounting. In two disjoint coordinate products of survivor masses \(u,v'\), if the event sizes are bounded by \(d\le u\) and \(e\le v'\), their combined mass is at most \(dv'+eu-de\). This follows from the rectangle formula, increasing in each size on those intervals. For the indicated blocks \(d=(\sum_{a\ge3}3^{-a})x_s=x_s/18\), \(e=x_vx_w\). Hence each pairing saves \(de=1/4320\). Summing the three separate gains gives \(59/1080+3/4320=239/4320\). No sharpness is claimed for this four-prime constant or for the five-prime bound.

For the five smallest odd primes, put \(T=\{5,7,11,13\}\), \(P=\prod_{s\in T}x_s=1/(4\cdot6\cdot10\cdot12)=1/2880\). The six supports consisting of two satellites partition into three pairs of complementary supports. Neither event in such a pair uses the ternary coordinate; the rectangle correction on that coordinate's survivor is \(q_3P=P/2=1/5760\) per pair. Next, for each of the four \(s\in T\), pair the high-ternary block \(3^as^b\), \(a\ge3\), with the block supported exactly on the other three satellites. Their rectangle correction is \(P/18=1/51840\) per pair. The seven pairings use disjoint lists of moduli, and none of these lists was jointly charged by the two-level test. The resulting bound is
\[
\frac{13}{12960}+\frac{3}{5760}+\frac{4}{51840}
=\frac{52+27+4}{51840}=\boxed{\frac{83}{51840}} .
\]

## A necessary constraint on the nonsmooth part of a full cover

Let \(H\) be the residues missed by the \(\{3,5,7\}\)-smooth subfamily of a hypothetical odd cover. Work in the smooth part of the lcm of the entire family, so outside moduli can be projected to this same group. Write \(h=\Pr(H)>53/432\). Factor every nonsmooth modulus as \(m=s_m r_m\), where \(s_m\) is smooth, \(r_m>1\), and \(\gcd(r_m,105)=1\).

**Lemma (outside capacity on the missed residues).** For every \(v\in H\),
\[
\sum_{\substack{m\ {\rm nonsmooth}\\v\equiv a_m\pmod{s_m}}}\frac1{r_m}\ge1 .
\]
Indeed, fix \(v\) and vary all outside coordinates. The indicated classes are the only ones available; each occupies exactly \(1/r_m\) of that fiber. Averaging the inequality on the original smooth group yields
\[
h\le\sum_{m\ {\rm nonsmooth}}\frac{\Pr(H\cap[a_m]_{s_m})}{r_m}
\le\sum_{m\ {\rm nonsmooth}}\frac{\min(h,1/s_m)}{r_m}.
\]
In particular \(\sum_{m\ {\rm nonsmooth}}1/m>53/432\), and the shape-sensitive necessary test is
\[
\boxed{\sum_{m\ {\rm nonsmooth}}\frac1{r_m}
\min\!\left(1,\frac{432}{53s_m}\right)\ge1.}
\]
The finite-height value \(u_{\min}\) may replace \(53/432\) for a specified head. An outside-only modulus cannot spend all its raw density on smooth holes: it hits them in exactly their original proportion. This is why the fiber constraint can detect a failure that the reciprocal sum alone misses.

There is also a two-sided version. Let \(K\) be the holes in the outside coordinates for the subfamily with \(s_m=1\), and let \(k=\Pr(K)\). Only crossing moduli, those with both \(s_m,r_m>1\), can cover \(H\times K\). CRT factors the intersection of a crossing class with this product into its separate intersections with \(H\) and \(K\), giving the unconditional inequalities
\[
hk\ \le\ \sum_{m\ {\rm crossing}}\min(h,1/s_m)\min(k,1/r_m)
\ \le\ \sum_{m\ {\rm crossing}}\frac1m .
\]
In particular at least one crossing modulus is necessary: \(h>53/432\), and \(k>0\) because a finite distinct family of odd outside-only moduli, all coprime to 3, cannot itself cover by [Hough and Nielsen, Theorem 1](https://arxiv.org/html/1703.02133). This conclusion concerns a prime from the head and a prime from outside in the same modulus, not just both types appearing in the lcm.

## What remains

The three-prime optimization above is sharp and needs no conjecture. The four- and five-prime estimates are one-sided. For six primes, a concrete next test is to optimize the \(3^a s^b\) and \(5^b s^c\) blocks jointly on the \(9\times25\) residue grid, assigning each modulus to exactly one block; the two-level test gives a signed deficit \(6217/165888\) to overcome for the six smallest primes. A gain of that size has not been proved here, and separately estimated discounts on overlapping lists of moduli must not simply be added.

No positive uncovered constant can hold uniformly for all finite odd supports: the classes \(0\bmod p\) for odd primes \(p\le X\) alone leave \(\prod_{3\le p\le X}(1-1/p)\). The reciprocal product dominates \(\sum_{n\le X,\ n\ {\rm odd}}1/n\), which diverges. Thus even a proof of general noncoverage would have to allow its density guarantee to tend to zero; none of the negative certificate values above is a counterexample to the [unrestricted Erdős–Selfridge problem](https://www.erdosproblems.com/7).
