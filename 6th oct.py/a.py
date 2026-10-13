no_of_customers=int(input())
allowed=int(input())
if(no_of_customers%allowed==0):
  print(no_of_customers/allowed)
else:
  print(int(no_of_customers/allowed)+1)