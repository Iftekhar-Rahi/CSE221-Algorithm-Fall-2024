input_file=open("input1b.txt","r")
output_file=open("output1b.txt","w")
output_file=open("output1b.txt","a")
test_case=int(input_file.readline())
for i in range(test_case):
    line=input_file.readline().split()
    if line[2]=="+":
        result=int(line[1])+int(line[3])
    elif line[2]=="-":
        result=int(line[1])-int(line[3])
    elif line[2]=="*":
        result=int(line[1])*int(line[3])
    elif line[2]=="/":
        result=int(line[1])/int(line[3])
        
    print(f"The result of {line[1]} {line[2]} {line[3]} is {result}",file=output_file)
input_file.close()
output_file.close()