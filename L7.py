#I/O in PYTHON : input output
#types:
#  -> text files: .txt, .docx, .log, etc(data stored as charac)
# -> binary files: .mp4, .mov, .png, .jpeg, etc
# all data in files stored as bits(0,1)
#cant readline after read

f = open("demo.txt","r")
data1 =f.readline()  #reads data line by line
print(data1)

data= f.read()   #reads data all in one go
print(data)

f.close()
#space in terminal due to "\n" in txt file(invisible)