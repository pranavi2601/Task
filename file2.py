import file1
s1=input("enter the 1st string to check=")
s2=input("enter the 2nd string to check=")
s3=input("enter the 3rd string to check=")
s4=input("enter the 4th string to check=")
s5=input("enter the 5th string to check=")
s6=""
# print(file1.str1)
# print(file1.str2)
# print(file1.str3)
if(s1!=s6):
    if(s1==file1.str1):
     pass
    elif(s1!=file1.str1):
     print("Line no 1 modified from",file1.str1,"to",s1)
else:
    print("Line no 1 is deleted")
if(s2!=s6):
    if(s2==file1.str2):
     pass
    elif(s2!=file1.str2):
     print("Line no 2 modified from",file1.str2,"to",s2)
else:
    print("Line no 2 is deleted")
if(s3!=s6):
    if(s3==file1.str3):
     pass
    elif(s3!=file1.str3):
     print("Line no 3 modified from",file1.str3,"to",s3)
else:
    print("Line no 3 is deleted")
if(s4!=s6):
    if(s4==file1.str4):
     pass
    elif(s4!=file1.str4):
     print("Line no 4 modified from",file1.str4,"to",s4)
else:
    print("Line no 4 is deleted")
if(s5!=s6):
    if(s5==file1.str5):
     pass
    elif(s5!=file1.str5):
     print("Line no 5 modified from",file1.str5,"to",s5)
else:
    print("Line no 5 is deleted")
