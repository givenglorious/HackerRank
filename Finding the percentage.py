if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, line , *rest = input().split()
        convert = line,*rest
        scores = list(map(float, convert))
        student_marks[name] = scores
 
  
    query_name = input()
    if query_name in student_marks:
        scores = student_marks[query_name]
        average = sum(scores) / len(scores)
        print(f"{average:.2f}") 
