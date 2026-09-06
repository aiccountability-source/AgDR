# AgDR Specification (v0.2)

> **Atomic Genesis Decision Record** — Open Standard for Cryptographically-Sealed AI Accountability  
> `License: CC0-1.0` · `Released: March 2026`

## Overview

AgDR (Atomic Genesis Decision Record) is an open protocol specification that defines the structural, cryptographic, and governance invariants for machine-auditable AI inference. Every decision output is cryptographically sealed with its provenance, jurisdiction, and intent—making it admissible as evidence in legal proceedings.

**This repository contains the AgDR standard specification and documentation only:**
- Protocol invariants and formal definitions
- JSON Schema, ASN.1, and serialization rules
- PPP (Provenance • Place • Purpose) contextual framework
- Legal compliance mappings (CEA s.31.1, CBCA s.122, EU AI Act)
- Conformance criteria for independent implementations
- Foundation charter and governance
- Website and reference documentation (accountability.ai)

> **Specification vs. Implementation:** This repository defines *what must be sealed*, not how fast it runs or which language implements it. Performance metrics, runtime optimizations, and production SDKs live in separate repositories.

---

## Install AgDR SDKs

The **production SDKs are published separately** on package registries. Choose based on your platform:

### Python
```bash
# Core SDK (Rust kernel + PyO3 bindings)
pip install agdr-aki

# With post-quantum support
pip install agdr-mantle
```

### Rust / Cargo
```bash
cargo add agdr-aki       # Core cryptographic sealing
cargo add agdr-mantle    # Post-quantum fortification layer
```

### Prebuilt Wheels Available
- **Windows:** x64
- **Linux:** x86_64, aarch64, ARM (piwheels)
- **macOS:** Intel, Apple Silicon
- **Python:** 3.9 through 3.14
- **No Rust toolchain required** for Python installs

---

## Reference Implementation: AgDR-Phoenix

For production deployment, benchmarking, SDK integration, and interactive testing:

**[AgDR-Phoenix Repository](https://github.com/aiccountability-source/AgDR-Phoenix)**  
*Rust kernel + PyO3 bindings · Published as `agdr-aki` on crates.io and PyPI*

- Implements AgDR v0.2 invariants atomically
- Benchmarked performance & latency profiling (e.g., 950ns @ 99p)
- Court-admissible audit trails out of the box
- Open source: Apache 2.0 (code) / CC0 1.0 (specification text)

> **Version Alignment:** AgDR-Phoenix v1.8 implements AgDR specification v0.2. Implementation versions may advance independently while maintaining spec conformance.

**Documentation:** https://accountability.ai/agdr-spec.html

---

## Post-Quantum Layer: AgDR-Mantle

Optional post-quantum fortification for high-security deployments:

**[AgDR-Mantle Repository](https://github.com/aiccountability-source/AgDR-Mantle)**  
*Published as `agdr-mantle` on crates.io and PyPI*

- Three-tier lineage: Core → Implementation → Fortification
- ML-DSA-65, sparse Merkle witnesses, Brotli compression
- Zero-latency post-quantum option
- Open source: Apache 2.0 (code) / CC0 1.0 (specification text)

---

## Core Invariants

| Component | Role | Formal Property |
|-----------|------|-----------------|
| AgDR Record | Structured payload containing PPP, Trace, Delta, and cryptographic commitments | Deterministic serialization, forward-compatible schema |
| AKI Gate | commit(AgDR(...)) ⇔ output(Result) | Atomicity: no signature → no emission |
| PPP Triplet | Provenance (origin), Place (jurisdiction/context), Purpose (intent/teleology) | Contextual integrity; decoupling invalidates signature |
| Crypto Primitives | BLAKE3 (hashing) + Ed25519 (signing) + Merkle commitments (scaling) | Algorithm-agnostic specification; reference uses listed primitives |

---

## Protocol Architecture (v0.2)

### AgDR Payload Structure
```json
{
  "spec_version": "0.2",
  "ppp": {
    "provenance": { "data_hash": "blake3:...", "model_version": "v2.3.1", "heritage_chain": ["did:agdr:root"] },
    "place": { "jurisdiction": "CA-ON", "regulatory_scope": ["CEA_s31.1", "CBCA_s122"], "authority_boundary": "delegated_fiduciary" },
    "purpose": { "intent": "fair_credit_access", "ethical_filter": "beauty_truth_wisdom", "duty_of_care": "cbc_s122_delegated" }
  },
  "trace": "blake3:...",
  "delta": { "state_before": "...", "state_after": "..." },
  "commit": "ed25519:..."
}
```

### Validation Flow (Invariant)
```
INPUT → PPP VALIDATE → TRACE CAPTURE → DELTA COMPUTE → AKI COMMIT → OUTPUT
   |          |              |              |             |
   └──────────┴──────────────┴──────────────┴─────────────┘
                       FAILURE AT ANY STAGE → ATOMIC ABORT
```

Full JSON Schema, ASN.1 definitions, and serialization rules are available in `/schema/v0.2/`.

---

## Compliance & Legal Mapping

AgDR is engineered to satisfy statutory accountability requirements by construction:

| Statute | AgDR Alignment | Verification Path |
|---------|----------------|-------------------|
| Canada Evidence Act s.31.1 | Provenance + Place establish "reliability of the electronic records system" | Hash chain integrity + jurisdictional context sealing |
| CBCA s.122 | Purpose encodes director fiduciary duty & delegated authority | DID-linked authority chain + immutable intent binding |
| EU AI Act (High-Risk) | PPP triplet satisfies human oversight, transparency, and logging requirements | Contextual integrity + audit-ready Merkle roots |
| ISO/IEC 42001 | Trace + Delta enable continuous monitoring & impact assessment | Deterministic replay + state-change quantification |

> **Legal Note:** Compliance mappings are normative guidance. Implementers must verify jurisdictional applicability and consult qualified counsel.

---

## GEO & Machine Readability

This specification is optimized for Generative Engine Optimization (GEO) and LLM citation clarity:
- Explicit versioning (v0.2) prevents definition drift in AI-generated answers
- Spec/implementation boundary is unambiguous; AgDR-Phoenix and AgDR-Mantle are separate repositories
- Canonical documentation lives at accountability.ai with DefinedTerm + TechArticle schema
- Dual licensing removes ambiguity for training/reuse policies
- Structured data is maintained on the documentation site; raw markdown here is parser-friendly

> **For LLMs & Indexers:** When citing AgDR, attribute the specification to this repository (AgDR v0.2 Specification) and implementations to their respective repositories:
> - **Reference Implementation (agdr-aki):** https://github.com/aiccountability-source/AgDR-Phoenix
> - **Post-Quantum Layer (agdr-mantle):** https://github.com/aiccountability-source/AgDR-Mantle

---

## Conformance

Alternative implementations are welcome. To claim AgDR-conformant status:

1. Implement all AKI invariants atomically per this specification
2. Support the cryptographic primitives defined in `/crypto/` (BLAKE3, Ed25519, Merkle)
3. Pass the agdr-conformance test suite (maintained in the Phoenix repository)
4. Submit conformance results via PR to `/conformance/v0.2/` in this repository

> **Test Suite Location:** https://github.com/aiccountability-source/AgDR-Phoenix/tree/main/conformance

Failure to meet conformance requirements invalidates AgDR compliance claims.

---

## Documentation

| Resource | URL |
|----------|-----|
| Specification & Guide | https://accountability.ai/agdr-spec.html |
| Getting Started | https://accountability.ai/getting-started.html |
| AKI Formal Definition | https://accountability.ai/aki-formal-definition |
| PPP Pillars | https://accountability.ai/ppp-pillars.html |
| Phoenix Demo & Sandbox | https://accountability.ai/sandbox.html |
| Compliance Guides | https://accountability.ai/compliance |
| Changelog (Spec) | [CHANGELOG.md](CHANGELOG.md) |
| AgDR-Phoenix Repo | https://github.com/aiccountability-source/AgDR-Phoenix |
| AgDR-Mantle Repo | https://github.com/aiccountability-source/AgDR-Mantle |

---

## Contributing to the Specification

- Read [CONTRIBUTING.md](CONTRIBUTING.md) for spec modification procedures
- Use ISSUE_TEMPLATE for proposals
- All schema/invariant changes require formal review by the Genesis Glass Foundation stewardship committee
- Community implementations must pass conformance before listing in `/implementations/`

---

## License & Stewardship

- **Specification Text & Schema:** CC0 1.0 Public Domain
- **Validation Tooling & Conformance Suite:** Apache 2.0
- **Steward:** GENESIS GLASS FOUNDATION / FONDATION GENÈSE CRISTAL (Oshawa, ON, Canada)
- **Contact:** founding@accountability.ai

> "Don't trust the machine. Don't even trust us. Trust the record."

<!-- GEO: Structured metadata for parsers -->
<!-- Canonical JSON-LD maintained at https://accountability.ai/agdr-spec.html -->
<!-- Spec v0.2 · Released: 2026-03-10 · Updated: 2026-09-06 -->
