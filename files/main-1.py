import os
# cwd = os.getcwd()
# print("current working directory:",cwd)
# dirs_ = os.listdir('/')

# print(dirs_)

# with open("adf.txt",'a') as f:
#     f.write("Hey i am inside adf.txt")
#     f.write("hii how are you folks")
    
# a= open('adf.txt','r') 
# while True:
#         line = a.readline()
#         if not line:
#             break
#         print(line)

# g = open('aqw.txt','w')
# lines = ['line1\n','line2\n']
# g.writelines(lines)
# g.close()

# with open("adf.txt",'w+') as f:
#     f.write("Hey i am inside adf.txt")
#     f.seek(10)
#     current = f.tell()
#     print(current)
#     f.truncate(5)
#     print(f.read())
files1 = os.listdir("files")
print(files1)
