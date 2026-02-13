
import sys

write = sys.stdout.write

def emit_input(cases):
    # cases: list of (n,x,y,d)
    s = [str(len(cases)), "\n"]
    s.extend(" ".join(map(str, c)) + "\n" for c in cases)
    return "".join(s)

write("**Test Cases: **\n")

# Input 1: n=1 special-case, but with huge d values
cases1 = [
    (1, 1, 1, 1),
    (1, 1, 1, 10**18),
    (1, 1, 1, 10**18 - 1),
]
write("Input 1:\n")
write(emit_input(cases1))
write("\n")

# Input 2: n=2, includes "frozen residue" with d%L==0 and a reachable case
cases2 = [
    (2, 1, 2, 2),  # L=2, d%L==0 => cannot change shown room
    (2, 1, 2, 1),  # reachable
    (2, 2, 1, 2),  # also frozen (stuck at room 2)
]
write("Input 2:\n")
write(emit_input(cases2))
write("\n")

# Input 3: n very large, d = N (n-1) gives gcd=N with L=2N; endpoints reachable in 1 press
n3 = 10**18
N3 = n3 - 1
cases3 = [
    (n3, 1, n3, N3),
    (n3, n3, 1, N3),
]
write("Input 3:\n")
write(emit_input(cases3))
write("\n")

# Input 4: large n with L exactly 1e18, and d=L => d%L==0 freezes the residue
n4 = 500_000_000_000_000_001  # N=5e17, L=1e18
cases4 = [
    (n4, 2, 3, 10**18),
]
write("Input 4:\n")
write(emit_input(cases4))
write("\n")

# Input 5: only the mirrored residue is reachable (tests "check both residues for middle rooms")
n5 = 999_999_999_999_999_996  # N=1e18-5 divisible by 5 => L divisible by 10
cases5 = [
    (n5, 2, 10, 10),
]
write("Input 5:\n")
write(emit_input(cases5))
write("\n")

# Input 6: both residues unreachable (gcd divisibility fails for both)
cases6 = [
    (n5, 2, 3, 10),
]
write("Input 6:\n")
write(emit_input(cases6))
write("\n")

# Input 7: minimal presses uses the negative direction (min(t0, M-t0))
cases7 = [
    (10**18, 3, 2, 1),
]
write("Input 7:\n")
write(emit_input(cases7))
write("\n")

# Input 8: endpoint uniqueness + gcd parity restriction (room 1 needs residue 0)
cases8 = [
    (10**18, 2, 1, 2),
]
write("Input 8:\n")
write(emit_input(cases8))
write("\n")

# Input 9: d much larger than L + mix of d=L (freeze), d=L+1, etc.
n9 = 200_000_000_000_000_001
N9 = n9 - 1
L9 = 2 * N9  # 400000000000000000
cases9 = [
    (n9, 123_456_789_012_345_678, 98_765_432_109_876_543, 10**18),
    (n9, 2, 3, L9 + 1),
    (n9, n9, 1, L9),
    (n9, 2, n9, L9),
]
write("Input 9:\n")
write(emit_input(cases9))
write("\n")

# Input 10: stress with very large t (2e5), large n, mixed d patterns
# Use n = 2^59 + 1 so L = 2^60 (pure power of 2), making gcd behavior predictable.
t10 = 200_000
N10 = 2**59
n10 = N10 + 1
d_odd = 10**18 - 1  # odd => gcd(d, L)=1 when L is power of two
d_big_even = 2**59  # gcd(d, L)=2^59 (very restrictive), also large
d_med_even = 2**58  # gcd(d, L)=2^58

write("Input 10:\n")
write(str(t10) + "\n")
chunk = []
CHUNK_SIZE = 5000

for i in range(t10):
    m = i % 10000
    if m == 0:
        x, y, d = 1, n10, d_odd
    elif m == 1:
        x, y, d = n10, 1, d_odd
    elif m == 2:
        v = (i * 1234567) % n10 + 1
        x, y, d = v, v, d_odd
    elif m == 3:
        x, y, d = 2, 3, d_big_even
    elif m == 4:
        x, y, d = 3, 2, d_med_even
    else:
        x = (i * 1234567) % n10 + 1
        y = (i * 7654321) % n10 + 1
        d = d_odd

    chunk.append(f"{n10} {x} {y} {d}\n")
    if len(chunk) >= CHUNK_SIZE:
        write("".join(chunk))
        chunk.clear()

if chunk:
    write("".join(chunk))

write("\n")
