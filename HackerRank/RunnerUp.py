if __name__ == '__main__':
    n = int(input())
    arr =list(map(int, input().split(" "))) 
    i = max(arr)
    for i in range(0,n):
        if max(arr) == i:   
            arr.remove(max(arr))
    arr.sort(reverse=True)
    print(arr[0])

