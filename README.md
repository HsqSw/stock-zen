# Stock Monitor Tool

## Environment Setup

This project uses `uv` for dependency management.

### Prerequisites

- Python 3.10+
- `uv` installed

### Installation

```bash
uv sync
```

### Usage

```bash
uv run main.py
```

## Dependencies

- **AkShare**: Main data source for sector fund flows.
- **eFinance**: Supplementary data source for individual stock flows/bills.
- **Pandas**: Data processing.
