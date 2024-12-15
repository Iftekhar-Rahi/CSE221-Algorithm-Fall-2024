with open ("input.txt","r") as input_file:
    first_line=input_file.readline().split()
    n=int(first_line[0])
    m=int(first_line[1])
    ad_list = [[] for i in range(n + 1)]
    for i in range(m):
        line = [int(num) for num in input_file.readline().split()]
        ad_list[line[0]].append((line[1],line[2]))
    for i in range(len(ad_list)):
        print(f"{i} : {ad_list[i]}")

# t","w") as out_file:
#     for i,row in enumerate(ad_list):
#         out_file.write(f"{i} : ")
#         for i in row:
#             out_file.write(str(i)+'\n')