#!/usr/bin/env python3
"""Unconditional density bounds on Z/(3^A 5^B 7^C)Z. Standard library only.

    python3 unconditional_cover_bound.py         # endpoint and N=945
    python3 unconditional_cover_bound.py 3 2 2   # endpoint and N=33075
"""

import argparse
from fractions import Fraction as F


def power_mass(p, exponent):
    """Sum of 1/p^j for 1 <= j <= exponent."""
    return (1 - F(1, p**exponent)) / (p - 1)


def five_tower(d, exponent):
    """Sum of 1/(d*5^b) for 1 <= b <= exponent, with 5-free cofactor d."""
    if d < 1 or d % 5 == 0:
        raise ValueError("expected a positive 5-free cofactor")
    return (1 - F(1, 5**exponent)) / (4 * d)


def bounds(x, y, z):
    # Pad each pure-coordinate union to density x, y, or z. All densities
    # below use the ORIGINAL uniform probability, never a conditional law.
    pure = 1 - (1 - x) * (1 - y) * (1 - z)
    mixed_raw = x * z + y * (x + z + x * z)
    mixed_new = (x * y * (1 - z) + x * z * (1 - y)
                 + y * z * (1 - x) + x * y * z)
    raw_gap = 1 - pure - mixed_raw
    sharp_gap = 1 - pure - mixed_new
    assert raw_gap == 1 - x - y - z - 2 * x * y * z
    assert sharp_gap == 1 - x - y - z + x * y * z
    return raw_gap, sharp_gap


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("exponents", metavar="E", nargs="*", type=int,
                        help="supply A B C, all nonnegative (default: 3 1 1)")
    args = parser.parse_args()
    exponents = args.exponents or [3, 1, 1]
    if len(exponents) != 3 or min(exponents) < 0:
        parser.error("supply exactly three nonnegative exponents A B C")
    a, b, c = exponents
    n = 3**a * 5**b * 7**c
    x, y, z = power_mass(3, a), five_tower(1, b), power_mass(7, c)
    endpoint = bounds(F(1, 2), F(1, 4), F(1, 6))
    assert endpoint == (F(1, 24), F(5, 48))
    raw, refined = bounds(x, y, z)
    assert raw > endpoint[0] and refined > endpoint[1]
    assert (n * refined).denominator == 1
    print(f"Endpoint lower bounds: raw={endpoint[0]}, refined={endpoint[1]}")
    print(f"N={n}  (A,B,C)={tuple(exponents)}")
    print(f"Finite uncovered fraction >= {raw} (raw), >= {refined} (refined)")
    print(f"Missed residues >= {n * refined} out of {n}")
    for p in (3, 7):
        print(f"Sum over {p}*5^j, 1 <= j <= {b}: {five_tower(p, b)}")


if __name__ == "__main__":
    main()
