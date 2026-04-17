name = input("What's your name? ")

# if name == "Harry":
#     print("Gryffindor")
# elif name == "Hermione":
#     print("Griffindor")
# elif name == "Ron":
#     print("Griffindor")
# elif name == "Draco":
#     print("Slytherin")
# else:
#     print("Who?")


match name:
    case "Harry":
        print("Griffindor")
    case "Hermione":
        print("Griffindor")
    case "Ron":
        print("Griffindor")
    case "Draco":
        print("Slytherin")
    case _:
        print("Who?")

#Cleaner way to do the same thing as above 
match name:
    case "Harry" | "Hermione" | "Ron":
        print("Griffindor")
    case "Draco":
        print("Slytherin")
    case _:
        print("Who?")

