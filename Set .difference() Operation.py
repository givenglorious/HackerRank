#Difference → yang hanya ada di A
n = int(input())
nn = set(map(int, input().split()))
n2 = int(input())
nn2 = set(map(int, input().split()))

data = nn.difference(nn2) 
print(len(data))