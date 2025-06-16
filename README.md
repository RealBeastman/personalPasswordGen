# Personal Password Generator

> A simple CLI tool for generating secure passwords using Python.

---

## Overview

This is one of my first Python projects, before I even started college. This script is designed to generate random passwords using sample text. It saves generated passwords to a local file and provides basic way to archive account/password pairs.

---

## Usage

`python passGen.py`

You will be prompted to:
- Specify whether you want to create a new password
- Input an account name and username/email
- Automatically generate a secure password using randomized text and numbers

The password will be saved to `passwords.txt` along with the provided account information

---

## Features
- Randomized password creation using sample text + substitutions
- Mixed-case and symbol substitution for complexity
- Appends each credential set to a plaintext file (`passwords.txt`) **Not Secure**
- Automatically craetes and checks required files: `passwords.txt` and `sampleText.txt`

---

## Extra

- If `sampleText.txt` does not exist, it is created and filled with default text.
  - You can replace this with any text of your choosing. (e.g. first chapter of *Moby Dick*)
- If `passwords.txt` not not exist, it is created automatically
- Passwords are written with account and username headers for readability

---

## Status
**Archived:** This is an early utility project and is no longer actively maintained.

---

## License

MIT License
