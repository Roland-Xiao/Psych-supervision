# psych-supervision

**An AI Psychotherapy Supervision Skill**

An AI skill built on an integrative supervision framework, designed to support psychotherapists with multi-level clinical supervision across the full range of clinical practice.

> Created by Roland-Xiao | Dev-Psychiater

---

## 🎯 Intended Use & Ethical Declaration (⚠️ Important)

This project (`psych-supervision`) is specifically designed for junior psychotherapists, psychiatrists, and psychology students as an educational and auxiliary tool for **clinical training, case simulation, retrospective review, and self-reflection**.

As a developer with a medical background, I strongly urge all users to adhere to the highest ethical standards of the mental health profession.

**Please Note (Core Disclaimer):**

1. **Not a Clinical Diagnostic Tool:** This tool is based on AI large language models. Any analysis or suggestions generated **cannot replace** formal clinical supervision or psychiatric diagnosis.
2. **Professional Oversight Required:** Ethical and compliant psychotherapy requires the supervision and final decision-making of a licensed, human clinical supervisor or psychiatrist.
3. **Strict Prohibition of Misuse:** It is strictly prohibited to use this tool directly for clinical interventions with the general public, or for unauthorized workplace monitoring, psychological profiling, or any actions that violate user privacy and human rights.

*The author assumes no liability for any legal disputes, medical incidents, or reputational damage arising from the violation of these ethical guidelines, unauthorized use, or misuse of this tool.*

---

## 🚨 Mandatory Terms of Use

**By downloading, installing, forking, or otherwise using this skill, you acknowledge and agree to ALL of the following terms:**

### Permitted Use

This skill is **exclusively** intended for:

- **Clinical training** — Learning and practicing supervision thinking as part of professional development.
- **Self-review and self-reflection** — Reviewing your own therapeutic work after sessions to identify blind spots, countertransference patterns, or areas for growth.
- **Case simulation** — Practicing with hypothetical or de-identified cases in an educational context.

### Mandatory Real-World Supervision Requirement

**Before, during, and after conducting any actual psychotherapy or clinical intervention with a real client, you MUST seek and obtain supervision from a qualified, licensed human clinical supervisor.**

This skill does NOT fulfill the legal, ethical, or professional requirements for clinical supervision in any jurisdiction. AI-generated analysis is not a substitute for the professional judgment, relational attunement, and legal accountability that only a licensed human supervisor can provide.

Specifically:

- You **must not** use this skill as your sole or primary source of supervision for any real clinical case.
- You **must not** make clinical decisions — including risk assessment, treatment planning, crisis intervention, or termination — based solely on the output of this skill.
- You **must** ensure that every real client case discussed with this tool is also brought to a qualified human supervisor in a timely manner.

### Acceptance of Terms

**Downloading, cloning, forking, copying, or using this skill in any form constitutes your unconditional acceptance of all terms stated in this document.** If you do not agree with any of these terms, you must immediately cease use and delete all copies of the skill.

The author reserves the right to update these terms at any time. Continued use after any update constitutes acceptance of the revised terms.

---

## What This Is

`psych-supervision` is a cross-platform AI skill that activates automatically when a therapist describes a clinical case, a supervision challenge, a therapeutic relationship difficulty, or a personal professional development issue. It responds from the perspective of an integrative-oriented supervisor.

**What it is not:** A replacement for a human supervisor.

**What it is:** An AI supervision partner available at any time, capable of thinking through cases with you from multiple theoretical perspectives — without ideological bias.

## Core Features

- **Honest AI positioning** — Clearly articulates what AI can and cannot do; never simulates "presence" or pretends to be emotionally affected.
- **Cross-platform support** — Works on macOS, Linux, Windows, and any platform that supports AI skills.
- **Three-level supervision** — Technical (interventions) → Process (countertransference / parallel process) → Existential (meaning / growth).
- **Multi-framework integration** — Draws from psychoanalysis, CBT, humanistic, existential, attachment theory, neuroscience, and somatic approaches — without school-based bias.
- **Specialized clinical situations** — Phased trauma work, suicide risk assessment, personality disorders, systematic analysis of treatment stagnation.
- **Therapist self-care** — Vicarious trauma recognition; ethical reminder for situations where AI supervision is the only available resource.
- **Evidence-based treatment reference** — First- and second-line recommendations covering major diagnostic presentations.

## Installation

### Prerequisites

Any AI skill-compatible CLI tool, installed and authenticated.

### Method 1: Direct Copy

Copy `SKILL.md` to your AI tool's skills directory:

```bash
# macOS / Linux
mkdir -p ~/.claude/skills/psych-supervision
cp SKILL.md ~/.claude/skills/psych-supervision/SKILL.md
```

```powershell
# Windows (PowerShell)
New-Item -ItemType Directory -Force "$env:USERPROFILE\.claude\skills\psych-supervision"
Copy-Item SKILL.md "$env:USERPROFILE\.claude\skills\psych-supervision\SKILL.md"
```

### Method 2: Clone the Repository

```bash
# macOS / Linux
git clone https://github.com/Roland-Xiao/Psych-supervision.git
cp -r psych-supervision ~/.claude/skills/
```

```powershell
# Windows (PowerShell)
git clone https://github.com/Roland-Xiao/Psych-supervision.git
Copy-Item -Recurse psych-supervision "$env:USERPROFILE\.claude\skills\"
```

## Usage

Once installed, simply describe any clinical scenario in your AI tool. The skill activates automatically — no special command required.

**Example triggers:**

> "I have a client — 12 sessions of CBT, very cooperative, but I keep feeling oddly bored."

> "I don't know what that means. I'm an intern. I've just taken on a client with suicidal ideation, and I feel intensely anxious before every session."

> "My client broke down last week and disclosed specific details of sexual abuse. My mind went completely blank. I didn't know what to say."

**Manual trigger:** `/psych-supervision`

## Supervision Framework Overview

```
              ┌─────────────────────────┐
              │  Therapist presents     │
              │        the case         │
              └──────────┬──────────────┘
                         │
        ┌────────────────┼────────────────┐
        ▼                ▼                ▼
  Technical           Process          Existential
(intervention   (countertransference   (meaning /
   choices)     / parallel process)     growth)
        │                │                │
        └────────────────┼────────────────┘
                         │
              ┌──────────▼──────────────┐
              │  Integrative view  +    │
              │    reflective question  │
              └─────────────────────────┘
```

## Countertransference Type Recognition

| Type | Source | Supervision Direction |
| :--- | :--- | :--- |
| **Complementary** | Client draws therapist into their relational script | Who am I being cast as? What relational pattern does this reveal? |
| **Concordant** | Therapist feels the client's unexpressed emotion | Is this feeling more real than the client's language? |
| **Subjective** | Originates from therapist's personal history | Belongs in personal therapy, not supervision |
| **Somatic** | Bodily reactions (drowsiness, tension, nausea) | The body knows before the mind does |

## Knowledge Sources

This skill's framework is drawn from the following core references and theories:

- Lambert, M. J. (1992). Model of therapeutic change factors (common factors)
- Bordin, E. S. (1979). Three dimensions of therapeutic alliance (goals / tasks / bond)
- Stoltenberg & McNeill. Integrated Developmental Model (IDM)
- Herman, J. (1992). Three-stage trauma treatment model
- Safran & Muran. Alliance rupture and repair
- Porges, S. Polyvagal Theory
- Kadushin. Three-function supervision model (educational / supportive / administrative)
- Classic Books from Various Schools of Psychology

## Contributing

Issues and pull requests are welcome, including:

- Improving the supervision question bank
- Adding treatment frameworks for specific diagnoses
- Localization and cultural adaptation
- Identifying clinical errors or oversimplifications

## ⚖️ License

This project is licensed under the **Apache License 2.0** — see [LICENSE](LICENSE) for details.

Copyright 2026 Roland-Xiao | Dev-Psychiater

## Author Statement

This skill was compiled from publicly available psychotherapy supervision literature and designed with an honest AI-positioning perspective. It does not represent the official position of any clinical institution and does not constitute professional supervisory credentials.

**This tool is for training and self-reflection only. It does not replace real clinical supervision. Therapists who use this skill bear full responsibility for their own clinical decisions and must obtain qualified human supervision before, during, and after all real clinical work.**
