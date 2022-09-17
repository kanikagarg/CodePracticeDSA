# b contains list of bits count for finding bytes max value 
b = [8, 16, 24, 32]
for item in b:
    bits = item
    # bits = len(item)
    val = 0
    for bit in range(0,bits):
        val += pow(2,bit)
    print(f"value for {bits} bits or {int(bits/8)} bytes is  {val} unsigned integer or range [-{ int(val/2) +1} to { int(val/2)} ] for signed")
