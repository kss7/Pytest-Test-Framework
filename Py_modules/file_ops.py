
try:
    f = open("myfile.txt", 'r')
    #print(f.read())
    line = f.readline()
    while line:
        print(line)
        line = f.readline()
    #print(f.readlines())
finally:
    f.close()

print ("****Using with Option*****")
with open("myfile.txt",'r') as f:
   #print(f.readline())
   #list2 = f.read().split("\n")
   #print(list2)
   for line in f:
        print(line.strip())
