if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    
    arr.sort(reverse=True)
    maxNumber = arr[0]
    for i in arr:
        if i < maxNumber:
            maxNumber2 = i
            break   
            
    print(maxNumber2)
