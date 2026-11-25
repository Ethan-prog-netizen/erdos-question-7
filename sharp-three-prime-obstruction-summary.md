 # The sharp \(\{3,5,7\}\)-smooth obstruction

Every finite family of distinct \(\{3,5,7\}\)-smooth moduli greater than one leaves **strictly more than \(53/432\)** of the integers uncovered. This improves \(5/48\) by exactly \(1/54\), and no larger uniform constant is possible. The limiting value and the sharp counts at periods \(315\) and \(945\) are also recorded in the [TrureTuring research report](https://github.com/the-omega-institute/trureturing-experiments/blob/main/docs/reports/erdos7-odd-covering/problem-details/02-current-bounds-and-comparisons.md). The attached **Sharp three-prime covering densities and the obstruction modulo 9** gives the finite-height proof, an attaining construction, and the four- and five-prime extensions.[30]

## Exact theorem and tight examples

Let \(N=3^A p^B q^C\), where \(5\le p<q\) are primes. Write \(u_{\min}(N)\) for the minimum uncovered fraction when at most one residue class is used for each divisor \(m>1\) of \(N\). Set
\[
x=\frac{1-3^{-A}}2,\qquad
y=\frac{1-p^{-B}}{p-1},\qquad
z=\frac{1-q^{-C}}{q-1}.
\]
Then the exact answer, including zero exponents, is
\[
\boxed{
u_{\min}(N)=1-x-y-z+(x+\kappa_A)yz,\qquad
\kappa_A=
\begin{cases}
0&A=0,1,\\
1/3&A=2,\\
4/9&A\ge3.
\end{cases}}
\]

For \(p=5,q=7\), the minimum numbers missed at periods \(105,315,945\) are respectively \(35,74,191\). At \(105\), the old bound is already sharp: after the pure \(3,5,7\) classes leave \(48\) points, the \(15,21,35,105\) classes can remove \(6,4,2,1\) disjoint points. Thus a proof that charges an unavoidable collision between the \(15\)- and \(21\)-classes alone would be false. The improvement begins at period \(315\), when the modulus \(9\) enters.

## Why the extra loss is forced

All densities here are unconditional on \(\mathbb Z/N\mathbb Z\). Enlarge the pure-class unions in their own coordinates to densities \(x,y,z\). Charging each mixed class only inside the product of the three surviving sets gives
\[
\begin{aligned}
F_0
&=(1-x)(1-y)(1-z)-xy(1-z)-xz(1-y)-yz(1-x)-xyz\\
&=1-x-y-z+xyz.
\end{aligned}
\]
This is the bound whose limit is \(5/48\). Its precise defect is that it charges the families \(3^ap^b\) and \(3^aq^c\) separately even at the two ternary depths \(a=1,2\).

Fix a ternary residue. If these two families occupy absolute coordinate densities \(f,g\) in the surviving \(p,q\) coordinates, their combined section has density
\[
f(1-z)+g(1-y)-fg.
\]
Distinctness limits each depth’s available weights to \(y\) and \(z\). The expression is increasing up to the resulting majorants \(f\le2y,\ g\le2z\), and is affine in either family’s allocations with the other fixed. Thus, to upper-bound coverage, one can concentrate each family on one cell modulo \(3\) and one cell modulo \(9\). This is a reduction to four placements, not an assumption that the original classes were aligned.

For \(A\ge2\) and \(yz>0\), put
\[
U=(1-z)/z,\qquad V=(1-y)/y,\qquad \theta=9(1-x)-4.
\]
Here \(U\ge V\ge3\). Six cells modulo \(9\) lie outside the pure \(3\)-class, but the ternary survivor occupies only \(4+\theta\) cell units. Measure the overcharge in units of \(yz/9\).

- **Same coarse cell:** The three common ninths already cost three units of overlap. Avoiding a fourth unit requires putting the two fine cells separately outside that branch, where only \(1+\theta\) cell units remain after retaining the coarse branch. The loss is at least \(\min\{4,\,3+(1-\theta)V\}\).
- **Different coarse cells:** All six ninths have initial score at least \(V\), and \(2-\theta\) cell units must be omitted. The fine placements cannot add more than their original charges, so the loss is at least \((2-\theta)V\).

At \(A=2\), \(\theta=1\), so either case loses at least \(3yz/9=yz/3\). At \(A\ge3\), \(\theta\le2/3\), so either loses at least \(4yz/9\). There is no separate parity penalty: translation by the odd period exchanges parities without changing membership in any class.

**Sharpness is constructive.** For \(A\ge3\), put both coarse families on \(2\bmod3\), and their fine families on \(2\bmod9\) and \(6\bmod9\), respectively. The construction in the attachment assigns every remaining modulus so that the only additional duplicate charges have disjoint masses \(yz/3\) and \(yz/9\). Taking all heights to infinity therefore gives exactly
\[
\frac5{48}+\frac49\cdot\frac14\cdot\frac16
=\frac5{48}+\frac1{54}
=\frac{53}{432}.
\]
No finite family attains this limit: a fresh smooth multiple of its period can place a new class entirely inside one missed residue.

## Where the method stops for more primes

For an odd prime support \(S\), put \(x_s=1/(s-1)\), \(q_s=1-x_s\), \(t_s=x_s/q_s=1/(s-2)\), and \(Q=\prod_{s\in S}q_s\). Charging each mixed support only inside the pure-survivor product gives the exponent-independent lower bound
\[
G_0=Q\left[2+\sum_{s\in S}t_s-\prod_{s\in S}(1+t_s)\right].
\]
Its sign criterion is the classical [Berger–Felzenbaum–Fraenkel obstruction stated by Guo and Sun](https://arxiv.org/html/math/0412217). The following are unconditional lower bounds; a negative entry means that estimate is inconclusive.[2]

| Prime support | Pure CRT, mixed classes at raw density | Mixed classes restricted to pure survivors | After additional overlaps |
|---|---:|---:|---:|
| \(3,5,7\) | \(1/24\) | \(5/48\) | \(53/432\), sharp infimum |
| \(3,5,7,11\) | \(-13/120\) | \(1/40\) | \(239/4320\) |
| \(3,5,7,11,13\) | \(-239/960\) | \(-71/1920\) | \(83/51840\) |
| \(3,5,7,11,13,17\) | \(-2807/7680\) | \(-83/1024\) | Inconclusive: the two-level score is \(-6217/165888\) |

The distinction is important. **Four primes do not require a new collision lemma merely to prove noncoverage:** restricting mixed classes to the pure survivors already leaves \(1/40\). At the five smallest primes, that argument genuinely fails. Optimizing the first two ternary depths recovers \(1969/51840\), more than the shortfall \(71/1920=1917/51840\); pairing further blocks on disjoint coordinate sets raises the result from \(52/51840\) to \(83/51840\). The attachment gives the finite integer maximization behind the two-level calculation. Neither the four- nor five-prime constant is claimed sharp, and qualitative five-prime noncoverage was already proved by [Berger, Felzenbaum and Fraenkel](https://geodesic.mathdoc.fr/articles/10.4064/aa-48-1-73-79/).[13]

## A necessary condition on the nonsmooth moduli

Let \(H\) be the residues missed by the smooth subfamily of a hypothetical full odd cover, with density \(h>53/432\). Factor each nonsmooth modulus as \(m=s_mr_m\), with \(s_m\) its \(\{3,5,7\}\)-smooth part and \(\gcd(r_m,105)=1\). For **every** \(v\in H\), only classes matching \(v\bmod s_m\) can help, and each covers exactly \(1/r_m\) of the outside coordinates. Hence
\[
\sum_{\substack{m\ {\rm nonsmooth}\\v\equiv a_m\pmod{s_m}}}\frac1{r_m}\ge1.
\]
Summing over the original smooth group, without renormalizing its measure, gives
\[
h\le\sum_{m\ {\rm nonsmooth}}
\frac{\Pr(H\cap[a_m]_{s_m})}{r_m}
\le\sum_{m\ {\rm nonsmooth}}\frac{\min(h,1/s_m)}{r_m}.
\]
Thus the nonsmooth moduli need reciprocal mass strictly greater than \(53/432\), but mass alone is not enough: it must reach the particular smooth residues that were missed.

There is also a divisibility consequence. Let \(K\) be the holes left by moduli entirely coprime to \(105\), and let \(k\) be their density. Then \(k>0\) by [Hough and Nielsen’s theorem](https://arxiv.org/html/1703.02133), since those odd moduli are all coprime to \(3\). Only moduli with **both** \(s_m>1\) and \(r_m>1\) can cover \(H\times K\), so CRT gives[79]
\[
0<hk\le
\sum_{\substack{m\\s_m,r_m>1}}
\min(h,1/s_m)\min(k,1/r_m).
\]
In particular, a hypothetical odd cover must put a prime from \(\{3,5,7\}\) and a prime outside that set **in the same modulus**. Merely having both kinds of primes in the lcm does not suffice.

## Next proof strategy, not a proved bound

For the six smallest odd primes, the concrete next test is to optimize the low \(3\)- and \(5\)-power placements jointly on the \(9\times25\) grid. The two-level method leaves an exact deficit of \(6217/165888\) to overcome. The key is to assign each modulus to one jointly optimized block: independently computed discounts for the ternary and quinary grids cannot simply be added when they charge the same classes. This is a target for extending the argument, not a claim about the resolution of the [unrestricted Erdős–Selfridge problem](https://www.erdosproblems.com/7).[71]

來源
[1] 1. Introduction https://arxiv.org/html/math/0412217
[2] Necessary condition for the existence of an incongruent covering system with odd moduli II https://geodesic.mathdoc.fr/articles/10.4064/aa-48-1-73-79/
[3] trureturing-experiments/docs/reports/erdos7-odd-covering/problem-details/02-current-bounds-and-comparisons.md at main · the-omega-institute/trureturing-experiments https://github.com/the-omega-institute/trureturing-experiments/blob/main/docs/reports/erdos7-odd-covering/problem-details/02-current-bounds-and-comparisons.md
[4] 7 | Erdős Problems https://www.erdosproblems.com/7
[5] Covering systems with restricted divisibilityThanks: The project was sponsored by the National Security Agency under Grant Number H98230-16-1-0048 and by the National Science Foundation under grant numbers DMS-1712682 and DMS-1802336. https://arxiv.org/html/1703.02133
[6] On the moduli of distinct covering systems https://arxiv.org/html/2611.15110v1
[7] Finiteness of Disjoint Covering Systems with Precisely One ... https://arxiv.org/pdf/2603.26043.pdf
[8] [PDF] Necessary conditions for distinct covering systems with square-free ... https://sites.math.rutgers.edu/~zeilberg/mamarimY/creative.pdf
[9] A Question of Erdős and Graham on Covering Systems https://arxiv.org/html/2501.15170v1
[10] [PDF] On covering systems of integers - arXiv https://arxiv.org/pdf/1705.04372.pdf
[11] A further investigation on covering systems with odd moduli https://arxiv.org/html/2507.16135v1
[12] arXiv:1703.02133v1  [math.NT]  6 Mar 2017 https://arxiv.org/pdf/1703.02133v1.pdf
[13] Necessary conditions for distinct covering systems with ... https://sites.math.rutgers.edu/~zeilberg/mamarimY/Zeilberger_y1991_p59.pdf
[14] Solution of the minimum modulus problem for covering systemsThanks: This research was begun while the author was a postdoctoral research fellow at Department of Pure Maths and Math Stats, Cambridge, and completed while a postdoctoral research fellow at the Mathematical Institute, Oxford. He is grateful for financial support from ERC Research Grant 279438, Approximate Algebraic Structure and Applications. https://arxiv.org/html/1307.0874
[15] NEARLY DISJOINT COVERING SYSTEMS https://www.renyi.hu/~p_erdos/1988-18.pdf
[16] Acta Arithmetica, Volume 45 (1985) https://geodesic.mathdoc.fr/volume/AA2_1985__45_1/
[17] Necessary condition for the existence of an incongruent covering system with odd moduli https://geodesic.mathdoc.fr/articles/10.4064/aa-45-4-375-379/
[18] BULLETIN (New Series) OF THE https://www.ams.org/journals/bull/1986-14-01/S0273-0979-1986-15414-5/S0273-0979-1986-15414-5.pdf
[19] Parcourir par https://geodesic.mathdoc.fr/volume/AA2_1985__45_2/
[20] Covers of product sets and the Korec-Zna´m result | European Journal of Combinatorics https://dl.acm.org/doi/10.1016/S0195-6698(88)80037-4
[21] Instructions for reporting errors https://arxiv.org/html/1801.05097v1
[22] On odd covering systems with distinct moduli | Advances in Applied Mathematics https://dl.acm.org/doi/10.1016/j.aam.2005.01.004
[23] Global Nonexistence of Odd Distinct Covering https://zenodo.org/records/18440762/files/Paper_I.pdf?download=1
[24] Two dimensional covering systems and possible prime producing a ... https://arxiv.org/html/2601.10296
[25] Kernel-Checked Exclusions for the Erdős–Selfridge Odd Covering Problem: Any Odd Covering of ℤ\mathbb{Z} Has lcm Exceeding 1000010000 https://arxiv.org/html/2607.25628
[26] Results for distinct covering systems with a prime minimum ... https://arxiv.org/html/2610.34541
[27] A further investigation on covering systems with odd moduli ... https://dl.acm.org/doi/abs/10.1016/j.disc.2026.115013
[28] On the 𝑗-th smallest modulus of a covering system with distinct moduli https://arxiv.org/html/2212.01299v2
[29] Weighted density bounds for covering systems over Dedekind domains https://arxiv.org/abs/2610.35139v1
[30] Covering systems where the prime divisors of all moduli are only 2 ... https://arxiv.org/html/2605.18644v1
[31] Solution of the minimum modulus problem for covering systems https://annals.math.princeton.edu/wp-content/uploads/annals-v181-n1-p06-p.pdf
[32] Necessary condition for odd incongruent coverings II — Erdős Problems https://erdosproblems.ai/wiki/library/covering_systems/berger_1987_necessary_condition_odd_covering_systems_ii
[33] On the Erdős covering problem: the density of the uncovered set https://par.nsf.gov/servlets/purl/10339936
[34] Covering systems with the sum of the reciprocals of the moduli close to 11 https://arxiv.org/html/2407.15280
[35] A further investigation on covering systems with odd moduli https://arxiv.org/pdf/2507.16135.pdf
[36] A Density Version of the Vinogradov Three Primes Theorem https://arxiv.org/html/1206.6139
[37] #A52 INTEGERS 26 (2026) A QUESTION OF ERD˝OS ... https://math.colgate.edu/~integers/aa52/aa52.pdf
[38] Resolving Adenwalla’s conjecture related to a question of Erdős and Graham about covering systems https://arxiv.org/html/2504.09579v3
[39] Densities in certain three-way prime number races https://arxiv.org/html/1908.10902
[40] COMPUTATIONS AND OBSERVATIONS ON CONGRUENCE COVERING SYSTEMS https://math.colgate.edu/~integers/a1Proc23/a1Proc23.pdf
[41] Extreme Covering Systems https://arxiv.org/html/1905.07386
[42] ON THE j-TH SMALLEST MODULUS OF A COVERING SYSTEM WITH ... https://dms.umontreal.ca/~koukoulo/documents/publications/covering-systems.pdf
[43] On covering systems of integers https://arxiv.org/html/1705.04372v1
[44] On the densities of covering numbers and abundant numbers https://arxiv.org/pdf/2507.23041.pdf
[45] Many Representations as Sums of Three Prime Cubes https://arxiv.org/html/2608.19262
[46] On covering systems over finite nilpotent groups and lattices https://arxiv.org/html/2611.03290v1
[47] arXiv:1801.05097v1  [math.CO]  16 Jan 2018 https://arxiv.org/pdf/1801.05097v1.pdf
[48] Introduction COVERING SYSTEMS WITH RESTRICTED - Math https://mathdept.byu.edu/~pace/CoveringHough_web.pdf
[49] Covering Systems of Polynomial Rings Over Finite Fields https://egrove.olemiss.edu/cgi/viewcontent.cgi?article=1038&context=etd
[50] A congruence obstruction to Roman’s bound for Zarankiewicz numbers https://arxiv.org/html/2608.07607v2
[51] trureturing-experiments/docs/reports/erdos7-odd-covering/profile-notes/001-064/15-a-clean-cylinder-makes-all-current-prime-pair-caps-exact.md at main · the-omega-institute/trureturing-experiments https://github.com/the-omega-institute/trureturing-experiments/blob/main/docs/reports/erdos7-odd-covering/profile-notes/001-064/15-a-clean-cylinder-makes-all-current-prime-pair-caps-exact.md
[52] Supplementary Information: The Lonely Runner Problem on Pair-Sum Lattices https://www.preprints.org/frontend/manuscript/1cdd11c5add837a8fb1504284f2609e6/download_pub/supplementary
[53] trureturing-experiments/docs/reports/erdos7-odd-covering/problem-details/40-fixed-order-scalar-threshold-barrier-and-cofactor-colors.md at main · the-omega-institute/trureturing-experiments https://github.com/the-omega-institute/trureturing-experiments/blob/main/docs/reports/erdos7-odd-covering/problem-details/40-fixed-order-scalar-threshold-barrier-and-cofactor-colors.md
[54] Covering subsets of the integers by congruences https://hal.science/hal-04167632v1/document
[55] 1. Introduction https://arxiv.org/html/math/0409521v1
[56] The Lonely Runner Problem on Pair-Sum Lattices: A Lossless Finitization ... https://www.preprints.org/frontend/manuscript/1cdd11c5add837a8fb1504284f2609e6/download_pub
[57] Prime supports and vanishing in restricted coprime representations https://arxiv.org/pdf/2611.10059.pdf
[58] arXiv:1811.03547v1  [math.NT]  8 Nov 2018 https://arxiv.org/pdf/1811.03547.pdf
[59] Alex Rice https://alexricemath.com/wp-content/uploads/2022/08/CoveringSystemPaper818.pdf
[60] Sieving by large integers and covering systems of congruences https://www.math.kent.edu/~yu/research/covering.pdf
[61] On the densities of covering numbers and abundant numbers https://arxiv.org/pdf/2507.23041v1.pdf
[62] Covering systems with odd moduli | Discrete Mathematics https://dl.acm.org/doi/10.1016/j.disc.2022.112936
[63] trureturing/Problems/erdos-7-odd-covering-systems.md at dev · the-omega-institute/trureturing https://github.com/the-omega-institute/trureturing/blob/dev/Problems/erdos-7-odd-covering-systems.md
[64] trureturing-experiments/docs/reports/erdos7-odd-covering/problem-details/21-coupled-first-root-profiles-and-an-exceptional-five-prime-block.md at main · the-omega-institute/trureturing-experiments https://github.com/the-omega-institute/trureturing-experiments/blob/main/docs/reports/erdos7-odd-covering/problem-details/21-coupled-first-root-profiles-and-an-exceptional-five-prime-block.md
[65] trureturing-experiments/docs/reports/erdos7-odd-covering/profile-notes/arithmetic/350-399/389-saturated-chain-source-has-small-complete-layout-second-moment.md at main · the-omega-institute/trureturing-experiments https://github.com/the-omega-institute/trureturing-experiments/blob/main/docs/reports/erdos7-odd-covering/profile-notes/arithmetic/350-399/389-saturated-chain-source-has-small-complete-layout-second-moment.md
[66] An Odd-Arch Family of Perturbed Hofstadter Q-Recursions: Gaussian Profiles and Exact Frequency Laws https://arxiv.org/pdf/2611.01453.pdf
[67] trureturing-experiments/docs/reports/erdos7-odd-covering/profile-notes/arithmetic/450-499/450-weighted-original-depths-and-the-uniform-lift-boundary.md at main · the-omega-institute/trureturing-experiments https://github.com/the-omega-institute/trureturing-experiments/blob/main/docs/reports/erdos7-odd-covering/profile-notes/arithmetic/450-499/450-weighted-original-depths-and-the-uniform-lift-boundary.md
[68] Completely Additive Height Functions: Profile Laws, Matula Bounds, and Inverse Growth https://arxiv.org/html/2308.00455v3
[69] The closure of the nonreal roots of bounded-height polynomials is connected exactly at pronic heights https://arxiv.org/pdf/2611.14517.pdf
[70] Sharp bounds, stability, and arithmetic fluctuations for induced pentagons https://arxiv.org/html/2610.40691v1
[71] Short-time height distribution in 1d KPZ equation: starting from a parabola https://arxiv.org/html/1605.06130v2
[72] An Almost-Covering Threshold for Golomb-Ruler ... https://arxiv.org/html/2608.13739v1
[73] Computations and Observations on Congruence Covering Systems https://arxiv.org/html/2208.09720v3
[74] dmj-17-123.dvi https://par.nsf.gov/servlets/purl/10165797
[75] V3R1T4S/known-unknowns/erdos-and-proofs/erdos-7-odd-covering ... https://github.com/elder-plinius/V3R1T4S/blob/main/known-unknowns/erdos-and-proofs/erdos-7-odd-covering-system.md
[76] Covering systems with odd moduli https://par.nsf.gov/servlets/purl/10431135
[77] [1705.04372] On covering systems of integers - ar5iv - arXiv https://ar5iv.labs.arxiv.org/html/1705.04372
[78] J. Yangzhou Teachers College (Nat. Sci. Ed.) 11(1991), no.3, 21–27. http://maths.nju.edu.cn/~zwsun/10y.pdf
[79] 7 Discussion Thread | Erdős Problems https://www.erdosproblems.com/forum/thread/7
[80] Erdős Problems https://www.erdosproblems.com/tags/covering%20systems
[81] There are no solutions, partial or complete, claimed in the comments. https://www.erdosproblems.com/search_bib/Er97/open
[82] Covering system - Wikipedia https://en.wikipedia.org/wiki/Covering_system
[83] Every friend of 10 has at least eleven distinct prime factors https://arxiv.org/html/2611.28126v1
[84] Erdős Problems https://erdosproblems.ai/wiki/problems/covering_systems/E0007/claims
[85] [PDF] integers 20 (2020) distinct covering systems in number fields https://math.colgate.edu/~integers/u89/u89.pdf
[86] Covering systems with restricted divisibility https://par.nsf.gov/servlets/purl/10123214
[87] trureturing/Library/Arith/schroeder2026nine.md at dev · the-omega-institute/trureturing https://github.com/the-omega-institute/trureturing/blob/dev/Library/Arith/schroeder2026nine.md
[88] On the generalized Sierpiński and Riesel numbers https://arxiv.org/html/2610.05149
[89] Resolving Adenwalla’s conjecture related to a question of Erdős and Graham about covering systems https://arxiv.org/html/2504.09579v1
[90] On Integers of the Forms k−2n and k2n+1 https://www.sciencedirect.com/science/article/pii/S0022314X0192640X
[91] Erdős Problems https://www.erdosproblems.com/prizes/25
[92] s https://www.yau-awards.com/uploads/file/20261113/20261113153715_12849.pdf
[93] Kernel-Checked Exclusions for theErdős–Selfridge Odd Covering Problem:Any Odd Covering of Z Has lcm Exceeding 10000 https://ar5iv.labs.arxiv.org/html/2607.25628
[94] s https://yau-awards.com/uploads/file/20261028/20261028144404_51638.pdf
[95] Finiteness of Disjoint Covering Systems with Precisely One Repeated Modulus https://arxiv.org/html/2603.26043v2
[96] 11-XX Number theory https://eudml.org/subject/MSC/11-XX?prefix=n
[97] Disjoint covering systems with precisely one multiple modulus https://geodesic.mathdoc.fr/articles/10.4064/aa-50-2-171-182/
[98] [PDF] CLASSIFIED PUBLICATIONS ON COVERING SYSTEMS Collected ... http://maths.nju.edu.cn/~zwsun/Cref.pdf
[99] MATHEMATICS OF COMPUTATION https://www.ams.org/journals/mcom/2009-78-266/S0025-5718-08-02154-6/S0025-5718-08-02154-6.pdf
[100] Covering systems with odd moduli https://arxiv.org/html/2104.00602
[101] [PDF] Problems and Results on Covering Systems http://maths.nju.edu.cn/~zwsun/Cover.pdf
[102] A non-analytic proof of the newman—znám result for disjoint covering systems - Combinatorica https://link.springer.com/article/10.1007/BF02579384
[103] Erdős covering systems - Acta Mathematica Hungarica https://link.springer.com/10.1007/s10474-020-01048-z
[104] On the minimum modulus problem in number fields https://arxiv.org/html/2302.05946
[105] Weighted density bounds for covering systems over Dedekind domains https://arxiv.org/pdf/2610.35139.pdf
[106] © 2023 European Mathematical Society https://ems.press/content/serial-article-files/31439
[107] On Erdős covering systems in global function fields https://arxiv.org/html/2402.03810
[108] On covering systems of polynomial rings over finite fields https://arxiv.org/html/2308.05378
[109] On odd covering systems with distinct moduli https://arxiv.org/abs/math/0412217
[110] Necessary condition for the existence of an incongruent covering system with odd moduli II https://www.impan.pl/en/publishing-house/journals-and-series/acta-arithmetica/all/48/11/105179/necessary-condition-for-the-existence-of-an-incongruent-covering-system-with-odd-moduli-ii
