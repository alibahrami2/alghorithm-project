def PrefixSum(arr):
    n = len(arr)
    prefix = [0] * n
    prefix[0] = arr[0]
    for i in range(1 , n):
        print("arr " ,arr[i])
        prefix[i] = prefix[i - 1] + arr[i]
        print(prefix[i])
    return prefix

arr = [2, 5, 3, 0, 8]
prefix = PrefixSum(arr)
print(prefix)