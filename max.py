length = int(input())
a = [0] * length
for q in range (0, length):
    a[q] = int (input())
min = 100000000000
for i in range (0, len(a)):
    if min > a[i]:
        min = a[i]
print (min)
