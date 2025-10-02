a=10

b=3.5


name="JESSENIA"
is_active=True

print(a, b, name)

print (type(a))
print (type(name))
print (type(is_active))

devise='router'
id=101

print(f'Devise {devise} and ID: {id}')

# ARIMETHIC OPERATIONS

numbera=2
numberb=3

#result=numbera+numberb
#print(f"the sum is: " ,(result))

print(f"the sum of adding two numbers is: ", numbera+numberb)


print("the result of subtraction is : ", numbera-numberb)
print("the  result is: ", numbera*numberb)
print("the result power to any number  is: " ,(numbera**numberb))
print("the result is", numbera/numberb)
print("the result is", numbera//numberb)



#String 
print("String")
name="Jessenia Zambrano"
print(name.upper())
print(name.capitalize())
name2=name.upper()
print(name2)
print(name2.lower())
languaje = 'python'
print(languaje[0])
print(languaje[-1])
print(languaje[-2])


print(len(languaje))

#list
print("list")
devices=['router', 'swtich', 'cable',45,True,False]

print(len(devices))

print(devices[0])
print(devices[-1])


devices.append('Server')
print(devices)


names=list()
names.append('Javier')
names.append('Jessy')
names.append('Saray')
names.append('Luis')
print(names)
names[1]='Sebastian'
print(names)

print(names.pop())
print(names)


numbers=list(range(10))
print(numbers)

selecednumbers=numbers[2:4]
print(selecednumbers)


print(numbers[:-1])

print(numbers[:3])

numbers[2:3]=[100,100]
print(numbers)

#tuples
print("tuples")
containertuple=(10,20)
print(containertuple[0])

containerslist=list(containertuple)
print(type(containerslist))



#diccionary
print('#tuples')
animals={'dog':'nice','cat':'pretty','monkey':'black'}

print(animals['cat'])
animals['cat']='ugly'
print(animals)

print('cat' in animals)


del animals['monkey']
print(animals)


animals['monkey']='ungly'
animals['mouse']='small'
animals['donkey']='big'

for item, feature in animals.items():
  
    print(f"{item} has {feature}")



mydictionary=dict()
mydictionary['humans']=2
mydictionary['mouse']=4
mydictionary['spider']=8

for animal in mydictionary:
    data=mydictionary[animal]
    print('the %s has %d' % (animal,data))





#LOPS

counter=0
while counter<10:
    print(counter)
    counter=counter+1



#name=input('Enter your name: \n')
#print(f'Hola, {name}')

myList=list()
 
for i in range(10):
    if  i%2==0:
        myList.append(i)
print(myList)

print('*****')
myList=[i for i in range(10) if i%2==0]
print(myList)


print('****')
myList=[i*i for i in range(100)]
print(myList)


def greting():
    return f'Hello my friends...'


tmp=greting()
print(tmp)


def greting2(name='friend'):
    print(f'hello, {name}')
    return

#greting2('Jessenia')
greting2()

#list 

list = [2, 5, 8, 10, 12, 15, 16, 18, 19, 20]
print("Lista:", list)

maxi = list[0]  
for i in list:
    if i > maxi:
        maxi = i

print("El número máximo es:", maxi)


while True:
    numbera=int(input('Enter the first numer\n'))
    numbera=input('Enter the second numer\n')
    numberb=int(numberb)

    operationType=input('Enter numbers from 1 to 4. \n 1 adding \n 2 substract \n 3 multiply\n 4 division\n')
    if int(operationType)==1:
        result=numbera+numberb
    if int(operationType) == 1:
        result = numbera + numberb
        print("The sum is:", result)
    elif int(operationType) == 2:
        result = numbera - numberb
        print("The subtraction is:", result)
    elif int(operationType) == 3:
        result = numbera * numberb
        print("The multiplication is:", result)
    elif int(operationType) == 4:
        if numberb != 0:
            result = numbera / numberb
            print("The division is:", result)
        else:
            print("Error: Division by zero is not allowed.")
    else:
        print("Invalid option, please enter a number between 1 and 4.")

   
    cont = input("Do you want to continue? (yes/no): ")
    if cont.lower() != "yes":
        break


print('ok')













































































































































































