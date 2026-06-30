# Gate note — n_g^λ vs n_g^σ: do rank-novelty stops break the cancellation lemma?

Internal analysis (loose, English). Decides whether deriving the rank-novelty Φ (CC-Note, the shellwise
Weil–BFS estimate) is worth pursuing FOR THE MASS HIERARCHY, by comparing the existing λ2-crossing
generation depths n_g^λ with the candidate rank-novelty sectoral stops n_g^σ. Verdict gates the heavy
work.

## 1. The two depth definitions

n_g^λ — existing (fermionic-matter front, `def:nproj`). The stabilisation rank of stratigraphic level
λ_g against the growing relaxation:
  n_g^λ = n_proj(λ_g) = inf{ n : λ_g ≤ Λ_proj(n) },   Λ_proj(n) = c_χ(n)²/A_min²,
  chain c_χ(n) → h(G(n)) → λ2(n).
In the exponential (trajectory-branching) regime Λ_proj(n) ~ L0·exp(β* n) (`cor:linear-law`), so
  n_g^λ = (1/β*) ln(λ_g/L0).                                   (λ-form)
KEY: n_g^λ is q-INDEPENDENT — it depends on the spectral level λ_g, not on the Heisenberg modulus q.

n_g^σ — candidate (rank-novelty, the CC-Note observable made sectoral). Partition the Weil k=3
fingerprints by generation sector g; let σ_g(n) = Δr_g(n)/|S_n| be the per-sector capacity-novelty
density; define the sectoral window edge
  n_g^σ = last n with σ_g(n) > ε_sat.
By the CC-Note reduction applied per sector,
  n_g^σ = (x_g(q)/C_Heis)^{1/4} √q,   x_g(q) = |B_{n_g^σ}|/q²   the sectoral critical coverage. (σ-form)
KEY: n_g^σ is q-DEPENDENT — it grows like √q (sub-√q in practice).

## 2. The cancellation lemma (recap; exact-symbolic in the fermionic front)

With the mass amplification A(n) = exp(β* n) and the λ-form n_g^λ = (1/β*) ln(λ_g/L0),
  A(n_i^λ)/A(n_j^λ) = exp(β*(n_i^λ − n_j^λ)) = exp(ln(λ_i/λ_j)) = λ_i/λ_j,   independent of β*.
On the charged-lepton levels the level ratios are O(1) (≤ 1.5 on {20,24,30}), nowhere near the required
~3477. So the hierarchy CANNOT come from λ-crossing depths. The cancellation is structural: it is
ENTIRELY a consequence of the logarithmic form n_g ∝ ln λ_g.

## 3. The evasion condition (Jérôme's criterion, made precise)

Because the cancellation follows solely from n_g ∝ ln λ_g, any depth that is an affine function of
ln λ_g reproduces it. Therefore:

  n_g^σ evades the cancellation  ⟺  n_g^σ is NOT affine in ln λ_g
                                 ⟺  x_g(q) does NOT take the form  x_g ∝ (ln λ_g)^4   (mod q).

Indeed x_g ∝ (ln λ_g)^4 gives n_g^σ = (x_g/C_Heis)^{1/4}√q ∝ ln λ_g·√q ∝ ln λ_g, and the √q cancels in
the ratio, reproducing A_i/A_j = λ_i/λ_j exactly. This is condition (G1):

  (G1)  x_g ≁ (ln λ_g)^4    [non-logarithmic sectoral coverage law].

## 4. The deeper obstacle the comparison exposes: q-dependence

n_g^λ is q-independent; n_g^σ ~ √q is q-dependent. A physical generation depth (a mass) must be
q-independent. So the rank-novelty stops live in the regularisation (the prime q), not directly in the
physics, and the q-dependence must cancel in observable ratios. Spell it out under the two mass laws on
record in the fermionic front:

(a) Exponential law A(n)=exp(β* n) (the one the cancellation lemma uses):
    A(n_i^σ)/A(n_j^σ) = exp(β*√q · Δ_{ij}),   Δ_{ij} = (x_i/C_Heis)^{1/4} − (x_j/C_Heis)^{1/4}.
    A large, q-stable ratio then requires
      (G2a)  Δ_{ij} ∝ 1/√q   with   β*√q·Δ_{ij} ≈ ln(target) ≈ 8.
    I.e. the inter-sector coverage differences must shrink EXACTLY as 1/√q — a sharp, fine-tuned,
    falsifiable requirement, neither guaranteed nor natural.

(b) Inverse law M_i ~ E_P/n_proj (`eq:mass-def`):
    M_j/M_i = n_i^σ/n_j^σ = (x_i/x_j)^{1/4},   q-independent automatically (the √q cancels) —
    but then the hierarchy ~3477 needs (x_i/x_j)^{1/4} ≈ 3477, i.e. a sectoral coverage spread
      (G2b)  x_i/x_j ≈ 1.5×10^14,
    which is absurd (x_g ≤ O(1) by construction, |B|/q²).

## 5. Verdict — the gate is (very likely) NOT passed

For rank-novelty Φ to unlock the hierarchy, one needs (G1) AND a resolution of the q-dependence:

- Under (a): (G1) ∧ (G2a). (G2a) demands inter-sector coverage gaps tuned to 1/√q so that β*√q·Δ ≈ 8.
  Possible only with a very specific sectoral law; no corpus mechanism forces it.
- Under (b): the √q cancels for free, but the required coverage spread (G2b ~ 10^14) is impossible since
  x_g ≤ O(1).

Either way the rank-novelty route hits a quantitative wall of the SAME flavour the fermionic front
already documented (the ~3477 hierarchy is carried by no forced quantity). The comparison adds a precise
reason: under the inverse mass law the rank-novelty ratio is bounded by the O(1) coverage spread (no
hierarchy), and under the exponential law it needs a fine-tuned 1/√q sectoral scaling (no forced
mechanism). The earlier λ-crossing no-go (cancellation) and these two obstructions are three faces of
the same fact: an O(1)-controlled depth family cannot manufacture a 10³–10⁴ ratio without an input of
that size.

  Gate: rank-novelty stops break the cancellation?  →  NO, not by default; only under an unforced
  fine-tuned sectoral coverage law (G1 ∧ G2a) that the corpus does not supply.

## 6. Recommendation (decision for the P1→P3 fork)

- Do NOT invest in the shellwise Φ machinery (C) FOR THE HIERARCHY. Its β* justification already
  vanished (P0: β* decoupled from Φ), and its n_g justification fails this gate.
- KEEP x_1(q) as an autonomous SPECTRAL result: the exact reduction n_1=(x_1/C_Heis)^{1/4}√q, the
  model-free n_1/q→0, and the open law of x_1(q) stand on their own (the CC-Note), independent of the
  hierarchy programme.
- Φ would become worth building only if a concrete sectoral structure is exhibited that satisfies
  (G1) ∧ (G2a) — i.e. a forced reason for the sectoral coverage gaps to scale as 1/√q with the right
  prefactor. That is now the single precise thing to look for BEFORE any heavy construction; absent it,
  the hierarchy is not a coverage/Φ problem.

## Status

Structural analysis, not a theorem: it shows the rank-novelty route faces a quantitative obstruction
under both recorded mass laws, strongly suggesting (but not proving) the gate fails. The one escape
(G1 ∧ G2a) is named precisely so it can be tested if a sectoral candidate ever appears.
