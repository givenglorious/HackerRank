import numpy

n, m = map(int, input().split())
data = []

for _ in range(n):
    row = list(map(int, input().split()))
    data.append(row)
arr = numpy.array(data)

print(numpy.transpose(arr))
print(arr.flatten())