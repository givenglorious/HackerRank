# Enter your code here. Read input from STDIN. Print output to STDOUT
no = int(input())
row = set((map(int, input().split())))
no2 = int(input())
row2 = set((map(int, input().split())))


z = row.intersection(row2) 
print(len(z))



# Trial and error moment
# no = int(input())
# row = set((map(int, input().split())))
# no2 = int(input())
# row2 = set((map(int, input().split())))

# if no == len(row): 👎
#     z = row.union(row2) 
#     print(len(z))

#In this case we don't need to check `no == len(row)` in this case because
# the input already guarantees that the number of roll numbers