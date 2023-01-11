# C: Write your first number: (User write 100)
# C: Write your command: (User write [+, -, *, /])
# C: Write your second number: (User write 50)
# if it is a +:
# C: print 150
# elif it is a -:
# C: print 50



first_number = int(input('Write your first number:'))

print("Commands list:\n+\n-\n*\n/")

command = input('Enter your comman:')

second_number = int(input('Write your second number:'))

if command == "+":
    print (first_number + second_number) #print (50+50)

if command == "-":
    print (first_number - second_number)

if command == "/":
    print (first_number / second_number)

if command == "*":
    print (first_number * second_number)


