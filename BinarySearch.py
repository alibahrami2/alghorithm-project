def binary_search(arr,target):
    low = 0
    high = len(arr)

    while low <=  high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] > low:
            low = mid + 1
        else:
            high = mid - 1
    return -1

arr = [10 , 20 , 30 , 40 , 50 , 60]

target = 40

result= binary_search(arr , target)

if result != -1:
    print("index of array is " , result)
else:
    print("not found ")