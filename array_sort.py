def Sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] < arr[j+1]:
                arr[j] , arr[j+1] = arr[j+1] , arr[j]

arr = [5, 3, 8, 6, 2]
print("آرایه قبل از مرتب‌سازی:", arr)

Sort(arr)  # فراخوانی تابع مرتب‌سازی
print("آرایه بعد از مرتب‌سازی:", arr)