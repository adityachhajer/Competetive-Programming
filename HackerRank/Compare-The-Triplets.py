
# Complete the compareTriplets function below.
def compareTriplets(a, b):
    al =0
    bo=0
    for i in range(3):
        if(a[i]>b[i]):
            al+=1
        elif(b[i]>a[i]):
            bo+=1
    return(al,bo)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = list(map(int, input().rstrip().split()))

    b = list(map(int, input().rstrip().split()))

    result = compareTriplets(a, b)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
