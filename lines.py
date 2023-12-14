L=["python\n","programming\n","language\n"]
file1=open('myfile.txt','w')
file1.writelines(L)
file1.close()
file1=open('myfile.txt','r')
Lines=file1.readlines()
count=0
for Line in Lines:
     count+=1
     print("Line{}:{}".format(count,Line.strip()))


