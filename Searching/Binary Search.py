def binary_search(arr,target):
    left=0
    right=len(arr)-1
    while left<=right:
        mid=left+(right-left)//2
        if arr[mid]==target:
            return mid
        elif target>arr[mid]:
            left=mid+1
        else:
            right=mid-1
arr = [100, 1201, 292, 21323, 2132, 3123, 31, 31, 3]
arr.sort()  # Sorting the array first
print(binary_search(arr, 100))