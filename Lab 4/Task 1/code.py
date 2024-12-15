with open ("input.txt","r") as input_file:
    first_line=input_file.readline().split()
    n=int(first_line[0])
    m=int(first_line[1])

    matrix = [[0] * (n+1) for i in range(n+1)]

    for i in range(m):
        line = [int(num) for num in input_file.readline().split()]
        matrix[line[0]][line[1]]=line[2]
        # matrix[line[1]][line[0]] = line[2]
with open ("output.txt","w") as out_file:
    for row in matrix:
        out_file.write(str(row)+"\n")