
def check(str):
    for i  in range(0,len(str)//2):
        if str[i]!=str[len(str)-i-1]:
            return False
    return True
str="1111111122222222333333333335666677889944"
if(check(str))==True:
    print("its a palandrome")
else:
    print("it is not a palindrome")

