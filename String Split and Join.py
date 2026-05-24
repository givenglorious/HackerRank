def split_and_join(line):
    a = line 
    a = a.split(" ")
    for ass in a:
         ass = "-".join(a)
    print(ass)

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
  
