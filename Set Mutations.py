# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
inpt = set(map(int, input().split()))
row = int(input())
data = set(inpt)

#Notes : Literasi
for _ in range(row):
    command = input().split()

    if command[0] == "intersection_update":
            inpts = set(map(int, input().split()))
            data.intersection_update(inpts) 
                 
    elif command[0] == "update":
            inpts = set(map(int, input().split()))
            data.update(inpts)
        
    elif command[0] == "symmetric_difference_update":
            inpts = set(map(int, input().split()))
            data.symmetric_difference_update(inpts)
            
    elif command[0] == "difference_update":
            inpts = set(map(int, input().split()))
            data.difference_update(inpts)
            
print(sum(data))
            
    
