# Enter your code here. Read input from STDIN. Print output to STDOUT
k = int(input())
rooms = list(map(int, input().split()))

for room in rooms:
    if rooms.count(room) == 1:
        print(room)
        break
   