n=int(input())
if n>0 and n<6:
    print(n*5) 
elif n>=6 and n<13:
     print(25 + (n-5)*6)
elif n>=13 and n<21:
     print(25 + 42 + (n-12)*8)
elif n>=21 and n<31:
     print(25 + 42 + 64 + (n-20)*10)
else:
     print("ride not accepted")                   

"""n = int(input())

if n <= 0 or n > 30:
    print("ride not accepted")
else:
    fare = 0git push

    for km in range(1, n + 1):
        if km <= 5:
            fare += 5
        elif km <= 12:
            fare += 6
        elif km <= 20:
            fare += 8
        else:
            fare += 10

    print(fare)"""