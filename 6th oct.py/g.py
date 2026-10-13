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

  """year=int(input("must be in [1,2,3,4]:"))
if year==4:
    marks=int(input("enter marks:"))
    
    if marks>80 and marks<=100:
        backlogs=int(input("enter bakclogs:"))
        
        if backlogs!=0:
            if backlogs>=1 and backlogs<=3:
                
                pay=input("you have to pay 5000 extra: [yes (or) no]:")
                if pay=="yes":
                    print("eligible for training")
                else:
                    print("must need to pay")

            elif backlogs>3:
                
                pay=input("you have to pay 10k [yes (or) no]:")
                if pay=="yes":
                    print("eligible for trainig")
                else:
                    print("must need to pay 10k")
                    
            
        else:
            print("eligbile for training")

    else:
        print("marks must greater than 80")
else:
    print("year must be 4")"""