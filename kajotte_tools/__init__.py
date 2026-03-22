# LEGAL & TECHNICAL DOCUMENTATION: https://kajotte-studio.com/docs
"""
Module: All Colors & Backgrounds
Purpose: Explore practical examples of ANSI color encapsulation
License: MIT
Author: Kajotte Studio (kajotte-studio.com)
"""
import os

# Terminal color initialization (essential for Windows systems)
os.system('echo.') # nosec

class Colors:
    # Reset all formatting
    RESET = '\033[0m'
    
    # Text colors (Standard: 30-37)
    BLACK   = '\033[30m'
    RED     = '\033[31m'
    GREEN   = '\033[32m'
    YELLOW  = '\033[33m'
    BLUE    = '\033[34m'
    MAGENTA = '\033[35m'
    CYAN    = '\033[36m'
    WHITE   = '\033[37m'
    
    # Text colors (Bright: 90-97)
    BR_BLACK   = '\033[90m'
    BR_RED     = '\033[91m'
    BR_GREEN   = '\033[92m'
    BR_YELLOW  = '\033[93m'
    BR_BLUE    = '\033[94m'
    BR_MAGENTA = '\033[95m'
    BR_CYAN    = '\033[96m'
    BR_WHITE   = '\033[97m'
    
    # Background colors (Standard: 40-47)
    BG_BLACK   = '\033[40m'
    BG_RED     = '\033[41m'
    BG_GREEN   = '\033[42m'
    BG_YELLOW  = '\033[43m'
    BG_BLUE    = '\033[44m'
    BG_MAGENTA = '\033[45m'
    BG_CYAN    = '\033[46m'
    BG_WHITE   = '\033[47m'
    
    # Background colors (Bright: 100-107)
    BG_BR_BLACK   = '\033[100m'
    BG_BR_RED     = '\033[101m'
    BG_BR_GREEN   = '\033[102m'
    BG_BR_YELLOW  = '\033[103m'
    BG_BR_BLUE    = '\033[104m'
    BG_BR_MAGENTA = '\033[105m'
    BG_BR_CYAN    = '\033[106m'
    BG_BR_WHITE   = '\033[107m'

def preview():
    print(f"{Colors.BLACK}Colors.BLACK{Colors.RESET}")
    print(f"{Colors.RED}Colors.RED{Colors.RESET}")
    print(f"{Colors.GREEN}Colors.GREEN{Colors.RESET}")
    print(f"{Colors.YELLOW}Colors.YELLOW{Colors.RESET}")
    print(f"{Colors.BLUE}Colors.BLUE{Colors.RESET}")
    print(f"{Colors.MAGENTA}Colors.MAGENTA{Colors.RESET}")
    print(f"{Colors.CYAN}Colors.CYAN{Colors.RESET}")
    print(f"{Colors.WHITE}Colors.WHITE){Colors.RESET}")

    print(f"{Colors.BR_BLACK}Colors.BR_BLACK{Colors.RESET}")
    print(f"{Colors.BR_RED}Colors.BR_RED{Colors.RESET}")
    print(f"{Colors.BR_GREEN}Colors.BR_GREEN{Colors.RESET}")
    print(f"{Colors.BR_YELLOW}Colors.BR_YELLOW{Colors.RESET}")
    print(f"{Colors.BR_BLUE}Colors.BR_BLUE{Colors.RESET}")
    print(f"{Colors.BR_MAGENTA}Colors.BR_MAGENTA{Colors.RESET}")
    print(f"{Colors.BR_CYAN}Colors.BR_CYAN{Colors.RESET}")
    print(f"{Colors.BR_WHITE}Colors.BR_WHITE){Colors.RESET}")

    print(f"{Colors.BG_BLACK}Colors.BG_BLACK{Colors.RESET}")
    print(f"{Colors.BG_RED}Colors.BG_RED{Colors.RESET}")
    print(f"{Colors.BG_GREEN}Colors.BG_GREEN{Colors.RESET}")
    print(f"{Colors.BG_YELLOW}Colors.BG_YELLOW{Colors.RESET}")
    print(f"{Colors.BG_BLUE}Colors.BG_BLUE{Colors.RESET}")
    print(f"{Colors.BG_MAGENTA}Colors.BG_MAGENTA{Colors.RESET}")
    print(f"{Colors.BG_CYAN}Colors.BG_CYAN{Colors.RESET}")
    print(f"{Colors.BG_WHITE}Colors.BG_WHITE){Colors.RESET}")

    print(f"{Colors.BG_BR_BLACK}Colors.BG_BR_BLACK{Colors.RESET}")
    print(f"{Colors.BG_BR_RED}Colors.BG_BR_RED{Colors.RESET}")
    print(f"{Colors.BG_BR_GREEN}Colors.BG_BR_GREEN{Colors.RESET}")
    print(f"{Colors.BG_BR_YELLOW}Colors.BG_BR_YELLOW{Colors.RESET}")
    print(f"{Colors.BG_BR_BLUE}Colors.BG_BR_BLUE{Colors.RESET}")
    print(f"{Colors.BG_BR_MAGENTA}Colors.BG_BR_MAGENTA{Colors.RESET}")
    print(f"{Colors.BG_BR_CYAN}Colors.BG_BR_CYAN{Colors.RESET}")
    print(f"{Colors.BG_BR_WHITE}Colors.BG_BR_WHITE){Colors.RESET}")

if __name__ == "__main__":
    print(f"{Colors.BG_BR_RED}{Colors.WHITE} PALETTE TEST {Colors.RESET}")
    print(f"{Colors.GREEN}Standard Green (32){Colors.RESET}")
    print(f"{Colors.BR_BLUE}Bright Blue (94){Colors.RESET}")
    print(f"{Colors.BG_YELLOW}{Colors.BLACK} Yellow Background (43) {Colors.RESET}")