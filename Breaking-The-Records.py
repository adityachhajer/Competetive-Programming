

# Complete the breakingRecords function below.
def breakingRecords(scores):
    min_ele = scores[0]
    max_ele = scores[0]
    min_cnt = 0
    max_cnt = 0
     
    for score in scores:
        if score > max_ele:
            max_ele = ele
            max_cnt += 1
        if score < min_ele:
            min_ele = ele
            min_cnt += 1
     
    return [max_cnt, min_cnt]
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
