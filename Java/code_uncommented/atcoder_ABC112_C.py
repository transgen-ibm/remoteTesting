
import sys

def check(n, x, y, h, cx, cy):
    ch = -1
    for i in range(n):
        if h[i] > 0:
            ch = abs(x[i] - cx) + abs(y[i] - cy) + h[i]
            break
    for i in range(n):
        if h[i]!= max(ch - abs(x[i] - cx) - abs(y[i] - cy), 0):
            return -1
    return ch

def main():
    n = int(input())
    x = [0] * n
    y = [0] * n
    h = [0] * n
    for i in range(n):
        x[i], y[i], h[i] = map(int, input().split())
    for i in range(1, 101):
        for j in range(1, 101):
            ch = check(n, x, y, h, i, j)
            if ch > 0:
                print(i, j, ch)

if __name__ == "__main__":
    main()

# 