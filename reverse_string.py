#!/usr/bin/env python3
"""
Simple utility to reverse strings.

Usage:
  python reverse_string.py "hello world"
  echo "hello" | python reverse_string.py

This script defines `reverse_string()` and a small CLI.
"""
import sys

def reverse_string(s: str) -> str:
    """Return the reverse of the input string."""
    return s[::-1]

def main() -> None:
    if len(sys.argv) > 1:
        # Join all args so users can pass multi-word strings without quotes
        s = " ".join(sys.argv[1:])
    else:
        # Read from stdin (echo "text" | python reverse_string.py)
        s = sys.stdin.read()
        if not s:
            return
        s = s.rstrip("\n")
    print(reverse_string(s))

if __name__ == "__main__":
    main()
