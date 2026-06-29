# Note — n1(q)/q → 0, and the Critical Coverage x1(q) as the Real Unknown

Working note (loose, not a paper edit). English per programme convention. Closes the O25/O28
``central open direction'' in its model-free part (n1/q → 0) and re-poses the residual question — the
asymptotic law of the auto-calibrated window upper edge n1(q) — as a law for a single dimensionless
object, the critical coverage x1(q) = |B_{n1}|/q², into which all remaining uncertainty collapses.

## Two tiers: what is strongly supported vs what is the structural candidate

The result splits cleanly into a strongly-supported negative statement and a structurally-motivated
positive candidate. They must not be conflated.

TIER A — strongly supported (the actual closure of the open direction). The O28 premise
n1(q) = α q with a positive constant α = lim n1(q)/q is not supported:

    lim_{q→∞} n1(q)/q = 0.

The OLS estimate α̂ ≈ 0.053 (R² ≈ 0.88) of O28 is a finite-window residue of forcing a straight line
through a sublinear curve, not an asymptotic constant. The evidence is independent of any scaling
model: the linear law calibrated on q ≤ 211 predicts n1(307) ≈ 20 against a measured 16, and n1/q
decreases monotonically 0.138 → 0.052 over q ∈ {29,…,307}. This is what genuinely closes the
``central open direction'' of PTO/SAN, which had implicitly carried a characteristic depth Θ(q)
inherited from the BFS window.

TIER B — structural candidate (plausible, not demonstrated). The law is sublinear, and its whole
content collapses, via the exact identity of step (5), onto one measurable object:

    n1(q) = (x1(q) / C_Heis)^{1/4} · √q,        x1(q) = |B_{n1}| / q².

So ``which asymptotic law does n1 obey?'' IS ``which asymptotic law does the critical coverage x1(q)
obey?''. This rests on a coverage-scaling hypothesis (★ in step (4), r_q(n) ≈ q Φ(|B_n|/q²)) that is
NOT yet proved. The q=601 point (n1=19) settles the gross shape: the clean constant-x1 plateau — a true
Θ(√q) — is EXCLUDED (x1≈0.22 predicts n1(601)≈21 via the exact identity; measured 19). The CURRENTLY OBSERVED effective exponent over the
available range 101 ≤ q ≤ 601 is ≈ 0.30–0.33, below ½ — but this is a range observation, not an
established asymptotic value (the n1 are small integers; the 503→601 step is 19→19, which weighs
heavily on any power fit). The two surviving readings, n1 ≈ κ√q/ln q and n1 ∝ q^{1/3}, are both
SUB-√q and remain numerically indistinguishable on the data. What is established for n1 is therefore:
sublinear, incompatible with Θ(q), and (over the observed range) below Θ(√q), with the precise law
equal to the still-open asymptotic law of x1(q).

The honest summary is therefore: replace the old narrative ``n1/q → a positive constant'' by
``n1/q → 0, and the residual question is a law for the critical coverage x1(q)'', presenting
r_q(n) ≈ q Φ(|B_n|/q²) as the central structural hypothesis still to be demonstrated.

## Exact definition of the target (read from the pipeline, not reconstructed)

n1 is the upper edge of the auto-calibrated fitting window in `o25_paired_pipeline.run_one_prime`
(`auto_window`), computed by `find_fitting_window` of `spectral_O12.py`:

    n1 = last shell n with  σ̄(n) > EPS_SAT,   EPS_SAT = 1e-3,

where σ̄(n) is the mean over 5 probe blocks (rng seed+999999) of the per-block capacity
σ_c(n) = Δr(n) / |S_n|, and Δr(n) is the Gram–Schmidt rank increment contributed by the Weil k=3
fingerprint vectors of BFS shell S_n. The fingerprints live in ℂ^q; the cumulative Gram–Schmidt
rank r(n) = Σ_{m≤n} Δr(m) is monotone and bounded by q.

Crucial empirical fact (informs the model): at n = n1 the cumulative rank is NOT full
(min rank ≈ 137/307 at q = 307). So n1 is the crossing of the capacity-novelty DENSITY below a
fixed threshold, not the depth at which ℂ^q is fully spanned.

## Numerical basis (this session)

A faithful, resumable re-implementation (`simulation/spectral/o25/n1_resumable.py`, multicore
variant `n1_parallel.py`) reuses the validated primitives `fingerprint_vectors_batch` and the exact
absolute-1e-10 Gram–Schmidt threshold. It reproduces the production O28 window edge exactly on the
calibration set:

    q     29   61  101  151  211     (O28 / this work, identical)
    n1     4    8   11   13   14

Out-of-sample (the regime O28 never reached), measured with `n1_parallel.py` (12 cores):

    q                  307     401     503     601
    n1 (measured)       16      17      19      19
    n1 (O28 linear, calibrated on q ≤ 211)   20.3    25.3    30.7    35.8
    n1/sqrt(q)         0.913   0.849   0.847   0.775
    x1 = |B_n1|/q²     0.297   0.222   0.220   0.154

The O28 linear law overpredicts by +27/+49/+62/+88 % at q = 307/401/503/601; rejected out of sample.
Across q ∈ {29,…,601} the ratio n1/q falls monotonically 0.138 → 0.032. Tier A is now overwhelming.

The Tier-B verdict after q=601: the plateau was a transient, the clean √q is OUT. The apparent stall
x1 = 0.222 (401) → 0.220 (503) suggested x1 might converge (reviving a clean asymptotic √q); q=601
settles it the other way. The constant-coverage reading (x1≈0.22, via the exact identity
n1=(x1/C_Heis)^{1/4}√q) predicts n1(601) ≈ 20.8 → 21; measured 19. The stall was an
integer-rounding artefact (n1 sat on 19 across 503 and the 601 neighbourhood), not a convergence:
x1 RESUMED decaying, 0.220 (503) → 0.154 (601), tracking x1 ~ q^{-0.76}. On q ≥ 101 (now 7 points):

- constant-κ √q (n1 = k√q): R² = 0.66, residual arch (+2.2,…,−2.4) — REJECTED;
- log-corrected √q (n1 = κ √q / ln q, κ ≈ 5.14): R² = 0.982;
- sub-½ power (n1 = k q^{1/3}, k ≈ 2.34): R² = 0.980;
- best free fit over the available range: exponent ≈ 0.30–0.33, n1 ≈ 2.84 q^{0.30} (R² = 0.986).
  This is the CURRENTLY OBSERVED effective exponent on 101 ≤ q ≤ 601, NOT an established asymptotic
  value: the 503→601 step is 19→19 (small integers), which dominates any power fit. The log and the
  q^{1/3} laws remain numerically INDISTINGUISHABLE (both predicted n1(601) = 20, measured 19, within
  rounding); both are sub-√q.

Bottom line: q=601 kills the clean Θ(√q). The genuinely new fact is not a power exponent but that x1
RESUMED decaying after the apparent plateau (0.222 → 0.220 → 0.154): the coverage at which the crossing
σ(n1) = ε_sat occurs keeps moving to ever-lower values as q grows — the mechanism does not settle. The
open problem is therefore the asymptotic law of x1(q), and the mathematical front is the
Φ'(x1) = ε_sat q tension of step (4) — explaining WHY x1 decreases, not fitting a better exponent. (The first q=601 attempt segfaulted in Apple Accelerate's complex
matmul; the scripts now route complex matmuls through real BLAS, and the rerun completed cleanly.)

Two exact supporting constants measured this session:

- Ball-growth constant. |B_n| = C_Heis n⁴ (1 + o(1)) with homogeneous dimension D = 4
  (Bass–Guivarc'h), fitted exponent p = 4.003, C_Heis ≈ 0.427 (shell ratio |S_n|/n³ → 4 C_Heis ≈
  1.71). [`cheis_ballgrowth.py`]
- Spectral gap. λ2(L_G) · q² → ≈ 39 and rising toward 4π² ≈ 39.48 over q ∈ {5,…,19}, i.e.

      λ2(Cay(Heis3(Z/qZ), {X^±,Y^±})) ≈ 4π² / q²,

  the gap of the horizontal abelianization torus (ℤ/q)². The relaxation is diffusive; the coverage
  scale of the walk is q². [`/tmp/lambda2.py`, to be archived in the repo]

## The conceptual discovery (independent of the √q law, and probably more important)

The single most important observation in this note is empirical and model-free:

    at n = n1 the cumulative rank r(n1) is NOT full (e.g. ≈ 137/307 at q = 307).

This breaks the naive reading r(n1) ~ q. The window edge n1 is NOT the depth at which the Weil
fingerprints span ℂ^q. It is the depth at which the creation of new directions per explored vertex
falls below a fixed threshold — a stop of marginal novelty, not a completion of a basis:

    n1 = last n with σ(n) > ε_sat,   σ(n) = Δr(n)/|S_n| = marginal rank per shell vertex.

This reformulation stands on its own, independently of whether the asymptotic law turns out to be
exactly √q. It says the relevant physical content of n1 is a saturation of incremental projective
capacity (in the O7 sense), governed by how fast the diffusive relaxation stops producing novelty,
rather than a dimension count of ℂ^q.

It is also the part that transfers directly to the n_g programme. The per-generation depths n_g are
the same kind of object — a marginal-novelty stop, read off the relaxation trajectory, not a
rank-filling — so the right state variable to carry forward is σ(n) (equivalently the cumulative
I(n) = σ_pair(0) − σ_pair(n)) and its threshold crossing, not the rank r(n). This is the reusable
piece.

## The real unknown is the critical coverage x1(q)

Two of the three ingredients of the depth law are already understood: |B_n| ~ C_Heis n⁴ (D = 4) and
λ2 ~ 4π²/q² (diffusive). By the exact identity n1(q) = (x1(q)/C_Heis)^{1/4} √q, ALL remaining
uncertainty is concentrated in a single dimensionless object — the critical coverage at the window
edge,

    x1(q) = |B_{n1}| / q².

This is the cleaner way to pose the open problem: not ``what is the exponent of n1?'' but ``what is
the asymptotic law of x1(q)?''. Every competing law for n1 is merely a law for x1: x1 → const ↔ clean
√q; x1 ∝ (ln q)^{-4} ↔ √q/ln q; x1 ∝ q^{-2/3} ↔ q^{1/3}. The several hypotheses of the previous draft
are one question about one measurable quantity.

The empirically striking fact is not the mild drift of n1/√q but the FAST, sustained fall of the
coverage:

    x1 :  0.61 (q=101) → 0.54 → 0.37 → 0.30 → 0.22 (q=401) → 0.22 (q=503) → 0.15 (q=601),

a steep decrease, a brief integer-rounding stall at q=401–503, then a resumed fall — overall
x1 ~ q^{-0.76}. The q=601 point shows x1 does NOT settle to a constant. So the central question is not
the exponent of n1 but: what is the asymptotic law of x1(q), and why does the critical coverage decay
this fast? The natural form of a future theorem here is a LAW FOR x1(q) — derived from a shellwise
Weil–BFS novelty estimate controlled by λ2 — rather than a direct exponent law for n1. x1(q) is
precisely the object that absorbs the unresolved Φ'(x1) = ε_sat q tension of step (4), and is the
right target for the next push.

## The derivation

The chain has five links; the load-bearing, still-unproven one is the coverage-scaling step (4).
Each is labelled proved / structural-hypothesis / structural / conditional / open.

(1) Volume growth — PROVED / robust. Cay(Heis3(Z/qZ), S) has homogeneous dimension D = 4, so for
    n ≪ q, |B_n| = C_Heis n⁴ (1 + o(1)). (Bass–Guivarc'h; O9 Heisenberg-growth proposition; confirmed
    here, p = 4.003, C_Heis ≈ 0.427.)

(2) Diffusive spectral gap — PROVED / robust (numerically). λ2(L_G) ≈ 4π²/q², the gap of the
    horizontal abelianisation torus (ℤ/q)². Verified: λ2 q² → ≈ 39 → 4π² over q ∈ {5,…,19}. The walk
    relaxes diffusively; its horizontal phase space has q² vertices.

(3) Natural coverage scale q² — STRUCTURAL (follows from (1)+(2)). A diffusive walk with gap q^{-2}
    on a space whose horizontal extent is q² has a single natural coverage variable: the reduced
    volume x = |B_n| / q². This is a sound consequence of (1) and (2).

(4) Coverage-scaling hypothesis — STRUCTURAL HYPOTHESIS (the one load-bearing, unproven link).
    Assume the cumulative rank depends on the explored volume only through that reduced coverage:

        r_q(n) ≈ q · Φ(|B_n| / q²),     Φ smooth, Φ(0)=0, Φ increasing.            (★)

    This is Jérôme's proposed lock and the heart of the derivation. It is a SCALING ANSATZ: that the
    q-dependence of the whole rank trajectory collapses onto the single variable |B_n|/q². It is
    motivated by (3) but is NOT derived from it — establishing (★) (e.g. from a shellwise Weil–BFS
    novelty estimate controlled by λ2) is the remaining hard step. Granting (★), and using
    σ(n) = Δr/|S_n| ≈ dr/d|B| (the marginal density of the conceptual section), the ansatz gives
    σ(n) = Φ'(x)/q with x = |B_n|/q². The window criterion σ(n1) = ε_sat (ε_sat = 10⁻³ fixed,
    independent of q) then reads

        Φ'(x1) = ε_sat · q,

    whose right-hand side GROWS with q. This is the precise, still-unresolved tension of the
    derivation — a fixed threshold against the explicit 1/q in σ — and it is exactly where a technical
    reader should look. It can be met only if (i) Φ' has a region taking values that grow with q (so
    the crossing coverage x1 drifts into the steep part of Φ as q grows), or (ii) the simple form
    σ = Φ'(x)/q is too coarse and the true q-dependence of x1 is subtler. The ansatz predicts only
    that the crossing is controlled by the reduced coverage variable x; whether the corresponding
    x1(q) converges to a constant, drifts logarithmically, or carries a residual power correction is
    precisely what the q ∈ {401,503,601} campaign is designed to determine. (Measured so far,
    x1 = |B_{n1}|/q² falls fast 0.61 (q=101) → 0.22 (q=401), a brief rounding stall at 0.22 (q=503),
    then resumes to 0.15 (q=601) — overall x1 ~ q^{-0.76}, not converging; the law of x1(q) is the real
    open problem, see the dedicated section above.) This tension is the natural source of scenarios
    1 vs 2 vs 3 below.

(5) Conclusion — STRUCTURAL, modulo the behaviour of x1(q). Inverting |B_n| = C_Heis n⁴ at the
    crossing volume |B_{n1}| = x1(q) q² gives, exactly,

        n1(q) = (x1(q) / C_Heis)^{1/4} · √q.

    The growth verdict is therefore LITERALLY the behaviour of x1(q), nothing more:
      - x1 → const          ⟹  clean Θ(√q), κ = (x1/C_Heis)^{1/4}        (scenario 1 — EXCLUDED by q=601);
      - x1 ∝ (ln q)^{-4}     ⟹  n1 ≈ κ √q / ln q                          (scenario 2 — survives);
      - x1 ∝ q^{-2/3}        ⟹  n1 ∝ q^{1/3}                              (scenario 3 — survives).
    In every case x1 ≤ O(1) keeps n1 = O(√q), so n1/q → 0 (Tier A) holds independent of which law wins;
    q=601 additionally rules out the x1-constant endpoint, so the data sit at scenario 2/3 (sub-√q,
    observed effective exponent ≈ 0.30–0.33 over the available range). The naive ``span all of ℂ^q''
    reading (x1 = 1, κ = C_Heis^{-1/4} ≈ 1.24) is the x1-constant extreme and overshoots most.

    Logical status: (1) and (2) are robust; (3) is a sound consequence; (5) is arithmetic. The ONLY
    genuine assumption is the scaling collapse (★) in (4), and even granting it, the unresolved
    Φ'(x1) = ε_sat q tension means x1(q) — hence the exact growth law — is not yet fixed. So
    ``λ2 ~ q^{-2} and |B_n| ~ n⁴'' make n1 sublinear (n1/q → 0) beyond doubt; q=601 further excludes a
    clean Θ(√q) (x1 does not settle), leaving a sub-√q law (observed effective exponent ≈ 0.30–0.33,
    range-limited) whose precise form is the open asymptotic law of x1(q).

## What is proved, what is supported, what remains

- PROVED: D = 4 volume growth; n1 ≤ diameter = q − 1; λ2 = Θ(1/q²) (≈ 4π²/q²).
- STRONGLY SUPPORTED, model-free (Tier A): lim n1/q = 0. The linear law is rejected out of sample
  (predicts 20.3 at q=307, measured 16) and n1/q decreases monotonically. This is the real closure of
  the open direction and does not depend on the scaling ansatz (★).
- STRUCTURAL, conditional on (★) (Tier B): n1 = (x1(q)/C_Heis)^{1/4} √q exactly, with the entire
  asymptotic behaviour carried by the critical coverage x1(q). Sublinearity (n1/q → 0) is robust, and
  q=601 also excludes a clean Θ(√q) (observed effective exponent ≈ 0.30–0.33, range-limited); the
  precise law (√q/ln q vs q^{1/3}, both sub-√q) is open and is literally the asymptotic law of x1(q).
  Rests on (★).

The discriminating question is the asymptotic law of the reduced coverage x1(q). Three scenarios, now
adjudicated by q=601 (n1=19, x1=0.154 — x1 resumed decaying after the 401–503 rounding stall):

  1. x1 → const (≈ 0.22)       → clean asymptotic Θ(√q), κ ≈ 0.85.   EXCLUDED: predicts n1(601)≈21
                                 (x1=0.22 via the exact identity), measured 19; the stall was an
                                 integer-rounding artefact, not a limit.
  2. x1 ∝ (ln q)^{-4}          → n1 ≈ κ√q/ln q.   Fits q≥101 at R² = 0.982; predicted n1(601)=20.
  3. x1 ∝ q^{-2/3}             → n1 ∝ q^{1/3}.    Fits q≥101 at R² = 0.980; predicted n1(601)=20.
                                 (2) and (3) survive, remain numerically indistinguishable, both sub-√q.

The effective exponent observed on 101 ≤ q ≤ 601 is ≈ 0.30–0.33 (best free fit n1 ≈ 2.84 q^{0.30},
R² = 0.986), with x1(q) ~ q^{-0.76} over the same range — a range observation, not an established
asymptotic value (the 503→601 step 19→19 dominates the fit). Separating the log law (2) from the power
law (3) would need q well beyond 601 (they differ by < 1 in n1 out to q ~ 10³); both agree n1 grows
BELOW √q on the observed range.

Calibrated confidence after q=601: ≈ 99 % that the linear law is dead (Tier A, model-free); ≈ 99 %
that the growth is sublinear and incompatible with Θ(q) (n1/q → 0); ≈ 85 % that it is also below
Θ(√q) over the observed range (clean √q excluded by q=601); the log-vs-power form of x1(q), and the
true asymptotic exponent, are open.
The centre of gravity has shifted: the next target is a structural law for x1(q) (a shellwise
Weil–BFS novelty estimate controlled by λ2), not a further exponent fit. No strong integration into
O28 yet — Tier A is reportable now; Tier B awaits the x1(q) law.

## Circularity guard

κ is NOT fitted to make n1/√q ≈ 1. C_Heis = 0.427 is computed from exact ball counts independently
of n1; λ2 ≈ 4π²/q² is computed from the graph Laplacian independently of n1; the only O(1) freedom
is the coverage fraction x1, which the model ties to ε_sat and Φ, both fixed by the pipeline, not by
the target. The √q SCALING uses no fitted target value.

## Bridge to n_g (why this was the right wedge)

The object that the derivation forces — a rank/capacity saturation controlled by the diffusive
relaxation λ2(L_G(n)) rather than by a direct power-law fit — is exactly the machinery the
per-generation depths n_g require. n1 (global saturation) and the n_g (saturations by generation) are
the same phenomenon governed by the same λ2. The clean outcome here (coverage scale q² from
λ2 ≈ 4π²/q², depth √q from D = 4) is the template to carry into the n_g front.

## Reproduction pointers

- `simulation/spectral/o25/n1_resumable.py`   — faithful, per-(block,shell) resumable n1, budget-aware.
- `simulation/spectral/o25/n1_parallel.py`    — multicore (joblib over probe blocks), no checkpoint.
- `simulation/spectral/o25/cheis_ballgrowth.py` (scratch) — C_Heis ≈ 0.427, D = 4.
- λ2 scaling script — λ2 q² → 4π², archive under `simulation/spectral/o25/`.
- Validation: both n1 scripts reproduce O28 {29,61,101,151,211} → {4,8,11,13,14} exactly.
