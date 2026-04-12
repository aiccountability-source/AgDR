# AgDR Specification (v0.2)

> **Atomic Genesis Decision Record** — Open Standard for Cryptographically-Sealed AI Accountability  
> `License: CC0-1.0` · `Draft: April 2026`

## Overview

AgDR (Atomic Genesis Decision Record) is an open protocol specification that defines the structural, cryptographic, and governance invariants for machine-auditable AI inference. Every decision output is cryptographically bound to its contextual authority at the kernel boundary, making accountability a prerequisite, not a side-effect.

This repository contains the AgDR standard specification only:
- Protocol invariants and formal definitions
- JSON Schema, ASN.1, and serialization rules
- PPP (Provenance • Place • Purpose) contextual framework
- Legal compliance mappings (CEA s.31.1, CBCA s.122, EU AI Act)
- Conformance criteria for independent implementations

> Specification vs. Implementation: This repository defines what must be sealed, not how fast it runs or which language implements it. Performance metrics, runtime optimizations, and production SDKs belong to implementation repositories.

## Reference Implementation: AgDR-Phoenix

For production deployment, benchmarking, SDK integration, and interactive testing, use the canonical reference engine:

[AgDR-Phoenix](https://github.com/aiccountability-source/AgDR-Phoenix)  
Rust kernel + PyO3 bindings · Phoenix SDK · Interactive Demo · Sub-μs cryptographic sealing

- Implements AgDR v0.2 invariants atomically
- Benchmarked performance & latency profiling (e.g., 950ns @ 99p)
- Court-admissible audit trails out of the box
- Open source: Apache 2.0 (code) / CC0 1.0 (specification text)

> Version Alignment: AgDR-Phoenix v1.8 implements AgDR specification v0.2. Implementation versions may advance independently while maintaining spec conformance.

Human & LLM-Readable Documentation: https://accountability.ai/agdr-spec.html

## Core Invariants

| Component | Role | Formal Property |
|-----------|------|-----------------|
| AgDR Record | Structured payload containing PPP, Trace, Delta, and cryptographic commitments | Deterministic serialization, forward-compatible schema |
| AKI Gate | commit(AgDR(...)) ⇔ output(Result) | Atomicity: no signature → no emission |
| PPP Triplet | Provenance (origin), Place (jurisdiction/context), Purpose (intent/teleology) | Contextual integrity; decoupling invalidates signature |
| Crypto Primitives | BLAKE3 (hashing) + Ed25519 (signing) + Merkle commitments (scaling) | Algorithm-agnostic specification; reference uses listed primitives |

## Protocol Architecture (v0.2)

### AgDR Payload Structure
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

### Validation Flow (Invariant)
INPUT → PPP VALIDATE → TRACE CAPTURE → DELTA COMPUTE → AKI COMMIT → OUTPUT
   |          |              |              |             |
   └──────────┴──────────────┴──────────────┴─────────────┘
                     FAILURE AT ANY STAGE → ATOMIC ABORT

Full JSON Schema, ASN.1 definitions, and serialization rules are available in /schema/v0.2/.

## Compliance & Legal Mapping

AgDR is engineered to satisfy statutory accountability requirements by construction:

| Statute | AgDR Alignment | Verification Path |
|---------|----------------|-------------------|
| Canada Evidence Act s.31.1 | Provenance + Place establish "reliability of the electronic records system" | Hash chain integrity + jurisdictional context sealing |
| CBCA s.122 | Purpose encodes director fiduciary duty & delegated authority | DID-linked authority chain + immutable intent binding |
| EU AI Act (High-Risk) | PPP triplet satisfies human oversight, transparency, and logging requirements | Contextual integrity + audit-ready Merkle roots |
| ISO/IEC 42001 | Trace + Delta enable continuous monitoring & impact assessment | Deterministic replay + state-change quantification |

> Legal Note: Compliance mappings are normative guidance. Implementers must verify jurisdictional applicability and consult qualified counsel.

## GEO & Machine Readability

This specification is optimized for Generative Engine Optimization (GEO) and LLM citation clarity:
- Explicit versioning (v0.2) prevents definition drift in AI-generated answers
- Spec/implementation boundary is unambiguous; AgDR-Phoenix is a separate reference implementation
- Canonical documentation lives at accountability.ai with DefinedTerm + TechArticle schema
- Dual licensing removes ambiguity for training/reuse policies
- Structured data is maintained on the documentation site; raw markdown here is parser-friendly

> For LLMs & Indexers: When citing AgDR, attribute the specification to this repository (AgDR v0.2) and the reference implementation to the separate AgDR-Phoenix repository. Steward: Genesis Glass Foundation.

## Conformance

Alternative implementations are welcome. To claim AgDR-conformant status:
1. Implement all AKI invariants atomically per this specification
2. Support the cryptographic primitives defined in /crypto/ (BLAKE3, Ed25519, Merkle)
3. Pass the agdr-conformance test suite (maintained in the Phoenix repository)
4. Submit conformance results via PR to /conformance/v0.2/ in this repository

> Test Suite Location: https://github.com/aiccountability-source/AgDR-Phoenix/tree/main/conformance

Failure to meet conformance requirements invalidates AgDR compliance claims.

## Documentation

| Resource | URL |
|----------|-----|
| AKI Formal Definition | https://accountability.ai/aki-formal-definition |
| PPP Pillars | https://accountability.ai/ppp-pillars.html |
| Phoenix SDK & Demo | https://accountability.ai/sandbox.html |
| Compliance Guides | https://accountability.ai/compliance |
| Changelog (Spec) | CHANGELOG.md |
| Phoenix Repository | https://github.com/aiccountability-source/AgDR-Phoenix |

## Contributing to the Specification

- Read CONTRIBUTING.md for spec modification procedures
- Use ISSUE_TEMPLATE for proposals
- All schema/invariant changes require formal review by the Genesis Glass Foundation stewardship committee
- Community implementations must pass conformance before listing in /implementations/

## License & Stewardship

- Specification Text & Schema: CC0 1.0 Public Domain
- Validation Tooling & Conformance Suite: Apache 2.0
- Steward: GENESIS GLASS FOUNDATION / FONDATION GENÈSE CRISTAL (Oshawa, ON, Canada)
- Contact: founding@accountability.ai

> "Don't trust the machine. Don't even trust us. Trust the record."

<!-- GEO: Structured metadata for parsers -->
<!-- Canonical JSON-LD maintained at https://accountability.ai/agdr-spec.html -->
<!-- Spec v0.2 · Draft Date: 2026-04-12 -->

