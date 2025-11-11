# AI Coding Agent Instructions - My-Python-Project

## Project Overview
A collection of three utility scripts for common automation tasks. Each script is **independently functional** - no shared modules or cross-dependencies exist. Each file operates as a standalone tool with user input/output via CLI.

- **Instagram Bot.py** - Currently empty; placeholder for Instagram automation
- **Check validate E-mail Address.py** - Email validation utility using regex
- **QR Code Generator.py** - URL-to-QR code conversion tool

## Code Organization & Patterns

### Validation Pattern (Check validate E-mail Address.py)
- Uses **regex pattern matching** for user input validation
- Pattern: `r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'`
- Returns user-friendly boolean strings ("Yes!" / "Sorry...")
- Input via `input()`, output via `print()`

### External Dependencies
- **qrcode** - Used in QR Code Generator.py for QR generation
- **re** - Standard library regex for email validation
- No external framework dependencies; pure Python

### CLI Design Pattern
All scripts follow a simple pattern:
1. Accept user input via `input()` prompt
2. Process data through utility function
3. Output result or save file (QR generator saves PNG)
4. No error handling - scripts assume valid input

## Key Conventions

### Naming & Comments
- File names use spaces (not underscores): `Instagram Bot.py`
- Comment style is casual and descriptive: `# link convert to qr code`
- Inline explanations for parameter values: `version=1, # Size if the QR code`

### QR Code Generation (QR Code Generator.py)
- Uses `qrcode.QRCode()` with specific parameters:
  - `version=1` - Smallest size
  - `error_correction=ERROR_CORRECT_H` - High error correction
  - `box_size=10`, `border=4` - Visual sizing
- Output filename: `"Scan the QR Code please!.png"`
- Always black/white color scheme

## When Extending This Codebase

1. **New utilities** - Follow the standalone script model (no shared utils module)
2. **Error handling** - Currently minimal; add input validation for new features
3. **User prompts** - Keep simple input()/print() pattern for CLI
4. **Dependencies** - List in comments or requirements.txt if adding packages
5. **QR generation** - Reference existing `qrcode` implementation as template
