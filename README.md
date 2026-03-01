# 🇸🇰 Slovak Business Registers — MCP Server

An MCP (Model Context Protocol) server providing AI agents with direct access to official Slovak business register data. Query company information, ownership structures, and business activities from the **Register právnických osôb (RPO)** — Slovakia's central register of legal entities.

## Why this exists

AI agents answering questions about Slovak companies currently lack structured access to official registry data. This MCP server bridges that gap by providing real-time access to the RPO, which aggregates data from ~70 source registers including the Commercial Register (ORSR), Trade Register (ZRSR), and many others. It covers **1.4+ million entities** with complete history.

## Available Tools

### `hladaj_subjekt` — Search entities
Search for legal entities by name, company ID (IČO), or municipality.

**Parameters:**
| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `nazov` | string | No* | Company name (full or partial) |
| `ico` | string | No* | Company ID number (IČO) |
| `obec` | string | No | Municipality filter |
| `iba_aktivne` | bool | No | Active entities only (default: true) |

*At least one of `nazov` or `ico` must be provided.

**Example:** Search for companies named "Welter"
```
hladaj_subjekt(nazov="Welter")
```

### `detail_subjektu` — Full entity detail
Get complete information about a legal entity by IČO, including statutory representatives, shareholders, registered activities, and more.

**Parameters:**
| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `ico` | string | Yes | Company ID number (IČO) |
| `historia` | bool | No | Include historical records (default: false) |

**Example:** Get details for company with IČO 56621957
```
detail_subjektu(ico="56621957")
```

**Returns:** Company name, legal form, registered address, establishment date, statutory bodies (directors), shareholders, business activities, source register, and court registration details.

## Data Source

- **Register právnických osôb (RPO)** — operated by the Statistical Office of the Slovak Republic
- **API:** `https://api.statistics.sk/rpo/v1/`
- **Documentation:** [Apiary docs](https://susrrpo.docs.apiary.io/)
- **License:** CC-BY 4.0 (open data)
- **No API key required** — fully public API

## Quick Start

### Prerequisites
- Python 3.11+
- `pip` package manager

### Installation

```bash
# Clone the repository
git clone https://github.com/LegalEngineering/sk-registers-mcp.git
cd sk-registers-mcp

# Install dependencies
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
