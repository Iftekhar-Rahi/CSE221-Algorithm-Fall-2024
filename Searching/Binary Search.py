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
arr = arr = [23,2,19,3,7,11,5,13]
print(binary_search(arr, 2))