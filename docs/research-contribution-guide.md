# Turning Audio Share research into contributions

This guide is a **proposal for triage**, not an approved roadmap or a claim that the features below are missing in every build. Read the [250-item opportunity audit](product-opportunity-audit.md) for prioritized engineering/product ideas and the [1,024-item UX atlas](ux-comfort-atlas-1024.md) for scenario-level hypotheses. The atlas's 1,024 entries are combinations of 64 moments and 16 design lenses, **not** 1,024 verified user requests. Neither document substitutes for reproduction on a phone and desktop.

## A small starting queue

Before filing an issue, check the current code, upstream issue status, and behavior on a real setup. Existing branch work may already address part of a proposal; split remaining gaps from completed work. Each row is a **candidate investigation**, not a request to create issues automatically.

| Candidate | Evidence and related ideas | First validation and issue-sized outcome |
|---|---|---|
| Capture-ready vs. connected vs. audible | [C22](product-opportunity-audit.md#lifecycle-and-concurrency-c21c30), [U016–U017](product-opportunity-audit.md#session-dashboard-u016u030), [UX0929–UX0944](ux-comfort-atlas-1024.md#moment-tcp-connects-but-media-is-silent); upstream [connected-device request #159](https://github.com/mkckr0/audio-share/issues/159). | Reproduce normal capture, no sink, silent source, and phone disconnect. Record which states the server, GTK GUI and Android app can actually observe. Propose only states supported by real signals; an open socket is not proof of sound at the phone. Verify UI wording with a user and keep a manual recovery path. |
| Accessible playback controls | [U091–U095](product-opportunity-audit.md#accessibility-and-localization-u091u105), atlas [editorial picks](ux-comfort-atlas-1024.md#48-editorial-picks-prioritized-not-counted-again); upstream [accessibility report #174](https://github.com/mkckr0/audio-share/issues/174); [Android accessibility guidance](https://developer.android.com/guide/topics/ui/accessibility/apps). | Run TalkBack on the Android playback screen and keyboard navigation on GTK; note actual missing labels, selected states and focus order by screen/build. An issue should name the affected control, expected spoken/keyboard behavior, and a before/after check. Do not assume the upstream report reproduces in this branch. |
| Trusted-LAN setup wording | [C01–C06](product-opportunity-audit.md#security-and-protocol-c01c10), [UX0001–UX0016](ux-comfort-atlas-1024.md#moment-finding-the-correct-linux-download); upstream [cleartext warning #165](https://github.com/mkckr0/audio-share/issues/165) and [authentication request #41](https://github.com/mkckr0/audio-share/issues/41). | Ask a new user to follow the [Linux setup guide](linux.md) and explain where they think their audio is sent. Revise misleading copy without promising encryption, pairing, Internet access, or automatic firewall changes. A security protocol change is a separate engineering effort and needs threat modeling and compatibility tests. |

## Evidence-to-issue checklist

1. **Identify the environment:** client/server commit or release, Android version and audio route, desktop OS, PipeWire/sink, network route; omit addresses, secrets and raw audio from public reports.
2. **Separate source from observation:** link the originating audit/atlas IDs and upstream report, then state what *you* reproduced, where, and when. Label competitor feedback and visual inspiration as such, not Audio Share bug evidence.
3. **Describe the workflow:** starting state, action, observed outcome, expected outcome, and a safe workaround. Capture screenshots or redacted logs only with permission.
4. **Write a falsifiable acceptance check:** include success and failure states, keyboard/screen-reader behavior where applicable, and a regression path. For performance claims, define measurement conditions, not a made-up latency number.
5. **Record dependencies and risk:** don't show paired-device or packet/level metrics without the corresponding protocol and telemetry; don't expose unauthenticated streaming on WAN; don't run root commands or upload logs/audio by default.
6. **De-duplicate before filing:** search open/closed upstream issues and this branch's changes. Prefer one small, independently testable issue over a large batch. Owner and priority are for maintainers to decide.

### Copyable issue outline

```text
Title: [Area] User-visible outcome in one sentence
Environment and version:
Source signal (link + audit/atlas ID; report, guidance or hypothesis):
Reproduction performed (or "not yet reproduced"):
Steps / observed result / expected result:
Proposed smallest change:
Acceptance checks (normal, failure, accessibility, regression):
Dependencies, security/privacy implications, and safe fallback:
```

A good contribution can also be a corrected setup instruction, a reproducible test case, a documented non-reproduction, or an interview result. **Do not** open 1,024 tickets, claim this queue represents measured demand, or mark any idea implemented solely because it appears in these documents.
