n=input()
print((lambda n: "valid" if 5 <= len(n) <= 12 else "invalid")(n))