def square_root_finder(target):
    left=0
    right=target
    result=-1
    while left<right:
        mid=(left+right)//2
        if mid*mid==target:
            return mid
        elif mid*mid>target:
            result=mid
            right-=1
        elif mid*mid<target:
            result = mid
            left+=1
    return result
print(square_root_finder(10))