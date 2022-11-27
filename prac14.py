fopen = open("oldfile.txt","r") #opening old File
fwrite = open("newfile.txt","w") #New File created storing the data as required
oldfileinfo = fopen.readlines() #Reading the lines 1by1

print(oldfileinfo)

for i in range(0,len(oldfileinfo),2):
    fwrite.write(oldfileinfo[i])
    
fwrite.close()#Closing File Handling Links
fopen.close()
