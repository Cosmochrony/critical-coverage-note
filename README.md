# Critical Coverage and the Saturation Depth Problem

Working note of the Cosmochrony **spectral admissibility** sub-programme.
PDF: `out/CriticalCoverageNote.pdf`.

## Summary

The auto-calibrated saturation depth `n_1(q)` of the breadth-first exploration of
`Heis_3(Z/qZ)` was the central open asymptotic variable of O25–O28. This note reframes the problem
around a single observable.

The window edge `n_1` is not a vector-space filling time: at `n_1` the cumulative Weil-fingerprint
rank is far from full (e.g. `137/307` at `q=307`, `183/601` at `q=601`). It is a stop of marginal
novelty — the depth at which the new directions gained per explored vertex drop below a fixed
threshold.

Two robust facts — the ball growth `|B_n| ~ C_Heis n^4` (`D=4`, `C_Heis ≈ 0.427`) and the diffusive
spectral gap `λ_2 ≈ 4π²/q²` — give the exact identity

    n_1(q) = (x_1(q) / C_Heis)^(1/4) · sqrt(q),   x_1(q) = |B_{n_1}| / q²,

so the asymptotic law of `n_1` reduces to the asymptotic law of the **critical coverage** `x_1(q)`.

## Result

- Model-free: `n_1(q)/q → 0` (the linear law is excluded out of sample).
- `x_1(q)` falls fast, `0.61 → 0.15` over `q = 101 → 601`, which excludes the constant-coverage
  (clean `sqrt(q)`) scenario; the surviving readings (`sqrt(q)/ln q`, `q^{1/3}`) are sub-`sqrt(q)` and
  numerically indistinguishable on present data.
- The governing front is the tension `Φ'(x_1) = ε_sat · q` (fixed threshold vs. an explicit `1/q`).

## Open problem

Derive the asymptotic law of `x_1(q)` from a shellwise Weil–BFS novelty estimate controlled by `λ_2`,
of which the depth law `n_1(q)` is a corollary.

## Reproduction

Scripts in `simulation/spectral/o25` of the Cosmochrony repository:
`n1_resumable.py`, `n1_parallel.py` (depth `n_1`), `cheis_ballgrowth.py` (`C_Heis`, `D=4`),
`lambda2_scaling.py` (`λ_2 q² → 4π²`). Both depth scripts reproduce the O28 values
`{29,61,101,151,211} → {4,8,11,13,14}` exactly.

## Status

Working note (not yet deposited). Companion to O28; the speculative coverage analysis is kept here,
out of O28 itself.
