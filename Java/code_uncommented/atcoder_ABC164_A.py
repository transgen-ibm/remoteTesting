
# <START-OF-CODE>
import sys

def main():
    scList = []
    while True:
        try:
            scList.append(input())
        except:
            break
    numlist = scList[0].split()
    Sheep = int(numlist[0])
    Wolve = int(numlist[1])
    if Wolve >= Sheep:
        print("unsafe")
    else:
        print("safe")

if __name__ == "__main__":
    main()
# 