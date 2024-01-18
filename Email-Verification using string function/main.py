email=input("Enter your Email:")#g@gmail.com
valid=True
# valid=False
k,j,d=0,0,0
if len(email)>=8:
    if email[0].isalpha():#First letter of any email must be in alphabet
        if ("@" in email) and (email.count("@")==1):
            if (email[-4]==".") or  (email[-3]=="."):#  email[-4] means fourth character from left to right direction in string list ((.com)=.). and  emial[-3] means that third positioned character in string data which is "." in (.in/.co)
                for i in email:
                    if i==" ":
                        k=1
                    elif i.isalpha():#isalhpa() returns boolean data and checks that weather the character is string or not
                        if i==i.upper():
                            j=1
                    elif i.isdigit():
                        continue
                    elif i=="_" or i=="." or i=="@":
                        continue
                    else:
                        d=1                 
                if k==1 or j==1 or d==1:
                    valid=False
                    print("Invalid Email 5")
            else:
                valid=False
                print("Invalid Email 4")
        else:
            valid=False
            print("Invalid Email 3")
    else:
        valid=False
        print("Invalid Email 2")
else:
    valid=False
    print("Invalid Email 1")
if valid:
    print("valid Email")