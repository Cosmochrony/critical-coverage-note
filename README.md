# Inverse-Square Critical Coverage and Constant Saturation Depth from an Exact Interval Theorem

Working note of the Cosmochrony **spectral admissibility** sub-programme.
Citable version: Zenodo concept DOI [10.5281/zenodo.21049163](https://doi.org/10.5281/zenodo.21049163).
Web page: <https://cosmochrony.org/science/spectral/program/critical-coverage/>.

## Summary

The auto-calibrated saturation depth $n_1(q)$ of the breadth-first exploration of
$\mathrm{Heis}_3(\mathbb{Z}/q\mathbb{Z})$ — the central asymptotic variable of the O25–O28 window
calibration — converges in probability to the constant $n_* = 22$ under uniform generic block
sampling, and the critical coverage $x_1(q) = |B_{n_1}|/q^2$ obeys the inverse-square law
$x_1(q) \asymp q^{-2}$.

The mechanism is an exact algebraic reduction.
Every implemented three-step Weil fingerprint is a non-zero scalar multiple of a single Fourier
character, so the cumulative rank is a sumset cardinality,

$$r_c(n) = \bigl|\,T'_c + C\,I_{n+1}\,\bigr|,
\qquad T'_c = \{(c_2+c_3)\eta_2 + c_3\eta_3 : \eta_i \in \{-1,0,1\}\},$$

with $C = c_1+c_2+c_3$ and $I_m$ the reduction of $[-m,m]$; the shellwise novelty obeys the
universal deterministic ceiling $\Delta r_c(n) \le 2|T'_c| \le 18$, with a complete classification
of the block resonances that lower it.
Exact sphere counts of the infinite discrete Heisenberg group give the strict threshold crossing
$s_{22} = 16{,}934 < 18/\varepsilon_{\mathrm{sat}} = 18{,}000 < s_{23} = 19{,}412$.

## Results

- **Deterministic** (every prime $q \ge 311$, every admissible block sequence):
  $n_1(q) \le 22$ and $5/q^2 \le x_1(q) \le 99{,}689/q^2$, so $x_1(q) \asymp q^{-2}$;
  the positive-edge and logarithmic scenarios are excluded without probabilistic input.
- **Probabilistic** (i.i.d. uniform generic blocks): $n_1(q) \to 22$ and
  $q^2 x_1(q) \to |B_{22}| = 99{,}689$ in probability.
- **Exact depth–coverage identity**: $n_1(q) = (x_1(q)/\kappa_{n_1})^{1/4}\sqrt{q}$ with
  $\kappa_n = |B_n|/n^4$.
- **Transitional regime**: the measured depths ($n_1 = 14$ at $q = 211$, $19$ at $q = 601$) are
  explained by block resonances; their deficits produce the observed effective exponent
  $\approx -0.76$ en route to the exact asymptotic $-2$.
- **Window closure**: the implemented auto-calibrated fitting window $[n_0, n_1]$ is
  deterministically empty for $q > 4 \cdot 22^4 = 937{,}024$.
- **Collapse degeneracy**: the coverage-collapse ansatz $r_q(n) \approx q\,\Phi(|B_n|/q^2)$ is
  degenerate near the threshold front ($\Phi \equiv 0$ there); the law of $x_1$ is combinatorial,
  not diffusive.
- **Consequence**: in the dual-window limit of the canonical Fourier filtration (Q5a), the
  potential coefficient $\lambda = \lim x_1/C_{\mathrm{Heis}}$ vanishes: that limit carries no
  oscillator potential.

## Reproduction

- `code/h3z_spheres.py` — exact integer BFS of $H_3(\mathbb{Z})$ to depth 31: sphere sizes $s_n$,
  ball sizes $|B_n|$, central extent $\Gamma(n) = \lfloor n^2/4 \rfloor$, and the strict crossing
  $n_*(10^{-3}) = 22$, $|B_{22}| = 99{,}689$.
- Scripts in `simulation/spectral/o25` of the Cosmochrony repository: `n1_resumable.py`,
  `n1_parallel.py` (depth $n_1$), `cheis_ballgrowth.py` ($C_{\mathrm{Heis}}$, $D=4$),
  `lambda2_scaling.py`.
  Both depth scripts reproduce the O28 values $4, 8, 11, 13, 14$ at $q = 29, 61, 101, 151, 211$
  exactly.

The compiled PDF is generated into `out/` by `compile.sh` (pdflatex → bibtex → pdflatex ×2).

## Status

Working paper, deposited on Zenodo (concept DOI
[10.5281/zenodo.21049163](https://doi.org/10.5281/zenodo.21049163)).
Companion to O28: it resolves the saturation-depth asymptotics that O28 left open.
