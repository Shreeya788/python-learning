'''
In python, user input is taken using  input function --> input()
'''

num1 = input ('Enter the first number: ')
num2 = input('Enter the second number: ')

#then typecasting is used as num1 and num2 is in string form 

print(type(num1))
print(num1, num2, sep=' , ')
print('The sum of ' + num1 + ' and ' + num2 + ' is ' + str(int(num1)+int(num2)))