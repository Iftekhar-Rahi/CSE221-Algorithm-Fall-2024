with open("input.txt","r") as input_file:
    first_len=int(input_file.readline())
    first_list=[int(num) for num in input_file.readline().split()]
    sec_len=int(input_file.readline())
    sec_list=[int(num) for num in input_file.readline().split()]
    full_list=first_list+sec_list
#merge_sort
