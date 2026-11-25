#!/usr/bin/env python3
"""Exact certificates for distinct covering moduli supported on {3,5,7}.

Python 3.10+, standard library only. Examples:
    python3 smooth_cover_check.py
    python3 smooth_cover_check.py --triple 3 2 2 --self-test
    python3 smooth_cover_check.py --coprime 9 25 7
    python3 smooth_cover_check.py --scan 4 2 2

The default lists ALL coordinatewise-minimal reciprocal-feasible triples.
The optional scan is only for inspection; its cutoff is not used in the proof.
"""

import argparse
from fractions import Fraction as F
from itertools import combinations, product
from math import gcd, prod


PRIMES = (3, 5, 7)


def period(t):
    return prod(p**e for p, e in zip(PRIMES, t))


def prime_mass(p, e):
    """Sum of p**(-j) for j=1,...,e, including the empty sum at e=0."""
    if e < 0:
        raise ValueError("exponents must be nonnegative")
    n = p**e
    return F(n - 1, (p - 1) * n)


def masses(t):
    return tuple(prime_mass(p, e) for p, e in zip(PRIMES, t))


def reciprocal_sum(t):
    return prod(1 + s for s in masses(t)) - 1  # exclude modulus 1


def density_frontier():
    """Return the necessary floor and prove the full frontier without a cutoff."""
    floor = []
    for p in PRIMES:
        # Free the other two exponents. Their finite factors are strictly
        # below these limits, so even equality with 2 rules this exponent out.
        other_limits = prod(F(q, q - 1) for q in PRIMES if q != p)
        e = 0
        while (1 + prime_mass(p, e)) * other_limits <= 2:
            e += 1
        floor.append(e)
    base = tuple(floor)
    if reciprocal_sum(base) >= 1:
        return base, [base]
    neighbors = [base[:i] + (base[i] + 1,) + base[i + 1:] for i in range(3)]
    # An exact certificate specific to {3,5,7}: all three neighbors pass.
    # Every feasible triple dominates the floor and is not the floor, hence
    # dominates a neighbor. The neighbors are mutually incomparable.
    if not all(reciprocal_sum(t) >= 1 for t in neighbors):
        raise ArithmeticError("one-step frontier certificate does not apply")
    return base, sorted(neighbors, key=period)


def coprime_waste(moduli):
    """Exact sum of densities minus union density, for any pairwise-coprime T."""
    ds = tuple(moduli)
    if any(d <= 1 for d in ds) or any(gcd(d, e) != 1 for d, e in combinations(ds, 2)):
        raise ValueError("expected pairwise-coprime moduli greater than one")
    weights = [F(1, d) for d in ds]
    return sum(weights, F(0)) - 1 + prod((1 - w for w in weights), start=F(1))


def pure_power_waste(x, y, z):
    """Attainable MINIMUM waste of all available pure prime-power classes."""
    return x*y + x*z + y*z - x*y*z


def conditional_floor(x, y, z):
    """Lower bound on the uniform uncovered fraction; not an optimum claim."""
    return 1 - x - y - z + x*y*z


def print_screen(triples):
    print("A,B,C\tN\tS\tW(primes)\tprime gap\tmin W(pure)\t"
          "conditional floor\tmissed >=\tfirst exclusion")
    for t in triples:
        x, y, z = masses(t)
        n = period(t)
        s = reciprocal_sum(t)
        w = coprime_waste(p for p, e in zip(PRIMES, t) if e)
        prime_gap = 1 - s + w
        pure_w = pure_power_waste(x, y, z)
        lower = conditional_floor(x, y, z)
        missed = n * lower
        if missed.denominator != 1:
            raise ArithmeticError("the cardinality certificate must be integral")
        if s < 1:
            reason = "raw density"
        elif prime_gap > 0:
            reason = "prime CRT"
        elif 1 - s + pure_w > 0:
            reason = "pure-power CRT"
        else:
            reason = "conditional" if lower > 0 else "no certificate"
        print(f"{','.join(map(str, t))}\t{n}\t{s}\t{w}\t{prime_gap}\t"
              f"{pure_w}\t{lower}\t{missed.numerator}\t{reason}")


def self_test():
    # Direct divisor enumeration is independent of the factored formula.
    base, frontier = density_frontier()
    assert base == (2, 1, 1)
    assert frontier == [(3, 1, 1), (2, 2, 1), (2, 1, 2)]
    assert coprime_waste((3, 5, 7)) == F(2, 15)
    assert coprime_waste((9, 25, 7)) == (
        F(1, 9*25) + F(1, 9*7) + F(1, 25*7) - F(1, 9*25*7)
    )
    for t in product(range(4), repeat=3):
        div_exps = product(*(range(e + 1) for e in t))
        direct = sum((F(1, period(u)) for u in div_exps if any(u)), F(0))
        assert direct == reciprocal_sum(t)
        assert (direct >= 1) == any(all(a <= b for a, b in zip(v, t)) for v in frontier)
        x, y, z = masses(t)
        q, r, s = 1 - x, 1 - y, 1 - z
        i, j, k = x/q, y/r, z/s
        assert q*r*s*(1 - i*j - i*k - j*k - i*j*k) == conditional_floor(x, y, z)
        assert conditional_floor(x, y, z) > F(5, 48)
        assert 1 - direct + pure_power_waste(x, y, z) == 1 - x - y - z - 2*x*y*z
        assert 1 - direct + pure_power_waste(x, y, z) > F(1, 24)

    # Independent, exhaustive coverage check at N=105. A single translation
    # sets all three prime residues to 0 by CRT. Enumerate every choice for
    # 15,21,35; the last modulus (105) can cover exactly one additional point
    # if any point remains. No heuristic or random residue choices are used.
    def mask(d, a):
        return sum(1 << n for n in range(a, 105, d))

    pure = mask(3, 0) | mask(5, 0) | mask(7, 0)
    assert F(71 - pure.bit_count(), 105) == coprime_waste(PRIMES)
    choices = [[mask(d, a) for a in range(d)] for d in (15, 21, 35)]
    best = max((pure | a | b | c).bit_count() for a, b, c in product(*choices))
    assert 105 - min(105, best + 1) == 105*conditional_floor(*masses((1, 1, 1))) == 35
    print("Self-tests passed: divisor sums, frontier, rational identities, and exhaustive N=105.")


def main():
    parser = argparse.ArgumentParser(description=__doc__,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--triple", metavar=("A", "B", "C"), type=int, nargs=3,
                        action="append", default=[], help="screen one additional triple (repeatable)")
    parser.add_argument("--scan", metavar=("A", "B", "C"), type=int, nargs=3,
                        help="screen the inclusive box from (0,0,0) to (A,B,C)")
    parser.add_argument("--coprime", metavar="D", type=int, nargs="+",
                        help="also compute the exact standalone waste for these coprime moduli")
    parser.add_argument("--self-test", action="store_true", help="run independent exact checks")
    args = parser.parse_args()
    if any(e < 0 for t in args.triple + ([args.scan] if args.scan else []) for e in t):
        parser.error("all exponents must be nonnegative")
    if args.coprime:
        try:
            w = coprime_waste(args.coprime)
        except ValueError as exc:
            parser.error(str(exc))
        print(f"Exact standalone W{tuple(args.coprime)} = {w}")
    if args.self_test:
        if not __debug__:
            parser.error("--self-test needs assertions enabled; do not use python -O")
        self_test()
    base, frontier = density_frontier()
    print(f"Necessary floor: {base}; S(floor) = {reciprocal_sum(base)}")
    print("All minimal triples (in order of N):", ", ".join(map(str, frontier)))
    print("Smallest reciprocal-feasible N:", period(frontier[0]))
    print("A positive prime gap excludes a cover; a nonpositive gap is inconclusive.")
    print_screen(frontier + [tuple(t) for t in args.triple])
    if args.scan:
        print("\nRequested scan:")
        print_screen(product(*(range(e + 1) for e in args.scan)))


if __name__ == "__main__":
    main()
