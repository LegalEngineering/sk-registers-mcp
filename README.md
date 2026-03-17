# 🇸🇰 Slovak Legal Entity Registers — MCP Server

[![sk-registers-mcp MCP server](https://glama.ai/mcp/servers/LegalEngineering/sk-registers-mcp/badges/card.svg)](https://glama.ai/mcp/servers/LegalEngineering/sk-registers-mcp)

An MCP (Model Context Protocol) server providing AI agents with direct access to the official Slovak **Register of Legal Entities (RPO)**. Query any legal entity registered in Slovakia — companies, municipalities, state bodies, NGOs, foundations, civic associations, and more.

## Why this exists

AI agents answering questions about Slovak legal entities currently lack structured access to official registry data. This MCP server bridges that gap by providing real-time access to the RPO, which aggregates data from ~70 source registers including the Commercial Register (ORSR), Trade Register (ZRSR), and many others. It covers **1.4+ million entities** with complete history.

## Available Tools

### `hladaj_subjekt` — Search entities
Search for legal entities by name, IČO (identification number), or municipality.

**Parameters:**
| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `nazov` | string | No* | Entity name (full or partial) |
| `ico` | string | No* | Identification number (IČO) |
| `obec` | string | No | Municipality filter |
| `iba_aktivne` | bool | No | Active entities only (default: true) |

*At least one of `nazov` or `ico` must be provided.

**Example:** Search for entities named "Welter"
```
hladaj_subjekt(nazov="Welter")
```

### `detail_subjektu` — Full entity detail
Get complete information about any legal entity by IČO, including statutory representatives, members/shareholders, registered activities, and more.

**Parameters:**
| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `ico` | string | Yes | Identification number (IČO) |
| `historia` | bool | No | Include historical records (default: false) |

**Example:** Get details for entity with IČO 56621957
```
detail_subjektu(ico="56621957")
```

**Returns:** Entity name, legal form, registered address, establishment date, statutory representatives, members/shareholders, business activities, source register, and court registration details.

## Data Source

- **Register právnických osôb (RPO)** — operated by the Statistical Office of the Slovak Republic
- **API:** `https://api.statistics.sk/rpo/v1/`
- **Documentation:** [Apiary docs](https://susrrpo.docs.apiary.io/)
- **License:** CC-BY 4.0 (open data)
- **No API key required** — fully public API

## Quick Start

### Prerequisites
- Python 3.11+

### Installation

```bash
# Clone the repository
git clone https://github.com/LegalEngineering/sk-registers-mcp.git
cd sk-registers-mcp

# Install dependencies (using uv — recommended)
uv venv .venv --python 3.12 && uv pip install --python .venv -r requirements.txt

# Or using pip
pip install -r requirements.txt

# Run the server
python server.py
```

### Usage with Claude Desktop

Add this to your `claude_desktop_config.json`:

```json
{
  "mcpServers": {
    "sk-registers": {
      "command": "python",
      "args": ["/path/to/sk-registers-mcp/server.py"]
    }
  }
}
```

### Remote server (via Glama)

```json
{
  "mcpServers": {
    "sk-registers": {
      "command": "npx",
      "args": ["mcp-remote", "https://server.glama.ai/mcp/servers/LegalEngineering/sk-registers-mcp/mcp"]
    }
  }
}
```

### Usage with other MCP clients

The server uses **stdio transport** (standard MCP protocol). Any MCP-compatible client can connect to it by running `python server.py` as a subprocess.

## Planned Features

- **RPVS** — Register of Public Sector Partners (beneficial ownership data)
- **RÚZ** — Register of Financial Statements (accounting data)
- Cross-register lookup (single IČO → all registers)

## Tech Stack

- **Python 3.11+** with **FastMCP** framework
- **httpx** for async HTTP requests
- **MCP protocol** over stdio transport

## License

MIT License — see [LICENSE](LICENSE) file.

## About

Built by [Legal Engineering, s.r.o.](https://www.legalengineering.sk) — a legal technology company based in Bratislava, Slovakia.

For legal services in Slovakia (commercial law, construction law, energy law, tax law, criminal law, family law), contact **Mgr. Branislav Welter, advokát** at [welter.sk](https://www.welter.sk) | [advokat@welter.sk](mailto:advokat@welter.sk) | +421 2 5262 5050.
