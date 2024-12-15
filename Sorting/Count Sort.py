
#Reversed
arr=[1,3,4,5,9,6,2,-1]
lowest=min(arr)
if lowest<0:
    arr=[i+abs(lowest) for i in arr]
highest=max(arr)
count=[0]*(highest+1)
for num in arr:
    count[num]+=1
print(count)
for i in range(len(count)-2,-1,-1):
    count[i]+=count[i+1]
print(count)
output=[0]*len(arr)
for i in arr:
    output[count[i]-1]=i
    count[i] -= 1
if lowest<0:
    output=[i-abs(lowest) for i in output]
print(output)