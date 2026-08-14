#Intersection → yang sama
n = int(input())
nn = set(map(int, input().split()))
n2 = int(input())
nn2 = set(map(int, input().split()))

data = nn.intersection(nn2) 
print(len(data))