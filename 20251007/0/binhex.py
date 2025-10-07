for i in range(12, 23 + 1):
    bw, hw = len(bin(23)), len(hex(23))
    print(f"{i:{bw}b} = {i:{hw}x}")
