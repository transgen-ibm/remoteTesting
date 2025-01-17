
# FastReader class to handle fast input
class FastReader:
    def __init__(self):
        self.val = input()
        self.pos = 0

    def next(self):
        self.pos += 1
        if self.pos > len(self.val):
            self.pos = 0
            self.val = input()
        return self.val[self.pos - 1]

    def nextInt(self):
        return int(self.next())

    def nextLong(self):
        return int(self.next())

    def nextDouble(self):
        return float(self.next())

    def nextLine(self):
        return self.val

# Method to compute (x^y) % mod using modular exponentiation
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

# Pair class to hold two related values
class pair:
    def __init__(self, first, second):
        self.first = first
        self.second = second

# Main method to execute the program
def main():
    in = FastReader()
    a = [0] * 4
    for i in range(4):
        a[i] = in.nextLong()
    print(max(a[0] * a[2], max(a[1] * a[3], max(a[0] * a[3], a[1] * a[2]))))

if __name__ == '__main__':
    main()

