# R6 Tracker

A Python project that uses the R6Data API to fetch Rainbow Six Siege player statistics and generate role-based reports.

The current focus is on an Entry Performance Score that evaluates how well a player performs in opening fights, entry involvement, and kill pressure.

## Features

- Fetches full player stats from the R6Data API
- Loads the API key securely from a `.env` file
- Supports PlayStation, Xbox, and PC accounts
- Generates operator summaries and general totals reports
- Calculates an Entry Performance Score
- Identifies top entry operators for a player
- Filters out small sample sizes to reduce misleading results

## Project Structure

```text
r6_tracker/
├── main.py
├── r6data_api.py
├── parsers.py
├── summaries.py
├── scores.py
├── roles.py
├── output/
└── README.md
```

## Getting Started

### 1. Prerequisites

- Python 3.9+
- `pip`

### 2. Install dependencies

```bash
python -m pip install requests python-dotenv
```

### 3. Configure your API key

Create a file named `.env` in the project root and add your R6Data API key:

```env
R6DATA_API_KEY=your_api_key_here
```

> Do not commit this file to GitHub.

## Usage

### Run the summary report

```bash
python .\main.py summary
```

The script will prompt you for:

- your in-game name
- your platform (`psn`, `xbl`, or `uplay`)

It then generates reports in the `output/` folder, including:

- full stats export
- operator summary
- general operator totals

### Run the entry report

```bash
python .\main.py entry
```

This prints an entry-focused performance report in the terminal after the same prompts.

### Try it without your own account

If you just want to see how the program works, you can use my pc account:

- player name: `sebakee`
- platform: `uplay`

This will let you explore the output format even if you do not have your own Rainbow Six account.

## Platform Settings

The script asks for the platform when you run it:

- PlayStation: `psn`
- Xbox: `xbl`
- PC: `uplay`

The program automatically maps `uplay` to the PC platform family and uses the console family for `psn` and `xbl`.

## Entry Performance Score

The Entry Performance Score is designed to estimate how effective a player is when taking opening fights.

It is based on three components:

- Opening success: how often the player wins opening duels
- Opening involvement: how often the player is involved in opening fights
- Kill pressure: how many kills the player gets per round

### How it works

- Opening success is based on:
  `first bloods / (first bloods + first deaths)`
- Opening involvement measures how frequently the player is involved in opening fights
- Kill pressure measures kills per round, adjusted by entry weighting

### Operator entry weights

Each attacking operator has an entry weight, so a first blood on a true entry operator matters more than one on a support-style operator.

Example values include:

- `Ash`: `1.0`
- `Deimos`: `1.0`
- `Twitch`: `0.4`
- `Thermite`: `0.1`

## Score Interpretation

Suggested ranges:

- `90–100`: elite entry performance
- `80–89`: extremely strong
- `70–79`: very good
- `60–69`: good entry
- `50–59`: decent / usable
- `40–49`: mixed or role-dependent
- `30–39`: weak entry
- `0–29`: not working

## Notes

This project uses public API data, so the score is only as accurate as the available stats.

Some older seasons may have incomplete opening duel data, and small sample sizes can make results look misleading. The score should be treated as an estimate rather than a perfect measure of skill.

## Disclaimer

This project is unofficial and is not affiliated with Ubisoft, Rainbow Six Siege, or R6Data.