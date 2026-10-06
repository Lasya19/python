#Write a program to check if a number is greater than 10. 
n=int(input())
if(n>10):
  print("greater than 10")
else:
    print("not greater than 10")

#Write a program to check if a person is eligible to vote (age 18 or above). 
age=int(input())
if(age>=18):
  print("eligible to vote") 
else:
  print("not eligible to vote")

#Write a program to check if a number is positive.
num=int(input())
if(num>0):
  print("positive")
else:
  print("not positive")

#Write a program to check if a number is negative.
no=int(input())
if(no<0):
  print("negative")
else:
    print("not negative")  

#Write a program to check if a number is even or odd. 
a=int(input())  
if(a%2==0):
  print("even")
else:
  print("odd")
#Write a program to check if a person is eligible for a driving license (age 18 or above). 
b=int(input())
if(b>=18):
  print("eligible for driving license")
else:
  print("not eligible for driving license")


#Write a program to check if a number is positive or negative. 
c=int(input())
if(c>0):
  print("positive")
else:
  print("negative or zero")


#Write a program to check if a student passed or failed based on marks (Pass: 40+, Fail: below 40). 
marks=int(input())
if(marks>=40):
  print("passed")
else:
  print("failed")

# Write a program to classify a number as positive, negative, or zero. 
d=int(input())
if(d>0):
  print("positive")
elif(d<0):
  print("negative") 
else:
  print("zero") 

#Write a program to categorize a person’s age as a child (0-12), teenager (13-19), or adult (20+). 
e=int(input())
if(e>=0 and e<=12):
  print("child")        
elif(e>=13 and e<=19):
  print("teenager")    
else:
  print("adult") 

#Write a program to determine the grade of a student based on marks (A: 90+, B: 80+, C: 70+, D: 60+, Fail: <40). 
f=int(input())
if(f>=90):
  print("A")  
elif(f>=80):
  print("B")
elif(f>=70):
  print("C")
elif(f>=60):
  print("D")
else:
  print("fail")

#  A bank checks if a person is eligible for a loan based on their age and salary. 
age1=int(input())
salary=int(input())  #???

#A student needs at least 35 marks to pass. If they score above 90, they get a scholarship. 
marksofstudent=int(input())
if(marksofstudent>=35):
  print("pass")
  if(marksofstudent>90):
    print("elgible for scholarship")
  else:
    print(" passed not eligible for scholarship")
else:
  print("not passed")    

