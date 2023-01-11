age = int (input("Please enter the age:"))

if age <= 5 and age > -1:
    if age < 3:
        print("Please use babysitter")
    else:
        print("Attend to Kindergarden")
elif age > 5 and age <= 12:
    print("Attend to Primary School")
elif age > 12 and age <= 18:
    print("Attend to Hight School")
elif age > 18 and age <= 23:
    print("Attend to College")
elif age > 23 and age <= 75:
    print("You are eligible to work")
elif age > 75 and age <= 102:
    print("Enjoy your life")
else:
    if age > 102 and age <= 200:
        print("Are you centenarian? ")
    elif age > 200 and age <= 500:
        print("Are you a vampire?")
    elif age > 500 and age <= 1000:
        print("Are you imortal?")
    elif age > 1000:
        print("Are you God?")
