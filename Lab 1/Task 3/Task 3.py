#Task 3
with open("input.txt", "r") as input_file:
    n=int(input_file.readline())
    id=[int(num) for num in input_file.readline().split()]
    marks=[int(num) for num in input_file.readline().split()]
    def selection_sort(students):
        n=len(students)
        for i in range(n):
            min_index=i
            for j in range(i+1,n):
                if students[j][0]>students[min_index][0] or (students[j][0] == students[min_index][0] and students[j][1] < students[min_index][1]):
                    min_index=j
            students[i],students[min_index]=students[min_index],students[i]
        return students
    students=list(zip(marks,id))
    print(students)
    result=selection_sort(students)
with open ("output.txt","w") as output_file:
    for student in result:
        output_file.write(f"ID: {student[1]}, Mark:{student[0]}\n")
