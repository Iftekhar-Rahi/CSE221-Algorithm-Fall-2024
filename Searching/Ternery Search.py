def ternery_search(arr,target):
    left=0
    right=len(arr)-1
    while left<=right:
        mid1=left+(right-left)//3
        mid2 = right-(right - left) //3
        if arr[mid1]==target or arr[mid2]==target:
            return mid1
        else:
            if target<arr[mid1]:
                right=mid1-1
            elif target>arr[mid2]:
                left=mid2+1
            else:
                left=mid1+1
                right=mid2-1
arr = [100, 1201, 292, 21323, 2132, 3123, 31, 31, 3]
arr.sort()  # Sorting the array first
print(ternery_search(arr, 100))