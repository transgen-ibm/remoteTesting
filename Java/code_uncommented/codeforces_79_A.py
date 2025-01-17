
import sys

def canTake(xNeeded, xAvailable, yNeeded, yAvailable):
    if xNeeded > xAvailable:
        return False
    if yNeeded > yAvailable:
        return False
    return True

def main():
    br = sys.stdin.readline()
    st = br.split()
    x = int(st[0])
    y = int(st[1])
    turn = 0
    while True:
        if turn % 2 == 0:
            if canTake(2, x, 2, y):
                x -= 2
                y -= 2
            elif canTake(1, x, 12, y):
                x -= 1
                y -= 12
            elif canTake(0, x, 22, y):
                y -= 22
            else:
                print("Hanako")
                return
        else:
            if canTake(0, x, 22, y):
                y -= 22
            elif canTake(1, x, 12, y):
                x -= 1
                y -= 12
            elif canTake(2, x, 2, y):
                x -= 2
                y -= 2
            else:
                print("Ciel")
                return
        turn += 1

if __name__ == "__main__":
    main()

