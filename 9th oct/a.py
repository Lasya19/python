toy=input("battery or wire or wireless")
bill=int(input())
paidamount=bill

if toy=="battery":
 if bill>500:
   paidamount=bill*0.9
   print(paidamount)
elif toy=="wire":
  if bill>500:
  freetoys=bill//500
  print(f"{bill} + {freetoys}")
elif toy=="wireless":
   bill>2000:
   paidamount=bill*0.95
   print(paidamount)