## CLI usage examples

You can place orders directly from the command line using `cli.py`. Run these from the project root after creating `.env` and activating the virtualenv.

PowerShell / Bash examples:

```powershell
# Market buy
python cli.py market --symbol BTCUSDT --side BUY --quantity 0.001

# Limit sell
python cli.py limit --symbol BTCUSDT --side SELL --quantity 0.001 --price 45000

# Cancel an order by id
python cli.py cancel --symbol BTCUSDT --orderId 123456789

# List open orders
python cli.py open
```

Notes:

- `--side` should be `BUY` or `SELL`.
- `--quantity` and `--price` are numeric; respect exchange precision and lot size rules.
- Errors and responses are printed to stdout and also logged to `logs/` per `bot/logging_config.py`.

# TradingBOT (example project)

Small trading-bot example project. Contains a light `bot` package plus example runners `aa.py` and `cli.py`.

**Status:** Minimal example code for learning and experimentation.

## Requirements

- Python 3.8+
- Internet access for any API calls
- See `requirements.txt` for Python dependencies

## Setup

1. Open a terminal in the project root (the folder that contains this README).
2. Create and activate a virtual environment (Windows PowerShell example):

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

On Windows (cmd):

```cmd
python -m venv .venv
.\.venv\Scripts\activate.bat
```

On macOS / Linux:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Environment variables: this project reads configuration from a `.env` file in the project root. Create or edit `.env` to supply any required secrets (API keys, etc.). Check `bot/config.py` for variable names used by the code.

## Running the example runners

- From the project root you can run the simple example scripts:

```bash
python aa.py
python cli.py
```

- These scripts are lightweight examples that import and exercise parts of the `bot` package. If you need a different entrypoint, inspect files in the `bot/` package.

## Logging

Logs are written to the `logs/` directory. See `bot/logging_config.py` for logging setup and log levels.

## Project layout

- `aa.py` — example runner
- `cli.py` — CLI-style runner
- `bot/` — package containing the main logic
  - `client.py`, `orders.py`, `utils.py`, `config.py`, `validators.py`, `logging_config.py`
- `requirements.txt` — Python dependencies
- `.env` — environment variables (not committed)
- `logs/` — runtime logs

## Assumptions

- You will run commands from the project root.
- Python 3.8+ is installed and on your PATH.
- Any API credentials required by the bot are provided via the `.env` file.
- The `requirements.txt` file lists all required packages; if you add dependencies, update that file.

## Troubleshooting

- If you see import errors, ensure the virtualenv is activated and `pip install -r requirements.txt` completed successfully.
- If the bot cannot access an external API, confirm network access and that required API keys are present in `.env`.
- Check `logs/` for runtime errors and refer to `bot/logging_config.py` to adjust log level.

## Next steps (suggested)

- Inspect `bot/config.py` to see what environment variables are required and add them to `.env`.
- Run `python aa.py` to exercise the code and review logs in `logs/`.

If you'd like, I can also run a quick smoke test or add a `README` example showing expected `.env` keys.
