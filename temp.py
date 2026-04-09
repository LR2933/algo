import sys
from collections import defaultdict
def solve():
    _ = int(sys.stdin.readline())
    data = defaultdict(list)
    lines = sys.stdin.readlines()
    for line in lines:
        a, b = map(int, line.split())
        data[b].append(a)

    count = 0
    tili_sum = 0
    for i in sorted(data): #最多允许消耗的体力
        data[i].sort()
        for j in data[i]: #需要消耗的体力
            if tili_sum <= i:
                tili_sum += j
                count += 1
            else:
                break
         
    print(count)

if __name__ == "__main__":
    solve()

