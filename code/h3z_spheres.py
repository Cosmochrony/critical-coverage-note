"""Exact BFS of the infinite discrete Heisenberg group H3(Z), generators {X^±1, Y^±1}.

Deliverables for R1 item 4: exact sphere sizes s_n, ball sizes |B_n|, central
extent Gamma(n) = max |gamma| over B_n, monotonicity of s_n, and the strict
crossing n* = max{n : 18/s_n > 1e-3} = max{n : s_n < 18000}.

Pure exact integer combinatorics of the infinite group; no prime q involved.
"""
from collections import deque

NMAX = 31
EPS = 1e-3

dist = {(0, 0, 0): 0}
frontier = deque([(0, 0, 0)])
s = [0] * (NMAX + 1)
s[0] = 1
gmax = [0] * (NMAX + 1)

def neighbours(a, b, g):
    # right multiplication by X, X^-1, Y, Y^-1 with (a,b,g)(a',b',g')=(a+a',b+b',g+g'+a*b')
    yield (a + 1, b, g)
    yield (a - 1, b, g)
    yield (a, b + 1, g + a)
    yield (a, b - 1, g - a)

n = 0
while n < NMAX:
    nxt = deque()
    for (a, b, g) in frontier:
        for v in neighbours(a, b, g):
            if v not in dist:
                dist[v] = n + 1
                nxt.append(v)
    n += 1
    s[n] = len(nxt)
    gmax[n] = max(gmax[n - 1], max((abs(v[2]) for v in nxt), default=0))
    frontier = nxt

B = 0
print(f"{'n':>3} {'s_n':>9} {'|B_n|':>9} {'Gamma(n)':>8} {'18/s_n':>12} {'|B_n|/n^4':>10}")
crossing = None
for n in range(NMAX + 1):
    B += s[n]
    ratio = 18.0 / s[n] if s[n] else float('inf')
    c4 = B / n**4 if n else float('nan')
    print(f"{n:>3} {s[n]:>9} {B:>9} {gmax[n]:>8} {ratio:>12.6f} {c4:>10.4f}")

inc = all(s[k] < s[k + 1] for k in range(1, NMAX))
print(f"\ns_n strictly increasing on [1,{NMAX}]: {inc}")
print(f"s_n == 18000 for some n: {any(s[k] == 18000 for k in range(1, NMAX + 1))}")
nstar = max(k for k in range(1, NMAX + 1) if s[k] < 18000)
print(f"n* = max{{n : s_n < 18000}} = {nstar}")
print(f"s_{nstar} = {s[nstar]}  (18/s = {18/s[nstar]:.6e} > 1e-3)")
print(f"s_{nstar+1} = {s[nstar+1]}  (18/s = {18/s[nstar+1]:.6e} < 1e-3)")
Bstar = sum(s[:nstar + 1])
print(f"K = |B_n*| = {Bstar}")
print(f"Gamma(n*+1) = {gmax[nstar+1]}  -> ball-isometry sufficient bound q > {2*gmax[nstar+1]+1}")
