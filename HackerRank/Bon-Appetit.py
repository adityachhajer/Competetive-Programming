

# Complete the bonAppetit function below.
def bonAppetit(bill, k, b):
    sum = 0
    for elem in range(len(bill)):
        sum +=bill[elem]
    final = sum-bill[k]
    final = final/2
    if final == b:
        print('Bon Appetit')
    else:
        print(int(abs(final-b)))


if __name__ == '__main__':
    nk = input().rstrip().split()

    n = int(nk[0])

    k = int(nk[1])

    bill = list(map(int, input().rstrip().split()))

    b = int(input().strip())

    bonAppetit(bill, k, b)
