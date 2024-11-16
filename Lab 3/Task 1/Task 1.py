with open ("input.txt","r") as input_file:
    n=int(input_file.readline())
    array=[int(num) for num in input_file.readline().split()]

def mergeSort(arr):
    if len(arr) <= 1:
        return arr
    else:
        mid = len(arr)//2
        a1 = mergeSort(arr[:mid])  # write the parameter
        a2 = mergeSort(arr[mid:])  # write the parameter

        return merge(a1, a2)
def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    if i<len(left):
        result.extend(left[i:])
    if j < len(right):
        result.extend(right[j:])

    return result
result=mergeSort(array)
with open("output.txt", "w") as out_file:
    # out_file.write([str(num) for num in mergeSort(array)].joint(" "))
    for i in range (len(result)):
        out_file.write(str(result[i])+" ")
