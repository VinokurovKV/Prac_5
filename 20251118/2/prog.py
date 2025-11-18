import sys

print(sys.stdin.read().encode('latin1', errors='replace').decode('cp1251', errors='replace'))