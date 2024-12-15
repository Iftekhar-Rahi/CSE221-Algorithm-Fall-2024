arr=[9,8,7,6,5,4,3,2,1]
# def quick_sort(A,first_index,last_index):
#     if first_index<last_index:
#         pivot_index=partition(A,first_index,last_index)
#         quick_sort(A,first_index,pivot_index-1)
#         quick_sort(A, pivot_index+1,last_index)
# def partition(A,f,l):
#     pivot=A[f]
#     i=f
#     for j in range (i+1,l+1):
#         if pivot>=A[j]:
#             i+=1
#             A[i],A[j]=A[j],A[i]
#     A[f],A[i]=A[i],A[f]
#     return i
# print(quick_sort(arr,0,len(arr)-1))
# print(arr)
def quick_sort(arr,first_index,last_index):
    if first_index<last_index:
        pivot = partition(arr, first_index, last_index)
        quick_sort(arr, first_index, pivot - 1)
        quick_sort(arr, pivot + 1, last_index)
def partition(arr,f,l):
    pivot=arr[f]
    i=f
    for j in range(i+1,l+1):
        if pivot>=arr[j]:
            i+=1
            arr[i],arr[j]=arr[j],arr[i]
    arr[f],arr[i]=arr[i],arr[f]
    return i
print(quick_sort(arr,0,len(arr)-1))
print(arr)