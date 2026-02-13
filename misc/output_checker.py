
import os
import re
from typing import Tuple, List

_INT_RE = re.compile(r"-?\d+\Z")


def _normalize_newlines(s: str) -> str:
    # Accept Windows newlines by normalizing to '\n'
    return s.replace("\r\n", "\n").replace("\r", "\n")


def _parse_input_ints(input_text: str) -> List[int]:
    toks = input_text.split()
    if not toks:
        raise ValueError("Input is empty")
    ints: List[int] = []
    for i, tok in enumerate(toks, 1):
        if not _INT_RE.match(tok):
            raise ValueError(f"Input token {i} is not a valid integer: {tok!r}")
        try:
            ints.append(int(tok))
        except Exception:
            raise ValueError(f"Input token {i} cannot be parsed as int: {tok!r}")
    return ints


def _strip_single_trailing_newline_strict(s: str) -> str:
    """
    Allow at most one trailing '\n'. Forbid other trailing whitespace.
    """
    if s.endswith("\n"):
        s2 = s[:-1]
        if s2.endswith("\n"):
            # This implies an extra blank line at EOF (or more than one trailing newline)
            raise ValueError("Output has more than one trailing newline (extra blank line at EOF)")
        return s2
    return s


def check(input_text: str, output_text: str) -> Tuple[bool, str]:
    try:
        input_text_nl = _normalize_newlines(input_text)
        output_text_nl = _normalize_newlines(output_text)

        data = _parse_input_ints(input_text_nl)
        t = data[0]
        if not (1 <= t <= 2 * 10**5):
            return (False, f"Input: t={t} is out of range [1..200000]")

        expected_ints = 1 + 4 * t
        if len(data) != expected_ints:
            return (
                False,
                f"Input: expected exactly {expected_ints} integers (1 + 4*t), got {len(data)}",
            )

        cases = []
        idx = 1
        for ci in range(1, t + 1):
            n, x, y, d = data[idx], data[idx + 1], data[idx + 2], data[idx + 3]
            idx += 4
            # Validate input constraints
            if not (1 <= n <= 10**18):
                return (False, f"Input case {ci}: n={n} out of range [1..1e18]")
            if not (1 <= d <= 10**18):
                return (False, f"Input case {ci}: d={d} out of range [1..1e18]")
            if not (1 <= x <= n):
                return (False, f"Input case {ci}: x={x} out of range [1..n={n}]")
            if not (1 <= y <= n):
                return (False, f"Input case {ci}: y={y} out of range [1..n={n}]")
            cases.append((n, x, y, d))

        # Strict output whitespace handling
        try:
            out_core = _strip_single_trailing_newline_strict(output_text_nl)
        except ValueError as e:
            return (False, str(e))

        if out_core == "":
            return (False, f"Output: expected {t} lines, got 0 (empty output)")

        # Forbid any leading/trailing whitespace other than the allowed single trailing newline.
        # In particular, forbid trailing spaces/tabs at EOF.
        if out_core and out_core[-1].isspace():
            return (False, "Output: trailing whitespace at EOF is not allowed (only optional single trailing newline)")

        lines = out_core.split("\n")
        if len(lines) != t:
            return (False, f"Output: expected exactly {t} lines, got {len(lines)}")

        for ci, line in enumerate(lines, 1):
            if line == "":
                return (False, f"Case {ci}: empty line; expected one integer")
            if line.strip() != line:
                return (False, f"Case {ci}: leading/trailing spaces are not allowed: {line!r}")
            # Forbid internal whitespace too (must be a single token)
            if any(ch.isspace() for ch in line):
                return (False, f"Case {ci}: whitespace within the line is not allowed: {line!r}")
            if not _INT_RE.match(line):
                return (False, f"Case {ci}: expected an integer, got {line!r}")

            ans = int(line)
            if ans != -1 and ans < 0:
                return (False, f"Case {ci}: answer must be -1 or a nonnegative integer, got {ans}")

            n, x, y, d = cases[ci - 1]

            # Trivially checkable correctness conditions (do not require solving):
            # - If x == y, minimum presses is 0.
            # - If answer is 0, necessarily x == y (since no button presses changes nothing).
            if x == y:
                if ans != 0:
                    return (False, f"Case {ci}: x == y, so the minimum number of presses is 0, got {ans}")
            else:
                if ans == 0:
                    return (False, f"Case {ci}: x != y, so 0 presses cannot reach y; got 0")

            # For n == 1, x and y must be 1; minimum is 0 (covered by x==y check),
            # but keep an explicit message if violated.
            if n == 1 and ans != 0:
                return (False, f"Case {ci}: n == 1 implies answer must be 0, got {ans}")

        return (True, "OK")

    except ValueError as e:
        return (False, str(e))
    except Exception as e:
        return (False, f"Checker error: {type(e).__name__}: {e}")


if __name__ == "__main__":
    in_path = os.environ.get("INPUT_PATH")
    out_path = os.environ.get("OUTPUT_PATH")
    if not in_path or not out_path:
        print("False")
    else:
        with open(in_path, "r", encoding="utf-8") as f:
            input_text = f.read()
        with open(out_path, "r", encoding="utf-8") as f:
            output_text = f.read()
        ok, _ = check(input_text, output_text)
        print("True" if ok else "False")
