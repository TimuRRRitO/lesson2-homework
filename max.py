length = int(input())
a = [0] * length
for q in range (0, length):
    a[q] = q
max = -100000000000
for i in range (0, len(a)):
    if max < a[i]:
        max = a[i]
print (max)
