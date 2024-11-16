#order of n square
with open ("input.txt","r") as input_file:
    first_line=[int(num) for num in input_file.readline().split()]
    n=first_line[0]
    target=first_line[1]
    array=[int(num) for num in input_file.readline().split()]
def my_searching(array,target):
    for i in range(len(array)):
        for j in range(len(array)-1,i,-1):
            if array[i]+array[j]==target:
                return (i+1,j+1)
    return "IMPOSSIBLE"
with open ("output.txt","w") as output_file:
    output_file.write(f"{my_searching(array,target)}")
