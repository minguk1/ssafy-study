def twojinsu(n):
    x = int(n, 16)
    l = 4 * len(n)

    bin = ""
    result = ""

    for i in range(l -1, -1, -1):
        bin += "1" if x & (1<<i) else "0"

    return bin

print(twojinsu("328D1AF6E4C9BB"))