def print_formatted(number):

    width = len(bin(number)[2:])
    for x in range(1, number + 1):
        print(f"{x:{width}d}", end=" ")
        print(f"{oct(x)[2:]:>{width}}", end=" ")
        print(f"{hex(x)[2:].upper():>{width}}", end=" ")
        print(f"{bin(x)[2:]:>{width}}")
        
if __name__ == '__main__':
    n = int(input())
    print_formatted(n)