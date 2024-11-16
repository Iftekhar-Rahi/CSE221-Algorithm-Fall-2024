#task 4
with open ("input.txt","r") as input_file:
    n=int(input_file.readline())
    info=[]
    for i in range(n):
        train=input_file.readline().split()
        info.append([train[0],train[4],train[6]])
    def selection_sort(info):
        n=len(info)
        for i in range(n):
            min_index=i
            for j in range(i+1,n):
                if info[j][0]<info[min_index][0] or (info[j][0] == info[min_index][0] and info[j][2] > info[min_index][2]):
                    min_index=j
            info[i],info[min_index]=info[min_index],info[i]
selection_sort(info)
with open("output.txt","w") as output_file:
    for i in range(n):
        output_file.write(f"{info[i][0]} will departure for {info[i][1]} at {info[i][2]}\n")
