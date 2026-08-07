if __name__ == '__main__':
    N = int(input())
    lst = []
    
    for _ in range(N):
        inpt = input().split()
        
        if inpt[0] == "insert":
            lst.insert(int(inpt[1]), int(inpt[2]))
            
        elif  inpt[0] == "print":
            print(lst)
            
        elif inpt[0] == "remove":
            lst.remove(inpt[1])
            
        elif inpt[0] == "append":
            lst.append(inpt[1])   
                 
        elif inpt[0] == "sort":
            lst.sort()
        
        elif inpt[0] == "pop":
            lst.pop()
        elif inpt[0] == "reverse":
            lst.reverse()
            
    
