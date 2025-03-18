#Password validation program
password=input()
l=len(password)
spl=["@", "#", "_", "%", "!" , "$", "^","&","*","(",")","+","-","=","?"," "]
if l<8:
    print("Invalid password. Password contains atleast 8 characters")
else:
    digit=False
    upper=False
    lower=False
    spsl=False
    for i in password:
        if i.isdigit():
            digit=True
        elif i.isupper():
            upper=True
        elif i.islower():
            lower=True
        elif i in spl:
            spsl=True
    if digit and upper and lower and spsl:
         print("Valid password")
    else:
         print("Invalid password")
