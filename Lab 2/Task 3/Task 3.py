with open("input.txt","r") as input_file:
    test_case=int(input_file.readline())
    times=[]
    for i in range(test_case):
        line=[int(x) for x in input_file.readline().split()]
        times.append(line)
times.sort(key=lambda x:x[1])
completed_task=[]
ending_time=-1
for i in range (len(times)):
    if times[i][0]>=ending_time:
        completed_task.append(times[i])
        ending_time=times[i][1]
with open("output.txt","w") as out_file:
    out_file.write(f'{len(completed_task)}\n')
    for i in range (len(completed_task)):
        out_file.write(f"{completed_task[i][0]} {completed_task[i][1]}\n")
#j kaj age ses hobe seita age ses hobe
#tokhn dekha lagbe j eitar surur time kokhon
#Step 1 , ses er time onujaiyi sajabo, karon kon kaj age ses hobe seita amdr nite hobe
# protibar surur time dekhte hobe j kokhon
#tarpor surur time ta ager tar ses howar sathe compare korte hobe
# def mergeSort(arr):
#     if len(arr) <= 1:
#         return arr
#
#     mid = len(arr) // 2
#     leftHalf = arr[:mid]
#     rightHalf = arr[mid:]
#
#     sortedLeft = mergeSort(leftHalf)
#     sortedRight = mergeSort(rightHalf)
#
#     return merge(sortedLeft, sortedRight)
# def merge(left, right):
#     result = []
#     i = j = 0
#     while i < len(left) and j < len(right):
#         if left[i] < right[j]:
#             result.append(left[i])
#             i += 1
#         else:
#             result.append(right[j])
#             j += 1
#     if i<len(left):
#         result.extend(left[i:])
#     if j < len(right):
#         result.extend(right[j:])
#
#     return result
# print(mergeSort(all_times))