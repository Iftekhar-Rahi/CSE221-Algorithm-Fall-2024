def linear_search(arr,target):
    n=len(arr)
    for i in range(n):
        if arr[i]==target:
            return i
arr = [100, 1201, 292, 21323, 2132, 3123, 31, 31, 3]
print(linear_search(arr, 100))