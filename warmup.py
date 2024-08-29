#gets users name
name = input('Please enter your name ')
#greeting
print('Hello ' + name)
#A message with the number of letters in your name
characterNum = len(name)
print(f'your name is {characterNum} numbers long!')
# get users birthday
birthMonth = input('please enter your birth month using the months name (example: january) ')
#set current month
currentMonth = 'august'
#compare if users birthday
if birthMonth.lower() == currentMonth.lower() :
    print('Happy Birthday!!')
else :
    print('It is not your birthday!')
