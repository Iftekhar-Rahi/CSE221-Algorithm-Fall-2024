with open ("input.txt","r") as input_file:
    first_line=input_file.readline().split()
    n=int(first_line[0])
    m=int(first_line[1])
    dic={}
    for i in range(m):
        dic[i] = []
    for i in range(m):
        line = [int(num) for num in input_file.readline().split()]

        dic[line[0]].append((line[1],line[2]))
    for key,value in dic.items():
        print(f'{key}: {value}')