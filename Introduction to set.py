def average(arr):
    random_num = set(arr)
    print(round(sum(random_num) / len(random_num), 3))

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)