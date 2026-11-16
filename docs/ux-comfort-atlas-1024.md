# Audio Share: 1,024 UX and comfort opportunities

**Research/ideation atlas · 2026-11-15 · not an implementation claim.** This expands [the prioritized 250-item audit](product-opportunity-audit.md). The 1,024 numbered entries are **64 Audio Share usage moments × 16 distinct design lenses per chapter**, not 1,024 independently verified customer requests. They are actionable hypotheses for a user-testing backlog. The 48 editorial picks below are a *shortlist drawn from those themes*, **not additional entries**. No feature described here is asserted to exist; dependencies such as pairing, telemetry, device lists, routing and compression must be implemented before presenting their controls. “Premium” means reliable, considered, safe and comfortable—not a paywall.

## What the research can and cannot say

- **Project signal:** Current repo has an Android Compose player (`HomeScreen.kt`, `AudioScreen.kt`, `NetClient.kt`) and a Linux GTK frontend (`linux-gui/audio-share-gui`, `backend.py`). Upstream requests include [device visibility](https://github.com/mkckr0/audio-share/issues/159), [saved profiles](https://github.com/mkckr0/audio-share/issues/148), [USB mode](https://github.com/mkckr0/audio-share/issues/161), [low latency](https://github.com/mkckr0/audio-share/issues/78), [accessibility](https://github.com/mkckr0/audio-share/issues/174), [nonfunctional sliders](https://github.com/mkckr0/audio-share/issues/171), and [encryption warning](https://github.com/mkckr0/audio-share/issues/165). These are issue reports/requests, **not independently reproduced facts**.
- **Comparable product, not Audio Share reviews:** [1](https://play.google.com/store/apps/details?id=com.georgie.SoundWireFree) (SoundWire Google Play listing/reviews) includes feedback about audible delay, missing output devices and cutouts; [1](https://play.google.com/store/apps/details?id=com.azefsw.audioconnect&hl=en_IN) (AudioRelay listing) exposes Wi-Fi/USB, buffer, compression and remote-volume affordances. Do **not** infer Audio Share has the same bugs or implements those features. Audio Share's listing is [1](https://f-droid.org/packages/io.github.mkckr0.audio_share_app/) (F-Droid); I did not find a verified Audio Share Google Play listing. [2](https://www.reddit.com/r/androidapps/comments/k6wrv6/best_pc_audio_streaming_app/) (Reddit) compares delay, buffer tuning and USB; [7](https://www.reddit.com/r/androidapps/comments/55yh0f/free_alternative_for_soundwire/) mentions long-session desync as a concern in a competitor; these are anecdotes, not benchmarks. [5](https://community.audiorelay.net/t/constant-hiccups-and-glitches/101) is a competitor support thread about glitches.
- **Design references, not validated workflows:** [2](https://www.pinterest.com/pin/635570566143845060/) (Pinterest sliders) and [1](https://www.pinterest.com/ideas/dj-software-interface-design/909119586117/) (dashboard ideas) can inspire legible value labels and restrained density, **never copy art/layouts**. Instagram searches yielded generic designer profiles rather than a verifiable Audio Share-relevant post; **no Instagram insight is claimed**. [1](https://developer.android.com/guide/topics/ui/accessibility/apps) recommends accessible controls (including ≥48dp touch targets); [2](https://developer.gnome.org/hig/patterns/feedback.html) distinguishes feedback patterns. [1](https://developer.android.com/reference/android/media/AudioTrack) discusses buffer/underrun tradeoffs.
- **Limits:** No sampled Play reviews are a representative survey; no new user interview, phone hardware test, security audit, accessibility audit, or latency measurement was run for this document. Do not turn perceived latency or “secure” claims into marketing until measured/verified. No cloud upload of sound or logs by default. No automatic root/firewall changes.

## Eight comfort tensions behind the catalog

1. **Connection is not sound.** The project UI can have a listening socket while a phone is not receiving or rendering audio. A trustworthy interface should show capture readiness, connected peer and audible playback independently; the upstream [connected-device request](https://github.com/mkckr0/audio-share/issues/159) highlights the visibility gap.
2. **Delay and resilience compete.** The [AudioTrack API](https://developer.android.com/reference/android/media/AudioTrack) links buffer size to latency and underruns; [2](https://www.reddit.com/r/androidapps/comments/k6wrv6/best_pc_audio_streaming_app/) (Reddit anecdote) favors both low lag and stability. A single “best” preset is not credible without device-specific measurements.
3. **“Easy USB” is usually network tethering.** A [USB feature request](https://github.com/mkckr0/audio-share/issues/161) and [1](https://play.google.com/store/apps/details?id=com.azefsw.audioconnect&hl=en_IN) (competitor listing) signal demand; the first UX step can guide selecting the tether interface without pretending a new wired protocol exists.
4. **Louder is not safer.** The project README separates PC volume, Android media volume, app gain and loudness enhancer. A [third-party review](https://alternativeto.net/software/audio-share/about/) mentions low loudness, but boosting everything can clip; explain each control and test actual output rather than promising equal loudness.
5. **Concealed complexity still needs a way back.** A novice needs one Start button; an expert may need sink IDs and packet diagnostics. Follow [2](https://developer.gnome.org/hig/patterns/feedback.html) (GNOME feedback patterns) with progressive disclosure, not a hidden error log as the sole path to recovery.
6. **A working LAN is not necessarily a trusted LAN.** A [cleartext warning request](https://github.com/mkckr0/audio-share/issues/165) and [authentication request](https://github.com/mkckr0/audio-share/issues/41) make pairing and transport protection prerequisites for any public-network convenience feature.
7. **Visual polish must not outrank access.** [2](https://www.pinterest.com/pin/635570566143845060/) offers slider inspiration, but [1](https://developer.android.com/guide/topics/ui/accessibility/apps) requires touch accessibility and [#174](https://github.com/mkckr0/audio-share/issues/174) reports missing labels. Verify semantics and live effect before polishing a dial.
8. **Long sessions change the problem.** [7](https://www.reddit.com/r/androidapps/comments/55yh0f/free_alternative_for_soundwire/) reports progressive desync in a comparable app; [5](https://community.audiorelay.net/t/constant-hiccups-and-glitches/101) mentions glitches. Those anecdotes justify a long-running test plan, not a claim that this repo has the same defect.

## 48 editorial picks (prioritized, not counted again)

**P0 — truth, safety, and first working stream**

1. Label “server listening” and “audio capture ready” separately; never imply that a phone hears sound from a bound socket.
2. Show phone connection, packet receipt and audible playback as separate states with no fabricated telemetry.
3. Warn that legacy LAN transport is unauthenticated and unencrypted before suggesting public networks.
4. Add pairing and authenticated encryption before any WAN or Internet-sharing affordance.
5. Fix Audio Screen sliders that do not affect the stream before shipping a visual redesign ([#171](https://github.com/mkckr0/audio-share/issues/171)).
6. Add accessible names and selected states for Play/Pause and every icon action ([#174](https://github.com/mkckr0/audio-share/issues/174)).
7. Replace blank loading with a short, cancellable connection sequence and meaningful failure.
8. Make “no audio endpoint” a preflight blocker with a safe workaround and retry.
9. Diagnose wrong address, port and firewall separately instead of “connection failed.”
10. Verify actual host interface and route; do not suggest 127.0.0.1 or an arbitrary private IP.
11. Test normal, silent, reconnecting, stopped and crashed paths using a fake server and on-device playback.
12. Let users see and revoke approved clients once real client authentication exists.

**P1 — comfort and predictability**

13. Give each phone a clearly named saved PC profile with last-success timestamp.
14. Offer a manual host field even when discovery/QR is available; explain DNS and IPv6 limits.
15. Keep the primary Play/Stop action in a stable place across loading and error states.
16. Show current sink, host and port in a glanceable session header.
17. Label volume, phone media volume and loudness enhancer as *different* controls.
18. Give amplification a hearing-safety cue and a safe reset, not a nagging alert.
19. Offer “Stable / Video / Gaming” profiles only after real latency/underrun measurement.
20. Put latency, loss and buffer numbers behind an honest “measured/estimated” distinction.
21. Tune AudioTrack buffering against underruns, not a made-up milliseconds promise.
22. Explain why Bluetooth headphones can add delay compared with phone speakers.
23. Make Linux sink refresh nonblocking and preserve a valid selection after hotplug.
24. Show a connected-phone list on desktop when protocol instrumentation can supply one ([#159](https://github.com/mkckr0/audio-share/issues/159)).
25. Make USB tethering setup a guided route with adapter/IP checks, not a new fake “USB protocol.”
26. Keep the server active on close only after a clear, reversible opt-in.
27. Follow system dark/light mode and fix the bright Android cold-launch splash ([#180](https://github.com/mkckr0/audio-share/issues/180)).
28. Make status understandable without color; audit keyboard focus and TalkBack order.
29. Turn technical logs into a redacted, optional Details drawer with copyable timestamps.
30. Give errors one contextual next action (Retry, Refresh sinks, Choose host, Open Help).
31. Distinguish a quiet source from a disconnected phone and an unavailable sink.
32. Preserve state across Android rotation and process recreation without phantom playback.

**P2 — differentiated but contingent**

33. Offer a local-only latency lab with repeatable test signal and user-visible limitations.
34. Add multi-device volume only after per-device authenticated sessions and actual telemetry.
35. Offer a dry-run firewall guide, never silently modify firewalld/ufw settings.
36. Support optional reminder to stop after a long session, default off.
37. Add a private listening mode that guides reversible PC output routing.
38. Add a “hear both PC and phone” explanation with echo warning when both outputs are active.
39. Make silence power saving explain the wake-up delay and show an opt-out.
40. Publish a device/OS compatibility chart from repeatable test reports.
41. Allow a diagnostics export preview with explicit Save and automatic secret redaction.
42. Add a keyboard-first compact desktop status surface before decorative waveform animations.
43. Explore a local, opt-in troubleshooting assistant only after a rules-only baseline works.
44. Treat Instagram/Pinterest aesthetics as prompts to test, never copied UI or proof of demand.
45. Make every installer say exactly which distro/library ABI it expects.
46. Offer a simple one-click Reset to Last Working Setup with an undo path.
47. Measure first-success rate, time to recovery and audible underruns with consent, not vanity screen views.
48. Refuse cloud sound/log upload and Internet port exposure as default UX paths.

## How to read the 1,024 entries

Every `UX####` line is a proposed micro-improvement for one specific **moment**. The chapter's 16 lenses cover copy, preflight, feedback, controls, recovery, inclusive input, privacy and measurement. Some depend on future telemetry, secure pairing or routing. An entry is ready for engineering only after validating the relevant workflow with real users and writing a falsifiable acceptance test. Use [the 250-item audit](product-opportunity-audit.md) for implementation sequencing. These 1,024 are intentionally **not** labeled “all verified needs.”

## 01 · First-run installation and setup

### Moment: finding the correct Linux download

- **UX0001** Name the distro-matched archive in a one-sentence header; avoid assuming the user knows its package or service name.
- **UX0002** Show compatible package selected as a distinct milestone; do not treat a previous setup step as proof of completion.
- **UX0003** Preflight the failure mode “the user picks an Arch binary on Debian” before presenting the primary Start action.
- **UX0004** Offer a one-click path to choose their distro, retaining a manual route for offline users.
- **UX0005** For finding the correct Linux download, preview exactly what files or settings this setup step changes before applying it. Verify “compatible package selected” despite “the user picks an Arch binary on Debian”.
- **UX0006** For finding the correct Linux download, keep a local checklist with the current step highlighted; never silently skip unmet prerequisites. Verify “compatible package selected” despite “the user picks an Arch binary on Debian”.
- **UX0007** Provide a copyable distro-specific setup instruction for distro-matched archive; never run sudo inside the GUI.
- **UX0008** Explain the situation “the user picks an Arch binary on Debian” in plain language and include the smallest safe recovery step.
- **UX0009** For finding the correct Linux download, save completed setup progress locally and make it easy to revisit later. Verify “compatible package selected” despite “the user picks an Arch binary on Debian”.
- **UX0010** Show a concise success confirmation for compatible package selected, followed by the next action.
- **UX0011** For finding the correct Linux download, make the action reachable with keyboard, pointer and screen reader at the same point in the flow. Verify “compatible package selected” despite “the user picks an Arch binary on Debian”.
- **UX0012** For finding the correct Linux download, render setup guidance on a narrow phone and a 540px GTK window without clipped content. Verify “compatible package selected” despite “the user picks an Arch binary on Debian”.
- **UX0013** For finding the correct Linux download, keep technical versions/path details in an expandable panel rather than the first-run hero. Verify “compatible package selected” despite “the user picks an Arch binary on Debian”.
- **UX0014** Never imply compatible package selected without testing its corresponding signal or receiving explicit confirmation.
- **UX0015** For finding the correct Linux download, give a reversible reset for this step without erasing unrelated user preferences. Verify “compatible package selected” despite “the user picks an Arch binary on Debian”.
- **UX0016** Track correct archive selected without help with consent; use it to remove friction, not to auto-upload diagnostics.

### Moment: unpacking the desktop bundle

- **UX0017** Name the archive contents in a one-sentence header; avoid assuming the user knows its package or service name.
- **UX0018** Show GUI and server found as a distinct milestone; do not treat a previous setup step as proof of completion.
- **UX0019** Preflight the failure mode “the extracted folder is mistaken for an installer” before presenting the primary Start action.
- **UX0020** Offer a one-click path to open README.txt, retaining a manual route for offline users.
- **UX0021** For unpacking the desktop bundle, preview exactly what files or settings this setup step changes before applying it. Verify “GUI and server found” despite “the extracted folder is mistaken for an installer”.
- **UX0022** For unpacking the desktop bundle, keep a local checklist with the current step highlighted; never silently skip unmet prerequisites. Verify “GUI and server found” despite “the extracted folder is mistaken for an installer”.
- **UX0023** Provide a copyable distro-specific setup instruction for archive contents; never run sudo inside the GUI.
- **UX0024** Explain the situation “the extracted folder is mistaken for an installer” in plain language and include the smallest safe recovery step.
- **UX0025** For unpacking the desktop bundle, save completed setup progress locally and make it easy to revisit later. Verify “GUI and server found” despite “the extracted folder is mistaken for an installer”.
- **UX0026** Show a concise success confirmation for GUI and server found, followed by the next action.
- **UX0027** For unpacking the desktop bundle, make the action reachable with keyboard, pointer and screen reader at the same point in the flow. Verify “GUI and server found” despite “the extracted folder is mistaken for an installer”.
- **UX0028** For unpacking the desktop bundle, render setup guidance on a narrow phone and a 540px GTK window without clipped content. Verify “GUI and server found” despite “the extracted folder is mistaken for an installer”.
- **UX0029** For unpacking the desktop bundle, keep technical versions/path details in an expandable panel rather than the first-run hero. Verify “GUI and server found” despite “the extracted folder is mistaken for an installer”.
- **UX0030** Never imply GUI and server found without testing its corresponding signal or receiving explicit confirmation.
- **UX0031** For unpacking the desktop bundle, give a reversible reset for this step without erasing unrelated user preferences. Verify “GUI and server found” despite “the extracted folder is mistaken for an installer”.
- **UX0032** Track first launch without a terminal search with consent; use it to remove friction, not to auto-upload diagnostics.

### Moment: installing GTK prerequisites

- **UX0033** Name the PyGObject/GTK dependency check in a one-sentence header; avoid assuming the user knows its package or service name.
- **UX0034** Show graphical runtime available as a distinct milestone; do not treat a previous setup step as proof of completion.
- **UX0035** Preflight the failure mode “the distro's GTK bindings are missing” before presenting the primary Start action.
- **UX0036** Offer a one-click path to install matching runtime packages, retaining a manual route for offline users.
- **UX0037** For installing GTK prerequisites, preview exactly what files or settings this setup step changes before applying it. Verify “graphical runtime available” despite “the distro's GTK bindings are missing”.
- **UX0038** For installing GTK prerequisites, keep a local checklist with the current step highlighted; never silently skip unmet prerequisites. Verify “graphical runtime available” despite “the distro's GTK bindings are missing”.
- **UX0039** Provide a copyable distro-specific setup instruction for PyGObject/GTK dependency check; never run sudo inside the GUI.
- **UX0040** Explain the situation “the distro's GTK bindings are missing” in plain language and include the smallest safe recovery step.
- **UX0041** For installing GTK prerequisites, save completed setup progress locally and make it easy to revisit later. Verify “graphical runtime available” despite “the distro's GTK bindings are missing”.
- **UX0042** Show a concise success confirmation for graphical runtime available, followed by the next action.
- **UX0043** For installing GTK prerequisites, make the action reachable with keyboard, pointer and screen reader at the same point in the flow. Verify “graphical runtime available” despite “the distro's GTK bindings are missing”.
- **UX0044** For installing GTK prerequisites, render setup guidance on a narrow phone and a 540px GTK window without clipped content. Verify “graphical runtime available” despite “the distro's GTK bindings are missing”.
- **UX0045** For installing GTK prerequisites, keep technical versions/path details in an expandable panel rather than the first-run hero. Verify “graphical runtime available” despite “the distro's GTK bindings are missing”.
- **UX0046** Never imply graphical runtime available without testing its corresponding signal or receiving explicit confirmation.
- **UX0047** For installing GTK prerequisites, give a reversible reset for this step without erasing unrelated user preferences. Verify “graphical runtime available” despite “the distro's GTK bindings are missing”.
- **UX0048** Track dependency recovery under three minutes with consent; use it to remove friction, not to auto-upload diagnostics.

### Moment: starting a PipeWire user session

- **UX0049** Name the PipeWire/WirePlumber readiness in a one-sentence header; avoid assuming the user knows its package or service name.
- **UX0050** Show user audio service active as a distinct milestone; do not treat a previous setup step as proof of completion.
- **UX0051** Preflight the failure mode “a root service is confused with the user's service” before presenting the primary Start action.
- **UX0052** Offer a one-click path to inspect user-service status, retaining a manual route for offline users.
- **UX0053** For starting a PipeWire user session, preview exactly what files or settings this setup step changes before applying it. Verify “user audio service active” despite “a root service is confused with the user's service”.
- **UX0054** For starting a PipeWire user session, keep a local checklist with the current step highlighted; never silently skip unmet prerequisites. Verify “user audio service active” despite “a root service is confused with the user's service”.
- **UX0055** Provide a copyable distro-specific setup instruction for PipeWire/WirePlumber readiness; never run sudo inside the GUI.
- **UX0056** Explain the situation “a root service is confused with the user's service” in plain language and include the smallest safe recovery step.
- **UX0057** For starting a PipeWire user session, save completed setup progress locally and make it easy to revisit later. Verify “user audio service active” despite “a root service is confused with the user's service”.
- **UX0058** Show a concise success confirmation for user audio service active, followed by the next action.
- **UX0059** For starting a PipeWire user session, make the action reachable with keyboard, pointer and screen reader at the same point in the flow. Verify “user audio service active” despite “a root service is confused with the user's service”.
- **UX0060** For starting a PipeWire user session, render setup guidance on a narrow phone and a 540px GTK window without clipped content. Verify “user audio service active” despite “a root service is confused with the user's service”.
- **UX0061** For starting a PipeWire user session, keep technical versions/path details in an expandable panel rather than the first-run hero. Verify “user audio service active” despite “a root service is confused with the user's service”.
- **UX0062** Never imply user audio service active without testing its corresponding signal or receiving explicit confirmation.
- **UX0063** For starting a PipeWire user session, give a reversible reset for this step without erasing unrelated user preferences. Verify “user audio service active” despite “a root service is confused with the user's service”.
- **UX0064** Track working user session without sudo launches with consent; use it to remove friction, not to auto-upload diagnostics.

### Moment: finding an audio sink

- **UX0065** Name the sink availability in a one-sentence header; avoid assuming the user knows its package or service name.
- **UX0066** Show usable sink selected as a distinct milestone; do not treat a previous setup step as proof of completion.
- **UX0067** Preflight the failure mode “no sink appears on a headless machine” before presenting the primary Start action.
- **UX0068** Offer a one-click path to review null-sink guidance, retaining a manual route for offline users.
- **UX0069** For finding an audio sink, preview exactly what files or settings this setup step changes before applying it. Verify “usable sink selected” despite “no sink appears on a headless machine”.
- **UX0070** For finding an audio sink, keep a local checklist with the current step highlighted; never silently skip unmet prerequisites. Verify “usable sink selected” despite “no sink appears on a headless machine”.
- **UX0071** Provide a copyable distro-specific setup instruction for sink availability; never run sudo inside the GUI.
- **UX0072** Explain the situation “no sink appears on a headless machine” in plain language and include the smallest safe recovery step.
- **UX0073** For finding an audio sink, save completed setup progress locally and make it easy to revisit later. Verify “usable sink selected” despite “no sink appears on a headless machine”.
- **UX0074** Show a concise success confirmation for usable sink selected, followed by the next action.
- **UX0075** For finding an audio sink, make the action reachable with keyboard, pointer and screen reader at the same point in the flow. Verify “usable sink selected” despite “no sink appears on a headless machine”.
- **UX0076** For finding an audio sink, render setup guidance on a narrow phone and a 540px GTK window without clipped content. Verify “usable sink selected” despite “no sink appears on a headless machine”.
- **UX0077** For finding an audio sink, keep technical versions/path details in an expandable panel rather than the first-run hero. Verify “usable sink selected” despite “no sink appears on a headless machine”.
- **UX0078** Never imply usable sink selected without testing its corresponding signal or receiving explicit confirmation.
- **UX0079** For finding an audio sink, give a reversible reset for this step without erasing unrelated user preferences. Verify “usable sink selected” despite “no sink appears on a headless machine”.
- **UX0080** Track preflight detects missing sink before Start with consent; use it to remove friction, not to auto-upload diagnostics.

### Moment: installing the launcher

- **UX0081** Name the desktop-entry install in a one-sentence header; avoid assuming the user knows its package or service name.
- **UX0082** Show menu entry usable as a distinct milestone; do not treat a previous setup step as proof of completion.
- **UX0083** Preflight the failure mode “server binary is installed in an unexpected path” before presenting the primary Start action.
- **UX0084** Offer a one-click path to install bundled bin/as-cmd, retaining a manual route for offline users.
- **UX0085** For installing the launcher, preview exactly what files or settings this setup step changes before applying it. Verify “menu entry usable” despite “server binary is installed in an unexpected path”.
- **UX0086** For installing the launcher, keep a local checklist with the current step highlighted; never silently skip unmet prerequisites. Verify “menu entry usable” despite “server binary is installed in an unexpected path”.
- **UX0087** Provide a copyable distro-specific setup instruction for desktop-entry install; never run sudo inside the GUI.
- **UX0088** Explain the situation “server binary is installed in an unexpected path” in plain language and include the smallest safe recovery step.
- **UX0089** For installing the launcher, save completed setup progress locally and make it easy to revisit later. Verify “menu entry usable” despite “server binary is installed in an unexpected path”.
- **UX0090** Show a concise success confirmation for menu entry usable, followed by the next action.
- **UX0091** For installing the launcher, make the action reachable with keyboard, pointer and screen reader at the same point in the flow. Verify “menu entry usable” despite “server binary is installed in an unexpected path”.
- **UX0092** For installing the launcher, render setup guidance on a narrow phone and a 540px GTK window without clipped content. Verify “menu entry usable” despite “server binary is installed in an unexpected path”.
- **UX0093** For installing the launcher, keep technical versions/path details in an expandable panel rather than the first-run hero. Verify “menu entry usable” despite “server binary is installed in an unexpected path”.
- **UX0094** Never imply menu entry usable without testing its corresponding signal or receiving explicit confirmation.
- **UX0095** For installing the launcher, give a reversible reset for this step without erasing unrelated user preferences. Verify “menu entry usable” despite “server binary is installed in an unexpected path”.
- **UX0096** Track launcher starts without environment hacks with consent; use it to remove friction, not to auto-upload diagnostics.

### Moment: first Android launch

- **UX0097** Name the phone first-run path in a one-sentence header; avoid assuming the user knows its package or service name.
- **UX0098** Show PC-to-phone role understood as a distinct milestone; do not treat a previous setup step as proof of completion.
- **UX0099** Preflight the failure mode “user expects Android to transmit instead” before presenting the primary Start action.
- **UX0100** Offer a one-click path to view three-step explanation, retaining a manual route for offline users.
- **UX0101** For first Android launch, preview exactly what files or settings this setup step changes before applying it. Verify “PC-to-phone role understood” despite “user expects Android to transmit instead”.
- **UX0102** For first Android launch, keep a local checklist with the current step highlighted; never silently skip unmet prerequisites. Verify “PC-to-phone role understood” despite “user expects Android to transmit instead”.
- **UX0103** Provide a copyable distro-specific setup instruction for phone first-run path; never run sudo inside the GUI.
- **UX0104** Explain the situation “user expects Android to transmit instead” in plain language and include the smallest safe recovery step.
- **UX0105** For first Android launch, save completed setup progress locally and make it easy to revisit later. Verify “PC-to-phone role understood” despite “user expects Android to transmit instead”.
- **UX0106** Show a concise success confirmation for PC-to-phone role understood, followed by the next action.
- **UX0107** For first Android launch, make the action reachable with keyboard, pointer and screen reader at the same point in the flow. Verify “PC-to-phone role understood” despite “user expects Android to transmit instead”.
- **UX0108** For first Android launch, render setup guidance on a narrow phone and a 540px GTK window without clipped content. Verify “PC-to-phone role understood” despite “user expects Android to transmit instead”.
- **UX0109** For first Android launch, keep technical versions/path details in an expandable panel rather than the first-run hero. Verify “PC-to-phone role understood” despite “user expects Android to transmit instead”.
- **UX0110** Never imply PC-to-phone role understood without testing its corresponding signal or receiving explicit confirmation.
- **UX0111** For first Android launch, give a reversible reset for this step without erasing unrelated user preferences. Verify “PC-to-phone role understood” despite “user expects Android to transmit instead”.
- **UX0112** Track novice can describe the audio direction with consent; use it to remove friction, not to auto-upload diagnostics.

### Moment: first successful sound

- **UX0113** Name the first-stream checklist in a one-sentence header; avoid assuming the user knows its package or service name.
- **UX0114** Show sound confirmed on phone as a distinct milestone; do not treat a previous setup step as proof of completion.
- **UX0115** Preflight the failure mode “connection status is mistaken for audible output” before presenting the primary Start action.
- **UX0116** Offer a one-click path to confirm sound or open checks, retaining a manual route for offline users.
- **UX0117** For first successful sound, preview exactly what files or settings this setup step changes before applying it. Verify “sound confirmed on phone” despite “connection status is mistaken for audible output”.
- **UX0118** For first successful sound, keep a local checklist with the current step highlighted; never silently skip unmet prerequisites. Verify “sound confirmed on phone” despite “connection status is mistaken for audible output”.
- **UX0119** Provide a copyable distro-specific setup instruction for first-stream checklist; never run sudo inside the GUI.
- **UX0120** Explain the situation “connection status is mistaken for audible output” in plain language and include the smallest safe recovery step.
- **UX0121** For first successful sound, save completed setup progress locally and make it easy to revisit later. Verify “sound confirmed on phone” despite “connection status is mistaken for audible output”.
- **UX0122** Show a concise success confirmation for sound confirmed on phone, followed by the next action.
- **UX0123** For first successful sound, make the action reachable with keyboard, pointer and screen reader at the same point in the flow. Verify “sound confirmed on phone” despite “connection status is mistaken for audible output”.
- **UX0124** For first successful sound, render setup guidance on a narrow phone and a 540px GTK window without clipped content. Verify “sound confirmed on phone” despite “connection status is mistaken for audible output”.
- **UX0125** For first successful sound, keep technical versions/path details in an expandable panel rather than the first-run hero. Verify “sound confirmed on phone” despite “connection status is mistaken for audible output”.
- **UX0126** Never imply sound confirmed on phone without testing its corresponding signal or receiving explicit confirmation.
- **UX0127** For first successful sound, give a reversible reset for this step without erasing unrelated user preferences. Verify “sound confirmed on phone” despite “connection status is mistaken for audible output”.
- **UX0128** Track audible-first-stream rate with consent; use it to remove friction, not to auto-upload diagnostics.

## 02 · LAN addressing and connection

### Moment: choosing the PC's LAN address

- **UX0129** Label interface-labeled IPv4 list with its real interface/route, not only a numeric address.
- **UX0130** Show reachable PC IP chosen separately from socket-open and audio-received states.
- **UX0131** Test the failure mode “the first private IP belongs to a VPN” with a targeted check instead of a generic connection toast.
- **UX0132** Surface select a reachable interface next to the failed field, not hidden in global settings.
- **UX0133** For choosing the PC's LAN address, preview PC and phone endpoints before committing a new network profile. Verify “reachable PC IP chosen” despite “the first private IP belongs to a VPN”.
- **UX0134** Keep a safe manual-address fallback when discovery cannot find interface-labeled IPv4 list.
- **UX0135** For choosing the PC's LAN address, show a transient connecting timer and allow Cancel before a retry loop starts. Verify “reachable PC IP chosen” despite “the first private IP belongs to a VPN”.
- **UX0136** For choosing the PC's LAN address, make the host/port error selectable and copyable for technical support. Verify “reachable PC IP chosen” despite “the first private IP belongs to a VPN”.
- **UX0137** Do not recommend opening the entire firewall when the first private IP belongs to a VPN is suspected.
- **UX0138** For choosing the PC's LAN address, retain the last working route and offer a clearly labeled one-tap rollback. Verify “reachable PC IP chosen” despite “the first private IP belongs to a VPN”.
- **UX0139** For choosing the PC's LAN address, use examples matching this route type instead of a hardcoded 192.168.x.x hint. Verify “reachable PC IP chosen” despite “the first private IP belongs to a VPN”.
- **UX0140** For choosing the PC's LAN address, announce route changes accessibly without repeating every packet status. Verify “reachable PC IP chosen” despite “the first private IP belongs to a VPN”.
- **UX0141** For choosing the PC's LAN address, keep network details visible on desktop and condensed on phone. Verify “reachable PC IP chosen” despite “the first private IP belongs to a VPN”.
- **UX0142** For choosing the PC's LAN address, warn before suggesting public hotspot or WAN use of unauthenticated transport. Verify “reachable PC IP chosen” despite “the first private IP belongs to a VPN”.
- **UX0143** For choosing the PC's LAN address, show what changed between a failed route and the last successful route. Verify “reachable PC IP chosen” despite “the first private IP belongs to a VPN”.
- **UX0144** Measure successful first connect and categorize the failure before adding auto-reconnect logic.

### Moment: entering host on Android

- **UX0145** Label host entry with its real interface/route, not only a numeric address.
- **UX0146** Show valid address saved separately from socket-open and audio-received states.
- **UX0147** Test the failure mode “an address typo passes superficial validation” with a targeted check instead of a generic connection toast.
- **UX0148** Surface correct the highlighted octet next to the failed field, not hidden in global settings.
- **UX0149** For entering host on Android, preview PC and phone endpoints before committing a new network profile. Verify “valid address saved” despite “an address typo passes superficial validation”.
- **UX0150** Keep a safe manual-address fallback when discovery cannot find host entry.
- **UX0151** For entering host on Android, show a transient connecting timer and allow Cancel before a retry loop starts. Verify “valid address saved” despite “an address typo passes superficial validation”.
- **UX0152** For entering host on Android, make the host/port error selectable and copyable for technical support. Verify “valid address saved” despite “an address typo passes superficial validation”.
- **UX0153** Do not recommend opening the entire firewall when an address typo passes superficial validation is suspected.
- **UX0154** For entering host on Android, retain the last working route and offer a clearly labeled one-tap rollback. Verify “valid address saved” despite “an address typo passes superficial validation”.
- **UX0155** For entering host on Android, use examples matching this route type instead of a hardcoded 192.168.x.x hint. Verify “valid address saved” despite “an address typo passes superficial validation”.
- **UX0156** For entering host on Android, announce route changes accessibly without repeating every packet status. Verify “valid address saved” despite “an address typo passes superficial validation”.
- **UX0157** For entering host on Android, keep network details visible on desktop and condensed on phone. Verify “valid address saved” despite “an address typo passes superficial validation”.
- **UX0158** For entering host on Android, warn before suggesting public hotspot or WAN use of unauthenticated transport. Verify “valid address saved” despite “an address typo passes superficial validation”.
- **UX0159** For entering host on Android, show what changed between a failed route and the last successful route. Verify “valid address saved” despite “an address typo passes superficial validation”.
- **UX0160** Measure host entry without retries and categorize the failure before adding auto-reconnect logic.

### Moment: choosing a TCP/UDP port

- **UX0161** Label port selector with its real interface/route, not only a numeric address.
- **UX0162** Show both protocols use same port separately from socket-open and audio-received states.
- **UX0163** Test the failure mode “a firewall allows TCP but drops UDP” with a targeted check instead of a generic connection toast.
- **UX0164** Surface test both protocol paths next to the failed field, not hidden in global settings.
- **UX0165** For choosing a TCP/UDP port, preview PC and phone endpoints before committing a new network profile. Verify “both protocols use same port” despite “a firewall allows TCP but drops UDP”.
- **UX0166** Keep a safe manual-address fallback when discovery cannot find port selector.
- **UX0167** For choosing a TCP/UDP port, show a transient connecting timer and allow Cancel before a retry loop starts. Verify “both protocols use same port” despite “a firewall allows TCP but drops UDP”.
- **UX0168** For choosing a TCP/UDP port, make the host/port error selectable and copyable for technical support. Verify “both protocols use same port” despite “a firewall allows TCP but drops UDP”.
- **UX0169** Do not recommend opening the entire firewall when a firewall allows TCP but drops UDP is suspected.
- **UX0170** For choosing a TCP/UDP port, retain the last working route and offer a clearly labeled one-tap rollback. Verify “both protocols use same port” despite “a firewall allows TCP but drops UDP”.
- **UX0171** For choosing a TCP/UDP port, use examples matching this route type instead of a hardcoded 192.168.x.x hint. Verify “both protocols use same port” despite “a firewall allows TCP but drops UDP”.
- **UX0172** For choosing a TCP/UDP port, announce route changes accessibly without repeating every packet status. Verify “both protocols use same port” despite “a firewall allows TCP but drops UDP”.
- **UX0173** For choosing a TCP/UDP port, keep network details visible on desktop and condensed on phone. Verify “both protocols use same port” despite “a firewall allows TCP but drops UDP”.
- **UX0174** For choosing a TCP/UDP port, warn before suggesting public hotspot or WAN use of unauthenticated transport. Verify “both protocols use same port” despite “a firewall allows TCP but drops UDP”.
- **UX0175** For choosing a TCP/UDP port, show what changed between a failed route and the last successful route. Verify “both protocols use same port” despite “a firewall allows TCP but drops UDP”.
- **UX0176** Measure working media after handshake and categorize the failure before adding auto-reconnect logic.

### Moment: connecting over guest Wi-Fi

- **UX0177** Label network-isolation check with its real interface/route, not only a numeric address.
- **UX0178** Show peers share reachable LAN separately from socket-open and audio-received states.
- **UX0179** Test the failure mode “client isolation blocks direct contact” with a targeted check instead of a generic connection toast.
- **UX0180** Surface switch to a trusted LAN next to the failed field, not hidden in global settings.
- **UX0181** For connecting over guest Wi-Fi, preview PC and phone endpoints before committing a new network profile. Verify “peers share reachable LAN” despite “client isolation blocks direct contact”.
- **UX0182** Keep a safe manual-address fallback when discovery cannot find network-isolation check.
- **UX0183** For connecting over guest Wi-Fi, show a transient connecting timer and allow Cancel before a retry loop starts. Verify “peers share reachable LAN” despite “client isolation blocks direct contact”.
- **UX0184** For connecting over guest Wi-Fi, make the host/port error selectable and copyable for technical support. Verify “peers share reachable LAN” despite “client isolation blocks direct contact”.
- **UX0185** Do not recommend opening the entire firewall when client isolation blocks direct contact is suspected.
- **UX0186** For connecting over guest Wi-Fi, retain the last working route and offer a clearly labeled one-tap rollback. Verify “peers share reachable LAN” despite “client isolation blocks direct contact”.
- **UX0187** For connecting over guest Wi-Fi, use examples matching this route type instead of a hardcoded 192.168.x.x hint. Verify “peers share reachable LAN” despite “client isolation blocks direct contact”.
- **UX0188** For connecting over guest Wi-Fi, announce route changes accessibly without repeating every packet status. Verify “peers share reachable LAN” despite “client isolation blocks direct contact”.
- **UX0189** For connecting over guest Wi-Fi, keep network details visible on desktop and condensed on phone. Verify “peers share reachable LAN” despite “client isolation blocks direct contact”.
- **UX0190** For connecting over guest Wi-Fi, warn before suggesting public hotspot or WAN use of unauthenticated transport. Verify “peers share reachable LAN” despite “client isolation blocks direct contact”.
- **UX0191** For connecting over guest Wi-Fi, show what changed between a failed route and the last successful route. Verify “peers share reachable LAN” despite “client isolation blocks direct contact”.
- **UX0192** Measure isolation diagnosis time and categorize the failure before adding auto-reconnect logic.

### Moment: connecting via USB tethering

- **UX0193** Label USB network interface with its real interface/route, not only a numeric address.
- **UX0194** Show phone reachable over tether adapter separately from socket-open and audio-received states.
- **UX0195** Test the failure mode “host is bound to Wi-Fi instead of tether” with a targeted check instead of a generic connection toast.
- **UX0196** Surface pick tether IP next to the failed field, not hidden in global settings.
- **UX0197** For connecting via USB tethering, preview PC and phone endpoints before committing a new network profile. Verify “phone reachable over tether adapter” despite “host is bound to Wi-Fi instead of tether”.
- **UX0198** Keep a safe manual-address fallback when discovery cannot find USB network interface.
- **UX0199** For connecting via USB tethering, show a transient connecting timer and allow Cancel before a retry loop starts. Verify “phone reachable over tether adapter” despite “host is bound to Wi-Fi instead of tether”.
- **UX0200** For connecting via USB tethering, make the host/port error selectable and copyable for technical support. Verify “phone reachable over tether adapter” despite “host is bound to Wi-Fi instead of tether”.
- **UX0201** Do not recommend opening the entire firewall when host is bound to Wi-Fi instead of tether is suspected.
- **UX0202** For connecting via USB tethering, retain the last working route and offer a clearly labeled one-tap rollback. Verify “phone reachable over tether adapter” despite “host is bound to Wi-Fi instead of tether”.
- **UX0203** For connecting via USB tethering, use examples matching this route type instead of a hardcoded 192.168.x.x hint. Verify “phone reachable over tether adapter” despite “host is bound to Wi-Fi instead of tether”.
- **UX0204** For connecting via USB tethering, announce route changes accessibly without repeating every packet status. Verify “phone reachable over tether adapter” despite “host is bound to Wi-Fi instead of tether”.
- **UX0205** For connecting via USB tethering, keep network details visible on desktop and condensed on phone. Verify “phone reachable over tether adapter” despite “host is bound to Wi-Fi instead of tether”.
- **UX0206** For connecting via USB tethering, warn before suggesting public hotspot or WAN use of unauthenticated transport. Verify “phone reachable over tether adapter” despite “host is bound to Wi-Fi instead of tether”.
- **UX0207** For connecting via USB tethering, show what changed between a failed route and the last successful route. Verify “phone reachable over tether adapter” despite “host is bound to Wi-Fi instead of tether”.
- **UX0208** Measure tether setup without guesswork and categorize the failure before adding auto-reconnect logic.

### Moment: using a LAN hostname

- **UX0209** Label resolved host preview with its real interface/route, not only a numeric address.
- **UX0210** Show DNS result reachable separately from socket-open and audio-received states.
- **UX0211** Test the failure mode “hostname resolves to an unsupported address family” with a targeted check instead of a generic connection toast.
- **UX0212** Surface choose valid resolved IP next to the failed field, not hidden in global settings.
- **UX0213** For using a LAN hostname, preview PC and phone endpoints before committing a new network profile. Verify “DNS result reachable” despite “hostname resolves to an unsupported address family”.
- **UX0214** Keep a safe manual-address fallback when discovery cannot find resolved host preview.
- **UX0215** For using a LAN hostname, show a transient connecting timer and allow Cancel before a retry loop starts. Verify “DNS result reachable” despite “hostname resolves to an unsupported address family”.
- **UX0216** For using a LAN hostname, make the host/port error selectable and copyable for technical support. Verify “DNS result reachable” despite “hostname resolves to an unsupported address family”.
- **UX0217** Do not recommend opening the entire firewall when hostname resolves to an unsupported address family is suspected.
- **UX0218** For using a LAN hostname, retain the last working route and offer a clearly labeled one-tap rollback. Verify “DNS result reachable” despite “hostname resolves to an unsupported address family”.
- **UX0219** For using a LAN hostname, use examples matching this route type instead of a hardcoded 192.168.x.x hint. Verify “DNS result reachable” despite “hostname resolves to an unsupported address family”.
- **UX0220** For using a LAN hostname, announce route changes accessibly without repeating every packet status. Verify “DNS result reachable” despite “hostname resolves to an unsupported address family”.
- **UX0221** For using a LAN hostname, keep network details visible on desktop and condensed on phone. Verify “DNS result reachable” despite “hostname resolves to an unsupported address family”.
- **UX0222** For using a LAN hostname, warn before suggesting public hotspot or WAN use of unauthenticated transport. Verify “DNS result reachable” despite “hostname resolves to an unsupported address family”.
- **UX0223** For using a LAN hostname, show what changed between a failed route and the last successful route. Verify “DNS result reachable” despite “hostname resolves to an unsupported address family”.
- **UX0224** Measure hostname resolution success and categorize the failure before adding auto-reconnect logic.

### Moment: changing networks mid-session

- **UX0225** Label network handoff state with its real interface/route, not only a numeric address.
- **UX0226** Show connection resumes or stops honestly separately from socket-open and audio-received states.
- **UX0227** Test the failure mode “old IP is cached after handoff” with a targeted check instead of a generic connection toast.
- **UX0228** Surface retry with new route next to the failed field, not hidden in global settings.
- **UX0229** For changing networks mid-session, preview PC and phone endpoints before committing a new network profile. Verify “connection resumes or stops honestly” despite “old IP is cached after handoff”.
- **UX0230** Keep a safe manual-address fallback when discovery cannot find network handoff state.
- **UX0231** For changing networks mid-session, show a transient connecting timer and allow Cancel before a retry loop starts. Verify “connection resumes or stops honestly” despite “old IP is cached after handoff”.
- **UX0232** For changing networks mid-session, make the host/port error selectable and copyable for technical support. Verify “connection resumes or stops honestly” despite “old IP is cached after handoff”.
- **UX0233** Do not recommend opening the entire firewall when old IP is cached after handoff is suspected.
- **UX0234** For changing networks mid-session, retain the last working route and offer a clearly labeled one-tap rollback. Verify “connection resumes or stops honestly” despite “old IP is cached after handoff”.
- **UX0235** For changing networks mid-session, use examples matching this route type instead of a hardcoded 192.168.x.x hint. Verify “connection resumes or stops honestly” despite “old IP is cached after handoff”.
- **UX0236** For changing networks mid-session, announce route changes accessibly without repeating every packet status. Verify “connection resumes or stops honestly” despite “old IP is cached after handoff”.
- **UX0237** For changing networks mid-session, keep network details visible on desktop and condensed on phone. Verify “connection resumes or stops honestly” despite “old IP is cached after handoff”.
- **UX0238** For changing networks mid-session, warn before suggesting public hotspot or WAN use of unauthenticated transport. Verify “connection resumes or stops honestly” despite “old IP is cached after handoff”.
- **UX0239** For changing networks mid-session, show what changed between a failed route and the last successful route. Verify “connection resumes or stops honestly” despite “old IP is cached after handoff”.
- **UX0240** Measure clean recovery time and categorize the failure before adding auto-reconnect logic.

### Moment: connecting through a VPN

- **UX0241** Label VPN-route warning with its real interface/route, not only a numeric address.
- **UX0242** Show peer reachability verified separately from socket-open and audio-received states.
- **UX0243** Test the failure mode “split tunnel sends phone traffic elsewhere” with a targeted check instead of a generic connection toast.
- **UX0244** Surface choose local route next to the failed field, not hidden in global settings.
- **UX0245** For connecting through a VPN, preview PC and phone endpoints before committing a new network profile. Verify “peer reachability verified” despite “split tunnel sends phone traffic elsewhere”.
- **UX0246** Keep a safe manual-address fallback when discovery cannot find VPN-route warning.
- **UX0247** For connecting through a VPN, show a transient connecting timer and allow Cancel before a retry loop starts. Verify “peer reachability verified” despite “split tunnel sends phone traffic elsewhere”.
- **UX0248** For connecting through a VPN, make the host/port error selectable and copyable for technical support. Verify “peer reachability verified” despite “split tunnel sends phone traffic elsewhere”.
- **UX0249** Do not recommend opening the entire firewall when split tunnel sends phone traffic elsewhere is suspected.
- **UX0250** For connecting through a VPN, retain the last working route and offer a clearly labeled one-tap rollback. Verify “peer reachability verified” despite “split tunnel sends phone traffic elsewhere”.
- **UX0251** For connecting through a VPN, use examples matching this route type instead of a hardcoded 192.168.x.x hint. Verify “peer reachability verified” despite “split tunnel sends phone traffic elsewhere”.
- **UX0252** For connecting through a VPN, announce route changes accessibly without repeating every packet status. Verify “peer reachability verified” despite “split tunnel sends phone traffic elsewhere”.
- **UX0253** For connecting through a VPN, keep network details visible on desktop and condensed on phone. Verify “peer reachability verified” despite “split tunnel sends phone traffic elsewhere”.
- **UX0254** For connecting through a VPN, warn before suggesting public hotspot or WAN use of unauthenticated transport. Verify “peer reachability verified” despite “split tunnel sends phone traffic elsewhere”.
- **UX0255** For connecting through a VPN, show what changed between a failed route and the last successful route. Verify “peer reachability verified” despite “split tunnel sends phone traffic elsewhere”.
- **UX0256** Measure VPN-related false errors avoided and categorize the failure before adding auto-reconnect logic.

## 03 · Pairing, identity and device trust

### Moment: approving a new phone

- **UX0257** State who can hear the PC audio in the new-device approval view.
- **UX0258** Only show known device admitted after cryptographic verification, never from a username alone.
- **UX0259** Give the situation “unknown LAN peer requests audio” a precise, non-alarming explanation and a safe route forward.
- **UX0260** Require explicit confirmation for approve or reject the phone; never approve a peer from a notification tap alone.
- **UX0261** For approving a new phone, expire temporary pairing offers visibly with a countdown that stops at zero. Verify “known device admitted” despite “unknown LAN peer requests audio”.
- **UX0262** For approving a new phone, keep the identity fingerprint selectable and spoken clearly by assistive tech. Verify “known device admitted” despite “unknown LAN peer requests audio”.
- **UX0263** For approving a new phone, differentiate paired, connected and currently listening devices visually and in text. Verify “known device admitted” despite “unknown LAN peer requests audio”.
- **UX0264** For approving a new phone, show the timestamp and origin of each trust change in a local audit view. Verify “known device admitted” despite “unknown LAN peer requests audio”.
- **UX0265** For approving a new phone, offer revoke/undo only where rollback does not re-enable a compromised key. Verify “known device admitted” despite “unknown LAN peer requests audio”.
- **UX0266** For approving a new phone, avoid showing reusable tokens or secret keys in QR preview/screenshots. Verify “known device admitted” despite “unknown LAN peer requests audio”.
- **UX0267** Explain why new-device approval cannot be controlled from a second unknown PC.
- **UX0268** For approving a new phone, show a compatibility warning rather than silently falling back to plaintext. Verify “known device admitted” despite “unknown LAN peer requests audio”.
- **UX0269** For approving a new phone, make the safe path the primary CTA and the legacy path an explicit advanced choice. Verify “known device admitted” despite “unknown LAN peer requests audio”.
- **UX0270** For approving a new phone, keep account creation unnecessary for local-only paired devices. Verify “known device admitted” despite “unknown LAN peer requests audio”.
- **UX0271** For approving a new phone, give key reset a clear impact summary covering all already paired phones. Verify “known device admitted” despite “unknown LAN peer requests audio”.
- **UX0272** Measure unapproved peers rejected without collecting fingerprints or device names remotely.

### Moment: scanning a pairing QR

- **UX0273** State who can hear the PC audio in the time-limited pairing code view.
- **UX0274** Only show one phone paired after cryptographic verification, never from a username alone.
- **UX0275** Give the situation “stale or copied code is reused” a precise, non-alarming explanation and a safe route forward.
- **UX0276** Require explicit confirmation for regenerate code; never approve a peer from a notification tap alone.
- **UX0277** For scanning a pairing QR, expire temporary pairing offers visibly with a countdown that stops at zero. Verify “one phone paired” despite “stale or copied code is reused”.
- **UX0278** For scanning a pairing QR, keep the identity fingerprint selectable and spoken clearly by assistive tech. Verify “one phone paired” despite “stale or copied code is reused”.
- **UX0279** For scanning a pairing QR, differentiate paired, connected and currently listening devices visually and in text. Verify “one phone paired” despite “stale or copied code is reused”.
- **UX0280** For scanning a pairing QR, show the timestamp and origin of each trust change in a local audit view. Verify “one phone paired” despite “stale or copied code is reused”.
- **UX0281** For scanning a pairing QR, offer revoke/undo only where rollback does not re-enable a compromised key. Verify “one phone paired” despite “stale or copied code is reused”.
- **UX0282** For scanning a pairing QR, avoid showing reusable tokens or secret keys in QR preview/screenshots. Verify “one phone paired” despite “stale or copied code is reused”.
- **UX0283** Explain why time-limited pairing code cannot be controlled from a second unknown PC.
- **UX0284** For scanning a pairing QR, show a compatibility warning rather than silently falling back to plaintext. Verify “one phone paired” despite “stale or copied code is reused”.
- **UX0285** For scanning a pairing QR, make the safe path the primary CTA and the legacy path an explicit advanced choice. Verify “one phone paired” despite “stale or copied code is reused”.
- **UX0286** For scanning a pairing QR, keep account creation unnecessary for local-only paired devices. Verify “one phone paired” despite “stale or copied code is reused”.
- **UX0287** For scanning a pairing QR, give key reset a clear impact summary covering all already paired phones. Verify “one phone paired” despite “stale or copied code is reused”.
- **UX0288** Measure pairing without secret leakage without collecting fingerprints or device names remotely.

### Moment: confirming PC identity

- **UX0289** State who can hear the PC audio in the server fingerprint view.
- **UX0290** Only show correct PC trusted after cryptographic verification, never from a username alone.
- **UX0291** Give the situation “lookalike hostname could be an impostor” a precise, non-alarming explanation and a safe route forward.
- **UX0292** Require explicit confirmation for compare short fingerprint; never approve a peer from a notification tap alone.
- **UX0293** For confirming PC identity, expire temporary pairing offers visibly with a countdown that stops at zero. Verify “correct PC trusted” despite “lookalike hostname could be an impostor”.
- **UX0294** For confirming PC identity, keep the identity fingerprint selectable and spoken clearly by assistive tech. Verify “correct PC trusted” despite “lookalike hostname could be an impostor”.
- **UX0295** For confirming PC identity, differentiate paired, connected and currently listening devices visually and in text. Verify “correct PC trusted” despite “lookalike hostname could be an impostor”.
- **UX0296** For confirming PC identity, show the timestamp and origin of each trust change in a local audit view. Verify “correct PC trusted” despite “lookalike hostname could be an impostor”.
- **UX0297** For confirming PC identity, offer revoke/undo only where rollback does not re-enable a compromised key. Verify “correct PC trusted” despite “lookalike hostname could be an impostor”.
- **UX0298** For confirming PC identity, avoid showing reusable tokens or secret keys in QR preview/screenshots. Verify “correct PC trusted” despite “lookalike hostname could be an impostor”.
- **UX0299** Explain why server fingerprint cannot be controlled from a second unknown PC.
- **UX0300** For confirming PC identity, show a compatibility warning rather than silently falling back to plaintext. Verify “correct PC trusted” despite “lookalike hostname could be an impostor”.
- **UX0301** For confirming PC identity, make the safe path the primary CTA and the legacy path an explicit advanced choice. Verify “correct PC trusted” despite “lookalike hostname could be an impostor”.
- **UX0302** For confirming PC identity, keep account creation unnecessary for local-only paired devices. Verify “correct PC trusted” despite “lookalike hostname could be an impostor”.
- **UX0303** For confirming PC identity, give key reset a clear impact summary covering all already paired phones. Verify “correct PC trusted” despite “lookalike hostname could be an impostor”.
- **UX0304** Measure identity confirmation success without collecting fingerprints or device names remotely.

### Moment: naming a connected phone

- **UX0305** State who can hear the PC audio in the local device nickname view.
- **UX0306** Only show recognized phone displayed after cryptographic verification, never from a username alone.
- **UX0307** Give the situation “two clients have identical default names” a precise, non-alarming explanation and a safe route forward.
- **UX0308** Require explicit confirmation for rename locally; never approve a peer from a notification tap alone.
- **UX0309** For naming a connected phone, expire temporary pairing offers visibly with a countdown that stops at zero. Verify “recognized phone displayed” despite “two clients have identical default names”.
- **UX0310** For naming a connected phone, keep the identity fingerprint selectable and spoken clearly by assistive tech. Verify “recognized phone displayed” despite “two clients have identical default names”.
- **UX0311** For naming a connected phone, differentiate paired, connected and currently listening devices visually and in text. Verify “recognized phone displayed” despite “two clients have identical default names”.
- **UX0312** For naming a connected phone, show the timestamp and origin of each trust change in a local audit view. Verify “recognized phone displayed” despite “two clients have identical default names”.
- **UX0313** For naming a connected phone, offer revoke/undo only where rollback does not re-enable a compromised key. Verify “recognized phone displayed” despite “two clients have identical default names”.
- **UX0314** For naming a connected phone, avoid showing reusable tokens or secret keys in QR preview/screenshots. Verify “recognized phone displayed” despite “two clients have identical default names”.
- **UX0315** Explain why local device nickname cannot be controlled from a second unknown PC.
- **UX0316** For naming a connected phone, show a compatibility warning rather than silently falling back to plaintext. Verify “recognized phone displayed” despite “two clients have identical default names”.
- **UX0317** For naming a connected phone, make the safe path the primary CTA and the legacy path an explicit advanced choice. Verify “recognized phone displayed” despite “two clients have identical default names”.
- **UX0318** For naming a connected phone, keep account creation unnecessary for local-only paired devices. Verify “recognized phone displayed” despite “two clients have identical default names”.
- **UX0319** For naming a connected phone, give key reset a clear impact summary covering all already paired phones. Verify “recognized phone displayed” despite “two clients have identical default names”.
- **UX0320** Measure correct device identified without collecting fingerprints or device names remotely.

### Moment: revoking an old phone

- **UX0321** State who can hear the PC audio in the paired-device roster view.
- **UX0322** Only show key revoked after cryptographic verification, never from a username alone.
- **UX0323** Give the situation “lost device still has access” a precise, non-alarming explanation and a safe route forward.
- **UX0324** Require explicit confirmation for revoke device; never approve a peer from a notification tap alone.
- **UX0325** For revoking an old phone, expire temporary pairing offers visibly with a countdown that stops at zero. Verify “key revoked” despite “lost device still has access”.
- **UX0326** For revoking an old phone, keep the identity fingerprint selectable and spoken clearly by assistive tech. Verify “key revoked” despite “lost device still has access”.
- **UX0327** For revoking an old phone, differentiate paired, connected and currently listening devices visually and in text. Verify “key revoked” despite “lost device still has access”.
- **UX0328** For revoking an old phone, show the timestamp and origin of each trust change in a local audit view. Verify “key revoked” despite “lost device still has access”.
- **UX0329** For revoking an old phone, offer revoke/undo only where rollback does not re-enable a compromised key. Verify “key revoked” despite “lost device still has access”.
- **UX0330** For revoking an old phone, avoid showing reusable tokens or secret keys in QR preview/screenshots. Verify “key revoked” despite “lost device still has access”.
- **UX0331** Explain why paired-device roster cannot be controlled from a second unknown PC.
- **UX0332** For revoking an old phone, show a compatibility warning rather than silently falling back to plaintext. Verify “key revoked” despite “lost device still has access”.
- **UX0333** For revoking an old phone, make the safe path the primary CTA and the legacy path an explicit advanced choice. Verify “key revoked” despite “lost device still has access”.
- **UX0334** For revoking an old phone, keep account creation unnecessary for local-only paired devices. Verify “key revoked” despite “lost device still has access”.
- **UX0335** For revoking an old phone, give key reset a clear impact summary covering all already paired phones. Verify “key revoked” despite “lost device still has access”.
- **UX0336** Measure access denied after revoke without collecting fingerprints or device names remotely.

### Moment: moving from legacy plaintext mode

- **UX0337** State who can hear the PC audio in the secure-mode migration view.
- **UX0338** Only show new encrypted session active after cryptographic verification, never from a username alone.
- **UX0339** Give the situation “old client cannot negotiate new protocol” a precise, non-alarming explanation and a safe route forward.
- **UX0340** Require explicit confirmation for update both endpoints; never approve a peer from a notification tap alone.
- **UX0341** For moving from legacy plaintext mode, expire temporary pairing offers visibly with a countdown that stops at zero. Verify “new encrypted session active” despite “old client cannot negotiate new protocol”.
- **UX0342** For moving from legacy plaintext mode, keep the identity fingerprint selectable and spoken clearly by assistive tech. Verify “new encrypted session active” despite “old client cannot negotiate new protocol”.
- **UX0343** For moving from legacy plaintext mode, differentiate paired, connected and currently listening devices visually and in text. Verify “new encrypted session active” despite “old client cannot negotiate new protocol”.
- **UX0344** For moving from legacy plaintext mode, show the timestamp and origin of each trust change in a local audit view. Verify “new encrypted session active” despite “old client cannot negotiate new protocol”.
- **UX0345** For moving from legacy plaintext mode, offer revoke/undo only where rollback does not re-enable a compromised key. Verify “new encrypted session active” despite “old client cannot negotiate new protocol”.
- **UX0346** For moving from legacy plaintext mode, avoid showing reusable tokens or secret keys in QR preview/screenshots. Verify “new encrypted session active” despite “old client cannot negotiate new protocol”.
- **UX0347** Explain why secure-mode migration cannot be controlled from a second unknown PC.
- **UX0348** For moving from legacy plaintext mode, show a compatibility warning rather than silently falling back to plaintext. Verify “new encrypted session active” despite “old client cannot negotiate new protocol”.
- **UX0349** For moving from legacy plaintext mode, make the safe path the primary CTA and the legacy path an explicit advanced choice. Verify “new encrypted session active” despite “old client cannot negotiate new protocol”.
- **UX0350** For moving from legacy plaintext mode, keep account creation unnecessary for local-only paired devices. Verify “new encrypted session active” despite “old client cannot negotiate new protocol”.
- **UX0351** For moving from legacy plaintext mode, give key reset a clear impact summary covering all already paired phones. Verify “new encrypted session active” despite “old client cannot negotiate new protocol”.
- **UX0352** Measure migration without silent downgrade without collecting fingerprints or device names remotely.

### Moment: pairing on shared Wi-Fi

- **UX0353** State who can hear the PC audio in the network trust warning view.
- **UX0354** Only show user makes informed decision after cryptographic verification, never from a username alone.
- **UX0355** Give the situation “a public LAN peer could listen” a precise, non-alarming explanation and a safe route forward.
- **UX0356** Require explicit confirmation for use secure pairing or trusted LAN; never approve a peer from a notification tap alone.
- **UX0357** For pairing on shared Wi-Fi, expire temporary pairing offers visibly with a countdown that stops at zero. Verify “user makes informed decision” despite “a public LAN peer could listen”.
- **UX0358** For pairing on shared Wi-Fi, keep the identity fingerprint selectable and spoken clearly by assistive tech. Verify “user makes informed decision” despite “a public LAN peer could listen”.
- **UX0359** For pairing on shared Wi-Fi, differentiate paired, connected and currently listening devices visually and in text. Verify “user makes informed decision” despite “a public LAN peer could listen”.
- **UX0360** For pairing on shared Wi-Fi, show the timestamp and origin of each trust change in a local audit view. Verify “user makes informed decision” despite “a public LAN peer could listen”.
- **UX0361** For pairing on shared Wi-Fi, offer revoke/undo only where rollback does not re-enable a compromised key. Verify “user makes informed decision” despite “a public LAN peer could listen”.
- **UX0362** For pairing on shared Wi-Fi, avoid showing reusable tokens or secret keys in QR preview/screenshots. Verify “user makes informed decision” despite “a public LAN peer could listen”.
- **UX0363** Explain why network trust warning cannot be controlled from a second unknown PC.
- **UX0364** For pairing on shared Wi-Fi, show a compatibility warning rather than silently falling back to plaintext. Verify “user makes informed decision” despite “a public LAN peer could listen”.
- **UX0365** For pairing on shared Wi-Fi, make the safe path the primary CTA and the legacy path an explicit advanced choice. Verify “user makes informed decision” despite “a public LAN peer could listen”.
- **UX0366** For pairing on shared Wi-Fi, keep account creation unnecessary for local-only paired devices. Verify “user makes informed decision” despite “a public LAN peer could listen”.
- **UX0367** For pairing on shared Wi-Fi, give key reset a clear impact summary covering all already paired phones. Verify “user makes informed decision” despite “a public LAN peer could listen”.
- **UX0368** Measure unsafe connection attempts averted without collecting fingerprints or device names remotely.

### Moment: recovering after reinstall

- **UX0369** State who can hear the PC audio in the trusted-device recovery view.
- **UX0370** Only show old trust removed intentionally after cryptographic verification, never from a username alone.
- **UX0371** Give the situation “reinstalled phone appears as a different peer” a precise, non-alarming explanation and a safe route forward.
- **UX0372** Require explicit confirmation for verify and pair again; never approve a peer from a notification tap alone.
- **UX0373** For recovering after reinstall, expire temporary pairing offers visibly with a countdown that stops at zero. Verify “old trust removed intentionally” despite “reinstalled phone appears as a different peer”.
- **UX0374** For recovering after reinstall, keep the identity fingerprint selectable and spoken clearly by assistive tech. Verify “old trust removed intentionally” despite “reinstalled phone appears as a different peer”.
- **UX0375** For recovering after reinstall, differentiate paired, connected and currently listening devices visually and in text. Verify “old trust removed intentionally” despite “reinstalled phone appears as a different peer”.
- **UX0376** For recovering after reinstall, show the timestamp and origin of each trust change in a local audit view. Verify “old trust removed intentionally” despite “reinstalled phone appears as a different peer”.
- **UX0377** For recovering after reinstall, offer revoke/undo only where rollback does not re-enable a compromised key. Verify “old trust removed intentionally” despite “reinstalled phone appears as a different peer”.
- **UX0378** For recovering after reinstall, avoid showing reusable tokens or secret keys in QR preview/screenshots. Verify “old trust removed intentionally” despite “reinstalled phone appears as a different peer”.
- **UX0379** Explain why trusted-device recovery cannot be controlled from a second unknown PC.
- **UX0380** For recovering after reinstall, show a compatibility warning rather than silently falling back to plaintext. Verify “old trust removed intentionally” despite “reinstalled phone appears as a different peer”.
- **UX0381** For recovering after reinstall, make the safe path the primary CTA and the legacy path an explicit advanced choice. Verify “old trust removed intentionally” despite “reinstalled phone appears as a different peer”.
- **UX0382** For recovering after reinstall, keep account creation unnecessary for local-only paired devices. Verify “old trust removed intentionally” despite “reinstalled phone appears as a different peer”.
- **UX0383** For recovering after reinstall, give key reset a clear impact summary covering all already paired phones. Verify “old trust removed intentionally” despite “reinstalled phone appears as a different peer”.
- **UX0384** Measure recovery without anonymous bypass without collecting fingerprints or device names remotely.

## 04 · Source and sink selection

### Moment: selecting the default sink

- **UX0385** Show default-sink option with human-readable sink name plus stable technical ID on demand.
- **UX0386** Represent active system sink captured separately from the system default selection.
- **UX0387** Warn about “the default changes after launch” with an explanation of its likely audible symptom.
- **UX0388** Offer follow or pin selection in place while keeping Stop available.
- **UX0389** For selecting the default sink, preview consequences for existing listeners before changing source. Verify “active system sink captured” despite “the default changes after launch”.
- **UX0390** For selecting the default sink, record the last working sink per PC profile, not as an opaque global string. Verify “active system sink captured” despite “the default changes after launch”.
- **UX0391** For selecting the default sink, avoid selecting a monitor/source node when the user asked for an output sink. Verify “active system sink captured” despite “the default changes after launch”.
- **UX0392** For selecting the default sink, show a signal meter only if the capture path reports real audio levels. Verify “active system sink captured” despite “the default changes after launch”.
- **UX0393** For selecting the default sink, make a missing device a recoverable state, not a blank dropdown. Verify “active system sink captured” despite “the default changes after launch”.
- **UX0394** For selecting the default sink, surface a safe test-tone option at a modest volume when technically available. Verify “active system sink captured” despite “the default changes after launch”.
- **UX0395** For selecting the default sink, keep source controls disabled with a reason while switching could break playback. Verify “active system sink captured” despite “the default changes after launch”.
- **UX0396** For selecting the default sink, allow mouse, keyboard and screen reader users to identify the same sink. Verify “active system sink captured” despite “the default changes after launch”.
- **UX0397** For selecting the default sink, provide an explicit default-versus-pinned choice in the advanced view. Verify “active system sink captured” despite “the default changes after launch”.
- **UX0398** For selecting the default sink, distinguish 'silent because app paused' from 'sink missing' before prompting a fix. Verify “active system sink captured” despite “the default changes after launch”.
- **UX0399** For selecting the default sink, log source changes locally with time and old/new sink IDs for support. Verify “active system sink captured” despite “the default changes after launch”.
- **UX0400** Measure capture matches expected PC output across hotplug and monitor change before claiming auto-follow reliability.

### Moment: pinning a USB DAC

- **UX0401** Show fixed sink selection with human-readable sink name plus stable technical ID on demand.
- **UX0402** Represent desired DAC captured separately from the system default selection.
- **UX0403** Warn about “USB device disappears and reappears” with an explanation of its likely audible symptom.
- **UX0404** Offer reselect the DAC in place while keeping Stop available.
- **UX0405** For pinning a USB DAC, preview consequences for existing listeners before changing source. Verify “desired DAC captured” despite “USB device disappears and reappears”.
- **UX0406** For pinning a USB DAC, record the last working sink per PC profile, not as an opaque global string. Verify “desired DAC captured” despite “USB device disappears and reappears”.
- **UX0407** For pinning a USB DAC, avoid selecting a monitor/source node when the user asked for an output sink. Verify “desired DAC captured” despite “USB device disappears and reappears”.
- **UX0408** For pinning a USB DAC, show a signal meter only if the capture path reports real audio levels. Verify “desired DAC captured” despite “USB device disappears and reappears”.
- **UX0409** For pinning a USB DAC, make a missing device a recoverable state, not a blank dropdown. Verify “desired DAC captured” despite “USB device disappears and reappears”.
- **UX0410** For pinning a USB DAC, surface a safe test-tone option at a modest volume when technically available. Verify “desired DAC captured” despite “USB device disappears and reappears”.
- **UX0411** For pinning a USB DAC, keep source controls disabled with a reason while switching could break playback. Verify “desired DAC captured” despite “USB device disappears and reappears”.
- **UX0412** For pinning a USB DAC, allow mouse, keyboard and screen reader users to identify the same sink. Verify “desired DAC captured” despite “USB device disappears and reappears”.
- **UX0413** For pinning a USB DAC, provide an explicit default-versus-pinned choice in the advanced view. Verify “desired DAC captured” despite “USB device disappears and reappears”.
- **UX0414** For pinning a USB DAC, distinguish 'silent because app paused' from 'sink missing' before prompting a fix. Verify “desired DAC captured” despite “USB device disappears and reappears”.
- **UX0415** For pinning a USB DAC, log source changes locally with time and old/new sink IDs for support. Verify “desired DAC captured” despite “USB device disappears and reappears”.
- **UX0416** Measure recovery after hotplug across hotplug and monitor change before claiming auto-follow reliability.

### Moment: switching HDMI monitors

- **UX0417** Show HDMI sink change with human-readable sink name plus stable technical ID on demand.
- **UX0418** Represent new display audio route recognized separately from the system default selection.
- **UX0419** Warn about “old endpoint vanishes on monitor switch” with an explanation of its likely audible symptom.
- **UX0420** Offer choose new monitor sink in place while keeping Stop available.
- **UX0421** For switching HDMI monitors, preview consequences for existing listeners before changing source. Verify “new display audio route recognized” despite “old endpoint vanishes on monitor switch”.
- **UX0422** For switching HDMI monitors, record the last working sink per PC profile, not as an opaque global string. Verify “new display audio route recognized” despite “old endpoint vanishes on monitor switch”.
- **UX0423** For switching HDMI monitors, avoid selecting a monitor/source node when the user asked for an output sink. Verify “new display audio route recognized” despite “old endpoint vanishes on monitor switch”.
- **UX0424** For switching HDMI monitors, show a signal meter only if the capture path reports real audio levels. Verify “new display audio route recognized” despite “old endpoint vanishes on monitor switch”.
- **UX0425** For switching HDMI monitors, make a missing device a recoverable state, not a blank dropdown. Verify “new display audio route recognized” despite “old endpoint vanishes on monitor switch”.
- **UX0426** For switching HDMI monitors, surface a safe test-tone option at a modest volume when technically available. Verify “new display audio route recognized” despite “old endpoint vanishes on monitor switch”.
- **UX0427** For switching HDMI monitors, keep source controls disabled with a reason while switching could break playback. Verify “new display audio route recognized” despite “old endpoint vanishes on monitor switch”.
- **UX0428** For switching HDMI monitors, allow mouse, keyboard and screen reader users to identify the same sink. Verify “new display audio route recognized” despite “old endpoint vanishes on monitor switch”.
- **UX0429** For switching HDMI monitors, provide an explicit default-versus-pinned choice in the advanced view. Verify “new display audio route recognized” despite “old endpoint vanishes on monitor switch”.
- **UX0430** For switching HDMI monitors, distinguish 'silent because app paused' from 'sink missing' before prompting a fix. Verify “new display audio route recognized” despite “old endpoint vanishes on monitor switch”.
- **UX0431** For switching HDMI monitors, log source changes locally with time and old/new sink IDs for support. Verify “new display audio route recognized” despite “old endpoint vanishes on monitor switch”.
- **UX0432** Measure no crash on profile switch across hotplug and monitor change before claiming auto-follow reliability.

### Moment: using a null sink

- **UX0433** Show virtual sink setup with human-readable sink name plus stable technical ID on demand.
- **UX0434** Represent PC audio routed privately separately from the system default selection.
- **UX0435** Warn about “no physical speaker exists” with an explanation of its likely audible symptom.
- **UX0436** Offer review reversible null-sink guide in place while keeping Stop available.
- **UX0437** For using a null sink, preview consequences for existing listeners before changing source. Verify “PC audio routed privately” despite “no physical speaker exists”.
- **UX0438** For using a null sink, record the last working sink per PC profile, not as an opaque global string. Verify “PC audio routed privately” despite “no physical speaker exists”.
- **UX0439** For using a null sink, avoid selecting a monitor/source node when the user asked for an output sink. Verify “PC audio routed privately” despite “no physical speaker exists”.
- **UX0440** For using a null sink, show a signal meter only if the capture path reports real audio levels. Verify “PC audio routed privately” despite “no physical speaker exists”.
- **UX0441** For using a null sink, make a missing device a recoverable state, not a blank dropdown. Verify “PC audio routed privately” despite “no physical speaker exists”.
- **UX0442** For using a null sink, surface a safe test-tone option at a modest volume when technically available. Verify “PC audio routed privately” despite “no physical speaker exists”.
- **UX0443** For using a null sink, keep source controls disabled with a reason while switching could break playback. Verify “PC audio routed privately” despite “no physical speaker exists”.
- **UX0444** For using a null sink, allow mouse, keyboard and screen reader users to identify the same sink. Verify “PC audio routed privately” despite “no physical speaker exists”.
- **UX0445** For using a null sink, provide an explicit default-versus-pinned choice in the advanced view. Verify “PC audio routed privately” despite “no physical speaker exists”.
- **UX0446** For using a null sink, distinguish 'silent because app paused' from 'sink missing' before prompting a fix. Verify “PC audio routed privately” despite “no physical speaker exists”.
- **UX0447** For using a null sink, log source changes locally with time and old/new sink IDs for support. Verify “PC audio routed privately” despite “no physical speaker exists”.
- **UX0448** Measure first sound without physical jack across hotplug and monitor change before claiming auto-follow reliability.

### Moment: capturing a Bluetooth sink

- **UX0449** Show Bluetooth output sink with human-readable sink name plus stable technical ID on demand.
- **UX0450** Represent correct wireless source captured separately from the system default selection.
- **UX0451** Warn about “Bluetooth profile switches mid-stream” with an explanation of its likely audible symptom.
- **UX0452** Offer inspect sink profile in place while keeping Stop available.
- **UX0453** For capturing a Bluetooth sink, preview consequences for existing listeners before changing source. Verify “correct wireless source captured” despite “Bluetooth profile switches mid-stream”.
- **UX0454** For capturing a Bluetooth sink, record the last working sink per PC profile, not as an opaque global string. Verify “correct wireless source captured” despite “Bluetooth profile switches mid-stream”.
- **UX0455** For capturing a Bluetooth sink, avoid selecting a monitor/source node when the user asked for an output sink. Verify “correct wireless source captured” despite “Bluetooth profile switches mid-stream”.
- **UX0456** For capturing a Bluetooth sink, show a signal meter only if the capture path reports real audio levels. Verify “correct wireless source captured” despite “Bluetooth profile switches mid-stream”.
- **UX0457** For capturing a Bluetooth sink, make a missing device a recoverable state, not a blank dropdown. Verify “correct wireless source captured” despite “Bluetooth profile switches mid-stream”.
- **UX0458** For capturing a Bluetooth sink, surface a safe test-tone option at a modest volume when technically available. Verify “correct wireless source captured” despite “Bluetooth profile switches mid-stream”.
- **UX0459** For capturing a Bluetooth sink, keep source controls disabled with a reason while switching could break playback. Verify “correct wireless source captured” despite “Bluetooth profile switches mid-stream”.
- **UX0460** For capturing a Bluetooth sink, allow mouse, keyboard and screen reader users to identify the same sink. Verify “correct wireless source captured” despite “Bluetooth profile switches mid-stream”.
- **UX0461** For capturing a Bluetooth sink, provide an explicit default-versus-pinned choice in the advanced view. Verify “correct wireless source captured” despite “Bluetooth profile switches mid-stream”.
- **UX0462** For capturing a Bluetooth sink, distinguish 'silent because app paused' from 'sink missing' before prompting a fix. Verify “correct wireless source captured” despite “Bluetooth profile switches mid-stream”.
- **UX0463** For capturing a Bluetooth sink, log source changes locally with time and old/new sink IDs for support. Verify “correct wireless source captured” despite “Bluetooth profile switches mid-stream”.
- **UX0464** Measure no silent capture on route switch across hotplug and monitor change before claiming auto-follow reliability.

### Moment: playing from one PC application

- **UX0465** Show per-app audio routing with human-readable sink name plus stable technical ID on demand.
- **UX0466** Represent chosen app audible on phone separately from the system default selection.
- **UX0467** Warn about “unwanted app audio leaks to phone” with an explanation of its likely audible symptom.
- **UX0468** Offer isolate the app route in place while keeping Stop available.
- **UX0469** For playing from one PC application, preview consequences for existing listeners before changing source. Verify “chosen app audible on phone” despite “unwanted app audio leaks to phone”.
- **UX0470** For playing from one PC application, record the last working sink per PC profile, not as an opaque global string. Verify “chosen app audible on phone” despite “unwanted app audio leaks to phone”.
- **UX0471** For playing from one PC application, avoid selecting a monitor/source node when the user asked for an output sink. Verify “chosen app audible on phone” despite “unwanted app audio leaks to phone”.
- **UX0472** For playing from one PC application, show a signal meter only if the capture path reports real audio levels. Verify “chosen app audible on phone” despite “unwanted app audio leaks to phone”.
- **UX0473** For playing from one PC application, make a missing device a recoverable state, not a blank dropdown. Verify “chosen app audible on phone” despite “unwanted app audio leaks to phone”.
- **UX0474** For playing from one PC application, surface a safe test-tone option at a modest volume when technically available. Verify “chosen app audible on phone” despite “unwanted app audio leaks to phone”.
- **UX0475** For playing from one PC application, keep source controls disabled with a reason while switching could break playback. Verify “chosen app audible on phone” despite “unwanted app audio leaks to phone”.
- **UX0476** For playing from one PC application, allow mouse, keyboard and screen reader users to identify the same sink. Verify “chosen app audible on phone” despite “unwanted app audio leaks to phone”.
- **UX0477** For playing from one PC application, provide an explicit default-versus-pinned choice in the advanced view. Verify “chosen app audible on phone” despite “unwanted app audio leaks to phone”.
- **UX0478** For playing from one PC application, distinguish 'silent because app paused' from 'sink missing' before prompting a fix. Verify “chosen app audible on phone” despite “unwanted app audio leaks to phone”.
- **UX0479** For playing from one PC application, log source changes locally with time and old/new sink IDs for support. Verify “chosen app audible on phone” despite “unwanted app audio leaks to phone”.
- **UX0480** Measure only intended audio captured across hotplug and monitor change before claiming auto-follow reliability.

### Moment: hearing both local and remote output

- **UX0481** Show dual-output explanation with human-readable sink name plus stable technical ID on demand.
- **UX0482** Represent both routes understood separately from the system default selection.
- **UX0483** Warn about “echo from unsynchronized PC and phone” with an explanation of its likely audible symptom.
- **UX0484** Offer choose one output or accept echo in place while keeping Stop available.
- **UX0485** For hearing both local and remote output, preview consequences for existing listeners before changing source. Verify “both routes understood” despite “echo from unsynchronized PC and phone”.
- **UX0486** For hearing both local and remote output, record the last working sink per PC profile, not as an opaque global string. Verify “both routes understood” despite “echo from unsynchronized PC and phone”.
- **UX0487** For hearing both local and remote output, avoid selecting a monitor/source node when the user asked for an output sink. Verify “both routes understood” despite “echo from unsynchronized PC and phone”.
- **UX0488** For hearing both local and remote output, show a signal meter only if the capture path reports real audio levels. Verify “both routes understood” despite “echo from unsynchronized PC and phone”.
- **UX0489** For hearing both local and remote output, make a missing device a recoverable state, not a blank dropdown. Verify “both routes understood” despite “echo from unsynchronized PC and phone”.
- **UX0490** For hearing both local and remote output, surface a safe test-tone option at a modest volume when technically available. Verify “both routes understood” despite “echo from unsynchronized PC and phone”.
- **UX0491** For hearing both local and remote output, keep source controls disabled with a reason while switching could break playback. Verify “both routes understood” despite “echo from unsynchronized PC and phone”.
- **UX0492** For hearing both local and remote output, allow mouse, keyboard and screen reader users to identify the same sink. Verify “both routes understood” despite “echo from unsynchronized PC and phone”.
- **UX0493** For hearing both local and remote output, provide an explicit default-versus-pinned choice in the advanced view. Verify “both routes understood” despite “echo from unsynchronized PC and phone”.
- **UX0494** For hearing both local and remote output, distinguish 'silent because app paused' from 'sink missing' before prompting a fix. Verify “both routes understood” despite “echo from unsynchronized PC and phone”.
- **UX0495** For hearing both local and remote output, log source changes locally with time and old/new sink IDs for support. Verify “both routes understood” despite “echo from unsynchronized PC and phone”.
- **UX0496** Measure fewer echo-related support reports across hotplug and monitor change before claiming auto-follow reliability.

### Moment: refreshing a changing sink list

- **UX0497** Show PipeWire discovery with human-readable sink name plus stable technical ID on demand.
- **UX0498** Represent fresh sinks displayed separately from the system default selection.
- **UX0499** Warn about “refresh blocks GTK or loses selection” with an explanation of its likely audible symptom.
- **UX0500** Offer retry without losing current choice in place while keeping Stop available.
- **UX0501** For refreshing a changing sink list, preview consequences for existing listeners before changing source. Verify “fresh sinks displayed” despite “refresh blocks GTK or loses selection”.
- **UX0502** For refreshing a changing sink list, record the last working sink per PC profile, not as an opaque global string. Verify “fresh sinks displayed” despite “refresh blocks GTK or loses selection”.
- **UX0503** For refreshing a changing sink list, avoid selecting a monitor/source node when the user asked for an output sink. Verify “fresh sinks displayed” despite “refresh blocks GTK or loses selection”.
- **UX0504** For refreshing a changing sink list, show a signal meter only if the capture path reports real audio levels. Verify “fresh sinks displayed” despite “refresh blocks GTK or loses selection”.
- **UX0505** For refreshing a changing sink list, make a missing device a recoverable state, not a blank dropdown. Verify “fresh sinks displayed” despite “refresh blocks GTK or loses selection”.
- **UX0506** For refreshing a changing sink list, surface a safe test-tone option at a modest volume when technically available. Verify “fresh sinks displayed” despite “refresh blocks GTK or loses selection”.
- **UX0507** For refreshing a changing sink list, keep source controls disabled with a reason while switching could break playback. Verify “fresh sinks displayed” despite “refresh blocks GTK or loses selection”.
- **UX0508** For refreshing a changing sink list, allow mouse, keyboard and screen reader users to identify the same sink. Verify “fresh sinks displayed” despite “refresh blocks GTK or loses selection”.
- **UX0509** For refreshing a changing sink list, provide an explicit default-versus-pinned choice in the advanced view. Verify “fresh sinks displayed” despite “refresh blocks GTK or loses selection”.
- **UX0510** For refreshing a changing sink list, distinguish 'silent because app paused' from 'sink missing' before prompting a fix. Verify “fresh sinks displayed” despite “refresh blocks GTK or loses selection”.
- **UX0511** For refreshing a changing sink list, log source changes locally with time and old/new sink IDs for support. Verify “fresh sinks displayed” despite “refresh blocks GTK or loses selection”.
- **UX0512** Measure responsive refresh under timeout across hotplug and monitor change before claiming auto-follow reliability.

## 05 · Audio level and hearing comfort

### Moment: changing phone media volume

- **UX0513** Use Android media volume wording that separates source level, transport gain and Android hardware volume.
- **UX0514** Show comfortable output level as a numeric value and audible effect, not a decorative slider position.
- **UX0515** Explain why “system volume is confused with app gain” happens before the user raises amplification as a workaround.
- **UX0516** Offer adjust media volume with a safe one-tap default restore beside the control.
- **UX0517** For changing phone media volume, preview the target level when audio route changes before unmuting. Verify “comfortable output level” despite “system volume is confused with app gain”.
- **UX0518** For changing phone media volume, constrain high-risk gain with clear warnings and a fast escape hatch. Verify “comfortable output level” despite “system volume is confused with app gain”.
- **UX0519** For changing phone media volume, show output device names rather than a generic speaker icon when a route is active. Verify “comfortable output level” despite “system volume is confused with app gain”.
- **UX0520** For changing phone media volume, avoid playing a diagnostic beep automatically on a new output route. Verify “comfortable output level” despite “system volume is confused with app gain”.
- **UX0521** For changing phone media volume, prefer smooth, short level transitions over sudden discontinuities. Verify “comfortable output level” despite “system volume is confused with app gain”.
- **UX0522** For changing phone media volume, keep slider adjustments responsive while a stream is active; show apply errors. Verify “comfortable output level” despite “system volume is confused with app gain”.
- **UX0523** For changing phone media volume, announce value changes via screen reader in manageable increments. Verify “comfortable output level” despite “system volume is confused with app gain”.
- **UX0524** For changing phone media volume, provide keyboard/Home/End adjustments with bounded steps on desktop. Verify “comfortable output level” despite “system volume is confused with app gain”.
- **UX0525** For changing phone media volume, offer a per-route preference only after users can see and override it. Verify “comfortable output level” despite “system volume is confused with app gain”.
- **UX0526** For changing phone media volume, never call a signal 'safe' based solely on a visual meter; preserve hearing caveats. Verify “comfortable output level” despite “system volume is confused with app gain”.
- **UX0527** For changing phone media volume, test actual PCM amplitude before labeling a boost or limiter effective. Verify “comfortable output level” despite “system volume is confused with app gain”.
- **UX0528** Measure safe comfortable loudness through user trials without recording their audio.

### Moment: adjusting in-app gain

- **UX0529** Use Audio Share gain slider wording that separates source level, transport gain and Android hardware volume.
- **UX0530** Show audible gain updated as a numeric value and audible effect, not a decorative slider position.
- **UX0531** Explain why “slider appears to move but sound is unchanged” happens before the user raises amplification as a workaround.
- **UX0532** Offer verify the applied value with a safe one-tap default restore beside the control.
- **UX0533** For adjusting in-app gain, preview the target level when audio route changes before unmuting. Verify “audible gain updated” despite “slider appears to move but sound is unchanged”.
- **UX0534** For adjusting in-app gain, constrain high-risk gain with clear warnings and a fast escape hatch. Verify “audible gain updated” despite “slider appears to move but sound is unchanged”.
- **UX0535** For adjusting in-app gain, show output device names rather than a generic speaker icon when a route is active. Verify “audible gain updated” despite “slider appears to move but sound is unchanged”.
- **UX0536** For adjusting in-app gain, avoid playing a diagnostic beep automatically on a new output route. Verify “audible gain updated” despite “slider appears to move but sound is unchanged”.
- **UX0537** For adjusting in-app gain, prefer smooth, short level transitions over sudden discontinuities. Verify “audible gain updated” despite “slider appears to move but sound is unchanged”.
- **UX0538** For adjusting in-app gain, keep slider adjustments responsive while a stream is active; show apply errors. Verify “audible gain updated” despite “slider appears to move but sound is unchanged”.
- **UX0539** For adjusting in-app gain, announce value changes via screen reader in manageable increments. Verify “audible gain updated” despite “slider appears to move but sound is unchanged”.
- **UX0540** For adjusting in-app gain, provide keyboard/Home/End adjustments with bounded steps on desktop. Verify “audible gain updated” despite “slider appears to move but sound is unchanged”.
- **UX0541** For adjusting in-app gain, offer a per-route preference only after users can see and override it. Verify “audible gain updated” despite “slider appears to move but sound is unchanged”.
- **UX0542** For adjusting in-app gain, never call a signal 'safe' based solely on a visual meter; preserve hearing caveats. Verify “audible gain updated” despite “slider appears to move but sound is unchanged”.
- **UX0543** For adjusting in-app gain, test actual PCM amplitude before labeling a boost or limiter effective. Verify “audible gain updated” despite “slider appears to move but sound is unchanged”.
- **UX0544** Measure slider changes actual sound through user trials without recording their audio.

### Moment: using loudness enhancement

- **UX0545** Use loudness enhancer wording that separates source level, transport gain and Android hardware volume.
- **UX0546** Show safe boost selected as a numeric value and audible effect, not a decorative slider position.
- **UX0547** Explain why “large gain clips or hurts ears” happens before the user raises amplification as a workaround.
- **UX0548** Offer lower enhancement with a safe one-tap default restore beside the control.
- **UX0549** For using loudness enhancement, preview the target level when audio route changes before unmuting. Verify “safe boost selected” despite “large gain clips or hurts ears”.
- **UX0550** For using loudness enhancement, constrain high-risk gain with clear warnings and a fast escape hatch. Verify “safe boost selected” despite “large gain clips or hurts ears”.
- **UX0551** For using loudness enhancement, show output device names rather than a generic speaker icon when a route is active. Verify “safe boost selected” despite “large gain clips or hurts ears”.
- **UX0552** For using loudness enhancement, avoid playing a diagnostic beep automatically on a new output route. Verify “safe boost selected” despite “large gain clips or hurts ears”.
- **UX0553** For using loudness enhancement, prefer smooth, short level transitions over sudden discontinuities. Verify “safe boost selected” despite “large gain clips or hurts ears”.
- **UX0554** For using loudness enhancement, keep slider adjustments responsive while a stream is active; show apply errors. Verify “safe boost selected” despite “large gain clips or hurts ears”.
- **UX0555** For using loudness enhancement, announce value changes via screen reader in manageable increments. Verify “safe boost selected” despite “large gain clips or hurts ears”.
- **UX0556** For using loudness enhancement, provide keyboard/Home/End adjustments with bounded steps on desktop. Verify “safe boost selected” despite “large gain clips or hurts ears”.
- **UX0557** For using loudness enhancement, offer a per-route preference only after users can see and override it. Verify “safe boost selected” despite “large gain clips or hurts ears”.
- **UX0558** For using loudness enhancement, never call a signal 'safe' based solely on a visual meter; preserve hearing caveats. Verify “safe boost selected” despite “large gain clips or hurts ears”.
- **UX0559** For using loudness enhancement, test actual PCM amplitude before labeling a boost or limiter effective. Verify “safe boost selected” despite “large gain clips or hurts ears”.
- **UX0560** Measure no clipped output at default through user trials without recording their audio.

### Moment: switching between phone speaker and earbuds

- **UX0561** Use output route levels wording that separates source level, transport gain and Android hardware volume.
- **UX0562** Show route-specific comfort preserved as a numeric value and audible effect, not a decorative slider position.
- **UX0563** Explain why “new route is much louder” happens before the user raises amplification as a workaround.
- **UX0564** Offer confirm adjusted level with a safe one-tap default restore beside the control.
- **UX0565** For switching between phone speaker and earbuds, preview the target level when audio route changes before unmuting. Verify “route-specific comfort preserved” despite “new route is much louder”.
- **UX0566** For switching between phone speaker and earbuds, constrain high-risk gain with clear warnings and a fast escape hatch. Verify “route-specific comfort preserved” despite “new route is much louder”.
- **UX0567** For switching between phone speaker and earbuds, show output device names rather than a generic speaker icon when a route is active. Verify “route-specific comfort preserved” despite “new route is much louder”.
- **UX0568** For switching between phone speaker and earbuds, avoid playing a diagnostic beep automatically on a new output route. Verify “route-specific comfort preserved” despite “new route is much louder”.
- **UX0569** For switching between phone speaker and earbuds, prefer smooth, short level transitions over sudden discontinuities. Verify “route-specific comfort preserved” despite “new route is much louder”.
- **UX0570** For switching between phone speaker and earbuds, keep slider adjustments responsive while a stream is active; show apply errors. Verify “route-specific comfort preserved” despite “new route is much louder”.
- **UX0571** For switching between phone speaker and earbuds, announce value changes via screen reader in manageable increments. Verify “route-specific comfort preserved” despite “new route is much louder”.
- **UX0572** For switching between phone speaker and earbuds, provide keyboard/Home/End adjustments with bounded steps on desktop. Verify “route-specific comfort preserved” despite “new route is much louder”.
- **UX0573** For switching between phone speaker and earbuds, offer a per-route preference only after users can see and override it. Verify “route-specific comfort preserved” despite “new route is much louder”.
- **UX0574** For switching between phone speaker and earbuds, never call a signal 'safe' based solely on a visual meter; preserve hearing caveats. Verify “route-specific comfort preserved” despite “new route is much louder”.
- **UX0575** For switching between phone speaker and earbuds, test actual PCM amplitude before labeling a boost or limiter effective. Verify “route-specific comfort preserved” despite “new route is much louder”.
- **UX0576** Measure no sudden loud transition through user trials without recording their audio.

### Moment: playing late at night

- **UX0577** Use quiet-listening preset wording that separates source level, transport gain and Android hardware volume.
- **UX0578** Show low distraction level as a numeric value and audible effect, not a decorative slider position.
- **UX0579** Explain why “notification or test tone wakes others” happens before the user raises amplification as a workaround.
- **UX0580** Offer enable quiet mode with a safe one-tap default restore beside the control.
- **UX0581** For playing late at night, preview the target level when audio route changes before unmuting. Verify “low distraction level” despite “notification or test tone wakes others”.
- **UX0582** For playing late at night, constrain high-risk gain with clear warnings and a fast escape hatch. Verify “low distraction level” despite “notification or test tone wakes others”.
- **UX0583** For playing late at night, show output device names rather than a generic speaker icon when a route is active. Verify “low distraction level” despite “notification or test tone wakes others”.
- **UX0584** For playing late at night, avoid playing a diagnostic beep automatically on a new output route. Verify “low distraction level” despite “notification or test tone wakes others”.
- **UX0585** For playing late at night, prefer smooth, short level transitions over sudden discontinuities. Verify “low distraction level” despite “notification or test tone wakes others”.
- **UX0586** For playing late at night, keep slider adjustments responsive while a stream is active; show apply errors. Verify “low distraction level” despite “notification or test tone wakes others”.
- **UX0587** For playing late at night, announce value changes via screen reader in manageable increments. Verify “low distraction level” despite “notification or test tone wakes others”.
- **UX0588** For playing late at night, provide keyboard/Home/End adjustments with bounded steps on desktop. Verify “low distraction level” despite “notification or test tone wakes others”.
- **UX0589** For playing late at night, offer a per-route preference only after users can see and override it. Verify “low distraction level” despite “notification or test tone wakes others”.
- **UX0590** For playing late at night, never call a signal 'safe' based solely on a visual meter; preserve hearing caveats. Verify “low distraction level” despite “notification or test tone wakes others”.
- **UX0591** For playing late at night, test actual PCM amplitude before labeling a boost or limiter effective. Verify “low distraction level” despite “notification or test tone wakes others”.
- **UX0592** Measure night-session comfort score through user trials without recording their audio.

### Moment: using hearing aids

- **UX0593** Use assisted-listening route wording that separates source level, transport gain and Android hardware volume.
- **UX0594** Show speech intelligible as a numeric value and audible effect, not a decorative slider position.
- **UX0595** Explain why “Bluetooth aid route has unexpected delay” happens before the user raises amplification as a workaround.
- **UX0596** Offer choose stable preset with a safe one-tap default restore beside the control.
- **UX0597** For using hearing aids, preview the target level when audio route changes before unmuting. Verify “speech intelligible” despite “Bluetooth aid route has unexpected delay”.
- **UX0598** For using hearing aids, constrain high-risk gain with clear warnings and a fast escape hatch. Verify “speech intelligible” despite “Bluetooth aid route has unexpected delay”.
- **UX0599** For using hearing aids, show output device names rather than a generic speaker icon when a route is active. Verify “speech intelligible” despite “Bluetooth aid route has unexpected delay”.
- **UX0600** For using hearing aids, avoid playing a diagnostic beep automatically on a new output route. Verify “speech intelligible” despite “Bluetooth aid route has unexpected delay”.
- **UX0601** For using hearing aids, prefer smooth, short level transitions over sudden discontinuities. Verify “speech intelligible” despite “Bluetooth aid route has unexpected delay”.
- **UX0602** For using hearing aids, keep slider adjustments responsive while a stream is active; show apply errors. Verify “speech intelligible” despite “Bluetooth aid route has unexpected delay”.
- **UX0603** For using hearing aids, announce value changes via screen reader in manageable increments. Verify “speech intelligible” despite “Bluetooth aid route has unexpected delay”.
- **UX0604** For using hearing aids, provide keyboard/Home/End adjustments with bounded steps on desktop. Verify “speech intelligible” despite “Bluetooth aid route has unexpected delay”.
- **UX0605** For using hearing aids, offer a per-route preference only after users can see and override it. Verify “speech intelligible” despite “Bluetooth aid route has unexpected delay”.
- **UX0606** For using hearing aids, never call a signal 'safe' based solely on a visual meter; preserve hearing caveats. Verify “speech intelligible” despite “Bluetooth aid route has unexpected delay”.
- **UX0607** For using hearing aids, test actual PCM amplitude before labeling a boost or limiter effective. Verify “speech intelligible” despite “Bluetooth aid route has unexpected delay”.
- **UX0608** Measure task completion with assistive output through user trials without recording their audio.

### Moment: preventing sudden peaks

- **UX0609** Use peak limiter option wording that separates source level, transport gain and Android hardware volume.
- **UX0610** Show clipping risk signaled as a numeric value and audible effect, not a decorative slider position.
- **UX0611** Explain why “a loud game event jumps above normal level” happens before the user raises amplification as a workaround.
- **UX0612** Offer enable limiter cautiously with a safe one-tap default restore beside the control.
- **UX0613** For preventing sudden peaks, preview the target level when audio route changes before unmuting. Verify “clipping risk signaled” despite “a loud game event jumps above normal level”.
- **UX0614** For preventing sudden peaks, constrain high-risk gain with clear warnings and a fast escape hatch. Verify “clipping risk signaled” despite “a loud game event jumps above normal level”.
- **UX0615** For preventing sudden peaks, show output device names rather than a generic speaker icon when a route is active. Verify “clipping risk signaled” despite “a loud game event jumps above normal level”.
- **UX0616** For preventing sudden peaks, avoid playing a diagnostic beep automatically on a new output route. Verify “clipping risk signaled” despite “a loud game event jumps above normal level”.
- **UX0617** For preventing sudden peaks, prefer smooth, short level transitions over sudden discontinuities. Verify “clipping risk signaled” despite “a loud game event jumps above normal level”.
- **UX0618** For preventing sudden peaks, keep slider adjustments responsive while a stream is active; show apply errors. Verify “clipping risk signaled” despite “a loud game event jumps above normal level”.
- **UX0619** For preventing sudden peaks, announce value changes via screen reader in manageable increments. Verify “clipping risk signaled” despite “a loud game event jumps above normal level”.
- **UX0620** For preventing sudden peaks, provide keyboard/Home/End adjustments with bounded steps on desktop. Verify “clipping risk signaled” despite “a loud game event jumps above normal level”.
- **UX0621** For preventing sudden peaks, offer a per-route preference only after users can see and override it. Verify “clipping risk signaled” despite “a loud game event jumps above normal level”.
- **UX0622** For preventing sudden peaks, never call a signal 'safe' based solely on a visual meter; preserve hearing caveats. Verify “clipping risk signaled” despite “a loud game event jumps above normal level”.
- **UX0623** For preventing sudden peaks, test actual PCM amplitude before labeling a boost or limiter effective. Verify “clipping risk signaled” despite “a loud game event jumps above normal level”.
- **UX0624** Measure peak-related complaints reduced through user trials without recording their audio.

### Moment: returning from mute

- **UX0625** Use unmute transition wording that separates source level, transport gain and Android hardware volume.
- **UX0626** Show sound ramps gently as a numeric value and audible effect, not a decorative slider position.
- **UX0627** Explain why “unmute jumps to a stale high level” happens before the user raises amplification as a workaround.
- **UX0628** Offer preview level before unmute with a safe one-tap default restore beside the control.
- **UX0629** For returning from mute, preview the target level when audio route changes before unmuting. Verify “sound ramps gently” despite “unmute jumps to a stale high level”.
- **UX0630** For returning from mute, constrain high-risk gain with clear warnings and a fast escape hatch. Verify “sound ramps gently” despite “unmute jumps to a stale high level”.
- **UX0631** For returning from mute, show output device names rather than a generic speaker icon when a route is active. Verify “sound ramps gently” despite “unmute jumps to a stale high level”.
- **UX0632** For returning from mute, avoid playing a diagnostic beep automatically on a new output route. Verify “sound ramps gently” despite “unmute jumps to a stale high level”.
- **UX0633** For returning from mute, prefer smooth, short level transitions over sudden discontinuities. Verify “sound ramps gently” despite “unmute jumps to a stale high level”.
- **UX0634** For returning from mute, keep slider adjustments responsive while a stream is active; show apply errors. Verify “sound ramps gently” despite “unmute jumps to a stale high level”.
- **UX0635** For returning from mute, announce value changes via screen reader in manageable increments. Verify “sound ramps gently” despite “unmute jumps to a stale high level”.
- **UX0636** For returning from mute, provide keyboard/Home/End adjustments with bounded steps on desktop. Verify “sound ramps gently” despite “unmute jumps to a stale high level”.
- **UX0637** For returning from mute, offer a per-route preference only after users can see and override it. Verify “sound ramps gently” despite “unmute jumps to a stale high level”.
- **UX0638** For returning from mute, never call a signal 'safe' based solely on a visual meter; preserve hearing caveats. Verify “sound ramps gently” despite “unmute jumps to a stale high level”.
- **UX0639** For returning from mute, test actual PCM amplitude before labeling a boost or limiter effective. Verify “sound ramps gently” despite “unmute jumps to a stale high level”.
- **UX0640** Measure no startle after unmute through user trials without recording their audio.

## 06 · Latency, quality and stability

### Moment: watching video with phone sound

- **UX0641** Label video-sync preset by its tradeoff rather than a bare buffer count.
- **UX0642** Show dialogue tracks picture only when confirmed by measured playback data.
- **UX0643** Tie the symptom “audio trails lip movements” to loss, underruns and route metrics instead of a generic 'lag' badge.
- **UX0644** Offer run sync calibration with a reversible comparison to last working values.
- **UX0645** For watching video with phone sound, explain that network ping is not end-to-end audible latency. Verify “dialogue tracks picture” despite “audio trails lip movements”.
- **UX0646** For watching video with phone sound, show measured, estimated and unavailable values with distinct labels. Verify “dialogue tracks picture” despite “audio trails lip movements”.
- **UX0647** For watching video with phone sound, avoid promising zero latency on USB or any other transport. Verify “dialogue tracks picture” despite “audio trails lip movements”.
- **UX0648** For watching video with phone sound, provide a brief A/B sample test before applying an advanced audio preset. Verify “dialogue tracks picture” despite “audio trails lip movements”.
- **UX0649** For watching video with phone sound, use a bounded graph window so momentary spikes do not look like permanent failure. Verify “dialogue tracks picture” despite “audio trails lip movements”.
- **UX0650** For watching video with phone sound, offer a simple Stable/Video/Gaming mode and hide expert knobs by default. Verify “dialogue tracks picture” despite “audio trails lip movements”.
- **UX0651** For watching video with phone sound, warn when a smaller buffer could increase clicks or cutouts. Verify “dialogue tracks picture” despite “audio trails lip movements”.
- **UX0652** For watching video with phone sound, give underflow counts a human explanation and a safe starting fix. Verify “dialogue tracks picture” despite “audio trails lip movements”.
- **UX0653** For watching video with phone sound, preserve playback continuity while updating only controls safe to change live. Verify “dialogue tracks picture” despite “audio trails lip movements”.
- **UX0654** For watching video with phone sound, screen-reader summaries should speak trend and value without announcing every packet. Verify “dialogue tracks picture” despite “audio trails lip movements”.
- **UX0655** For watching video with phone sound, only show codec/bit depth claims when the negotiated format is known. Verify “dialogue tracks picture” despite “audio trails lip movements”.
- **UX0656** Measure measured audiovisual offset on real devices before promoting the preset.

### Moment: playing an action game

- **UX0657** Label gaming preset by its tradeoff rather than a bare buffer count.
- **UX0658** Show low-latency mode stable only when confirmed by measured playback data.
- **UX0659** Tie the symptom “buffer is too deep for reactions” to loss, underruns and route metrics instead of a generic 'lag' badge.
- **UX0660** Offer try tested gaming buffer with a reversible comparison to last working values.
- **UX0661** For playing an action game, explain that network ping is not end-to-end audible latency. Verify “low-latency mode stable” despite “buffer is too deep for reactions”.
- **UX0662** For playing an action game, show measured, estimated and unavailable values with distinct labels. Verify “low-latency mode stable” despite “buffer is too deep for reactions”.
- **UX0663** For playing an action game, avoid promising zero latency on USB or any other transport. Verify “low-latency mode stable” despite “buffer is too deep for reactions”.
- **UX0664** For playing an action game, provide a brief A/B sample test before applying an advanced audio preset. Verify “low-latency mode stable” despite “buffer is too deep for reactions”.
- **UX0665** For playing an action game, use a bounded graph window so momentary spikes do not look like permanent failure. Verify “low-latency mode stable” despite “buffer is too deep for reactions”.
- **UX0666** For playing an action game, offer a simple Stable/Video/Gaming mode and hide expert knobs by default. Verify “low-latency mode stable” despite “buffer is too deep for reactions”.
- **UX0667** For playing an action game, warn when a smaller buffer could increase clicks or cutouts. Verify “low-latency mode stable” despite “buffer is too deep for reactions”.
- **UX0668** For playing an action game, give underflow counts a human explanation and a safe starting fix. Verify “low-latency mode stable” despite “buffer is too deep for reactions”.
- **UX0669** For playing an action game, preserve playback continuity while updating only controls safe to change live. Verify “low-latency mode stable” despite “buffer is too deep for reactions”.
- **UX0670** For playing an action game, screen-reader summaries should speak trend and value without announcing every packet. Verify “low-latency mode stable” despite “buffer is too deep for reactions”.
- **UX0671** For playing an action game, only show codec/bit depth claims when the negotiated format is known. Verify “low-latency mode stable” despite “buffer is too deep for reactions”.
- **UX0672** Measure p95 latency and underruns on real devices before promoting the preset.

### Moment: listening to music over Wi-Fi

- **UX0673** Label music stability profile by its tradeoff rather than a bare buffer count.
- **UX0674** Show music plays without gaps only when confirmed by measured playback data.
- **UX0675** Tie the symptom “weak Wi-Fi causes short dropouts” to loss, underruns and route metrics instead of a generic 'lag' badge.
- **UX0676** Offer select stable buffer with a reversible comparison to last working values.
- **UX0677** For listening to music over Wi-Fi, explain that network ping is not end-to-end audible latency. Verify “music plays without gaps” despite “weak Wi-Fi causes short dropouts”.
- **UX0678** For listening to music over Wi-Fi, show measured, estimated and unavailable values with distinct labels. Verify “music plays without gaps” despite “weak Wi-Fi causes short dropouts”.
- **UX0679** For listening to music over Wi-Fi, avoid promising zero latency on USB or any other transport. Verify “music plays without gaps” despite “weak Wi-Fi causes short dropouts”.
- **UX0680** For listening to music over Wi-Fi, provide a brief A/B sample test before applying an advanced audio preset. Verify “music plays without gaps” despite “weak Wi-Fi causes short dropouts”.
- **UX0681** For listening to music over Wi-Fi, use a bounded graph window so momentary spikes do not look like permanent failure. Verify “music plays without gaps” despite “weak Wi-Fi causes short dropouts”.
- **UX0682** For listening to music over Wi-Fi, offer a simple Stable/Video/Gaming mode and hide expert knobs by default. Verify “music plays without gaps” despite “weak Wi-Fi causes short dropouts”.
- **UX0683** For listening to music over Wi-Fi, warn when a smaller buffer could increase clicks or cutouts. Verify “music plays without gaps” despite “weak Wi-Fi causes short dropouts”.
- **UX0684** For listening to music over Wi-Fi, give underflow counts a human explanation and a safe starting fix. Verify “music plays without gaps” despite “weak Wi-Fi causes short dropouts”.
- **UX0685** For listening to music over Wi-Fi, preserve playback continuity while updating only controls safe to change live. Verify “music plays without gaps” despite “weak Wi-Fi causes short dropouts”.
- **UX0686** For listening to music over Wi-Fi, screen-reader summaries should speak trend and value without announcing every packet. Verify “music plays without gaps” despite “weak Wi-Fi causes short dropouts”.
- **UX0687** For listening to music over Wi-Fi, only show codec/bit depth claims when the negotiated format is known. Verify “music plays without gaps” despite “weak Wi-Fi causes short dropouts”.
- **UX0688** Measure uninterrupted session time on real devices before promoting the preset.

### Moment: changing AudioTrack buffer

- **UX0689** Label buffer-delay control by its tradeoff rather than a bare buffer count.
- **UX0690** Show chosen latency/stability tradeoff applied only when confirmed by measured playback data.
- **UX0691** Tie the symptom “buffer value has no visible effect” to loss, underruns and route metrics instead of a generic 'lag' badge.
- **UX0692** Offer compare before and after with a reversible comparison to last working values.
- **UX0693** For changing AudioTrack buffer, explain that network ping is not end-to-end audible latency. Verify “chosen latency/stability tradeoff applied” despite “buffer value has no visible effect”.
- **UX0694** For changing AudioTrack buffer, show measured, estimated and unavailable values with distinct labels. Verify “chosen latency/stability tradeoff applied” despite “buffer value has no visible effect”.
- **UX0695** For changing AudioTrack buffer, avoid promising zero latency on USB or any other transport. Verify “chosen latency/stability tradeoff applied” despite “buffer value has no visible effect”.
- **UX0696** For changing AudioTrack buffer, provide a brief A/B sample test before applying an advanced audio preset. Verify “chosen latency/stability tradeoff applied” despite “buffer value has no visible effect”.
- **UX0697** For changing AudioTrack buffer, use a bounded graph window so momentary spikes do not look like permanent failure. Verify “chosen latency/stability tradeoff applied” despite “buffer value has no visible effect”.
- **UX0698** For changing AudioTrack buffer, offer a simple Stable/Video/Gaming mode and hide expert knobs by default. Verify “chosen latency/stability tradeoff applied” despite “buffer value has no visible effect”.
- **UX0699** For changing AudioTrack buffer, warn when a smaller buffer could increase clicks or cutouts. Verify “chosen latency/stability tradeoff applied” despite “buffer value has no visible effect”.
- **UX0700** For changing AudioTrack buffer, give underflow counts a human explanation and a safe starting fix. Verify “chosen latency/stability tradeoff applied” despite “buffer value has no visible effect”.
- **UX0701** For changing AudioTrack buffer, preserve playback continuity while updating only controls safe to change live. Verify “chosen latency/stability tradeoff applied” despite “buffer value has no visible effect”.
- **UX0702** For changing AudioTrack buffer, screen-reader summaries should speak trend and value without announcing every packet. Verify “chosen latency/stability tradeoff applied” despite “buffer value has no visible effect”.
- **UX0703** For changing AudioTrack buffer, only show codec/bit depth claims when the negotiated format is known. Verify “chosen latency/stability tradeoff applied” despite “buffer value has no visible effect”.
- **UX0704** Measure underruns at chosen buffer on real devices before promoting the preset.

### Moment: using a slow phone

- **UX0705** Label device capability hint by its tradeoff rather than a bare buffer count.
- **UX0706** Show playback stays smooth only when confirmed by measured playback data.
- **UX0707** Tie the symptom “older device cannot process format quickly” to loss, underruns and route metrics instead of a generic 'lag' badge.
- **UX0708** Offer choose compatible format with a reversible comparison to last working values.
- **UX0709** For using a slow phone, explain that network ping is not end-to-end audible latency. Verify “playback stays smooth” despite “older device cannot process format quickly”.
- **UX0710** For using a slow phone, show measured, estimated and unavailable values with distinct labels. Verify “playback stays smooth” despite “older device cannot process format quickly”.
- **UX0711** For using a slow phone, avoid promising zero latency on USB or any other transport. Verify “playback stays smooth” despite “older device cannot process format quickly”.
- **UX0712** For using a slow phone, provide a brief A/B sample test before applying an advanced audio preset. Verify “playback stays smooth” despite “older device cannot process format quickly”.
- **UX0713** For using a slow phone, use a bounded graph window so momentary spikes do not look like permanent failure. Verify “playback stays smooth” despite “older device cannot process format quickly”.
- **UX0714** For using a slow phone, offer a simple Stable/Video/Gaming mode and hide expert knobs by default. Verify “playback stays smooth” despite “older device cannot process format quickly”.
- **UX0715** For using a slow phone, warn when a smaller buffer could increase clicks or cutouts. Verify “playback stays smooth” despite “older device cannot process format quickly”.
- **UX0716** For using a slow phone, give underflow counts a human explanation and a safe starting fix. Verify “playback stays smooth” despite “older device cannot process format quickly”.
- **UX0717** For using a slow phone, preserve playback continuity while updating only controls safe to change live. Verify “playback stays smooth” despite “older device cannot process format quickly”.
- **UX0718** For using a slow phone, screen-reader summaries should speak trend and value without announcing every packet. Verify “playback stays smooth” despite “older device cannot process format quickly”.
- **UX0719** For using a slow phone, only show codec/bit depth claims when the negotiated format is known. Verify “playback stays smooth” despite “older device cannot process format quickly”.
- **UX0720** Measure low-end phone first-play success on real devices before promoting the preset.

### Moment: using a congested network

- **UX0721** Label network-quality indicator by its tradeoff rather than a bare buffer count.
- **UX0722** Show congestion recognized only when confirmed by measured playback data.
- **UX0723** Tie the symptom “packet loss appears as a PC volume issue” to loss, underruns and route metrics instead of a generic 'lag' badge.
- **UX0724** Offer switch network or buffer with a reversible comparison to last working values.
- **UX0725** For using a congested network, explain that network ping is not end-to-end audible latency. Verify “congestion recognized” despite “packet loss appears as a PC volume issue”.
- **UX0726** For using a congested network, show measured, estimated and unavailable values with distinct labels. Verify “congestion recognized” despite “packet loss appears as a PC volume issue”.
- **UX0727** For using a congested network, avoid promising zero latency on USB or any other transport. Verify “congestion recognized” despite “packet loss appears as a PC volume issue”.
- **UX0728** For using a congested network, provide a brief A/B sample test before applying an advanced audio preset. Verify “congestion recognized” despite “packet loss appears as a PC volume issue”.
- **UX0729** For using a congested network, use a bounded graph window so momentary spikes do not look like permanent failure. Verify “congestion recognized” despite “packet loss appears as a PC volume issue”.
- **UX0730** For using a congested network, offer a simple Stable/Video/Gaming mode and hide expert knobs by default. Verify “congestion recognized” despite “packet loss appears as a PC volume issue”.
- **UX0731** For using a congested network, warn when a smaller buffer could increase clicks or cutouts. Verify “congestion recognized” despite “packet loss appears as a PC volume issue”.
- **UX0732** For using a congested network, give underflow counts a human explanation and a safe starting fix. Verify “congestion recognized” despite “packet loss appears as a PC volume issue”.
- **UX0733** For using a congested network, preserve playback continuity while updating only controls safe to change live. Verify “congestion recognized” despite “packet loss appears as a PC volume issue”.
- **UX0734** For using a congested network, screen-reader summaries should speak trend and value without announcing every packet. Verify “congestion recognized” despite “packet loss appears as a PC volume issue”.
- **UX0735** For using a congested network, only show codec/bit depth claims when the negotiated format is known. Verify “congestion recognized” despite “packet loss appears as a PC volume issue”.
- **UX0736** Measure reduced gaps under load on real devices before promoting the preset.

### Moment: switching sample rate

- **UX0737** Label capture format negotiation by its tradeoff rather than a bare buffer count.
- **UX0738** Show Android supports format only when confirmed by measured playback data.
- **UX0739** Tie the symptom “unsupported rate or encoding is selected” to loss, underruns and route metrics instead of a generic 'lag' badge.
- **UX0740** Offer return to default format with a reversible comparison to last working values.
- **UX0741** For switching sample rate, explain that network ping is not end-to-end audible latency. Verify “Android supports format” despite “unsupported rate or encoding is selected”.
- **UX0742** For switching sample rate, show measured, estimated and unavailable values with distinct labels. Verify “Android supports format” despite “unsupported rate or encoding is selected”.
- **UX0743** For switching sample rate, avoid promising zero latency on USB or any other transport. Verify “Android supports format” despite “unsupported rate or encoding is selected”.
- **UX0744** For switching sample rate, provide a brief A/B sample test before applying an advanced audio preset. Verify “Android supports format” despite “unsupported rate or encoding is selected”.
- **UX0745** For switching sample rate, use a bounded graph window so momentary spikes do not look like permanent failure. Verify “Android supports format” despite “unsupported rate or encoding is selected”.
- **UX0746** For switching sample rate, offer a simple Stable/Video/Gaming mode and hide expert knobs by default. Verify “Android supports format” despite “unsupported rate or encoding is selected”.
- **UX0747** For switching sample rate, warn when a smaller buffer could increase clicks or cutouts. Verify “Android supports format” despite “unsupported rate or encoding is selected”.
- **UX0748** For switching sample rate, give underflow counts a human explanation and a safe starting fix. Verify “Android supports format” despite “unsupported rate or encoding is selected”.
- **UX0749** For switching sample rate, preserve playback continuity while updating only controls safe to change live. Verify “Android supports format” despite “unsupported rate or encoding is selected”.
- **UX0750** For switching sample rate, screen-reader summaries should speak trend and value without announcing every packet. Verify “Android supports format” despite “unsupported rate or encoding is selected”.
- **UX0751** For switching sample rate, only show codec/bit depth claims when the negotiated format is known. Verify “Android supports format” despite “unsupported rate or encoding is selected”.
- **UX0752** Measure format mismatch errors reduced on real devices before promoting the preset.

### Moment: long uninterrupted session

- **UX0753** Label drift check by its tradeoff rather than a bare buffer count.
- **UX0754** Show audio/video alignment maintained only when confirmed by measured playback data.
- **UX0755** Tie the symptom “delay gradually accumulates” to loss, underruns and route metrics instead of a generic 'lag' badge.
- **UX0756** Offer resync without full reset with a reversible comparison to last working values.
- **UX0757** For long uninterrupted session, explain that network ping is not end-to-end audible latency. Verify “audio/video alignment maintained” despite “delay gradually accumulates”.
- **UX0758** For long uninterrupted session, show measured, estimated and unavailable values with distinct labels. Verify “audio/video alignment maintained” despite “delay gradually accumulates”.
- **UX0759** For long uninterrupted session, avoid promising zero latency on USB or any other transport. Verify “audio/video alignment maintained” despite “delay gradually accumulates”.
- **UX0760** For long uninterrupted session, provide a brief A/B sample test before applying an advanced audio preset. Verify “audio/video alignment maintained” despite “delay gradually accumulates”.
- **UX0761** For long uninterrupted session, use a bounded graph window so momentary spikes do not look like permanent failure. Verify “audio/video alignment maintained” despite “delay gradually accumulates”.
- **UX0762** For long uninterrupted session, offer a simple Stable/Video/Gaming mode and hide expert knobs by default. Verify “audio/video alignment maintained” despite “delay gradually accumulates”.
- **UX0763** For long uninterrupted session, warn when a smaller buffer could increase clicks or cutouts. Verify “audio/video alignment maintained” despite “delay gradually accumulates”.
- **UX0764** For long uninterrupted session, give underflow counts a human explanation and a safe starting fix. Verify “audio/video alignment maintained” despite “delay gradually accumulates”.
- **UX0765** For long uninterrupted session, preserve playback continuity while updating only controls safe to change live. Verify “audio/video alignment maintained” despite “delay gradually accumulates”.
- **UX0766** For long uninterrupted session, screen-reader summaries should speak trend and value without announcing every packet. Verify “audio/video alignment maintained” despite “delay gradually accumulates”.
- **UX0767** For long uninterrupted session, only show codec/bit depth claims when the negotiated format is known. Verify “audio/video alignment maintained” despite “delay gradually accumulates”.
- **UX0768** Measure drift after one hour on real devices before promoting the preset.

## 07 · Playback lifecycle and background comfort

### Moment: starting playback on Android

- **UX0769** State audio session preparing in words and keep it synchronized with the real service state.
- **UX0770** Make Play control available without opening advanced settings.
- **UX0771** Explain the symptom “a Play tap appears ignored” when it occurs, not in a generic permanent warning banner.
- **UX0772** Let the user view startup progress with immediate tactile/visual feedback.
- **UX0773** For starting playback on Android, keep Play, Pause and Stop semantics different; do not reuse an ambiguous single icon. Verify “audio session preparing” despite “a Play tap appears ignored”.
- **UX0774** For starting playback on Android, show reconnect attempts and remaining delay; allow cancel at every stage. Verify “audio session preparing” despite “a Play tap appears ignored”.
- **UX0775** For starting playback on Android, respect OS audio focus and media-session rules instead of bypassing them. Verify “audio session preparing” despite “a Play tap appears ignored”.
- **UX0776** For starting playback on Android, protect phone battery with bounded retries and user-visible idle status. Verify “audio session preparing” despite “a Play tap appears ignored”.
- **UX0777** For starting playback on Android, show an accurate persistent notification only while required for playback. Verify “audio session preparing” despite “a Play tap appears ignored”.
- **UX0778** For starting playback on Android, recover from rotation and process recreation without a false Playing state. Verify “audio session preparing” despite “a Play tap appears ignored”.
- **UX0779** For starting playback on Android, preserve the selected PC profile when a session ends unexpectedly. Verify “audio session preparing” despite “a Play tap appears ignored”.
- **UX0780** For starting playback on Android, announce one meaningful lifecycle change to TalkBack, not a stream of duplicates. Verify “audio session preparing” despite “a Play tap appears ignored”.
- **UX0781** For starting playback on Android, use a discreet desktop notification for unexpected loss, not normal pause events. Verify “audio session preparing” despite “a Play tap appears ignored”.
- **UX0782** For starting playback on Android, keep service state readable in the phone's quick settings and full app. Verify “audio session preparing” despite “a Play tap appears ignored”.
- **UX0783** For starting playback on Android, offer a manual reconnect even after automatic retries stop. Verify “audio session preparing” despite “a Play tap appears ignored”.
- **UX0784** Measure time to first audible sample on Android screen-off and wake cycles.

### Moment: pausing an active stream

- **UX0785** State phone playback paused in words and keep it synchronized with the real service state.
- **UX0786** Make Pause control available without opening advanced settings.
- **UX0787** Explain the symptom “server continues wasting bandwidth” when it occurs, not in a generic permanent warning banner.
- **UX0788** Let the user pause stream deliberately with immediate tactile/visual feedback.
- **UX0789** For pausing an active stream, keep Play, Pause and Stop semantics different; do not reuse an ambiguous single icon. Verify “phone playback paused” despite “server continues wasting bandwidth”.
- **UX0790** For pausing an active stream, show reconnect attempts and remaining delay; allow cancel at every stage. Verify “phone playback paused” despite “server continues wasting bandwidth”.
- **UX0791** For pausing an active stream, respect OS audio focus and media-session rules instead of bypassing them. Verify “phone playback paused” despite “server continues wasting bandwidth”.
- **UX0792** For pausing an active stream, protect phone battery with bounded retries and user-visible idle status. Verify “phone playback paused” despite “server continues wasting bandwidth”.
- **UX0793** For pausing an active stream, show an accurate persistent notification only while required for playback. Verify “phone playback paused” despite “server continues wasting bandwidth”.
- **UX0794** For pausing an active stream, recover from rotation and process recreation without a false Playing state. Verify “phone playback paused” despite “server continues wasting bandwidth”.
- **UX0795** For pausing an active stream, preserve the selected PC profile when a session ends unexpectedly. Verify “phone playback paused” despite “server continues wasting bandwidth”.
- **UX0796** For pausing an active stream, announce one meaningful lifecycle change to TalkBack, not a stream of duplicates. Verify “phone playback paused” despite “server continues wasting bandwidth”.
- **UX0797** For pausing an active stream, use a discreet desktop notification for unexpected loss, not normal pause events. Verify “phone playback paused” despite “server continues wasting bandwidth”.
- **UX0798** For pausing an active stream, keep service state readable in the phone's quick settings and full app. Verify “phone playback paused” despite “server continues wasting bandwidth”.
- **UX0799** For pausing an active stream, offer a manual reconnect even after automatic retries stop. Verify “phone playback paused” despite “server continues wasting bandwidth”.
- **UX0800** Measure pause response and battery cost on Android screen-off and wake cycles.

### Moment: resuming after a notification

- **UX0801** State playback restored correctly in words and keep it synchronized with the real service state.
- **UX0802** Make notification control available without opening advanced settings.
- **UX0803** Explain the symptom “notification button has stale state” when it occurs, not in a generic permanent warning banner.
- **UX0804** Let the user resume from notification with immediate tactile/visual feedback.
- **UX0805** For resuming after a notification, keep Play, Pause and Stop semantics different; do not reuse an ambiguous single icon. Verify “playback restored correctly” despite “notification button has stale state”.
- **UX0806** For resuming after a notification, show reconnect attempts and remaining delay; allow cancel at every stage. Verify “playback restored correctly” despite “notification button has stale state”.
- **UX0807** For resuming after a notification, respect OS audio focus and media-session rules instead of bypassing them. Verify “playback restored correctly” despite “notification button has stale state”.
- **UX0808** For resuming after a notification, protect phone battery with bounded retries and user-visible idle status. Verify “playback restored correctly” despite “notification button has stale state”.
- **UX0809** For resuming after a notification, show an accurate persistent notification only while required for playback. Verify “playback restored correctly” despite “notification button has stale state”.
- **UX0810** For resuming after a notification, recover from rotation and process recreation without a false Playing state. Verify “playback restored correctly” despite “notification button has stale state”.
- **UX0811** For resuming after a notification, preserve the selected PC profile when a session ends unexpectedly. Verify “playback restored correctly” despite “notification button has stale state”.
- **UX0812** For resuming after a notification, announce one meaningful lifecycle change to TalkBack, not a stream of duplicates. Verify “playback restored correctly” despite “notification button has stale state”.
- **UX0813** For resuming after a notification, use a discreet desktop notification for unexpected loss, not normal pause events. Verify “playback restored correctly” despite “notification button has stale state”.
- **UX0814** For resuming after a notification, keep service state readable in the phone's quick settings and full app. Verify “playback restored correctly” despite “notification button has stale state”.
- **UX0815** For resuming after a notification, offer a manual reconnect even after automatic retries stop. Verify “playback restored correctly” despite “notification button has stale state”.
- **UX0816** Measure notification action success on Android screen-off and wake cycles.

### Moment: locking the phone screen

- **UX0817** State stream remains audible in words and keep it synchronized with the real service state.
- **UX0818** Make background playback service available without opening advanced settings.
- **UX0819** Explain the symptom “battery optimizer stops service” when it occurs, not in a generic permanent warning banner.
- **UX0820** Let the user review OS restriction help with immediate tactile/visual feedback.
- **UX0821** For locking the phone screen, keep Play, Pause and Stop semantics different; do not reuse an ambiguous single icon. Verify “stream remains audible” despite “battery optimizer stops service”.
- **UX0822** For locking the phone screen, show reconnect attempts and remaining delay; allow cancel at every stage. Verify “stream remains audible” despite “battery optimizer stops service”.
- **UX0823** For locking the phone screen, respect OS audio focus and media-session rules instead of bypassing them. Verify “stream remains audible” despite “battery optimizer stops service”.
- **UX0824** For locking the phone screen, protect phone battery with bounded retries and user-visible idle status. Verify “stream remains audible” despite “battery optimizer stops service”.
- **UX0825** For locking the phone screen, show an accurate persistent notification only while required for playback. Verify “stream remains audible” despite “battery optimizer stops service”.
- **UX0826** For locking the phone screen, recover from rotation and process recreation without a false Playing state. Verify “stream remains audible” despite “battery optimizer stops service”.
- **UX0827** For locking the phone screen, preserve the selected PC profile when a session ends unexpectedly. Verify “stream remains audible” despite “battery optimizer stops service”.
- **UX0828** For locking the phone screen, announce one meaningful lifecycle change to TalkBack, not a stream of duplicates. Verify “stream remains audible” despite “battery optimizer stops service”.
- **UX0829** For locking the phone screen, use a discreet desktop notification for unexpected loss, not normal pause events. Verify “stream remains audible” despite “battery optimizer stops service”.
- **UX0830** For locking the phone screen, keep service state readable in the phone's quick settings and full app. Verify “stream remains audible” despite “battery optimizer stops service”.
- **UX0831** For locking the phone screen, offer a manual reconnect even after automatic retries stop. Verify “stream remains audible” despite “battery optimizer stops service”.
- **UX0832** Measure screen-off session reliability on Android screen-off and wake cycles.

### Moment: opening a voice call

- **UX0833** State call takes appropriate priority in words and keep it synchronized with the real service state.
- **UX0834** Make audio focus transition available without opening advanced settings.
- **UX0835** Explain the symptom “PC audio competes with call audio” when it occurs, not in a generic permanent warning banner.
- **UX0836** Let the user pause or duck stream with immediate tactile/visual feedback.
- **UX0837** For opening a voice call, keep Play, Pause and Stop semantics different; do not reuse an ambiguous single icon. Verify “call takes appropriate priority” despite “PC audio competes with call audio”.
- **UX0838** For opening a voice call, show reconnect attempts and remaining delay; allow cancel at every stage. Verify “call takes appropriate priority” despite “PC audio competes with call audio”.
- **UX0839** For opening a voice call, respect OS audio focus and media-session rules instead of bypassing them. Verify “call takes appropriate priority” despite “PC audio competes with call audio”.
- **UX0840** For opening a voice call, protect phone battery with bounded retries and user-visible idle status. Verify “call takes appropriate priority” despite “PC audio competes with call audio”.
- **UX0841** For opening a voice call, show an accurate persistent notification only while required for playback. Verify “call takes appropriate priority” despite “PC audio competes with call audio”.
- **UX0842** For opening a voice call, recover from rotation and process recreation without a false Playing state. Verify “call takes appropriate priority” despite “PC audio competes with call audio”.
- **UX0843** For opening a voice call, preserve the selected PC profile when a session ends unexpectedly. Verify “call takes appropriate priority” despite “PC audio competes with call audio”.
- **UX0844** For opening a voice call, announce one meaningful lifecycle change to TalkBack, not a stream of duplicates. Verify “call takes appropriate priority” despite “PC audio competes with call audio”.
- **UX0845** For opening a voice call, use a discreet desktop notification for unexpected loss, not normal pause events. Verify “call takes appropriate priority” despite “PC audio competes with call audio”.
- **UX0846** For opening a voice call, keep service state readable in the phone's quick settings and full app. Verify “call takes appropriate priority” despite “PC audio competes with call audio”.
- **UX0847** For opening a voice call, offer a manual reconnect even after automatic retries stop. Verify “call takes appropriate priority” despite “PC audio competes with call audio”.
- **UX0848** Measure correct focus behavior on Android screen-off and wake cycles.

### Moment: sleeping and waking the PC

- **UX0849** State user sees reconnection status in words and keep it synchronized with the real service state.
- **UX0850** Make resume state available without opening advanced settings.
- **UX0851** Explain the symptom “sleep leaves a phantom active server” when it occurs, not in a generic permanent warning banner.
- **UX0852** Let the user retry after wake with immediate tactile/visual feedback.
- **UX0853** For sleeping and waking the PC, keep Play, Pause and Stop semantics different; do not reuse an ambiguous single icon. Verify “user sees reconnection status” despite “sleep leaves a phantom active server”.
- **UX0854** For sleeping and waking the PC, show reconnect attempts and remaining delay; allow cancel at every stage. Verify “user sees reconnection status” despite “sleep leaves a phantom active server”.
- **UX0855** For sleeping and waking the PC, respect OS audio focus and media-session rules instead of bypassing them. Verify “user sees reconnection status” despite “sleep leaves a phantom active server”.
- **UX0856** For sleeping and waking the PC, protect phone battery with bounded retries and user-visible idle status. Verify “user sees reconnection status” despite “sleep leaves a phantom active server”.
- **UX0857** For sleeping and waking the PC, show an accurate persistent notification only while required for playback. Verify “user sees reconnection status” despite “sleep leaves a phantom active server”.
- **UX0858** For sleeping and waking the PC, recover from rotation and process recreation without a false Playing state. Verify “user sees reconnection status” despite “sleep leaves a phantom active server”.
- **UX0859** For sleeping and waking the PC, preserve the selected PC profile when a session ends unexpectedly. Verify “user sees reconnection status” despite “sleep leaves a phantom active server”.
- **UX0860** For sleeping and waking the PC, announce one meaningful lifecycle change to TalkBack, not a stream of duplicates. Verify “user sees reconnection status” despite “sleep leaves a phantom active server”.
- **UX0861** For sleeping and waking the PC, use a discreet desktop notification for unexpected loss, not normal pause events. Verify “user sees reconnection status” despite “sleep leaves a phantom active server”.
- **UX0862** For sleeping and waking the PC, keep service state readable in the phone's quick settings and full app. Verify “user sees reconnection status” despite “sleep leaves a phantom active server”.
- **UX0863** For sleeping and waking the PC, offer a manual reconnect even after automatic retries stop. Verify “user sees reconnection status” despite “sleep leaves a phantom active server”.
- **UX0864** Measure time to recovered playback on Android screen-off and wake cycles.

### Moment: leaving the Wi-Fi network

- **UX0865** State stream stops cleanly in words and keep it synchronized with the real service state.
- **UX0866** Make disconnect state available without opening advanced settings.
- **UX0867** Explain the symptom “infinite reconnect drains battery” when it occurs, not in a generic permanent warning banner.
- **UX0868** Let the user cancel retry with immediate tactile/visual feedback.
- **UX0869** For leaving the Wi-Fi network, keep Play, Pause and Stop semantics different; do not reuse an ambiguous single icon. Verify “stream stops cleanly” despite “infinite reconnect drains battery”.
- **UX0870** For leaving the Wi-Fi network, show reconnect attempts and remaining delay; allow cancel at every stage. Verify “stream stops cleanly” despite “infinite reconnect drains battery”.
- **UX0871** For leaving the Wi-Fi network, respect OS audio focus and media-session rules instead of bypassing them. Verify “stream stops cleanly” despite “infinite reconnect drains battery”.
- **UX0872** For leaving the Wi-Fi network, protect phone battery with bounded retries and user-visible idle status. Verify “stream stops cleanly” despite “infinite reconnect drains battery”.
- **UX0873** For leaving the Wi-Fi network, show an accurate persistent notification only while required for playback. Verify “stream stops cleanly” despite “infinite reconnect drains battery”.
- **UX0874** For leaving the Wi-Fi network, recover from rotation and process recreation without a false Playing state. Verify “stream stops cleanly” despite “infinite reconnect drains battery”.
- **UX0875** For leaving the Wi-Fi network, preserve the selected PC profile when a session ends unexpectedly. Verify “stream stops cleanly” despite “infinite reconnect drains battery”.
- **UX0876** For leaving the Wi-Fi network, announce one meaningful lifecycle change to TalkBack, not a stream of duplicates. Verify “stream stops cleanly” despite “infinite reconnect drains battery”.
- **UX0877** For leaving the Wi-Fi network, use a discreet desktop notification for unexpected loss, not normal pause events. Verify “stream stops cleanly” despite “infinite reconnect drains battery”.
- **UX0878** For leaving the Wi-Fi network, keep service state readable in the phone's quick settings and full app. Verify “stream stops cleanly” despite “infinite reconnect drains battery”.
- **UX0879** For leaving the Wi-Fi network, offer a manual reconnect even after automatic retries stop. Verify “stream stops cleanly” despite “infinite reconnect drains battery”.
- **UX0880** Measure idle battery after disconnect on Android screen-off and wake cycles.

### Moment: closing the desktop window

- **UX0881** State expected session lifetime in words and keep it synchronized with the real service state.
- **UX0882** Make server lifetime choice available without opening advanced settings.
- **UX0883** Explain the symptom “close accidentally kills active stream” when it occurs, not in a generic permanent warning banner.
- **UX0884** Let the user choose keep-running or stop with immediate tactile/visual feedback.
- **UX0885** For closing the desktop window, keep Play, Pause and Stop semantics different; do not reuse an ambiguous single icon. Verify “expected session lifetime” despite “close accidentally kills active stream”.
- **UX0886** For closing the desktop window, show reconnect attempts and remaining delay; allow cancel at every stage. Verify “expected session lifetime” despite “close accidentally kills active stream”.
- **UX0887** For closing the desktop window, respect OS audio focus and media-session rules instead of bypassing them. Verify “expected session lifetime” despite “close accidentally kills active stream”.
- **UX0888** For closing the desktop window, protect phone battery with bounded retries and user-visible idle status. Verify “expected session lifetime” despite “close accidentally kills active stream”.
- **UX0889** For closing the desktop window, show an accurate persistent notification only while required for playback. Verify “expected session lifetime” despite “close accidentally kills active stream”.
- **UX0890** For closing the desktop window, recover from rotation and process recreation without a false Playing state. Verify “expected session lifetime” despite “close accidentally kills active stream”.
- **UX0891** For closing the desktop window, preserve the selected PC profile when a session ends unexpectedly. Verify “expected session lifetime” despite “close accidentally kills active stream”.
- **UX0892** For closing the desktop window, announce one meaningful lifecycle change to TalkBack, not a stream of duplicates. Verify “expected session lifetime” despite “close accidentally kills active stream”.
- **UX0893** For closing the desktop window, use a discreet desktop notification for unexpected loss, not normal pause events. Verify “expected session lifetime” despite “close accidentally kills active stream”.
- **UX0894** For closing the desktop window, keep service state readable in the phone's quick settings and full app. Verify “expected session lifetime” despite “close accidentally kills active stream”.
- **UX0895** For closing the desktop window, offer a manual reconnect even after automatic retries stop. Verify “expected session lifetime” despite “close accidentally kills active stream”.
- **UX0896** Measure unexpected-stop complaints on Android screen-off and wake cycles.

## 08 · Recovery, diagnostics and help

### Moment: a bind-address error

- **UX0897** Title the bind failure card with the concrete failed operation, not 'Something went wrong'.
- **UX0898** Show correct local bind chosen only after a retry check confirms it.
- **UX0899** Explain the failure mode “address is not assigned to this PC” using a likely cause and one verifiable next step.
- **UX0900** Put select listed interface beside the error with an explicit retry/cancel affordance.
- **UX0901** For a bind-address error, record a short timestamped local timeline without raw audio samples. Verify “correct local bind chosen” despite “address is not assigned to this PC”.
- **UX0902** For a bind-address error, separate a fixable local setting from a remote device or network issue. Verify “correct local bind chosen” despite “address is not assigned to this PC”.
- **UX0903** For a bind-address error, keep error details selectable and copyable without dumping an unbounded log. Verify “correct local bind chosen” despite “address is not assigned to this PC”.
- **UX0904** For a bind-address error, offer one safe reset scope instead of resetting every saved profile. Verify “correct local bind chosen” despite “address is not assigned to this PC”.
- **UX0905** For a bind-address error, use a passive banner for transient failure and a modal only for user-initiated destructive action. Verify “correct local bind chosen” despite “address is not assigned to this PC”.
- **UX0906** For a bind-address error, never ask users to disable the whole firewall to resolve this case. Verify “correct local bind chosen” despite “address is not assigned to this PC”.
- **UX0907** For a bind-address error, show support commands as copyable text, not automatic root execution. Verify “correct local bind chosen” despite “address is not assigned to this PC”.
- **UX0908** For a bind-address error, include expected result and fallback for the proposed recovery step. Verify “correct local bind chosen” despite “address is not assigned to this PC”.
- **UX0909** For a bind-address error, avoid blaming the phone when PipeWire or the PC sink is the failing component. Verify “correct local bind chosen” despite “address is not assigned to this PC”.
- **UX0910** For a bind-address error, provide a screen-reader announcement once the retry outcome is known. Verify “correct local bind chosen” despite “address is not assigned to this PC”.
- **UX0911** For a bind-address error, allow privacy preview before any diagnostic file leaves the device. Verify “correct local bind chosen” despite “address is not assigned to this PC”.
- **UX0912** Measure recover without terminal to prioritize real failures over hypothetical ones.

### Moment: no route to host

- **UX0913** Title the route failure card with the concrete failed operation, not 'Something went wrong'.
- **UX0914** Show network path diagnosed only after a retry check confirms it.
- **UX0915** Explain the failure mode “phone and PC are on isolated subnets” using a likely cause and one verifiable next step.
- **UX0916** Put inspect both networks beside the error with an explicit retry/cancel affordance.
- **UX0917** For no route to host, record a short timestamped local timeline without raw audio samples. Verify “network path diagnosed” despite “phone and PC are on isolated subnets”.
- **UX0918** For no route to host, separate a fixable local setting from a remote device or network issue. Verify “network path diagnosed” despite “phone and PC are on isolated subnets”.
- **UX0919** For no route to host, keep error details selectable and copyable without dumping an unbounded log. Verify “network path diagnosed” despite “phone and PC are on isolated subnets”.
- **UX0920** For no route to host, offer one safe reset scope instead of resetting every saved profile. Verify “network path diagnosed” despite “phone and PC are on isolated subnets”.
- **UX0921** For no route to host, use a passive banner for transient failure and a modal only for user-initiated destructive action. Verify “network path diagnosed” despite “phone and PC are on isolated subnets”.
- **UX0922** For no route to host, never ask users to disable the whole firewall to resolve this case. Verify “network path diagnosed” despite “phone and PC are on isolated subnets”.
- **UX0923** For no route to host, show support commands as copyable text, not automatic root execution. Verify “network path diagnosed” despite “phone and PC are on isolated subnets”.
- **UX0924** For no route to host, include expected result and fallback for the proposed recovery step. Verify “network path diagnosed” despite “phone and PC are on isolated subnets”.
- **UX0925** For no route to host, avoid blaming the phone when PipeWire or the PC sink is the failing component. Verify “network path diagnosed” despite “phone and PC are on isolated subnets”.
- **UX0926** For no route to host, provide a screen-reader announcement once the retry outcome is known. Verify “network path diagnosed” despite “phone and PC are on isolated subnets”.
- **UX0927** For no route to host, allow privacy preview before any diagnostic file leaves the device. Verify “network path diagnosed” despite “phone and PC are on isolated subnets”.
- **UX0928** Measure route recovery time to prioritize real failures over hypothetical ones.

### Moment: TCP connects but media is silent

- **UX0929** Title the UDP path check with the concrete failed operation, not 'Something went wrong'.
- **UX0930** Show media path verified only after a retry check confirms it.
- **UX0931** Explain the failure mode “UDP blocked while TCP succeeds” using a likely cause and one verifiable next step.
- **UX0932** Put test selected UDP port beside the error with an explicit retry/cancel affordance.
- **UX0933** For TCP connects but media is silent, record a short timestamped local timeline without raw audio samples. Verify “media path verified” despite “UDP blocked while TCP succeeds”.
- **UX0934** For TCP connects but media is silent, separate a fixable local setting from a remote device or network issue. Verify “media path verified” despite “UDP blocked while TCP succeeds”.
- **UX0935** For TCP connects but media is silent, keep error details selectable and copyable without dumping an unbounded log. Verify “media path verified” despite “UDP blocked while TCP succeeds”.
- **UX0936** For TCP connects but media is silent, offer one safe reset scope instead of resetting every saved profile. Verify “media path verified” despite “UDP blocked while TCP succeeds”.
- **UX0937** For TCP connects but media is silent, use a passive banner for transient failure and a modal only for user-initiated destructive action. Verify “media path verified” despite “UDP blocked while TCP succeeds”.
- **UX0938** For TCP connects but media is silent, never ask users to disable the whole firewall to resolve this case. Verify “media path verified” despite “UDP blocked while TCP succeeds”.
- **UX0939** For TCP connects but media is silent, show support commands as copyable text, not automatic root execution. Verify “media path verified” despite “UDP blocked while TCP succeeds”.
- **UX0940** For TCP connects but media is silent, include expected result and fallback for the proposed recovery step. Verify “media path verified” despite “UDP blocked while TCP succeeds”.
- **UX0941** For TCP connects but media is silent, avoid blaming the phone when PipeWire or the PC sink is the failing component. Verify “media path verified” despite “UDP blocked while TCP succeeds”.
- **UX0942** For TCP connects but media is silent, provide a screen-reader announcement once the retry outcome is known. Verify “media path verified” despite “UDP blocked while TCP succeeds”.
- **UX0943** For TCP connects but media is silent, allow privacy preview before any diagnostic file leaves the device. Verify “media path verified” despite “UDP blocked while TCP succeeds”.
- **UX0944** Measure silent-connection resolution to prioritize real failures over hypothetical ones.

### Moment: PipeWire daemon unavailable

- **UX0945** Title the audio-service error card with the concrete failed operation, not 'Something went wrong'.
- **UX0946** Show user service restored only after a retry check confirms it.
- **UX0947** Explain the failure mode “server launched as root or no user session” using a likely cause and one verifiable next step.
- **UX0948** Put open service instructions beside the error with an explicit retry/cancel affordance.
- **UX0949** For PipeWire daemon unavailable, record a short timestamped local timeline without raw audio samples. Verify “user service restored” despite “server launched as root or no user session”.
- **UX0950** For PipeWire daemon unavailable, separate a fixable local setting from a remote device or network issue. Verify “user service restored” despite “server launched as root or no user session”.
- **UX0951** For PipeWire daemon unavailable, keep error details selectable and copyable without dumping an unbounded log. Verify “user service restored” despite “server launched as root or no user session”.
- **UX0952** For PipeWire daemon unavailable, offer one safe reset scope instead of resetting every saved profile. Verify “user service restored” despite “server launched as root or no user session”.
- **UX0953** For PipeWire daemon unavailable, use a passive banner for transient failure and a modal only for user-initiated destructive action. Verify “user service restored” despite “server launched as root or no user session”.
- **UX0954** For PipeWire daemon unavailable, never ask users to disable the whole firewall to resolve this case. Verify “user service restored” despite “server launched as root or no user session”.
- **UX0955** For PipeWire daemon unavailable, show support commands as copyable text, not automatic root execution. Verify “user service restored” despite “server launched as root or no user session”.
- **UX0956** For PipeWire daemon unavailable, include expected result and fallback for the proposed recovery step. Verify “user service restored” despite “server launched as root or no user session”.
- **UX0957** For PipeWire daemon unavailable, avoid blaming the phone when PipeWire or the PC sink is the failing component. Verify “user service restored” despite “server launched as root or no user session”.
- **UX0958** For PipeWire daemon unavailable, provide a screen-reader announcement once the retry outcome is known. Verify “user service restored” despite “server launched as root or no user session”.
- **UX0959** For PipeWire daemon unavailable, allow privacy preview before any diagnostic file leaves the device. Verify “user service restored” despite “server launched as root or no user session”.
- **UX0960** Measure service error recovery to prioritize real failures over hypothetical ones.

### Moment: endpoint disappears mid-session

- **UX0961** Title the sink-loss recovery with the concrete failed operation, not 'Something went wrong'.
- **UX0962** Show new sink chosen or paused only after a retry check confirms it.
- **UX0963** Explain the failure mode “hotplug leaves capture stale” using a likely cause and one verifiable next step.
- **UX0964** Put refresh and reselect sink beside the error with an explicit retry/cancel affordance.
- **UX0965** For endpoint disappears mid-session, record a short timestamped local timeline without raw audio samples. Verify “new sink chosen or paused” despite “hotplug leaves capture stale”.
- **UX0966** For endpoint disappears mid-session, separate a fixable local setting from a remote device or network issue. Verify “new sink chosen or paused” despite “hotplug leaves capture stale”.
- **UX0967** For endpoint disappears mid-session, keep error details selectable and copyable without dumping an unbounded log. Verify “new sink chosen or paused” despite “hotplug leaves capture stale”.
- **UX0968** For endpoint disappears mid-session, offer one safe reset scope instead of resetting every saved profile. Verify “new sink chosen or paused” despite “hotplug leaves capture stale”.
- **UX0969** For endpoint disappears mid-session, use a passive banner for transient failure and a modal only for user-initiated destructive action. Verify “new sink chosen or paused” despite “hotplug leaves capture stale”.
- **UX0970** For endpoint disappears mid-session, never ask users to disable the whole firewall to resolve this case. Verify “new sink chosen or paused” despite “hotplug leaves capture stale”.
- **UX0971** For endpoint disappears mid-session, show support commands as copyable text, not automatic root execution. Verify “new sink chosen or paused” despite “hotplug leaves capture stale”.
- **UX0972** For endpoint disappears mid-session, include expected result and fallback for the proposed recovery step. Verify “new sink chosen or paused” despite “hotplug leaves capture stale”.
- **UX0973** For endpoint disappears mid-session, avoid blaming the phone when PipeWire or the PC sink is the failing component. Verify “new sink chosen or paused” despite “hotplug leaves capture stale”.
- **UX0974** For endpoint disappears mid-session, provide a screen-reader announcement once the retry outcome is known. Verify “new sink chosen or paused” despite “hotplug leaves capture stale”.
- **UX0975** For endpoint disappears mid-session, allow privacy preview before any diagnostic file leaves the device. Verify “new sink chosen or paused” despite “hotplug leaves capture stale”.
- **UX0976** Measure no misleading Connected state to prioritize real failures over hypothetical ones.

### Moment: capture format unsupported

- **UX0977** Title the format mismatch explanation with the concrete failed operation, not 'Something went wrong'.
- **UX0978** Show compatible format selected only after a retry check confirms it.
- **UX0979** Explain the failure mode “device rejects current format” using a likely cause and one verifiable next step.
- **UX0980** Put restore automatic format beside the error with an explicit retry/cancel affordance.
- **UX0981** For capture format unsupported, record a short timestamped local timeline without raw audio samples. Verify “compatible format selected” despite “device rejects current format”.
- **UX0982** For capture format unsupported, separate a fixable local setting from a remote device or network issue. Verify “compatible format selected” despite “device rejects current format”.
- **UX0983** For capture format unsupported, keep error details selectable and copyable without dumping an unbounded log. Verify “compatible format selected” despite “device rejects current format”.
- **UX0984** For capture format unsupported, offer one safe reset scope instead of resetting every saved profile. Verify “compatible format selected” despite “device rejects current format”.
- **UX0985** For capture format unsupported, use a passive banner for transient failure and a modal only for user-initiated destructive action. Verify “compatible format selected” despite “device rejects current format”.
- **UX0986** For capture format unsupported, never ask users to disable the whole firewall to resolve this case. Verify “compatible format selected” despite “device rejects current format”.
- **UX0987** For capture format unsupported, show support commands as copyable text, not automatic root execution. Verify “compatible format selected” despite “device rejects current format”.
- **UX0988** For capture format unsupported, include expected result and fallback for the proposed recovery step. Verify “compatible format selected” despite “device rejects current format”.
- **UX0989** For capture format unsupported, avoid blaming the phone when PipeWire or the PC sink is the failing component. Verify “compatible format selected” despite “device rejects current format”.
- **UX0990** For capture format unsupported, provide a screen-reader announcement once the retry outcome is known. Verify “compatible format selected” despite “device rejects current format”.
- **UX0991** For capture format unsupported, allow privacy preview before any diagnostic file leaves the device. Verify “compatible format selected” despite “device rejects current format”.
- **UX0992** Measure format recovery time to prioritize real failures over hypothetical ones.

### Moment: heartbeat times out

- **UX0993** Title the timeout event timeline with the concrete failed operation, not 'Something went wrong'.
- **UX0994** Show network and service causes separated only after a retry check confirms it.
- **UX0995** Explain the failure mode “timeout message reveals no cause” using a likely cause and one verifiable next step.
- **UX0996** Put review route history beside the error with an explicit retry/cancel affordance.
- **UX0997** For heartbeat times out, record a short timestamped local timeline without raw audio samples. Verify “network and service causes separated” despite “timeout message reveals no cause”.
- **UX0998** For heartbeat times out, separate a fixable local setting from a remote device or network issue. Verify “network and service causes separated” despite “timeout message reveals no cause”.
- **UX0999** For heartbeat times out, keep error details selectable and copyable without dumping an unbounded log. Verify “network and service causes separated” despite “timeout message reveals no cause”.
- **UX1000** For heartbeat times out, offer one safe reset scope instead of resetting every saved profile. Verify “network and service causes separated” despite “timeout message reveals no cause”.
- **UX1001** For heartbeat times out, use a passive banner for transient failure and a modal only for user-initiated destructive action. Verify “network and service causes separated” despite “timeout message reveals no cause”.
- **UX1002** For heartbeat times out, never ask users to disable the whole firewall to resolve this case. Verify “network and service causes separated” despite “timeout message reveals no cause”.
- **UX1003** For heartbeat times out, show support commands as copyable text, not automatic root execution. Verify “network and service causes separated” despite “timeout message reveals no cause”.
- **UX1004** For heartbeat times out, include expected result and fallback for the proposed recovery step. Verify “network and service causes separated” despite “timeout message reveals no cause”.
- **UX1005** For heartbeat times out, avoid blaming the phone when PipeWire or the PC sink is the failing component. Verify “network and service causes separated” despite “timeout message reveals no cause”.
- **UX1006** For heartbeat times out, provide a screen-reader announcement once the retry outcome is known. Verify “network and service causes separated” despite “timeout message reveals no cause”.
- **UX1007** For heartbeat times out, allow privacy preview before any diagnostic file leaves the device. Verify “network and service causes separated” despite “timeout message reveals no cause”.
- **UX1008** Measure actionable timeout diagnosis to prioritize real failures over hypothetical ones.

### Moment: sending a support report

- **UX1009** Title the redacted diagnostics export with the concrete failed operation, not 'Something went wrong'.
- **UX1010** Show safe report saved locally only after a retry check confirms it.
- **UX1011** Explain the failure mode “IP/device keys leak in logs” using a likely cause and one verifiable next step.
- **UX1012** Put preview redacted report beside the error with an explicit retry/cancel affordance.
- **UX1013** For sending a support report, record a short timestamped local timeline without raw audio samples. Verify “safe report saved locally” despite “IP/device keys leak in logs”.
- **UX1014** For sending a support report, separate a fixable local setting from a remote device or network issue. Verify “safe report saved locally” despite “IP/device keys leak in logs”.
- **UX1015** For sending a support report, keep error details selectable and copyable without dumping an unbounded log. Verify “safe report saved locally” despite “IP/device keys leak in logs”.
- **UX1016** For sending a support report, offer one safe reset scope instead of resetting every saved profile. Verify “safe report saved locally” despite “IP/device keys leak in logs”.
- **UX1017** For sending a support report, use a passive banner for transient failure and a modal only for user-initiated destructive action. Verify “safe report saved locally” despite “IP/device keys leak in logs”.
- **UX1018** For sending a support report, never ask users to disable the whole firewall to resolve this case. Verify “safe report saved locally” despite “IP/device keys leak in logs”.
- **UX1019** For sending a support report, show support commands as copyable text, not automatic root execution. Verify “safe report saved locally” despite “IP/device keys leak in logs”.
- **UX1020** For sending a support report, include expected result and fallback for the proposed recovery step. Verify “safe report saved locally” despite “IP/device keys leak in logs”.
- **UX1021** For sending a support report, avoid blaming the phone when PipeWire or the PC sink is the failing component. Verify “safe report saved locally” despite “IP/device keys leak in logs”.
- **UX1022** For sending a support report, provide a screen-reader announcement once the retry outcome is known. Verify “safe report saved locally” despite “IP/device keys leak in logs”.
- **UX1023** For sending a support report, allow privacy preview before any diagnostic file leaves the device. Verify “safe report saved locally” despite “IP/device keys leak in logs”.
- **UX1024** Measure useful reports without secrets to prioritize real failures over hypothetical ones.

## Responsible use and next step

Start by user-testing the 48 editorial picks; pick no more than 8–12 for a sprint. For each selected entry record owner, prerequisite, baseline, observable acceptance criterion, accessibility check, and regression test. Consolidate overlapping ideas before turning this atlas into issues. **Do not** auto-generate 1,024 GitHub tickets, claim all are independently researched, or ship unauthenticated WAN sharing, speculative battery metrics, fake audio meters, unsafe hearing boosts, or unconsented AI/cloud diagnostics.
