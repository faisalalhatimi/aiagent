# Ai Agent 

This is a simple ai agent made using Python.

## About

This project is a part of a backend course on [boot.dev](https://www.boot.dev/). 

> [!Warning]
> This tool is not designed to run in a production environment. It's a proof-of-concept and watered down version of what a real coding agent does. Run at your own risk.

## Requirements

- uv
- Python 3.14+
- dotenv

## Installation

- Set up your API key in `.env`.
- Run the following:
```
uv sync
```

## Usage

- `uv run main.py <prompt>`
- `--verbose` displays prompt metadata (e.g. prompt tokens)
