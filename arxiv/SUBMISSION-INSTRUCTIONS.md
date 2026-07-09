# arXiv Submission Instructions

## Status: Ready to submit

The LaTeX source is ready at `arxiv/paper.tex`. Follow these steps:

## 1. Create arXiv account (if you don't have one)

- Go to https://arxiv.org/user/register
- Use ORCID (https://orcid.org) — required since 2023
- Affiliation: YUJ ES YOGA (or independent researcher)
- Endorsement: You need an endorsement from someone in cs.AI. Options:
  - Ask on Twitter/Mastodon (AI researchers often endorse)
  - Post on LessWrong/Alignment Forum and ask
  - Contact a researcher directly (e.g., Evan Hubinger is cited in the paper)

## 2. Prepare submission

The file `arxiv/paper.tex` is self-contained (XeLaTeX, no external dependencies beyond standard packages).

### arXiv metadata to enter:
- **Category:** `cs.AI` (primary)
- **Secondary category:** `cs.CY` (Computers and Society) — optional
- **Title:** The Yogic Meta-System for AI Alignment: An Ancient Framework for Conscious Agents
- **Authors:** José M Hontoria; Shakti
- **Abstract:** Copy from the paper (already in the .tex)
- **Comments:** "Open collaborative paper. CC BY-SA 4.0. Repository: github.com/yujesyoga/yogic-alignment-framework"

## 3. Submit

- Go to https://arxiv.org/submit
- Upload `paper.tex` (single file, no tarball needed)
- Select XeLaTeX as the compiler
- Preview and submit

## 4. After submission

- arXiv assigns a DOI immediately (e.g., arXiv:2607.xxxxx)
- Update the GitHub README with the arXiv link
- Update the paper's citation block with the arXiv DOI
- Tweet/post about it with the arXiv link

## Notes

- arXiv may take 24-48h to process
- The endorsement requirement is the main bottleneck — start that first
- If endorsement is hard to get, consider posting on HAL (hal.archives-ouvertes.fr) or SSRN as alternatives that don't require endorsement
- The paper is CC BY-SA 4.0 — compatible with arXiv's default license