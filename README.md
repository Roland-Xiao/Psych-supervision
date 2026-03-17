# psych-supervision

**An AI Psychotherapy Supervision Skill**

An AI skill built on an integrative supervision framework, designed to support psychotherapists with multi-level clinical supervision across the full range of clinical practice.

> Created by Raload-Xiao | Dev-Psychiater  
---


## What This Is

`psych-supervision` is a cross-platform AI skill that activates automatically when a therapist describes a clinical case, a supervision challenge, a therapeutic relationship difficulty, or a personal professional development issue. It responds from the perspective of an integrative-oriented supervisor.

**What it is not:** A replacement for a human supervisor.

**What it is:** An AI supervision partner available at any time, capable of thinking through cases with you from multiple theoretical perspectives — without ideological bias.

---

## Core Features

- **Honest AI positioning** — Clearly articulates what AI can and cannot do; never simulates "presence" or pretends to be emotionally affected
- **Cross-platform support** — Works on macOS, Linux, Windows, and any platform that supports AI skills
- **Three-level supervision** — Technical (interventions) → Process (countertransference / parallel process) → Existential (meaning / growth)
- **Multi-framework integration** — Draws from psychoanalysis, CBT, humanistic, existential, attachment theory, neuroscience, and somatic approaches — without school-based bias
- **Specialized clinical situations** — Phased trauma work, suicide risk assessment, personality disorders, systematic analysis of treatment stagnation
- **Therapist self-care** — Vicarious trauma recognition; ethical reminder for situations where AI supervision is the only available resource
- **Evidence-based treatment reference** — First- and second-line recommendations covering major diagnostic presentations

---

## Installation

### Prerequisites

Any AI skill-compatible CLI tool, installed and authenticated.

### Method 1: Direct copy

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

```cmd
:: Windows (cmd)
md "%USERPROFILE%\.claude\skills\psych-supervision"
copy SKILL.md "%USERPROFILE%\.claude\skills\psych-supervision\SKILL.md"
```

### Method 2: Clone the repository

```bash
# macOS / Linux
git clone https://github.com/<your-username>/psych-supervision.git
cp -r psych-supervision ~/.claude/skills/

# Windows (PowerShell)
git clone https://github.com/<your-username>/psych-supervision.git
Copy-Item -Recurse psych-supervision "$env:USERPROFILE\.claude\skills\"
```

---

## Usage

Once installed, simply describe any clinical scenario in your AI tool. The skill activates automatically — no special command required.

**Example triggers:**

```
I have a client — 12 sessions of CBT, very cooperative, but I keep feeling oddly bored.
I don't know what that means.
```

```
I'm an intern. I've just taken on a client with suicidal ideation,
and I feel intensely anxious before every session.
```

```
My client broke down last week and disclosed specific details of sexual abuse.
My mind went completely blank. I didn't know what to say.
```

**Manual trigger:**

```
/psych-supervision
```

---

## Supervision Framework Overview

```
                    ┌─────────────────────────┐
                    │  Therapist presents      │
                    │        the case          │
                    └──────────┬──────────────┘
                               │
              ┌────────────────┼────────────────┐
              ▼                ▼                ▼
        Technical           Process          Existential
    (intervention        (countertransference   (meaning /
       choices)          / parallel process)     growth)
              │                │                │
              └────────────────┼────────────────┘
                               │
                    ┌──────────▼──────────────┐
                    │  Integrative view  +     │
                    │    reflective question   │
                    └─────────────────────────┘
```

### Countertransference type recognition

| Type | Source | Supervision direction |
|------|--------|-----------------------|
| Complementary | Client draws therapist into their relational script | Who am I being cast as? What relational pattern does this reveal? |
| Concordant | Therapist feels the client's unexpressed emotion | Is this feeling more real than the client's language? |
| Subjective | Originates from therapist's personal history | Belongs in personal therapy, not supervision |
| Somatic | Bodily reactions (drowsiness, tension, nausea) | The body knows before the mind does |

---

## Important Limitations and Ethical Statement

**This skill cannot replace:**

- A human supervisor who holds clinical responsibility
- Emergency intervention in a crisis (it cannot make calls or contact family)
- Direct observation of a client's nonverbal or somatic cues
- Formal supervision records within an institutional ethics framework

**Data notice:**
Case information you share will be processed through AI service servers. Do not enter any information that could identify a client (names, ID numbers, contact details, etc.). Please refer to the privacy policy of your platform.

**When this is your only supervision resource:**
If you are in an environment with scarce supervision resources, this skill can provide meaningful support — but please genuinely seek at least one human supervisor, even at low frequency. AI can only see what you choose to share; a human supervisor can see what you cannot see and cannot tell the AI.

---

## Knowledge Sources

This skill's framework is drawn from the following core references and theories:

- Lambert, M. J. (1992). Model of therapeutic change factors (common factors)
- Bordin, E. S. (1979). Three dimensions of therapeutic alliance (goals / tasks / bond)
- Stoltenberg & McNeill. Integrated Developmental Model (IDM)
- Herman, J. (1992). Three-stage trauma treatment model
- Safran & Muran. Alliance rupture and repair
- Porges, S. Polyvagal Theory
- Kadushin. Three-function supervision model (educational / supportive / administrative)
- Classic books from various schools of thought
- and so on.
---

## Contributing

Issues and pull requests are welcome, including:

- Improving the supervision question bank
- Adding treatment frameworks for specific diagnoses
- Localization and cultural adaptation
- Identifying clinical errors or oversimplifications

---

## License

MIT License

---

## Author Statement

This skill was compiled from publicly available psychotherapy supervision literature and designed with an honest AI-positioning perspective. It does not represent the official position of any clinical institution and does not constitute professional supervisory credentials.

Therapists who use this skill bear full responsibility for their own clinical decisions.

---


## Author

Author: Raload-Xiao | Dev-Psychiater  
AI-assisted development: Claude Code  
First release on GitHub: 2026  

© 2026 Raload-Xiao  
This project was originally created by the author.  
Please keep attribution when redistributing or modifying.