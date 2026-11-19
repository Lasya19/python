command=input()
if command=="create":
    filename=input("what is the file name")
    with open(filename,"x") as file:
        print("file created")
elif command=="write":
    filename=input("what is the file name you want to write in"):
        with open(filename,"w") as file:
        write=input("what do you want to write in the file")
        file.write(write)
elif command="del":
    with open(filename,"w") as file:
        print("the content is deleted")