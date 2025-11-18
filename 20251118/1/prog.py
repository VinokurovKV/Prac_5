import sys

first = sys.stdin.buffer.read(1)
N = first[0]
tail = sys.stdin.buffer.read()
L = len(tail)
parts = []
for i in range(N):
    start = i * L // N
    end = (i + 1) * L // N
    part = tail[start:end]
    parts.append(part)
parts.sort()
result = first + b''.join(parts)
sys.stdout.buffer.write(result)