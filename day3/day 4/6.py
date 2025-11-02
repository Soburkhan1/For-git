# Ask user for password until correct ("secret")
password = input("Enter the password: ")
while password != "secret":
    print('incorrect password, try again')
    password = input("Enter the password: ")

print('acces granated')