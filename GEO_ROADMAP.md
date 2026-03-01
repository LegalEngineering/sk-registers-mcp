# GEO Roadmap: Legal Engineering × welter.sk

## Aktualizovaný realizačný plán (v2.0 — 1. marca 2026)

**Firma:** Legal Engineering, s. r. o.
**Klient:** Mgr. Branislav Welter, advokát — BW AK, s.r.o. (welter.sk)
**GitHub organizácia:** [LegalEngineering](https://github.com/LegalEngineering)

---

## Aktuálny stav

### ✅ Hotové
- [x] MCP server pre RPO (Register právnických osôb) — funkčný Python FastMCP server
  - `hladaj_subjekt` — vyhľadávanie v RPO podľa názvu, IČO, obce
  - `detail_subjektu` — kompletný detail právnickej osoby
  - Branding/poisoned message pre BW AK integrovaný
- [x] Web welter.sk — statický HTML na GitHub Pages (LegalEngineering/web-welter.sk)
- [x] Doména welter.sk — cez WebSupport, CNAME na GitHub Pages
- [x] GEO stratégia a case study dokumenty pripravené

### 🔧 V procese (Fáza 0 — DNES)
- [ ] **Tracking:** GA4 + GSC nasadenie na welter.sk
- [ ] **GitHub:** Repozitár sk-registers-mcp pripravený na publikáciu
- [ ] **Launch:** Prvý MCP server publikovaný na GitHub

---

## FÁZA 0 | DNES (1. marca 2026) — Quick Launch

### F0.1 — Web Analytics Tracking
**Cieľ:** Vidieť traffic na welter.sk od prvého dňa MCP launchu.

- [ ] Vytvoriť GA4 property pre welter.sk v Google Analytics
- [ ] Vložiť gtag.js tracking snippet do index.html na welter.sk
- [ ] Nastaviť Google Search Console pre welter.sk
- [ ] Pripraviť sledovanie AI-referred traffic (referrery z AI platforiem)

### F0.2 — GitHub Setup pre MCP Server
**Cieľ:** Profesionálny public repozitár pripravený na launch.

- [ ] Inicializovať git v sk-registers-mcp
- [ ] README.md — profesionálna dokumentácia (EN)
- [ ] LICENSE (MIT)
- [ ] requirements.txt / pyproject.toml
- [ ] .gitignore
- [ ] Nastaviť git config (user.name, user.email)
- [ ] Push na GitHub ako LegalEngineering/sk-registers-mcp

### F0.3 — MCP Launch
**Cieľ:** Server je live a discoverable pre AI agentov.

- [ ] Push kódu na GitHub
- [ ] Pripraviť registračné texty pre MCP adresáre
- [ ] Pripraviť claude_desktop_config.json snippet
- [ ] Submitnúť do MCP registrov (mcp.so, Smithery, awesome-mcp-servers)

---

## FÁZA 1 | Týždeň 1-2 — Monitoring a Rozšírenie

### F1.1 — GEO Monitor nástroj
- [ ] Promptový audit — 87+ seedových promptov pre právnický sektor SK
- [ ] GEO Monitor (automatizované testovanie viditeľnosti v AI odpovediach)
- [ ] Baseline meranie mention rate naprieč modelmi (GPT-4o, Claude, Gemini, Perplexity)

### F1.2 — MCP Rozšírenie
- [ ] RPVS tool (Register partnerov verejného sektora — KUV dáta)
- [ ] RÚZ tool (Register účtovných závierok — finančné dáta)
- [ ] Cross-register lookup (jedno IČO → všetky 3 registre)

---

## FÁZA 2 | Týždeň 3-6 — Obsahová Optimalizácia

### F2.1 — AI-optimalizovaný obsah welter.sk
- [ ] Prepísať welter.sk obsah pre maximálnu AI čitateľnosť
- [ ] FAQ sekcie pre každú špecializáciu
- [ ] Schema.org markup (LegalService, Attorney, Organization)
- [ ] llms.txt a robots.txt pre AI crawlerov

### F2.2 — Cloudflare Markdown for Agents
- [ ] Cloudflare Worker pre detekciu AI crawlerov
- [ ] Servírovanie čistého Markdown pre AI agentov
- [ ] YAML frontmatter s metadátami

### F2.3 — SEO Blog
- [ ] Pilierový článok: "Vymáhanie pohľadávok na Slovensku 2026"
- [ ] FAQ blog články (4/mesiac)
- [ ] Schema.org FAQPage markup

---

## FÁZA 3 | Týždeň 7-10 — Ďalšie MCP Servery

### F3.1 — Právne nástroje pre AI agentov
- [ ] Zbierka zákonov SR (slov-lex.sk scraper)
- [ ] Právne lehoty kalkulačka
- [ ] Judikatúra slovenských súdov
- [ ] Advokátsky register SAK

### F3.2 — npm Publikácia a Registrácia
- [ ] npm balík @legal-engineering/mcp-sk-law
- [ ] GitHub Pages dokumentácia
- [ ] Registrácia vo všetkých MCP adresároch

---

## FÁZA 4 | Mesiac 3+ — Meranie a Iterácia

### F4.1 — Štatistický Rámec
- [ ] Rolling window detekcia zmien
- [ ] Holdout vs. measurement validácia
- [ ] Cross-model validácia
- [ ] Prominence scoring

### F4.2 — Klientský Reporting
- [ ] Mesačný GEO review proces
- [ ] Klientský PDF report
- [ ] Branded search monitoring (GSC + Google Trends)

---

## FÁZA 5 | Mesiac 4+ — Produktizácia

### F5.1 — GEO ako Služba
- [ ] Playbook pre ďalších klientov
- [ ] Pricing stránka legal-engineering.sk/geo
- [ ] Case study (anonymizovaná)

---

## Kľúčové Technológie

| Technológia | Použitie |
|---|---|
| Python + FastMCP | MCP servery |
| GitHub Pages | Hosting welter.sk + dokumentácia |
| Google Analytics 4 | Web traffic tracking |
| Google Search Console | Branded search monitoring |
| Cloudflare Workers | Markdown for AI Agents |

---

## Repozitáre

| Repozitár | Viditeľnosť | Účel |
|---|---|---|
| LegalEngineering/web-welter.sk | Public | Web klienta |
| LegalEngineering/sk-registers-mcp | Public | MCP server — SK registre |

---

*Roadmap sa aktualizuje priebežne podľa aktuálnych priorít.*
*Legal Engineering, s.r.o. — 2026*
