#order of n
with open ("input.txt","r") as input_file:
    first_line=[int(num) for num in input_file.readline().split()]
    n=first_line[0]
    target=first_line[1]
    array=[int(num) for num in input_file.readline().split()]
def my_searching(array,target):
    i=0
    j=len(array)-1
    while i<j:
        if array[i]+array[j]==target:
            return (i+1, j+1)
        elif array[i]+array[j]<target:
            i+=1
            j=j
        elif array[i]+array[j]>target:
            i=i
            j-=1
        else:
            return "IMPOSSIBLE"
with open ("output.txt","w") as output_file:
    output_file.write(f"{my_searching(array,target)}")
