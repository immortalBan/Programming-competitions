n = int(input())

for _ in range(n):
    _ = int(input())
    s = input()
    t = input()
    if str(sorted(s)) < str(sorted(t, reverse=True)):
        print("Yes")
    else:
        print("No")