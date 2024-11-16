with open ("input.txt","r") as input_file:
    n=int(input_file.readline())
    arr=[int(num) for num in input_file.readline().split()]
def mergeSort(arr):
    if len(arr) <= 1:
        return arr
    else:
        mid = len(arr) // 2
        a1 = mergeSort(arr[:mid])  # write the parameter
        a2 = mergeSort(arr[mid:])  # write the parameter
        return my_max(a1, a2,)
def my_max(left,right,):
    i=left[len(left)-1]
    j=right[len(left)-1]
    value=left[i]+(left[j])**2
    if
result=mergeSort(arr)
with open("output.txt", "w") as out_file:
    out_file.write(str(result))