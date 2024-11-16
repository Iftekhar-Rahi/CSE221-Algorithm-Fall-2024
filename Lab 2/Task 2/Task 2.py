#merge// order of n
with open("input.txt","r") as input_file:
    first_len=int(input_file.readline())
    first_list=[int(num) for num in input_file.readline().split()]
    sec_len=int(input_file.readline())
    sec_list=[int(num) for num in input_file.readline().split()]

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
sorted_array=merge(first_list,sec_list)
# print(sorted_array)
with open ("output.txt","w") as output_file:
    output_file.write(" ".join(str(num) for num in sorted_array))