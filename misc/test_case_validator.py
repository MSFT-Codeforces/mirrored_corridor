
import sys
import re

def invalid():
    sys.stdout.write("False")
    sys.exit(0)

def main():
    data = sys.stdin.read()
    if data == "":
        invalid()

    # Split by lines strictly; reject any empty/blank lines
    lines = data.splitlines()
    if not lines:
        invalid()

    # Strictly: no leading/trailing spaces, no tabs, no multiple spaces
    int_line_re = re.compile(r"^[0-9]+$")
    tc_line_re = re.compile(r"^[0-9]+ [0-9]+ [0-9]+ [0-9]+$")

    # First line: exactly one integer token
    if not int_line_re.match(lines[0]):
        invalid()
    try:
        t = int(lines[0])
    except Exception:
        invalid()
    if not (1 <= t <= 2 * 10**5):
        invalid()

    # Must have exactly t test case lines
    if len(lines) != t + 1:
        invalid()

    LIM = 10**18

    for i in range(1, t + 1):
        line = lines[i]
        if not tc_line_re.match(line):
            invalid()
        try:
            n_s, x_s, y_s, d_s = line.split(" ")
            n = int(n_s)
            x = int(x_s)
            y = int(y_s)
            d = int(d_s)
        except Exception:
            invalid()

        if not (1 <= n <= LIM):
            invalid()
        if not (1 <= d <= LIM):
            invalid()
        if not (1 <= x <= n):
            invalid()
        if not (1 <= y <= n):
            invalid()

        # Structural property: if n == 1, only room 1 exists
        if n == 1 and (x != 1 or y != 1):
            invalid()

    sys.stdout.write("True")

if __name__ == "__main__":
    main()
