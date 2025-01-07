
# <START-OF-CODE>
import sys

def main():
    n = int(sys.stdin.readline())
    vec = []
    for i in range(n):
        vec.append(list(map(int, sys.stdin.readline().split())))

    ans = 500
    ansprice = 20000
    for i in range(n):
        fl = 1
        for j in range(n):
            if vec[i][0] < vec[j][0] and vec[i][1] < vec[j][1] and vec[i][2] < vec[j][2]:
                fl = 0
        if fl == 1:
            if vec[i][3] < ansprice:
                ansprice = vec[i][3]
                ans = i + 1

    print(ans)

if __name__ == '__main__':
    main()
# 