#list compreshension to reduce the lines of code
print((lambda n:[i for i in range(n)])(5))

x=[7,8,9,1,2,3,4]
l=[]
for i in x:
    if i%2==0:
        l.append(i)
print(l)

print([i for i in x if i%2==0])

x=[7,8,9,1,2,3,4]
l=[]
for i in x:
    if i%2==0:
        l.append(i)
    else:
        l.append("odd")
print(l)

print([i for i in x if i%2==0])
print([i if i%2==0 else "odd" for i in x])

