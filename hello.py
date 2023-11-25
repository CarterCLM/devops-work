# Asking user for their name
#name = input("What's your name? ").strip().title()

# Split user's name into first name last name 
#first, last = name.split(" ")

# Remove whitespace from str and capitalize user's name
#name = name.strip().title()

# Capitalize user's name
#name = name.title()

# Say hello to user
#print(f"hello, {first}")

#print(name)

# Create My Own Function
def main():
    name = input("What's your name? ")
    hello(name)

def hello(to="world"):
    print("Hello,", to)


main()
