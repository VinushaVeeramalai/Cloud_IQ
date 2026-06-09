# Cloud Cost Optimizer

## What This Is
Cloud Cost Optimizer is an autonomous Python AI agent that reads mock cloud billing CSV files, detects idle and oversized resources, reasons about each finding with a local Ollama model, files prioritized GitHub issues, sends Discord alerts, emails a formatted report, and generates a beautiful offline HTML dashboard.

## Business Problem It Solves
Cloud teams waste real budget on idle compute and oversized database instances. This agent automates cost discovery and prioritizes remediation so cloud operations teams can act quickly.

## How It Works
```
CSV Data -> reader.py -> detector.py -> llm_analyzer.py -> github_issues.py -> discord_alert.py -> email_report.py -> html_report.py
```

## Architecture Diagram
```
[ data ] -> reader.py -> detector.py -> llm_analyzer.py
                             |-> github_issues.py
                             |-> discord_alert.py
                             |-> email_report.py
                             |-> html_report.py
```

## Tech Stack
- Python 3
- Ollama local LLM
- GitHub Issues API
- Discord Webhooks
- SMTP email delivery
- Pure SVG HTML dashboard

## Setup Instructions
1. Clone or open the repository.
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Create a `.env` file from `.env.example` and update the GitHub, Discord, SMTP, and Ollama settings.
4. Ensure the Ollama endpoint defined in `config.py` / `.env` is available.

### Links / values to provide in `.env`
- `GITHUB_TOKEN`: GitHub personal access token
- `GITHUB_REPO`: repository name like `owner/repo`
- `DISCORD_WEBHOOK_URL`: Discord webhook URL
- `EMAIL_SENDER`, `EMAIL_PASSWORD`, `EMAIL_RECEIVER`: SMTP email credentials
- `SMTP_SERVER`, `SMTP_PORT`: email server details
- `OLLAMA_URL`: Ollama API endpoint URL

## Website and Dashboard
- Open `website/index.html` for the project website landing page.
- Run `python main.py` to generate the full dashboard at `output/dashboard.html`.
- Ask a cloud cost question directly with `python main.py --ask "Your question here"`.
- Generate AI training data from the latest findings with `python main.py --train`.
- Enable live watch mode to regenerate the dashboard when the CSV changes:
  `python main.py --watch 10`

## How To Run
```bash
python main.py
```

### Enable integrations on demand
```bash
python main.py --github --discord --email --ai
```

### Run live watch mode
```bash
python main.py --watch 10 --github --discord --email --ai
```

### Generate an AI training dataset
```bash
python main.py --train
```

## Sample Output
- Terminal progress steps with emojis
- `output/dashboard.html` opens automatically
- GitHub issues filed with cost optimization labels
- Discord summary alert delivered
- HTML email report sent

## Project Structure
```
cloud-cost-optimizer/
├── data/
├── output/
├── src/
├── main.py
├── config.py
├── requirements.txt
├── prompts.md
└── README.md
```

## Mandatory Requirements Checklist
- [x] AI-Assisted Development
- [x] Prompt Documentation (see prompts.md)
- [x] AI Capability: Agent Loop + External API

## Team
Cloud Cost Optimizer was designed as a placement project with clean module separation, resilient error handling, and production-minded extensibility.
