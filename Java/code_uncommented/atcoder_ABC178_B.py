
# <START-OF-CODE>

import sys

class FastReader:
    def __init__(self):
        self.buf = sys.stdin.buffer
        self.lines = self.buf.readlines

    def readline(self):
        return self.lines().decode('ascii').strip()

    def read(self):
        return self.buf.read().decode('ascii').strip()

    def nextInt(self):
        return int(self.read())

    def nextLong(self):
        return int(self.read())

    def nextDouble(self):
        return float(self.read())

def modPower(x, y, mod):
    res = 1
    x %= mod
    if x == 0:
        return 0
    while y > 0:
        if y % 2 == 1:
            res = (res * x) % mod
        y = y >> 1
        x = (x * x) % mod
    return res

class pair:
    def __init__(self, first, second):
        self.first = first
        self.second = second

def main():
    in_ = FastReader()
    a = [0] * 4
    for i in range(4):
        a[i] = in_.nextLong()
    print(max(a[0] * a[2], max(a[1] * a[3], max(a[0] * a[3], a[1] * a[2]))))

if __name__ == '__main__':
    main()

# 