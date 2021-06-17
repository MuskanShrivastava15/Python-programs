# to print alphabets in row
n = int(input("enter the number for pattern formation"))
d=65
for i in range(0,n+1):   #row
     for j in range(0,i+1):#column
         # chr=chr(d)
         # d=d+1
         c = chr(d)
         print(c ,end=" ")
         d = d + 1
     print(" ")