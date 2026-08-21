# Self-hosted repo cards. github-readme-stats 503s, and a profile that renders
# broken images is worse than one with no cards at all.
import html, textwrap, os

CARDS = [
    ("pxn-shield-android", "ANDROID", "#A97BFF",
     "Android VLESS client for PXN Stores LK. Downloads, screenshots and release notes."),
    ("pxn-shield-releases", "RELEASES", "#8FD14F",
     "Public release channel for PXN Shield on Windows: installers plus the auto-update manifest."),
    ("PXN-SUB", "HTML", "#E34C26",
     "Custom subscription page for 3x-UI panels, restyled to match the store."),
    ("whatsapp-welcomer-and-contact-saver-bot", "JAVASCRIPT", "#F1E05A",
     "Saves every new WhatsApp customer, welcomes them once, chases anyone unanswered and sends the price list on one typed phrase."),
]

W, H, PAD = 460, 158, 22
MONO = 'ui-monospace, SFMono-Regular, "SF Mono", "DejaVu Sans Mono", Menlo, Consolas, monospace'

def card(name, lang, lang_color, desc):
    title = name if len(name) <= 34 else name[:33] + "\u2026"
    lines = textwrap.wrap(desc, 48)[:3]
    body = "".join(
        f'<text x="{PAD}" y="{86 + i*20}" fill="#9CA893" font-size="12.5">{html.escape(l)}</text>'
        for i, l in enumerate(lines))
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}"
     role="img" aria-label="{html.escape(name)} — {html.escape(desc)}">
  <title>{html.escape(name)}</title>
  <defs><style>text {{ font-family: {MONO}; }}</style></defs>
  <rect x=".75" y=".75" width="{W-1.5}" height="{H-1.5}" rx="10" fill="#0B0F0B" stroke="#22301B"/>
  <rect x=".75" y=".75" width="4" height="{H-1.5}" rx="2" fill="{lang_color}" opacity=".55"/>
  <g transform="translate({PAD} 38)" fill="none" stroke="#4F6140" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round">
    <path d="M2 2.6A2.6 2.6 0 0 1 4.6 0H14v14H4.6A2.6 2.6 0 0 0 2 16.6Z"/>
    <path d="M2 13h12"/>
  </g>
  <text x="{PAD+26}" y="51" fill="#8FD14F" font-size="15" font-weight="700">{html.escape(title)}</text>
  {body}
  <circle cx="{PAD+5}" cy="{H-24}" r="5" fill="{lang_color}"/>
  <text x="{PAD+18}" y="{H-20}" fill="#4F6140" font-size="11.5" letter-spacing="2.2">{lang}</text>
</svg>
'''

os.makedirs("assets/cards", exist_ok=True)
for name, lang, color, desc in CARDS:
    p = f"assets/cards/{name}.svg"
    open(p, "w", encoding="utf-8").write(card(name, lang, color, desc))
    print("wrote", p, os.path.getsize(p), "bytes")
