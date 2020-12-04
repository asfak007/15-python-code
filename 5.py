#  find the area of triangle

a = input('Enter first side: ')
b = input('Enter second side: ')
c = input('Enter third side: ')


s = (a + b + c) / 2

area = (s*(s-a)*(s-b)*(s-c)) ** 0.5
print('The area of the triangle is %0.2f' %area)