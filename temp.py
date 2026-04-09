def solve():
    for i in range(ord('a'), ord('z') + 1):
        print(f"'{chr(i)}':{i - 96}, ", end= '')

if __name__ == "__main__":
    solve()

