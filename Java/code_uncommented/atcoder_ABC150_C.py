
# <START-OF-CODE>

def permutation(list, target, ans):
    if len(target) <= 1:
        list.append(ans + target)
    else:
        for i in range(len(target)):
            permutation(list, target[:i] + target[i+1:], ans + target[i])
    return list

def main():
    n = int(input())
    line = [input().split() for _ in range(2)]
    number = ""
    for i in range(1, n+1):
        number += str(i)
    listA = []
    permutation(listA, number, "")
    sum = 0
    for j in range(len(line)):
        for i in range(len(listA)):
            if listA[i] == line[j][0]:
                if sum == 0:
                    sum += i
                else:
                    sum -= i
    print(abs(sum))

if __name__ == "__main__":
    main()

# 