arr=[1,3,4,5,9,6,2,-1]
def binary_search(arr):
    left=0
    right=len(arr)-1
    while left<=right:
        mid=left+(right-left)//2
        if arr[mid]>arr[mid+1] and arr[mid]>arr[mid-1]:
            return mid
        # elif arr[mid]<arr[mid-1]:
        #     right = mid - 1
        # elif arr[mid]<arr[mid+1]:
        #     left = mid + 1
        elif arr[mid-1]>arr[mid]:
            right=mid+1
        elif arr[mid+1]>arr[mid]:
            left = mid - 1
print(arr[binary_search(arr)])