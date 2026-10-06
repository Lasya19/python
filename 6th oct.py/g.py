year=int(input())
marks=int(input())
backlogs=int(input())
if year==4:
  if marks>80 and marks<101:
     if(backlogs==0):
      print("allowed to training")
     else:
      print("must have zero backlogs")
  else:
    print("marks must be greater than 80")
else:
  print("must be in 4th year")    