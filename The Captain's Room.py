from collections import Counter #??????????????????? 

k = int(input())
rooms = list(map(int, input().split()))

count = Counter(rooms)

for room in count:
    if count[room] == 1:
        print(room)
        break