#!/usr/bin/env python3
"""Generate a reproducible scenario x lens UX ideation atlas. No network calls."""

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "docs/ux-comfort-atlas-1024.md"

INTRO = """# Audio Share: 1,024 UX and comfort opportunities

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

"""

# Each tuple is (moment, control/object, intended state, likely confusion/failure,
# immediate user action, success measure). Eight moments per chapter.
CHAPTERS = [
    ("01 · First-run installation and setup", [
        ("finding the correct Linux download", "distro-matched archive", "compatible package selected", "the user picks an Arch binary on Debian", "choose their distro", "correct archive selected without help"),
        ("unpacking the desktop bundle", "archive contents", "GUI and server found", "the extracted folder is mistaken for an installer", "open README.txt", "first launch without a terminal search"),
        ("installing GTK prerequisites", "PyGObject/GTK dependency check", "graphical runtime available", "the distro's GTK bindings are missing", "install matching runtime packages", "dependency recovery under three minutes"),
        ("starting a PipeWire user session", "PipeWire/WirePlumber readiness", "user audio service active", "a root service is confused with the user's service", "inspect user-service status", "working user session without sudo launches"),
        ("finding an audio sink", "sink availability", "usable sink selected", "no sink appears on a headless machine", "review null-sink guidance", "preflight detects missing sink before Start"),
        ("installing the launcher", "desktop-entry install", "menu entry usable", "server binary is installed in an unexpected path", "install bundled bin/as-cmd", "launcher starts without environment hacks"),
        ("first Android launch", "phone first-run path", "PC-to-phone role understood", "user expects Android to transmit instead", "view three-step explanation", "novice can describe the audio direction"),
        ("first successful sound", "first-stream checklist", "sound confirmed on phone", "connection status is mistaken for audible output", "confirm sound or open checks", "audible-first-stream rate"),
    ], [
        "Name the {target} in a one-sentence header; avoid assuming the user knows its package or service name.",
        "Show {state} as a distinct milestone; do not treat a previous setup step as proof of completion.",
        "Preflight the failure mode “{failure}” before presenting the primary Start action.",
        "Offer a one-click path to {action}, retaining a manual route for offline users.",
        "Preview exactly what files or settings this setup step changes before applying it.",
        "Keep a local checklist with the current step highlighted; never silently skip unmet prerequisites.",
        "Provide a copyable distro-specific setup instruction for {target}; never run sudo inside the GUI.",
        "Explain the situation “{failure}” in plain language and include the smallest safe recovery step.",
        "Save completed setup progress locally and make it easy to revisit later.",
        "Show a concise success confirmation for {state}, followed by the next action.",
        "Make the action reachable with keyboard, pointer and screen reader at the same point in the flow.",
        "Render setup guidance on a narrow phone and a 540px GTK window without clipped content.",
        "Keep technical versions/path details in an expandable panel rather than the first-run hero.",
        "Never imply {state} without testing its corresponding signal or receiving explicit confirmation.",
        "Give a reversible reset for this step without erasing unrelated user preferences.",
        "Track {metric} with consent; use it to remove friction, not to auto-upload diagnostics.",
    ]),
    ("02 · LAN addressing and connection", [
        ("choosing the PC's LAN address", "interface-labeled IPv4 list", "reachable PC IP chosen", "the first private IP belongs to a VPN", "select a reachable interface", "successful first connect"),
        ("entering host on Android", "host entry", "valid address saved", "an address typo passes superficial validation", "correct the highlighted octet", "host entry without retries"),
        ("choosing a TCP/UDP port", "port selector", "both protocols use same port", "a firewall allows TCP but drops UDP", "test both protocol paths", "working media after handshake"),
        ("connecting over guest Wi-Fi", "network-isolation check", "peers share reachable LAN", "client isolation blocks direct contact", "switch to a trusted LAN", "isolation diagnosis time"),
        ("connecting via USB tethering", "USB network interface", "phone reachable over tether adapter", "host is bound to Wi-Fi instead of tether", "pick tether IP", "tether setup without guesswork"),
        ("using a LAN hostname", "resolved host preview", "DNS result reachable", "hostname resolves to an unsupported address family", "choose valid resolved IP", "hostname resolution success"),
        ("changing networks mid-session", "network handoff state", "connection resumes or stops honestly", "old IP is cached after handoff", "retry with new route", "clean recovery time"),
        ("connecting through a VPN", "VPN-route warning", "peer reachability verified", "split tunnel sends phone traffic elsewhere", "choose local route", "VPN-related false errors avoided"),
    ], [
        "Label {target} with its real interface/route, not only a numeric address.",
        "Show {state} separately from socket-open and audio-received states.",
        "Test the failure mode “{failure}” with a targeted check instead of a generic connection toast.",
        "Surface {action} next to the failed field, not hidden in global settings.",
        "Preview PC and phone endpoints before committing a new network profile.",
        "Keep a safe manual-address fallback when discovery cannot find {target}.",
        "Show a transient connecting timer and allow Cancel before a retry loop starts.",
        "Make the host/port error selectable and copyable for technical support.",
        "Do not recommend opening the entire firewall when {failure} is suspected.",
        "Retain the last working route and offer a clearly labeled one-tap rollback.",
        "Use examples matching this route type instead of a hardcoded 192.168.x.x hint.",
        "Announce route changes accessibly without repeating every packet status.",
        "Keep network details visible on desktop and condensed on phone.",
        "Warn before suggesting public hotspot or WAN use of unauthenticated transport.",
        "Show what changed between a failed route and the last successful route.",
        "Measure {metric} and categorize the failure before adding auto-reconnect logic.",
    ]),
    ("03 · Pairing, identity and device trust", [
        ("approving a new phone", "new-device approval", "known device admitted", "unknown LAN peer requests audio", "approve or reject the phone", "unapproved peers rejected"),
        ("scanning a pairing QR", "time-limited pairing code", "one phone paired", "stale or copied code is reused", "regenerate code", "pairing without secret leakage"),
        ("confirming PC identity", "server fingerprint", "correct PC trusted", "lookalike hostname could be an impostor", "compare short fingerprint", "identity confirmation success"),
        ("naming a connected phone", "local device nickname", "recognized phone displayed", "two clients have identical default names", "rename locally", "correct device identified"),
        ("revoking an old phone", "paired-device roster", "key revoked", "lost device still has access", "revoke device", "access denied after revoke"),
        ("moving from legacy plaintext mode", "secure-mode migration", "new encrypted session active", "old client cannot negotiate new protocol", "update both endpoints", "migration without silent downgrade"),
        ("pairing on shared Wi-Fi", "network trust warning", "user makes informed decision", "a public LAN peer could listen", "use secure pairing or trusted LAN", "unsafe connection attempts averted"),
        ("recovering after reinstall", "trusted-device recovery", "old trust removed intentionally", "reinstalled phone appears as a different peer", "verify and pair again", "recovery without anonymous bypass"),
    ], [
        "State who can hear the PC audio in the {target} view.",
        "Only show {state} after cryptographic verification, never from a username alone.",
        "Give the situation “{failure}” a precise, non-alarming explanation and a safe route forward.",
        "Require explicit confirmation for {action}; never approve a peer from a notification tap alone.",
        "Expire temporary pairing offers visibly with a countdown that stops at zero.",
        "Keep the identity fingerprint selectable and spoken clearly by assistive tech.",
        "Differentiate paired, connected and currently listening devices visually and in text.",
        "Show the timestamp and origin of each trust change in a local audit view.",
        "Offer revoke/undo only where rollback does not re-enable a compromised key.",
        "Avoid showing reusable tokens or secret keys in QR preview/screenshots.",
        "Explain why {target} cannot be controlled from a second unknown PC.",
        "Show a compatibility warning rather than silently falling back to plaintext.",
        "Make the safe path the primary CTA and the legacy path an explicit advanced choice.",
        "Keep account creation unnecessary for local-only paired devices.",
        "Give key reset a clear impact summary covering all already paired phones.",
        "Measure {metric} without collecting fingerprints or device names remotely.",
    ]),
    ("04 · Source and sink selection", [
        ("selecting the default sink", "default-sink option", "active system sink captured", "the default changes after launch", "follow or pin selection", "capture matches expected PC output"),
        ("pinning a USB DAC", "fixed sink selection", "desired DAC captured", "USB device disappears and reappears", "reselect the DAC", "recovery after hotplug"),
        ("switching HDMI monitors", "HDMI sink change", "new display audio route recognized", "old endpoint vanishes on monitor switch", "choose new monitor sink", "no crash on profile switch"),
        ("using a null sink", "virtual sink setup", "PC audio routed privately", "no physical speaker exists", "review reversible null-sink guide", "first sound without physical jack"),
        ("capturing a Bluetooth sink", "Bluetooth output sink", "correct wireless source captured", "Bluetooth profile switches mid-stream", "inspect sink profile", "no silent capture on route switch"),
        ("playing from one PC application", "per-app audio routing", "chosen app audible on phone", "unwanted app audio leaks to phone", "isolate the app route", "only intended audio captured"),
        ("hearing both local and remote output", "dual-output explanation", "both routes understood", "echo from unsynchronized PC and phone", "choose one output or accept echo", "fewer echo-related support reports"),
        ("refreshing a changing sink list", "PipeWire discovery", "fresh sinks displayed", "refresh blocks GTK or loses selection", "retry without losing current choice", "responsive refresh under timeout"),
    ], [
        "Show {target} with human-readable sink name plus stable technical ID on demand.",
        "Represent {state} separately from the system default selection.",
        "Warn about “{failure}” with an explanation of its likely audible symptom.",
        "Offer {action} in place while keeping Stop available.",
        "Preview consequences for existing listeners before changing source.",
        "Record the last working sink per PC profile, not as an opaque global string.",
        "Avoid selecting a monitor/source node when the user asked for an output sink.",
        "Show a signal meter only if the capture path reports real audio levels.",
        "Make a missing device a recoverable state, not a blank dropdown.",
        "Surface a safe test-tone option at a modest volume when technically available.",
        "Keep source controls disabled with a reason while switching could break playback.",
        "Allow mouse, keyboard and screen reader users to identify the same sink.",
        "Provide an explicit default-versus-pinned choice in the advanced view.",
        "Distinguish 'silent because app paused' from 'sink missing' before prompting a fix.",
        "Log source changes locally with time and old/new sink IDs for support.",
        "Measure {metric} across hotplug and monitor change before claiming auto-follow reliability.",
    ]),
    ("05 · Audio level and hearing comfort", [
        ("changing phone media volume", "Android media volume", "comfortable output level", "system volume is confused with app gain", "adjust media volume", "safe comfortable loudness"),
        ("adjusting in-app gain", "Audio Share gain slider", "audible gain updated", "slider appears to move but sound is unchanged", "verify the applied value", "slider changes actual sound"),
        ("using loudness enhancement", "loudness enhancer", "safe boost selected", "large gain clips or hurts ears", "lower enhancement", "no clipped output at default"),
        ("switching between phone speaker and earbuds", "output route levels", "route-specific comfort preserved", "new route is much louder", "confirm adjusted level", "no sudden loud transition"),
        ("playing late at night", "quiet-listening preset", "low distraction level", "notification or test tone wakes others", "enable quiet mode", "night-session comfort score"),
        ("using hearing aids", "assisted-listening route", "speech intelligible", "Bluetooth aid route has unexpected delay", "choose stable preset", "task completion with assistive output"),
        ("preventing sudden peaks", "peak limiter option", "clipping risk signaled", "a loud game event jumps above normal level", "enable limiter cautiously", "peak-related complaints reduced"),
        ("returning from mute", "unmute transition", "sound ramps gently", "unmute jumps to a stale high level", "preview level before unmute", "no startle after unmute"),
    ], [
        "Use {target} wording that separates source level, transport gain and Android hardware volume.",
        "Show {state} as a numeric value and audible effect, not a decorative slider position.",
        "Explain why “{failure}” happens before the user raises amplification as a workaround.",
        "Offer {action} with a safe one-tap default restore beside the control.",
        "Preview the target level when audio route changes before unmuting.",
        "Constrain high-risk gain with clear warnings and a fast escape hatch.",
        "Show output device names rather than a generic speaker icon when a route is active.",
        "Avoid playing a diagnostic beep automatically on a new output route.",
        "Prefer smooth, short level transitions over sudden discontinuities.",
        "Keep slider adjustments responsive while a stream is active; show apply errors.",
        "Announce value changes via screen reader in manageable increments.",
        "Provide keyboard/Home/End adjustments with bounded steps on desktop.",
        "Offer a per-route preference only after users can see and override it.",
        "Never call a signal 'safe' based solely on a visual meter; preserve hearing caveats.",
        "Test actual PCM amplitude before labeling a boost or limiter effective.",
        "Measure {metric} through user trials without recording their audio.",
    ]),
    ("06 · Latency, quality and stability", [
        ("watching video with phone sound", "video-sync preset", "dialogue tracks picture", "audio trails lip movements", "run sync calibration", "measured audiovisual offset"),
        ("playing an action game", "gaming preset", "low-latency mode stable", "buffer is too deep for reactions", "try tested gaming buffer", "p95 latency and underruns"),
        ("listening to music over Wi-Fi", "music stability profile", "music plays without gaps", "weak Wi-Fi causes short dropouts", "select stable buffer", "uninterrupted session time"),
        ("changing AudioTrack buffer", "buffer-delay control", "chosen latency/stability tradeoff applied", "buffer value has no visible effect", "compare before and after", "underruns at chosen buffer"),
        ("using a slow phone", "device capability hint", "playback stays smooth", "older device cannot process format quickly", "choose compatible format", "low-end phone first-play success"),
        ("using a congested network", "network-quality indicator", "congestion recognized", "packet loss appears as a PC volume issue", "switch network or buffer", "reduced gaps under load"),
        ("switching sample rate", "capture format negotiation", "Android supports format", "unsupported rate or encoding is selected", "return to default format", "format mismatch errors reduced"),
        ("long uninterrupted session", "drift check", "audio/video alignment maintained", "delay gradually accumulates", "resync without full reset", "drift after one hour"),
    ], [
        "Label {target} by its tradeoff rather than a bare buffer count.",
        "Show {state} only when confirmed by measured playback data.",
        "Tie the symptom “{failure}” to loss, underruns and route metrics instead of a generic 'lag' badge.",
        "Offer {action} with a reversible comparison to last working values.",
        "Explain that network ping is not end-to-end audible latency.",
        "Show measured, estimated and unavailable values with distinct labels.",
        "Avoid promising zero latency on USB or any other transport.",
        "Provide a brief A/B sample test before applying an advanced audio preset.",
        "Use a bounded graph window so momentary spikes do not look like permanent failure.",
        "Offer a simple Stable/Video/Gaming mode and hide expert knobs by default.",
        "Warn when a smaller buffer could increase clicks or cutouts.",
        "Give underflow counts a human explanation and a safe starting fix.",
        "Preserve playback continuity while updating only controls safe to change live.",
        "Screen-reader summaries should speak trend and value without announcing every packet.",
        "Only show codec/bit depth claims when the negotiated format is known.",
        "Measure {metric} on real devices before promoting the preset.",
    ]),
    ("07 · Playback lifecycle and background comfort", [
        ("starting playback on Android", "Play control", "audio session preparing", "a Play tap appears ignored", "view startup progress", "time to first audible sample"),
        ("pausing an active stream", "Pause control", "phone playback paused", "server continues wasting bandwidth", "pause stream deliberately", "pause response and battery cost"),
        ("resuming after a notification", "notification control", "playback restored correctly", "notification button has stale state", "resume from notification", "notification action success"),
        ("locking the phone screen", "background playback service", "stream remains audible", "battery optimizer stops service", "review OS restriction help", "screen-off session reliability"),
        ("opening a voice call", "audio focus transition", "call takes appropriate priority", "PC audio competes with call audio", "pause or duck stream", "correct focus behavior"),
        ("sleeping and waking the PC", "resume state", "user sees reconnection status", "sleep leaves a phantom active server", "retry after wake", "time to recovered playback"),
        ("leaving the Wi-Fi network", "disconnect state", "stream stops cleanly", "infinite reconnect drains battery", "cancel retry", "idle battery after disconnect"),
        ("closing the desktop window", "server lifetime choice", "expected session lifetime", "close accidentally kills active stream", "choose keep-running or stop", "unexpected-stop complaints"),
    ], [
        "State {state} in words and keep it synchronized with the real service state.",
        "Make {target} available without opening advanced settings.",
        "Explain the symptom “{failure}” when it occurs, not in a generic permanent warning banner.",
        "Let the user {action} with immediate tactile/visual feedback.",
        "Keep Play, Pause and Stop semantics different; do not reuse an ambiguous single icon.",
        "Show reconnect attempts and remaining delay; allow cancel at every stage.",
        "Respect OS audio focus and media-session rules instead of bypassing them.",
        "Protect phone battery with bounded retries and user-visible idle status.",
        "Show an accurate persistent notification only while required for playback.",
        "Recover from rotation and process recreation without a false Playing state.",
        "Preserve the selected PC profile when a session ends unexpectedly.",
        "Announce one meaningful lifecycle change to TalkBack, not a stream of duplicates.",
        "Use a discreet desktop notification for unexpected loss, not normal pause events.",
        "Keep service state readable in the phone's quick settings and full app.",
        "Offer a manual reconnect even after automatic retries stop.",
        "Measure {metric} on Android screen-off and wake cycles.",
    ]),
    ("08 · Recovery, diagnostics and help", [
        ("a bind-address error", "bind failure card", "correct local bind chosen", "address is not assigned to this PC", "select listed interface", "recover without terminal"),
        ("no route to host", "route failure card", "network path diagnosed", "phone and PC are on isolated subnets", "inspect both networks", "route recovery time"),
        ("TCP connects but media is silent", "UDP path check", "media path verified", "UDP blocked while TCP succeeds", "test selected UDP port", "silent-connection resolution"),
        ("PipeWire daemon unavailable", "audio-service error card", "user service restored", "server launched as root or no user session", "open service instructions", "service error recovery"),
        ("endpoint disappears mid-session", "sink-loss recovery", "new sink chosen or paused", "hotplug leaves capture stale", "refresh and reselect sink", "no misleading Connected state"),
        ("capture format unsupported", "format mismatch explanation", "compatible format selected", "device rejects current format", "restore automatic format", "format recovery time"),
        ("heartbeat times out", "timeout event timeline", "network and service causes separated", "timeout message reveals no cause", "review route history", "actionable timeout diagnosis"),
        ("sending a support report", "redacted diagnostics export", "safe report saved locally", "IP/device keys leak in logs", "preview redacted report", "useful reports without secrets"),
    ], [
        "Title the {target} with the concrete failed operation, not 'Something went wrong'.",
        "Show {state} only after a retry check confirms it.",
        "Explain the failure mode “{failure}” using a likely cause and one verifiable next step.",
        "Put {action} beside the error with an explicit retry/cancel affordance.",
        "Record a short timestamped local timeline without raw audio samples.",
        "Separate a fixable local setting from a remote device or network issue.",
        "Keep error details selectable and copyable without dumping an unbounded log.",
        "Offer one safe reset scope instead of resetting every saved profile.",
        "Use a passive banner for transient failure and a modal only for user-initiated destructive action.",
        "Never ask users to disable the whole firewall to resolve this case.",
        "Show support commands as copyable text, not automatic root execution.",
        "Include expected result and fallback for the proposed recovery step.",
        "Avoid blaming the phone when PipeWire or the PC sink is the failing component.",
        "Provide a screen-reader announcement once the retry outcome is known.",
        "Allow privacy preview before any diagnostic file leaves the device.",
        "Measure {metric} to prioritize real failures over hypothetical ones.",
    ]),
]

assert len(CHAPTERS) == 8
lines = [INTRO]
count = 0
for chapter_title, moments, lenses in CHAPTERS:
    assert len(moments) == 8, chapter_title
    assert len(lenses) == 16, chapter_title
    lines.append(f"## {chapter_title}\n\n")
    for moment, target, state, failure, action, metric in moments:
        lines.append(f"### Moment: {moment}\n\n")
        fields = dict(target=target, state=state, failure=failure, action=action, metric=metric)
        for lens in lenses:
            count += 1
            proposal = lens.format(**fields)
            if "{" not in lens:
                # A cross-cutting heuristic is a separate task only when it has
                # a scenario-specific trigger and observable acceptance check.
                proposal = (f"For {moment}, {proposal[0].lower() + proposal[1:]} "
                            f"Verify “{state}” despite “{failure}”.")
            lines.append(f"- **UX{count:04d}** {proposal}\n")
        lines.append("\n")
assert count == 1024
lines.append("""## Responsible use and next step

Start by user-testing the 48 editorial picks; pick no more than 8–12 for a sprint. For each selected entry record owner, prerequisite, baseline, observable acceptance criterion, accessibility check, and regression test. Consolidate overlapping ideas before turning this atlas into issues. **Do not** auto-generate 1,024 GitHub tickets, claim all are independently researched, or ship unauthenticated WAN sharing, speculative battery metrics, fake audio meters, unsafe hearing boosts, or unconsented AI/cloud diagnostics.
""")
OUT.write_text("".join(lines), encoding="utf-8")
print(f"Wrote {OUT} with {count} numbered scenario-lens proposals")
