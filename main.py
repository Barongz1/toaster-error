"""The Funniest Toaster Error Message — entry for make.fun.

Writes one line to /output/entry.txt.
The line is the funniest error message a kitchen toaster would show, at most 120 characters.
"""
import os

LINE = "ERROR 404: Bread not found. It was here a minute ago. I have no idea what happened either."

def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE + "\n")

if __name__ == "__main__":
    main()
