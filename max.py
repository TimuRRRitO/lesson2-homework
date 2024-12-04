a = [7, 5, 9, -9, 0]
max = -100000000000
for i in range (0, len(a)):
    if max < a[i]:
        max = a[i]
print (max)
