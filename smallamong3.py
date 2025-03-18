#Smallest among 3 numbers
a=int(input())
b=int(input())
c=int(input())
if a==b==c:
   print(a, " is small")
elif a<b and a<c:
   print(a, " is small")
elif b<c:
   print(b, " is small")
elif c<a and c<b:
   print(c, " is small")
elif a==b <c:
   print(a, " is small")
elif b==c <a:
   print(b, " is small")
elif a==c<b:
   print(a, " is small")
