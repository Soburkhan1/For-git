# Print multiplication table of a number


char = int(input('enter a number:'))
i = 1
while i <= 12:
        print(char,  '*', i, '=', char * i)
        i += 1