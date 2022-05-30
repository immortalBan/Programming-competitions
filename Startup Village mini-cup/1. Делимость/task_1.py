n, X = list(map(int, input().split()))
a = list(map(int, input().split()))

mods = {}

summ = count = 0

for i in range(len(a)):
    summ = (summ + a[i]) % X
    count += mods.get(summ, 0)
    mods[summ] = mods.get(summ, 0) + 1

count += mods.get(0, 0)
print(count)