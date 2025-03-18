#multiples of both 2 and 3 in even
for i in range(1,101):
  if i%2==0:
    if i%3==0:
      print(i)
    else:
      print(i,"even but not multiple of 2 and 3")
