while True:
    mins = 0
    seconds = 0
    user = input("enter time: ")
    mins = int(user[0])
    seconds = int(user[2] + user[3])
    mins = 60 * mins
    
    result = 300 - (mins+seconds)
    print(result)
