
import time
password=input("Enter the password: ")

results={}
if len(password)>=8:
    results["Length"]=True

digit=False
uppercase=False

for i in password:
    if i.isdigit():
        digit=True
    elif i.isupper():
        uppercase=True
    else:
        continue

results["Digit"]=digit
results["Uppercase"]=uppercase

print(results)
if False in results.values():
    print("Weak Password")
else:
    print("Strong password")
