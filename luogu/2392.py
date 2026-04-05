import sys

def solve():
    input_data = iter(sys.stdin.read().split())
    s = []
    for _ in range(4):
        s.append(int(next(input_data)))

    ans = 0

    for n in s:
        times = []
        for _ in range(n):
            times.append(int(next(input_data)))

        current_min_time = float('inf')

        def dfs(idx, left, right):
            nonlocal current_min_time
            if current_min_time <= max(left, right):
                return
            if idx == n:
                current_min_time = max(left, right)
                return

            dfs(idx + 1, left + times[idx], right)
            dfs(idx + 1, left, right + times[idx])

        dfs(0, 0, 0)
        ans += current_min_time



    print(ans)

if __name__ == "__main__":
    solve()

