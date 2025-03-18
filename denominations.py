#Denominations
amount=int(input())
five100=amount//500
rem=amount%500
hundred=rem//100
rem1=rem%100
fifty=rem1//50
rem2=rem1%50
ten=rem2//10
rem3=rem%10
print("Five Hundred notes (500):",five100)
print("Hundred notes (100):", hundred)
print("Fifty notes (50):", fifty)
print("Ten notes (10) :", ten)
