n = int(input())
inpt = set(map(int, input().split()))
row = int(input())
data = set(inpt)


for _ in range(row):
    command = input().split()

    if command[0] == "remove":
            data.remove(int(command)) 
                 
    elif command[0] == "discard":
            data.discard(int(command))
        
    elif command[0] == "pop":
            data.pop()
            
print(sum(data))
            
    
