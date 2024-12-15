arr=[23,2,19,3,7,11,5,13]
def count_sort(arr):
    lowest = min(arr)
    if lowest < 0:
        arr = [i + abs(lowest) for i in arr]
    highest = max(arr)
    count=[0]*(highest+1)                       #if highest 8 and i didn't add 1 what will happen? (count arry's max index will be 7 so 8 rakhar jaga nai)

    for i in arr:                               #count array'r modhe sob rakhlam
        count[i]+=1
    print(count)
    for j in range(1,len(count)):               #cumilative sum er array banailam
        count[j]+=count[j-1]
    print(count)

    output=[0]*len(arr)
    # for i in reversed(arr):
    #     output[count[i]-1]=i
    #     count[i]-=1
    for i in range(len(arr)-1,-1,-1):
        output[count[arr[i]]-1]=arr[i]
        count[arr[i]]-=1

    if lowest <0:
        output=[x-abs(lowest) for x in output]
    print(output)
count_sort((arr))
