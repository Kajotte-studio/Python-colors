# Security Policy

## Supported Versions
We take the security of our tools seriously. Currently, only the latest stable version of this package is supported with security updates.

| Version | Supported          |
| ------- | ------------------ |
| 1.0.x   | :white_check_mark: |
| < 1.0   | :x:                |

---

## Reporting a Vulnerability
If you discover a security vulnerability, please do not open a public issue. Disclosure of vulnerabilities should be handled discreetly to protect users.

Please report any security-related concerns via:
* **Email**: security@kajotte-studio.com
* **Official Website**: [kajotte-studio.com](https://kajotte-studio.com)

### Our Commitment:
1. **Acknowledgement**: We will acknowledge receipt of your report within 48 hours.
2. **Investigation**: We will provide a status update and estimated timeline for a fix.
3. **Resolution**: Once a fix is verified, a new version will be released immediately.

---

## General Security Principles
This library is designed with a **zero-trust and minimalist approach**:
* **No Network Access**: The library never attempts to connect to the internet.
* **No File System Access**: It does not read or write to your local storage.
* **No Dependencies**: By avoiding external libraries, we minimize the attack surface for supply chain vulnerabilities.

---
**Developed by [Kajotte Studio](https://kajotte-studio.com)**
