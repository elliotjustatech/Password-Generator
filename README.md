# Password Generator

A simple, secure command-line password generator written in Python. Lets you choose the length and character types, generates a cryptographically secure password, and copies it straight to your clipboard.

## Features

- 🔢 Custom password length (1–20 characters)
- 🔠 Optional uppercase letters
- 🔢 Optional digits
- ✨ Optional special characters
- 🔐 Uses Python's `secrets` module — cryptographically secure, not `random`
- 📋 Automatically copies the generated password to your clipboard
- 🛡️ Input validation with clear error messages for invalid entries
- ⌨️ Graceful exit on `Ctrl+C`

## Why `secrets` instead of `random`?

Python's built-in `random` module is predictable and unsuitable for anything security-related — it's designed for simulations and games, not secrets. This generator uses the `secrets` module instead, which is built specifically for generating cryptographically strong random values like passwords, tokens, and keys.

## Installation

```bash
git clone https://github.com/elliotjustatech/password-generator.git
cd password-generator
pip install pyperclip
```

### Requirements

- Python 3.6+
- `pyperclip` (the `string` and `secrets` modules are part of the Python standard library, no install needed)

## Usage

```bash
python password.py
```

The script will then walk you through a few questions:

```

Какая нужна длина пароля?(От 1 до 20): 16
Нужны заглавные буквы?(y/n): y
Нужны ли цифры?(y/n): y
Нужны ли символы?(y/n): y

Пароль: [сгенерированный пароль]
Ваш пароль скопирован в буфер обмена.
```

Your password is generated and automatically copied to the clipboard — just hit paste wherever you need it.

## Notes

- Password length is capped at 20 characters by design; feel free to adjust the limit in the code if you need longer passwords.
- If no character type is selected beyond the default, the password is generated from lowercase letters only.
- Clipboard copying relies on `pyperclip`, which needs a working clipboard on your system (works out of the box on Windows/macOS/most Linux desktop environments).

## Disclaimer

This tool is provided as-is, for personal and educational use, with no warranty of any kind. While it uses a cryptographically secure random source, the overall security of any password also depends on how and where you store and use it. The author is not responsible for any loss, breach, or damage resulting from the use of generated passwords.
