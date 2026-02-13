
def main():
    # 15 small, diverse inputs. Each "Input i" is a full valid run (t + test lines).
    cases = []

    # 1) n=1 degenerate corridor (always room 1)
    cases.append("1\n1 1 1 7")

    # 2) n=2 (no real reflection), simple reachable
    cases.append("1\n2 1 2 1")

    # 3) n=3, gcd-based impossibility (cannot reach room 2 from room 1 with d=2)
    cases.append("1\n3 1 2 2")

    # 4) n=3, simple reachable with d=1
    cases.append("1\n3 3 1 1")

    # 5) Only the mirrored residue of y is reachable (n=5, d=4)
    cases.append("1\n5 4 2 4")

    # 6) d % L == 0 => residue frozen, x != y => impossible
    cases.append("1\n5 2 5 8")

    # 7) Optimal uses Shift− (negative direction) to reach endpoint (unique residue)
    cases.append("1\n6 2 6 3")

    # 8) Off-by-one trap: reaching r == N must map to room n (uses r <= N)
    cases.append("1\n4 1 4 1")

    # 9) Middle room unreachable due to gcd(d, L) divisibility
    cases.append("1\n6 1 2 4")

    # 10) d > L, only one of y's residues reachable; minimal uses Shift− once
    cases.append("1\n7 2 6 20")

    # 11) gcd(d, L) > 1 but reachable (alternates between two residues)
    cases.append("1\n7 3 5 6")

    # 12) Very large gcd relative to L (d = L/2), only endpoints reachable
    cases.append("1\n8 1 8 7")

    # 13) d = N for odd n (half-cycle), reflection effect visible in 1 step
    cases.append("1\n9 2 8 8")

    # 14) Explicit min(t, M-t) case for endpoint target (negative direction smaller)
    cases.append("1\n10 2 10 5")

    # 15) x == y for n > 1 should always be 0 presses
    cases.append("1\n5 3 3 3")

    print("**Test Cases: **")
    for i, inp in enumerate(cases, 1):
        print(f"Input {i}:")
        print(inp)
        if i != len(cases):
            print()

if __name__ == "__main__":
    main()
