name=input("Enter your name:")
surname=input("Enter your surname:")
question=input("Print 'YES' if you lox, print 'NO' if not:")
if (question=="YES"):
    print(name, surname, "is lox")
    print("Congratulations! You are lox!")
elif(question =="NO"):
    print(name, surname, "is not lox")
    print("Congratulations! You are not lox!")
else:
    print(name, surname, "is daun")
    print("Congratulations! You are daun!")
