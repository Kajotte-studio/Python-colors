[![GitHub Sponsors](https://img.shields.io/badge/Sponsor-Kajotte--Studio-ea4aaa?style=for-the-badge&logo=github-sponsors)](https://kajotte-studio.com/support_en.html)
# Kajotte Studio: Terminal Colors

![Python Version](https://img.shields.io/badge/Python-3.6%2B-blue?logo=python&logoColor=white)
![Status](https://img.shields.io/badge/status-stable-brightgreen)
![Release](https://img.shields.io/github/v/release/Kajotte-studio/Python-colors?include_prereleases&label=Release&color=blue)
<img src="https://img.shields.io/badge/License-MIT-black?style=flat-square" alt="MIT License" />

![Dependabot](https://img.shields.io/badge/Dependabot-Active-0250a3?style=flat&logo=dependabot)
![Security Policy](https://img.shields.io/badge/Security-Policy%20Active-success?style=flat&logo=github-security)
[![Python Quality Check](https://github.com/Kajotte-studio/python-colors/actions/workflows/python-app.yml/badge.svg)](https://github.com/Kajotte-studio/python-colors/actions)
![Code Quality](https://github.com/Kajotte-studio/Python-colors/workflows/CodeQL/badge.svg)
![GitHub Actions Quality](https://img.shields.io/github/check-runs/Kajotte-studio/Python-colors/main?style=flat-square&label=quality%20check)


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
pip install git+https://github.com/Kajotte-studio/Python-colors.git
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

### Colors Preview

Instantly visualize the full palette of 32 colors and available formatting styles in your terminal.

```bash
Colors.preview()
```

---

### 📝 Technical Reference

Detailed implementation details and the logic behind this class structure can be found in the technical documentation on the blog:

🔗 **[Internal Reference: index_blog_post_44_en.html](https://kajotte-studio.com/index_blog_post_44_en.html)**

---

## ⚖️ License & Documentation

### License: MIT License.

 * Official Website: [Kajotte-studio.com](https://Kajotte-studio.com)
 * Technical Support: [Kajotte-studio.com/docs](https://Kajotte-studio.com/docs)

## 💡 Philosophy
"Simplicity is the ultimate sophistication."

Following the Kajotte Studio principle, this library provides only what is necessary, ensuring maximum performance and zero overhead for your CLI applications and bots.

---

<div align="center">
  <img src="https://img.shields.io/badge/License-MIT-black?style=flat-square" alt="MIT License" />
  <br />
  <sub>Developed by Kajotte Studio</sub>
</div>
