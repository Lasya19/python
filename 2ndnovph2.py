#w+ -->write+read
with open("t2n2.txt","w+") as file:
    file.write("try to develop a real world application")
    print("success")
    print(file.tell())
    file.seek(0)
    print(file.read())
with open("t2n2.txt","r+") as file:
    file.write("hello how are you")
    print("success")
    print(file.tell())
    file.seek(0)
    print(file.read())    