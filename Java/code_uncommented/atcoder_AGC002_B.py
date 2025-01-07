
import sys

class Box:
    def __init__(self, num, red):
        self.num = num
        self.red = red

    def moveTo(self, other):
        if self.num == 0:
            return
        elif self.num == 1:
            self.num = 0
            other.num += 1
            if self.red:
                other.red = True
            self.red = False
        else:
            self.num -= 1
            other.num += 1
            if self.red:
                other.red = True

N = int(sys.stdin.readline())
M = int(sys.stdin.readline())
B = [Box(1, True)]
for i in range(1, N):
    B.append(Box(1, False))
for i in range(M):
    x, y = map(int, sys.stdin.readline().split())
    B[x-1].moveTo(B[y-1])
counter = 0
for b in B:
    if b.red:
        counter += 1
print(counter)

# 