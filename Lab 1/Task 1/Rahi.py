#1
# =============================================================================
# file=open("Name","mode")
# #This will read the entire file
# text=file.read()
# print(text)
# =============================================================================
#2
# =============================================================================
# file=open("input1a.txt","r")
# line1=file.readline()
# print(line1)
# line2=file.readline()
# print(line2)
# =============================================================================

#3
# =============================================================================
# file=open("input1a.txt","r")
# line1=file.readlines()
# print(line1)
# =============================================================================


# =============================================================================
# test_case=int(input())
# for i in range(test_case):
#     num=int(input())
#     if num%2==0:
#         print(f"{num} is an even Number")
#     else:
#         print(f"{num} is an odd Number")
# =============================================================================

# =============================================================================
# f=open("output1a.txt","a")
# #a will append all the time
# f.write("Now the file has more content!\n")
# f.close()
# =============================================================================

# =============================================================================
# f=open("output1a.txt","w")
# #a will forcedly write all the time
# f.write("Now the file has more content!\n")
# f.close()
# =============================================================================




input_file=open("input1a.txt","r")
output_file=open("output1a.txt","w")
output_file=open("output1a.txt","a")
test_case=int(input_file.readline())
for i in range(test_case):
     num=int(input_file.readline())
     if num%2==0:
         print(f"{num} is an even Number",file=output_file)
         
     else:
         print(f"{num} is an odd Number",file=output_file)
input_file.close()
output_file.close()
         
         