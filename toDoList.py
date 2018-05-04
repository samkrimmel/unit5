#Sam Krimmel
#5/4/18
#toDoList.py - make a list of things to of the do!

list = []

while True:
    print("Valid Commands: add, delete, print, quit")
    inp = input().split(' ')
    
    if inp[0] == "add":
        list.append(inp[1:])
    elif inp[0] == "delete":
        list.remove(inp[1:])
    elif inp[0] == "print":
        for item in list:
            print(item)
    elif inp[0] == "quit":
        break
    else:
        print("No, no, no, pick a valid command")
    
