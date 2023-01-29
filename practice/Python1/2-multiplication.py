print('*** multiplication or sum ***')
num1,num2 = list(map(int,input('Enter num1 num2 : ').split()))
if num1*num2 > 1000:
    print(f'The result is {num1+num2}')
else:
    print(f'The result is {num1*num2}')