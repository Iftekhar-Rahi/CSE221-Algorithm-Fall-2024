def first_index_binary_search(arr,target):
    left=0
    right=len(arr)-1
    count=0
    while left<=right:
        mid=left+(right-left)//2
        if arr[mid]==target:
            first_index=mid
            right=mid-1
        elif target<arr[mid]:
            right = mid - 1
        else:
            left = mid + 1
    for i in range(first_index,len(arr)):
        if arr[i]==target:
            count+=1
        else:
            break
    return (first_index, count)
arr = arr = [1, 2,2,2,2, 3, 4, 5,6,7,8]
print(first_index_binary_search(arr, 2))