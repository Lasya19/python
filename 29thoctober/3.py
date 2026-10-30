# prices=[900,1000,800,700,600,200,1200]
# result=map(lambda x:x if x>500 else "not",prices)
# print(list(result))

prices=[900,1000,800,700,600,200,300,1200]
result=filter(lambda x:x<500, prices)
print(list(result))
