with open ("input.txt","r") as input_file:
    first_line=input_file.readline().split()
    n=int(first_line[0])
    m=int(first_line[1])
    matrix = []
    for i in range(n):
        matrix.append(list(input_file.readline().rstrip()))
    for r in matrix:
        print(r)