print('What is your name?')
name = input()
name = name.title()
print('How old are you?')
age = input()
age = int(age)

if name == 'Alice' and age == 12:
    print('Hi, Alice.')
elif name != 'Alice' and age == 12:
    print('You are not Alice, kiddo.')
elif (name == 'Alice' or name != 'Alice') and (age < 12 or age >= 13 and age <= 59):
    print('You are not Alice, kiddo.')
elif (name == 'Alice' or name != 'Alice') and (age >= 60 and age <= 110):
    print ('You are not Alice, grannie.')
elif (name == 'Alice' or name != 'Alice') and age >= 111:
    print ('Unlike you, Alice is not an undead, immortal vampire.')
