# Grade system: A(>=90), B(>=80), C(>=70), D(>8=60), F

score =int(input('give your score'))

if score < 0 or score > 100:
    print("Invalid grade")
elif score >=80:
    print('grade A+')
elif score >= 70:
    print('grade A')
else:
    print('grade F')

