n = input()
half = len(n) // 2
if len(n) % 2 == 0:
    first = int(n[:half]+n[:half][::-1])
    second = str(int(n[:half])+1)
    second = int(second + second[::-1])
else:
    first = int(n[:half+1]+n[:half][::-1])
    second = int(str(int(n[:half+1])+1)+n[:half][::-1])
l = sorted([first, second, int(n)])
i = l.index(int(n))
print(l[i+1]-l[i])