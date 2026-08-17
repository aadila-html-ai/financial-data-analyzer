# 📈 Financial Data Analyzer

A lightweight, dependency-light Python toolkit for analyzing historical price data. Point it at a CSV of OHLCV data and it computes returns, volatility, drawdown, Sharpe/Sortino ratios, and moving averages — then generates clean, dark-themed charts and a shareable Markdown report.

![Cumulative Returns](assets/cumulative_returns.png)

## Features

- 📊 **Core metrics** — total return, CAGR, annualized volatility, Sharpe ratio, Sortino ratio, max drawdown, best/worst day
- 📉 **Multi-ticker support** — analyze a single instrument or an entire portfolio from one CSV
- 🔗 **Correlation matrix** — see how your holdings move relative to each other
- 🖼️ **Auto-generated charts** — price + moving averages, drawdown, cumulative return comparison, correlation heatmap
- 📝 **Markdown report** — a single `report.md` bundling every metric and chart, ready to drop into a wiki or GitHub repo
- 🎨 **Rich terminal output** — a formatted, color-coded summary table right in your terminal
- ✅ **Tested** — unit tests included for the core analysis engine

## Preview

| Price & Moving Averages | Correlation Matrix |
|---|---|
| ![Price](assets/AAPL_price_ma.png) | ![Correlation](assets/correlation_matrix.png) |

## Installation

```bash
git clone https://github.com/<your-username>/financial-data-analyzer.git
cd financial-data-analyzer
pip install -r requirements.txt
```

Or install as a CLI tool:

```bash
pip install -e .
```

## Usage

### Command line

```bash
python -m financial_analyzer.cli --file sample_data/portfolio.csv
```

This prints a summary table to the terminal and writes charts + `report.md` to `./output/`.

**Options:**

| Flag | Description | Default |
|---|---|---|
| `--file`, `-f` | Path to a CSV of price data (required) | — |
| `--risk-free`, `-r` | Annualized risk-free rate as a decimal, used in Sharpe/Sortino | `0.02` |
| `--outdir`, `-o` | Directory to write charts and report into | `output` |
| `--no-charts` | Skip chart generation, print summary only | off |

Example with a custom risk-free rate:

```bash
python -m financial_analyzer.cli -f sample_data/portfolio.csv -r 0.045 -o reports/
```

If you installed with `pip install -e .`, you can also run:

```bash
financial-analyzer --file sample_data/portfolio.csv
```

### As a library

```python
from financial_analyzer.analyzer import FinancialDataAnalyzer

analyzer = FinancialDataAnalyzer("sample_data/portfolio.csv")

for ticker in analyzer.tickers:
    metrics = analyzer.compute_metrics(ticker, risk_free_rate=0.02)
    print(metrics.as_dict())

# Correlation across all tickers in the file
print(analyzer.correlation_matrix())
```

## Input format

The analyzer expects a CSV with (at minimum) `Date` and `Close` columns. Column names are case-insensitive.

```csv
Date,Ticker,Open,High,Low,Close,Volume
2023-01-02,AAPL,133.82,134.47,132.05,133.19,4038383
2023-01-03,AAPL,131.96,132.57,130.90,132.44,4039763
...
```

- `Ticker` is optional — if omitted, the whole file is treated as one instrument (named from the filename).
- Multiple tickers can live in a single file; the analyzer groups by `Ticker` automatically.
- `Open`, `High`, `Low`, `Volume` are optional and used for extra context (volume averages, etc.) but not required.

A realistic 500-day, 3-ticker sample dataset is included at [`sample_data/portfolio.csv`](sample_data/portfolio.csv).

## Metrics reference

| Metric | Meaning |
|---|---|
| **Total Return** | Percent change from first to last close in the period |
| **CAGR** | Compound annual growth rate over the period |
| **Ann. Volatility** | Annualized standard deviation of daily returns |
| **Sharpe Ratio** | Risk-adjusted return vs. the risk-free rate (total volatility) |
| **Sortino Ratio** | Like Sharpe, but only penalizes downside volatility |
| **Max Drawdown** | Largest peak-to-trough decline, and the date it occurred |
| **Best / Worst Day** | Largest single-day gain and loss in the period |

## Project structure

```
financial-data-analyzer/
├── financial_analyzer/
│   ├── __init__.py
│   ├── analyzer.py       # Core metrics engine
│   ├── visualizer.py     # Matplotlib chart generation
│   ├── report.py         # Markdown report builder
│   └── cli.py            # Command-line interface
├── sample_data/
│   └── portfolio.csv     # Sample 3-ticker dataset
├── tests/
│   └── test_analyzer.py
├── assets/                # README preview images
├── requirements.txt
├── setup.py
└── README.md
```

## Running tests

```bash
pip install pytest
pytest
```

## Roadmap

- [ ] Support fetching live data from a market data API
- [ ] Rolling Sharpe ratio chart
- [ ] Portfolio-level (weighted) metrics, not just per-ticker
- [ ] Export report to PDF/HTML in addition to Markdown

## License

MIT — see [LICENSE](LICENSE).
