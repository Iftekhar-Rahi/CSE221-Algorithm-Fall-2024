#Task 2
with open("input.txt","r") as input_file:
    n=int(input_file.readline())
    num_array=[int(num) for num in input_file.readline().split()]
    def bubblesort(array):
        n=len(num_array)
        for i in range(n):
            flag = True
            for j in range(0, n - 1 - i):
                if array[j] > array[j + 1]:
                    array[j], array[j + 1] = array[j + 1], array[j]
                    flag = False
            if flag == True:
                break
        return array
with open ("output.txt","w") as output_file:
    output_file.write(" ".join([str(num) for num in bubblesort(num_array)]))