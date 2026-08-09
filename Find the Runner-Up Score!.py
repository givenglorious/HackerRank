if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    new_arr = list(set(arr))
    new_arr.sort()
    print(new_arr[-2])
    
    
    #Kode goblok
# if __name__ == '__main__':
#     n = int(input())
#     arr = map(int, input().split())
#     new_arr = list(arr)
#     runner_up = new_arr[0]
#     if len(new_arr) == n:
#         for x in new_arr:
#              if x > runner_up:
#                  runner_up = x
#         print(runner_up - 1)
