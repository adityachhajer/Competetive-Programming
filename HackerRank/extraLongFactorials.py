def extraLongFactorials(n):
    fact = 1
    for num in range(1,n+1):
        fact *=num
    print(fact)

if __name__ == '__main__':
    n = int(input())

    extraLongFactorials(n)
