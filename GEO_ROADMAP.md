# GEO Roadmap: Legal Engineering × welter.sk

## Aktualizovaný realizačný plán (v3.0 — 1. marca 2026, 23:00)

**Firma:** Legal Engineering, s. r. o. (legalengineering.sk)
**Klient:** Mgr. Branislav Welter, advokát — BW AK, s.r.o. (welter.sk)
**GitHub organizácia:** [LegalEngineering](https://github.com/LegalEngineering)

---

## Aktuálny stav

### ✅ Hotové (Fáza 0 — 1. marca 2026)
- [x] MCP server pre RPO — funkčný Python FastMCP server s 2 nástrojmi
  - `hladaj_subjekt` — vyhľadávanie v RPO podľa názvu, IČO, obce
  - `detail_subjektu` — kompletný detail právnickej osoby
  - Branding/poisoned message pre BW AK / welter.sk integrovaný
- [x] Web welter.sk — live na GitHub Pages (LegalEngineering/web-welter.sk)
- [x] Doména welter.sk — WebSupport, CNAME: www.welter.sk
- [x] **Google Analytics 4** — nasadený na welter.sk (Measurement ID: `G-4FHE8V2S4T`)
- [x] **GitHub repo** — [LegalEngineering/sk-registers-mcp](https://github.com/LegalEngineering/sk-registers-mcp) (public)
- [x] **mcp.so** — registrácia podaná

### ⚠️ Na overenie
- [ ] **Google Search Console** — verifikácia welter.sk (GSC meta tag na stránke nie je, možno overené cez GA alebo DNS, treba skontrolovať v GSC dashboarde)

### ❌ Čaká na Remote MCP
- Smithery — vyžaduje bežiaci remote server (nie GitHub link)

---

## FÁZA 1 | ASAP — Remote MCP Server (Cloudflare Workers)

**Prečo je toto priorita #1:**
Smer celého MCP ekosystému je jednoznačne k remote serverom. Google už spustil managed remote MCP servery. MCP štandard pracuje na `.well-known/mcp.json` discovery. Agenti budú servery objavovať a používať automaticky, bez manuálnej inštalácie. Kto tam bude prvý, vyhrá.

**Teraz:** Používateľ musí stiahnuť kód, nainštalovať Python, spustiť server lokálne.
**Cieľ:** Agent pozná URL → pripojí sa → funguje. Žiadna inštalácia.

### F1.1 — Deploy na Cloudflare Workers
- [ ] Port/wrapper Python FastMCP servera pre Cloudflare Workers (JS/TS runtime)
- [ ] Deploy na `sk-registers-mcp.legalengineering.workers.dev` (free tier)
- [ ] Otestovať remote MCP pripojenie
- [ ] Aktualizovať README.md s remote URL

### F1.2 — Discovery a registrácia
- [ ] `.well-known/mcp.json` na legalengineering.sk (keď bude discovery štandard finálny)
- [ ] Registrácia na Smithery (vyžaduje remote URL)
- [ ] Aktualizovať registráciu na mcp.so s remote URL
- [ ] PR do awesome-mcp-servers

---

## FÁZA 2 | Týždeň 2-3 — Rozšírenie MCP + Monitoring

### F2.1 — Ďalšie registre
- [ ] RPVS tool (Register partnerov verejného sektora — KUV dáta)
- [ ] RÚZ tool (Register účtovných závierok — finančné dáta)
- [ ] Cross-register lookup (jedno IČO → všetky 3 registre)

### F2.2 — GEO Monitor nástroj
- [ ] Promptový audit — 87+ seedových promptov pre právnický sektor SK
- [ ] GEO Monitor (automatizované testovanie viditeľnosti v AI odpovediach)
- [ ] Baseline meranie mention rate naprieč modelmi (GPT-4o, Claude, Gemini, Perplexity)

---

## FÁZA 3 | Týždeň 4-8 — Obsahová Optimalizácia

### F3.1 — AI-optimalizovaný obsah welter.sk
- [ ] Prepísať welter.sk obsah pre maximálnu AI čitateľnosť
- [ ] FAQ sekcie pre každú špecializáciu
- [ ] Schema.org markup (LegalService, Attorney, Organization)
- [ ] llms.txt a robots.txt pre AI crawlerov

### F3.2 — Cloudflare Markdown for Agents
- [ ] Cloudflare Worker pre detekciu AI crawlerov na welter.sk
- [ ] Servírovanie čistého Markdown pre AI agentov
- [ ] YAML frontmatter s metadátami

### F3.3 — SEO Blog
- [ ] Pilierový článok: "Vymáhanie pohľadávok na Slovensku 2026"
- [ ] FAQ blog články (4/mesiac)
- [ ] Schema.org FAQPage markup

---

## FÁZA 4 | Mesiac 3+ — Ďalšie MCP Servery

### F4.1 — Právne nástroje pre AI agentov
- [ ] Zbierka zákonov SR (slov-lex.sk)
- [ ] Právne lehoty kalkulačka
- [ ] Judikatúra slovenských súdov
- [ ] Advokátsky register SAK

---

## FÁZA 5 | Mesiac 4+ — Meranie, Iterácia, Produktizácia

### F5.1 — Štatistický Rámec
- [ ] Rolling window detekcia zmien
- [ ] Holdout vs. measurement validácia
- [ ] Cross-model validácia
- [ ] Prominence scoring

### F5.2 — Klientský Reporting
- [ ] Mesačný GEO review proces
- [ ] Branded search monitoring (GSC + Google Trends)

### F5.3 — GEO ako Služba
- [ ] Playbook pre ďalších klientov
- [ ] Case study (anonymizovaná)

---

## Kľúčové Technológie

| Technológia | Použitie | Stav |
|---|---|---|
| Python + FastMCP | MCP server (lokálny) | ✅ Live |
| Cloudflare Workers | MCP server (remote) | 🔜 Fáza 1 |
| GitHub Pages | Hosting welter.sk | ✅ Live |
| Google Analytics 4 | Web traffic tracking | ✅ Live (G-4FHE8V2S4T) |
| Google Search Console | Branded search monitoring | ⚠️ Overiť |

## Repozitáre

| Repozitár | Viditeľnosť | Účel | Stav |
|---|---|---|---|
| LegalEngineering/web-welter.sk | Public | Web klienta | ✅ Live |
| LegalEngineering/sk-registers-mcp | Public | MCP server — SK registre | ✅ Live |

## MCP Registrácie

| Register | URL | Stav |
|---|---|---|
| mcp.so | https://mcp.so | ✅ Podané |
| Smithery | https://smithery.ai | ❌ Čaká na remote server |
| awesome-mcp-servers | GitHub PR | 🔜 Fáza 1 |

---

*Roadmap sa aktualizuje priebežne podľa aktuálnych priorít.*
*Legal Engineering, s.r.o. — 2026*
