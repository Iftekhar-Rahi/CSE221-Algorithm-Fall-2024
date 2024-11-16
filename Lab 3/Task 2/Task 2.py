with open ("input.txt","r") as input_file:
    n=int(input_file.readline())
    arr=[int(num) for num in input_file.readline().split()]
def mergeSort(arr):
    if len(arr) <= 1:
        return arr[0]
    else:
        mid = len(arr) // 2
        a1 = mergeSort(arr[:mid])  # write the parameter
        a2 = mergeSort(arr[mid:])  # write the parameter
        return my_max(a1, a2)
def my_max(left,right):
    if left>right:
        max=left
    else:
        max=right
    return max
result=mergeSort(arr)
with open("output.txt", "w") as out_file:
    out_file.write(str(result))