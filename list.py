#ask user how many classes they are taking
numClases = int(input('How many classes are you taking? '))
listClasses = []
#run loop for amount of classes
for x in range(0, numClases) :
    className = input('Enter name of class ')
    listClasses.append(className)

for x in range(len(listClasses)):
    print(listClasses[x])