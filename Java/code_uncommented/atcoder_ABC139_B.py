import sys

def main():
    A = int(sys.stdin.readline())
    B = int(sys.stdin.readline())
    amari = 0
    result = 0
    result = (B - 1) / (A - 1)
    amari = (B - 1) % (A - 1)
    if amari!= 0:
        result += 1
    print(result)

if __name__ == "__main__":
    main()
