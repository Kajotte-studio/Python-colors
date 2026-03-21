[![GitHub Sponsors](https://img.shields.io/badge/Sponsor-Kajotte--Studio-ea4aaa?style=for-the-badge&logo=github-sponsors)](https://kajotte-studio.com/support_en.html)
# Kajotte Studio: Terminal Colors

![Python Version](https://img.shields.io/badge/python-3.6%2B-blue)
![License](https://img.shields.io/badge/license-MIT-green)
![Status](https://img.shields.io/badge/status-stable-brightgreen)

A professional, zero-dependency ANSI color encapsulation library for Python. Designed by **Kajotte Studio** for developers who value clean code and terminal aesthetics.

---

## 🚀 Overview

This package provides a complete set of ANSI escape sequences for terminal text styling. It includes standard and bright variants for both foreground and background colors.

### Key Features:
* **Zero Dependencies**: Pure Python, no external bloat.
* **Full Palette**: 16 text colors and 16 background colors.
* **Minimalist API**: Simple class-based access to ANSI codes.
* **Cross-Platform**: Initialized for modern terminal emulators.

---

## 📦 Installation

Install the package via pip:

```bash
pip install kajotte-tools
```

### 🛠 Usage
Simply import the Colors class and use f-strings to style your output.
```bash
from kajotte_tools import Colors
```

### Foreground colors
```bash
print(f"{Colors.GREEN}Success:{Colors.RESET} Operation completed.")
print(f"{Colors.BR_CYAN}Notice:{Colors.RESET} System update available.")
```

### Background colors
```bash
print(f"{Colors.BG_RED}{Colors.WHITE} CRITICAL ERROR {Colors.RESET}")
print(f"{Colors.BG_BR_YELLOW}{Colors.BLACK} WARNING {Colors.RESET} Check logs.")
```

### Alternative
```bash
import kajotte_tools as kt
```
```bash
print(kt.Colors.GREEN + "Clean code!" + kt.Colors.RESET)
```

## ⚖️ License & Documentation

### License: MIT License.

 * Official Website: [Kajotte-studio.com](https://Kajotte-studio.com)
 * Technical Support: [Kajotte-studio.com/docs](https://Kajotte-studio.com/docs)

## 💡 Philosophy
"Simplicity is the ultimate sophistication."

Following the Kajotte Studio principle, this library provides only what is necessary, ensuring maximum performance and zero overhead for your CLI applications and bots.

<div align="center">
  <img src="https://img.shields.io/badge/License-MIT-black?style=flat-square" alt="MIT License" />
  <br />
  <sub>Developed by Kajotte Studio</sub>
</div>
