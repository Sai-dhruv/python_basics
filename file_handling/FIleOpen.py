f = open("Text_file.txt", 'w')
print("File Name :", f.name)
print("FIle Mode :", f.mode)
print("file closed:", f.closed)
#f.close()
print("Is FIle closed :",f.closed)


list = ['sai','krishna','niharika','Dhruv']
for i in list:
    f.write(i+"\n")
    
            

f.close()