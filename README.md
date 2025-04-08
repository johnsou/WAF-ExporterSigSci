# WAF-ExporterSigSci
WAF Rule Exporter &amp; Dashboard Metabase

Extract, enrich, and visualize Signal Sciences (Fastly NGWAF) WAF rules using Python + SQLite + Metabase.

---

## 🚀 Features

- ✅ Extract all WAF rules (custom + signal) from every site in your corp
- ✅ Export to CSV and JSON
- ✅ Enrich rules with agent count + IP tag data
- ✅ Convert to SQLite for easy dashboarding
- ✅ Run Metabase locally via Docker for instant rule visualization

---

## 📦 Requirements

- Python 3.8+
- Docker (for Metabase)
- Signal Sciences (Fastly NGWAF) API token

---

## ⚙️ Setup

1. **Clone the repo**  
2. Create a `.env` file from `.env.example`:

```env
SIGSCI_EMAIL=your-email@example.com
SIGSCI_API_TOKEN=your-api-token
CORP_NAME=your-corp-name
