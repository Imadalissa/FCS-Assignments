numbers = [-12,4,12,25,67]
while True:
    user_input=int(input("enter a number to insert into the list(or -99 to quit):"))
    if user_input == -99:
        print("program terminated")
        break
    numbers.append(user_input)
    numbers.sort()
    print("update list:",numbers)
