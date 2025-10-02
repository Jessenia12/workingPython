

#while True:
    #number=int(input('Enter a number, please.\n'))
    
    #if number %2==0:
        #print(f'the number {number} entered is enven')
    #else: 
        #print(f'the number {number} entered is odd')



# userDefault='admin'
# passwordDefault=123

# user=input('enter the user of the account.\n')
# password=input('enter the password of the account.\n')


# if user==userDefault and password==passwordDefault:
#     print('You are allwed to come to the  system')
# else:
#     print('you are not user of the system....')


# repository=list()

# ramdonNumber=int(input('enter a number please \n'))
# sum=0

# for i in range(ramdonNumber):
#     repository.append(i)
# for i in repository:
#     sum=sum+i


# print(f'the total sum is: {sum}')


# balance=1000
# choice=input('1>deposit\n 2>withdraw\n 3> check balance')
# choice=int(choice)
# money=0

# while True:
#     if (choice)==1:
#         money=int(input('enter the amount to deposit\n'))
#         balance=balance+money
#     elif choice==2:
#         money=int(input('enter the amount of money to withdraw:'))
    
#         if balance>money:
#             balance=balance-money
#             print(f'Take your money, please...')
#         else:

#             print('you do not have enough money...')

#     elif choice==3:
#         print(f'The balance is {balance}')

#     else:
#         print('Yout choice is not allwed')
    
#     choice=input('1>deposit\n 2>withdraw\n 3> check balance')
#     choice=int(choice)


#programacion orientada a objetos


# class Students: 
#     def __init__(self, name, course='IA'):
#         print('The student has been registered')
#         self.name=name
#         self.course=course


#     def dataStudemt(self):
#         print(f'Name: {self.name} and course: {self.course}')
#         return

# Students1=Students('Jessenia')
# Students2=Students('Jesse', 'Distributed systems')

# Students1.dataStudemt()
# Students2.dataStudemt()


class Students: 
    def __init__(self, name, course='IA'):
        print('The student has been registered')
        self.name=name
        self.course=course
    def dataStudemt(self, status='No active'):
        print(f'Name: {self.name} and course: {self.course}, Status: {status}')
        return
Students1=Students('Jessenia')
Students2=Students('Jesse', 'Distributed systems')

Students1.dataStudemt()
Students2.dataStudemt('active')