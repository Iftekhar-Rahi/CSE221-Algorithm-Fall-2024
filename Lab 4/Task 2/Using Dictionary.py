with open ("input.txt","r") as infile:
    line1=[int(i) for i in infile.readline().split()]
    vertex=line1[0]
    edge=line1[1]
    dic={}
    for i in range(edge+1):
        dic[i]=[]
    for i in range(edge):
        s,d,wt=map(int,infile.readline().split())
        dic[s].append((d,wt))
with open("output.txt","w") as outfile:
    for key, value in dic.items():
        outfile.write(f"{key}:{value}\n")
        # print(key, value)
