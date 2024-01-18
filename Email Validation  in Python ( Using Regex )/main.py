#a-z
#0-9
#. _ time=1
#@ time=1
# . 2,3 position at last
import re #imports Regex module
email_condition="^[a-z] + [\._]?[a-z 0-9] + [@]\w+[.]\w{2,3}$"
user_email=input("Enter your Email:")

if re.search(email_condition,user_email):
    print("Valid Email")
else:
    print("Invalid Email")
    