# Audio Share opportunity audit — 250 proposals

**Date:** 2026-11-15 · **Scope:** this repository's v0.3.4-era server/Android code and the Linux GTK frontend present in this workspace. **Status:** research/backlog only; none of these 250 proposals is claimed as implemented. The Arch GUI prerelease is a starting point, not evidence that hardware streaming or all upstream issues are fixed. “Premium” means a polished, reliable outcome—not a proposed paywall.

## Method and evidence

I reviewed `server-core/src/{network_manager.cpp,main.cpp,linux/audio_manager_impl.cpp}`, `docs/protocol.md`, `protos/client.proto`, `android-app/.../{service,ui/screen}`, `linux-gui/{backend.py,audio-share-gui}`, the project's README, public upstream issues, and external platform/UX guidance. I sampled issue bodies, not just titles. **Open upstream issues are signals, not verified regressions in this checkout; closed reports are historical signals.** External community threads are directional, not measured demand. Pinterest is visual mood-board material only; do not copy its layouts/assets. No user interviews, security penetration test, or real phone audio benchmark was conducted.

Key signals: upstream requests for [encryption/cleartext warning](https://github.com/mkckr0/audio-share/issues/165), [authentication](https://github.com/mkckr0/audio-share/issues/41), [ultra-low latency](https://github.com/mkckr0/audio-share/issues/78), [compression](https://github.com/mkckr0/audio-share/issues/33), [connected-device visibility](https://github.com/mkckr0/audio-share/issues/159), [saved server profiles](https://github.com/mkckr0/audio-share/issues/148), [Linux GUI](https://github.com/mkckr0/audio-share/issues/137), [Android accessibility](https://github.com/mkckr0/audio-share/issues/174), [ineffective sliders](https://github.com/mkckr0/audio-share/issues/171), [Linux connection crash](https://github.com/mkckr0/audio-share/issues/156), [dark splash](https://github.com/mkckr0/audio-share/issues/180), and [compression/silence/battery ideas](https://github.com/mkckr0/audio-share/issues/192). Older [Arch no-audio](https://github.com/mkckr0/audio-share/issues/43), [rattling](https://github.com/mkckr0/audio-share/issues/31), and [USB latency](https://github.com/mkckr0/audio-share/issues/16) reports motivate instrumentation, not an assertion that every setup still fails. A [6](https://www.reddit.com/r/pipewire/comments/maiuru/streaming_audio_from_pc_to_android/) (Reddit PipeWire discussion) mentions stutter/disconnections; a [2](https://www.reddit.com/r/androidapps/comments/42epaw/request_app_that_treats_the_phone_like_usb/) (phone-as-speaker request) emphasizes wired connections and video sync. These are anecdotes. [1](https://www.pinterest.com/ideas/music-production-software-interface/952577877594/) (Pinterest audio-interface ideas) suggest restrained dashboards, not validated usability. Android's [1](https://developer.android.com/reference/android/media/AudioTrack) (AudioTrack documentation) explains the buffer/underrun tradeoff; [1](https://developer.android.com/develop/ui/compose/accessibility/api-defaults) (Compose accessibility guidance) recommends 48dp interactive targets; [2](https://developer.gnome.org/hig/patterns/feedback.html) (GNOME feedback guidance) informs state/error clarity; [2](https://github.com/OWASP/IoT-Security-Verification-Standard-ISVS/blob/master/en/V4-Communication_Requirements.md) (OWASP device-communication guidance) informs security proposals.

**Priority legend:** P0 = safety/data-security or severe reliability first; P1 = next release candidate; P2 = exploration/validation. Each line describes a proposed deliverable or testable behavior, not a finding of fact. IDs remain stable for issue planning. **Suggested first slice:** C01–C06, C11–C14, C21–C24, U001–U008, U016–U023, U091–U095, X01–X06. Gate any cloud/AI features on C01–C06 and explicit consent.

## 50 core engineering improvements

### Security and protocol (C01–C10)

| ID | Priority | Proposal / success criterion |
|---|---|---|
| C01 | P0 | Explicitly mark current LAN traffic as unauthenticated/unencrypted until a verified secure transport replaces it. |
| C02 | P0 | Add versioned handshake with minimum/maximum supported protocol versions and clean mismatch errors. |
| C03 | P0 | Add opt-in pairing using a short-lived challenge and per-device key; refuse unknown clients when enabled. |
| C04 | P0 | Protect both TCP control and UDP audio with authenticated encryption; reject modified packets before playback. |
| C05 | P0 | Bind UDP session identity to a paired peer, not merely a guessable integer from the control channel. |
| C06 | P0 | Reject replayed or stale audio packets with per-session nonce/sequence windows. |
| C07 | P0 | Bound protobuf frame sizes, command values, client counts and outbound queues before allocation. |
| C08 | P0 | Rate-limit failed handshakes and idle clients; release sockets and buffers predictably. |
| C09 | P1 | Rotate/forget device keys, display trust fingerprints and provide a one-tap revoke path. |
| C10 | P1 | Fuzz TCP framing, format decoding and UDP packets with sanitizers in CI. |

### Timing, audio quality and bandwidth (C11–C20)

| ID | Priority | Proposal / success criterion |
|---|---|---|
| C11 | P0 | Stamp packets with sequence and capture time; distinguish loss, reorder, jitter and render lag. |
| C12 | P0 | Count Android AudioTrack underruns and show actual buffer occupancy rather than relying on subjective latency. |
| C13 | P1 | Implement bounded adaptive jitter buffering with transparent minimum/target/maximum latency. |
| C14 | P1 | Handle a partial/non-blocking AudioTrack write by retrying the unwritten frames without duplicating samples. |
| C15 | P1 | Align captured packet sizes to whole frames and validate block alignment before segmentation. |
| C16 | P1 | Benchmark PCM versus optional low-delay Opus on Wi-Fi and tethering; default only after measured gains. |
| C17 | P1 | Negotiate sample rate/channel layout explicitly; reject unsupported formats with a fallback suggestion. |
| C18 | P1 | Stop or compress silent audio after a threshold while retaining a lightweight keepalive and fast wake-up. |
| C19 | P1 | Expose latency-versus-stability presets backed by measured buffer sizes, not fixed claims. |
| C20 | P2 | Evaluate packet-loss concealment and very short fades for gaps; compare against unprocessed audio. |

### Lifecycle and concurrency (C21–C30)

| ID | Priority | Proposal / success criterion |
|---|---|---|
| C21 | P0 | Make start, stop and restart idempotent; exercise 100 consecutive cycles without orphan sockets/threads. |
| C22 | P0 | Propagate PipeWire capture failure to the CLI/GUI instead of reporting “server started” without audio. |
| C23 | P0 | Stop cleanly when a selected sink disappears; optionally follow the new default sink after confirmation. |
| C24 | P0 | Catch malformed priority metadata and missing PipeWire properties without exceptions inside callbacks. |
| C25 | P1 | Make client/session state transitions explicit; disallow duplicate play requests and double close. |
| C26 | P1 | Cancel outstanding async sends before destroying UDP sockets; verify no use-after-free under stop. |
| C27 | P1 | Bound work posted from capture callback to network thread so slow clients cannot exhaust memory. |
| C28 | P1 | Distinguish intentional stop, network loss and audio-device failure in lifecycle result codes. |
| C29 | P1 | Add exponential reconnect with jitter and a user-visible cancel path on Android. |
| C30 | P1 | Resume after sleep, network change and Wi-Fi-to-USB handoff without duplicate server instances. |

### Platform and networking (C31–C40)

| ID | Priority | Proposal / success criterion |
|---|---|---|
| C31 | P1 | Add scoped IPv6 listen/connect support, including bracketed IPv6 host:port parsing. |
| C32 | P1 | Enumerate all usable interfaces with subnet, route and tethering labels instead of taking the first private IP. |
| C33 | P1 | Allow hostname/mDNS resolution with address-family fallback and short timeouts. |
| C34 | P1 | Probe both TCP control and UDP audio reachability; distinguish firewall, wrong address and no sink. |
| C35 | P1 | Build and smoke-test x86_64 and ARM64 Linux packages without assuming one architecture. |
| C36 | P1 | Test PipeWire/WirePlumber version matrix and default-sink changes on Arch/CachyOS. |
| C37 | P1 | Make Linux GUI endpoint refresh asynchronous, cancellable and resilient to PipeWire restart. |
| C38 | P1 | Add systemd user service integration that never launches a graphical GUI as root. |
| C39 | P2 | Evaluate a native USB transport after profiling tethering; retain network mode as fallback. |
| C40 | P2 | Prototype Windows/macOS receiver interoperability only after versioned secure protocol stabilizes. |

### Observability, quality and maintainability (C41–C50)

| ID | Priority | Proposal / success criterion |
|---|---|---|
| C41 | P1 | Emit structured, redacted diagnostics with correlation IDs across server and Android client. |
| C42 | P1 | Add an end-to-end loopback harness that injects known PCM and checks channel order, timing and clipping. |
| C43 | P1 | Test packet loss, reorder, duplicate, delay and abrupt disconnect with a deterministic network simulator. |
| C44 | P1 | Measure CPU, memory, battery and bandwidth for silence/music/video on low-end phones. |
| C45 | P1 | Add sanitizer/UBSan/ASan/TSan jobs where supported; triage failures before publishing. |
| C46 | P1 | Add Android instrumentation tests for connect, audio-route change and process recreation. |
| C47 | P1 | Add reproducible release provenance/SBOM and verify checksums and signatures before install. |
| C48 | P2 | Separate capture, transport and codec interfaces so backends can be tested independently. |
| C49 | P2 | Define compatibility tests for old clients and reject unsupported feature flags gracefully. |
| C50 | P2 | Publish performance budgets and regression gates for median/p95 latency and underrun rate. |

## 150 UI/UX recommendations

All UI entries are **design hypotheses**. Validate with an accessible prototype and actual Android+Arch users; do not mistake a screenshot or Pinterest concept for evidence. The current GTK view is a compact host/port/sink/start/log window; the Android HomeScreen has host/port, play/pause and a message card. [#174](https://github.com/mkckr0/audio-share/issues/174), [#159](https://github.com/mkckr0/audio-share/issues/159), and [#148](https://github.com/mkckr0/audio-share/issues/148) provide concrete feedback.

### First-run and pairing (U001–U015)

| ID | Priority | Proposal / success criterion |
|---|---|---|
| U001 | P0 | First-run card: “PC sends sound → phone plays it” with a three-step setup path. |
| U002 | P0 | Explain that phone and PC need a reachable network, not necessarily Internet access. |
| U003 | P1 | Show prerequisite checks for PipeWire, a usable sink and installed server binary. |
| U004 | P1 | Offer a read-only “Test setup” before enabling Start. |
| U005 | P1 | Show a pairing QR code only after C03/C04 are implemented; never encode a reusable cleartext secret. |
| U006 | P1 | Make manual IP entry the accessible fallback to QR/discovery. |
| U007 | P1 | Confirm PC identity/fingerprint on both screens before trusting a new device. |
| U008 | P1 | State exactly which address and port the phone should enter, with copy controls. |
| U009 | P1 | Show a sample Android screenshot at the corresponding setup step. |
| U010 | P1 | Add a “My devices cannot see each other” guided troubleshooter. |
| U011 | P2 | Offer a short animated path diagram, with reduced-motion alternative. |
| U012 | P2 | Remember completed onboarding but leave it reopenable from Help. |
| U013 | P2 | Provide distro-specific Arch/CachyOS prerequisite text without running sudo from the GUI. |
| U014 | P2 | Ask whether the user wants private listening or simultaneous local speakers. |
| U015 | P2 | Provide a reversible “Use phone as only speaker” guide, not an automatic global reroute. |

### Session dashboard (U016–U030)

| ID | Priority | Proposal / success criterion |
|---|---|---|
| U016 | P0 | Distinguish Idle, Starting, Listening, Phone connected, Playing, Reconnecting and Error. |
| U017 | P0 | Distinguish “server listening” from “audio actually captured and received.” |
| U018 | P1 | Put a single large Start/Stop control in a stable position across states. |
| U019 | P1 | List connected phones with approved display names and last-seen times. |
| U020 | P1 | Show current sink, LAN address and active port without opening settings. |
| U021 | P1 | Display measured end-to-end latency range with an “estimate” label until calibrated. |
| U022 | P1 | Show live packet loss and underrun badges only when measurements exist. |
| U023 | P1 | Provide a clear “Streaming locally / Not streaming” privacy indicator. |
| U024 | P1 | Separate “Stop sharing” from “Close window”; show what either action will do. |
| U025 | P1 | Use an activity indicator for capture silence that does not imply disconnection. |
| U026 | P1 | Add per-device mute/disconnect after authenticated per-device sessions exist. |
| U027 | P2 | Show an optional, lightweight level meter that works with reduced motion. |
| U028 | P2 | Offer compact status view and expanded diagnostics view. |
| U029 | P2 | Display elapsed session time only when it serves troubleshooting. |
| U030 | P2 | Remember whether the user last viewed simple or advanced mode. |

### Address, routes and connectivity (U031–U045)

| ID | Priority | Proposal / success criterion |
|---|---|---|
| U031 | P0 | Label selected IP with interface name and Wi-Fi/Ethernet/USB tethering context. |
| U032 | P1 | Explain why 127.0.0.1, a wildcard or unreachable interface cannot reach the phone. |
| U033 | P1 | Sort candidate addresses by route to the phone instead of raw interface order. |
| U034 | P1 | Let users edit the address while idle and preview binding before committing. |
| U035 | P1 | Validate port and host inline, with examples and no silent character filtering. |
| U036 | P1 | Show whether TCP and UDP on the selected port both pass a local preflight. |
| U037 | P1 | Offer a copyable firewalld/ufw command, clearly marked as needing user review. |
| U038 | P1 | Provide a “USB tethering selected” hint when the phone is on that interface. |
| U039 | P1 | Save named server profiles on Android; default to the last working profile. |
| U040 | P1 | Show recent hosts with last-success timestamps rather than a flat untrusted list. |
| U041 | P1 | Support hostnames once C33 lands; display resolved IP and family. |
| U042 | P1 | Explain “No route to host” with interface, subnet and firewall checks. |
| U043 | P2 | Warn when Wi-Fi client isolation or guest networks may block peers. |
| U044 | P2 | Detect address changes and prompt to update the phone's saved profile. |
| U045 | P2 | Show a privacy-safe QR containing address/port only for legacy mode, labeled insecure. |

### Audio controls and settings (U046–U060)

| ID | Priority | Proposal / success criterion |
|---|---|---|
| U046 | P0 | Fix sliders that do not apply while streaming before redesigning their appearance. |
| U047 | P0 | Show actual live volume gain and confirm it changes audible output. |
| U048 | P1 | Rename “buffer scale” to “Delay ↔ Stability” and show the real millisecond impact. |
| U049 | P1 | Separate phone media volume from app gain and loudness enhancement in labels. |
| U050 | P1 | Mark risky amplification with a hearing-safety warning, not a surprise modal every time. |
| U051 | P1 | Provide stable presets: Music, Video, Gaming and Custom, with honest tradeoffs. |
| U052 | P1 | Show negotiated sample rate, channels and encoding in an expandable details row. |
| U053 | P1 | Explain when a sink is silent, unavailable or only a monitor source. |
| U054 | P1 | Let users audition a local test tone at a safe starting volume. |
| U055 | P1 | Support an explicit output device choice on Android where the OS permits it. |
| U056 | P2 | Add balance/mono accessibility controls without altering the PC source. |
| U057 | P2 | Explain when changes need a reconnect and which take effect instantly. |
| U058 | P2 | Show numeric slider values and a Reset button beside each advanced control. |
| U059 | P2 | Debounce rapid slider edits; show pending/applied/error states. |
| U060 | P2 | Store per-profile audio preferences only when desired, with global default option. |

### Linux desktop control surface (U061–U075)

| ID | Priority | Proposal / success criterion |
|---|---|---|
| U061 | P0 | Make sink refresh nonblocking; keep Start and window close responsive on timeout. |
| U062 | P1 | Show separate controls for default sink versus a pinned device. |
| U063 | P1 | Auto-refresh sinks when PipeWire signals a device change; preserve valid selection. |
| U064 | P1 | Explain missing `as-cmd` with Install/Choose binary actions. |
| U065 | P1 | Avoid displaying raw CLI stack/log text as the only error explanation. |
| U066 | P1 | Add a status-area integration only where desktop supports it; keep window-only fallback. |
| U067 | P1 | Allow explicit “keep server running when window closes” with lifecycle explanation. |
| U068 | P1 | Save window size and last selected sink without leaking device identifiers in logs. |
| U069 | P1 | Support keyboard accelerators for Start/Stop, refresh and Help. |
| U070 | P1 | Use native GTK notifications for unexpected disconnects, with opt-out. |
| U071 | P2 | Offer a quick-switch menu for multiple local audio sinks. |
| U072 | P2 | Provide a quiet compact mode for a panel/sidebar. |
| U073 | P2 | Match GNOME/KDE light/dark preference rather than imposing one theme. |
| U074 | P2 | Add a direct link to relevant PipeWire user-service status, without automatic restart. |
| U075 | P2 | Show an offline-first Help dialog bundled with the app. |

### Android playback experience (U076–U090)

| ID | Priority | Proposal / success criterion |
|---|---|---|
| U076 | P0 | Replace blank loading with progress and a timed retry/failure state. |
| U077 | P0 | Keep play/pause state synchronized with actual service playback, not just button intent. |
| U078 | P1 | Put the active PC profile name above the Play action. |
| U079 | P1 | Provide a visible “Switch computer” action without deleting current address. |
| U080 | P1 | Show reconnect countdown and allow Cancel now. |
| U081 | P1 | Explain why Android battery restrictions may interrupt background playback. |
| U082 | P1 | Offer notification controls for play, stop and reconnect with clear labels. |
| U083 | P1 | Show whether output is phone speaker, wired headphones or Bluetooth. |
| U084 | P1 | Alert when Bluetooth route changes introduce additional delay. |
| U085 | P1 | Present the last failure in plain language with a Details expander. |
| U086 | P2 | Provide a “Test sound from PC” action once server-side safe test generation exists. |
| U087 | P2 | Add optional quick-settings tile onboarding that explains OS restrictions. |
| U088 | P2 | Preserve state across orientation/process recreation without a fake “playing” state. |
| U089 | P2 | Offer a restrained home-screen widget only if it can reflect true connection state. |
| U090 | P2 | Show a streaming-data estimate for metered tethering. |

### Accessibility and localization (U091–U105)

| ID | Priority | Proposal / success criterion |
|---|---|---|
| U091 | P0 | Add descriptive Play/Pause/Stop content descriptions and current-state semantics. |
| U092 | P0 | Announce connection-state changes through accessible live regions, without repeating rapidly. |
| U093 | P1 | Ensure every interactive Android control has at least a 48dp touch target. |
| U094 | P1 | Test the full onboarding and reconnect flow with TalkBack and keyboard. |
| U095 | P1 | Fix screen-reader order for host, port, play, status and troubleshooting. |
| U096 | P1 | Give sliders labels, current value, min/max and action semantics for assistive tech. |
| U097 | P1 | Use text or icons in addition to color for connected/error/silent states. |
| U098 | P1 | Verify contrast in light/dark and custom dynamic-color modes. |
| U099 | P1 | Respect large text and display scaling without clipped host/port fields. |
| U100 | P1 | Provide visible keyboard focus and sensible Tab order in GTK. |
| U101 | P1 | Replace jargon in primary actions while retaining technical details on demand. |
| U102 | P2 | Localize IP/help messages and plurals, not only top-level labels. |
| U103 | P2 | Respect reduced motion for meters and reconnect animations. |
| U104 | P2 | Keep high-contrast status accessible on grayscale/low-vision displays. |
| U105 | P2 | Test RTL layouts and numeric host/port rendering separately. |

### Error recovery and support (U106–U120)

| ID | Priority | Proposal / success criterion |
|---|---|---|
| U106 | P0 | Replace “server started” success with a staged readiness checklist. |
| U107 | P1 | Translate “bind failed” into wrong address, port in use or permissions guidance. |
| U108 | P1 | Distinguish TCP connection failure from UDP media failure. |
| U109 | P1 | Explain “no PipeWire sink” with a safe user-service check. |
| U110 | P1 | Show last-known-good sink when a selected device disappears. |
| U111 | P1 | Offer one-click retry after transient network loss; do not loop forever invisibly. |
| U112 | P1 | Show an error code and timestamp that can be copied for support. |
| U113 | P1 | Redact IPs, hostnames, keys and device names from diagnostics by default. |
| U114 | P1 | Provide a support bundle preview and explicit Save action, never automatic upload. |
| U115 | P1 | Put recovery actions near the failure, not only in a scrolling log. |
| U116 | P2 | Include “why this happened” and “what to try next” for common failures. |
| U117 | P2 | Keep last ten events in a bounded timeline with filterable categories. |
| U118 | P2 | Let users compare current and last-good network conditions locally. |
| U119 | P2 | Offer offline troubleshooting pages linked from error cards. |
| U120 | P2 | Provide a “Reset network settings” preview showing what is retained. |

### Visual hierarchy and responsive layout (U121–U135)

| ID | Priority | Proposal / success criterion |
|---|---|---|
| U121 | P1 | Use a clear primary status header, one primary action and secondary setup region. |
| U122 | P1 | Group Host and Port as connection settings, not as equal-weight hero controls. |
| U123 | P1 | Keep critical status above the fold on small Android screens. |
| U124 | P1 | Replace raw monospace output with a collapsible “Technical log” panel. |
| U125 | P1 | Adapt the GTK layout at narrow widths instead of clipping two-column labels. |
| U126 | P1 | Use system typography and spacing tokens consistently across Linux and Android. |
| U127 | P1 | Match the cold-launch splash to selected dark theme. |
| U128 | P2 | Use modest accent color for playing state; avoid decorative gradients that obscure controls. |
| U129 | P2 | Design empty, loading, success, reconnect and error states as separate compositions. |
| U130 | P2 | Add optional illustration only if it shortens setup comprehension in user tests. |
| U131 | P2 | Use a waveform/level meter only with a clear measurement label and low CPU cost. |
| U132 | P2 | Create coherent light/dark iconography rather than copying Pinterest examples. |
| U133 | P2 | Support landscape/tablet panes for controls and diagnostics side-by-side. |
| U134 | P2 | Use consistent terminology: sink, phone output, server, stream and connection. |
| U135 | P2 | Document state tokens and component behavior in a small design system. |

### Trust, privacy and power UX (U136–U150)

| ID | Priority | Proposal / success criterion |
|---|---|---|
| U136 | P0 | Warn clearly before using unencrypted legacy transport on shared Wi-Fi. |
| U137 | P0 | Require a visible, time-limited approval for an unknown phone once pairing exists. |
| U138 | P1 | Show which devices are authorized and let the owner revoke each. |
| U139 | P1 | State whether audio is captured, transmitted, muted or merely idle. |
| U140 | P1 | Explain that silent-stream optimization may trade wake latency for battery life. |
| U141 | P1 | Show a battery-saving mode with a measurable impact estimate, not a promise. |
| U142 | P1 | Make auto-start a separate, opt-in setting for GUI, server and Android playback. |
| U143 | P1 | Require an explicit confirmation before enabling remote/WAN listening. |
| U144 | P1 | Make “Forget this computer” erase trust material and saved connection details. |
| U145 | P2 | Show local-only telemetry defaults and optional collection choices. |
| U146 | P2 | Provide privacy labels for diagnostics export and saved profile fields. |
| U147 | P2 | Let users pause sharing instantly without changing their stored setup. |
| U148 | P2 | Warn when leaving an authenticated sharing session active on a public network. |
| U149 | P2 | Avoid dark patterns around optional power/security settings. |
| U150 | P2 | Provide an audit view of pairing and disconnect events stored only on device. |

## 50 other opportunities: ecosystem, AI Studio, release and research

These are adjacent product/operations ideas—not requests to put generative AI in the audio path. AI Studio concepts must remain opt-in, local-first, explainable, and unable to upload raw audio or credentials without explicit consent.

### Packaging and distribution (X01–X10)

| ID | Priority | Proposal / success criterion |
|---|---|---|
| X01 | P1 | Publish an Arch package recipe with correct dependency and uninstall metadata. |
| X02 | P1 | Add deterministic tarball checksums and reproducible-build instructions. |
| X03 | P1 | Distinguish Arch-only prerelease from universal Linux and full cross-platform release. |
| X04 | P1 | Publish an ARM64 Linux build only after CI and device smoke tests. |
| X05 | P1 | Add release notes for migration/compatibility, not only feature lists. |
| X06 | P1 | Document safe rollback to previous server/client pair. |
| X07 | P2 | Explore Flatpak with PipeWire portal/sandbox constraints validated first. |
| X08 | P2 | Explore a signed AppImage only if dynamic-library compatibility is solved. |
| X09 | P2 | Publish SBOM, dependency-update policy and security contact. |
| X10 | P2 | Add installer dry-run and uninstall instructions for system/user prefixes. |

### Quality, support and community (X11–X20)

| ID | Priority | Proposal / success criterion |
|---|---|---|
| X11 | P1 | Adopt a bug template requiring OS, PipeWire, route, versions and reproduction steps. |
| X12 | P1 | Add a privacy-safe diagnostic checklist for “connected but silent.” |
| X13 | P1 | Maintain a compatibility table for phones, Android versions and audio routes. |
| X14 | P1 | Publish a network troubleshooting matrix for Wi-Fi/USB/firewall/mDNS. |
| X15 | P1 | Run structured accessibility audits each release. |
| X16 | P1 | Define release-blocking security and crash criteria. |
| X17 | P2 | Recruit a small Arch/CachyOS beta cohort and collect opt-in qualitative feedback. |
| X18 | P2 | Triage upstream issues with reproduced/needs-info/fixed-in-fork labels. |
| X19 | P2 | Build an anonymized, opt-in benchmark corpus with consent and retention limits. |
| X20 | P2 | Compare real-world task completion time before and after onboarding changes. |

### “AI Studio” — assistive diagnostics, not cloud audio surveillance (X21–X30)

| ID | Priority | Proposal / success criterion |
|---|---|---|
| X21 | P2 | Prototype a local troubleshooting assistant that reads only user-approved redacted logs. |
| X22 | P2 | Show evidence lines and confidence for each AI-generated diagnosis. |
| X23 | P2 | Offer a deterministic rules-only fallback when no model is installed. |
| X24 | P2 | Provide a privacy dashboard showing exactly what is shared with any model. |
| X25 | P2 | Keep raw audio out of model input and logs by default. |
| X26 | P2 | Build a guided “latency lab” to compare settings with measured underruns. |
| X27 | P2 | Let the assistant propose settings, but require a user click to apply changes. |
| X28 | P2 | Run prompt-injection tests on log text and prohibit tool/command execution by model output. |
| X29 | P2 | Publish model/version provenance and allow full disable/uninstall. |
| X30 | P2 | Evaluate usefulness against a fixed troubleshooting checklist before shipping AI Studio. |

### Integrations and platform extension (X31–X40)

| ID | Priority | Proposal / success criterion |
|---|---|---|
| X31 | P2 | Explore KDE/GNOME system-tray behavior with native fallbacks. |
| X32 | P2 | Offer a documented local CLI status command for scripts and accessibility tools. |
| X33 | P2 | Add user-level systemd unit examples with explicit opt-in and secure defaults. |
| X34 | P2 | Evaluate per-application audio routing through PipeWire after a privacy review. |
| X35 | P2 | Explore receiver support on Android TV only after Android phone stability. |
| X36 | P2 | Explore Windows/Linux desktop receivers once transport security is complete. |
| X37 | P2 | Explore synchronized multi-phone playback with drift correction and clear latency cost. |
| X38 | P2 | Investigate phone microphone return path as a separate permissioned protocol feature. |
| X39 | P2 | Consider an API for accessibility/automation with local authentication and rate limits. |
| X40 | P2 | Evaluate LAN discovery interoperability with mDNS while minimizing exposed metadata. |

### Product discovery and responsible roadmap (X41–X50)

| ID | Priority | Proposal / success criterion |
|---|---|---|
| X41 | P1 | Interview users who need a substitute speaker, private listening, gaming and video sync separately. |
| X42 | P1 | Measure actual end-to-end latency, not ping, on at least three phone classes. |
| X43 | P1 | Compare USB tethering, Wi-Fi 2.4/5GHz and Ethernet-to-Wi-Fi in a repeatable test plan. |
| X44 | P1 | Define one primary audience and a default mode before adding advanced features. |
| X45 | P2 | Test whether “Premium” should mean better reliability/support rather than paywalled safety. |
| X46 | P2 | Avoid claims of lossless/low-latency until measured under documented conditions. |
| X47 | P2 | Maintain a public roadmap with evidence, dependencies and exit criteria. |
| X48 | P2 | Track consent-based metrics such as successful first stream and recovery time. |
| X49 | P2 | Establish a deprecation policy for insecure legacy clients before secure-only defaults. |
| X50 | P2 | Revisit this 250-item list quarterly; drop ideas that fail user tests. |

## Practical sequencing

1. **Safety and truthfulness:** C01–C10, C22, U016–U023, U091–U095, U136–U139. Do not advertise secure streaming before C03–C06 are verified.
2. **Audio reliability:** reproduce [#171](https://github.com/mkckr0/audio-share/issues/171) and [#156](https://github.com/mkckr0/audio-share/issues/156), then C11–C15 and U046–U055. Measure before claiming low latency.
3. **First successful stream:** U001–U010, U031–U044, C32–C37; test with a new user on Arch and Android.
4. **Distribution and maturity:** X01–X20, CI across architectures, then evaluate optional C16/C39 and X21–X40.

**Not recommended yet:** exposing the unauthenticated port to the Internet, always-on microphone capture, auto-running root commands, unconsented cloud log/audio uploads, or an AI model that executes diagnostic commands. These add serious risk before the basic streaming path is measured and secured.
