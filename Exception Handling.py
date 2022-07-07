try:
    print('resource Opened')
    a = int(input('Enter a number: '))
    b = int(input('Enter a number: '))
    print('{} / {} = '.format(a, b))
    print(a / b)
except ZeroDivisionError as e:
    print('Hey, you cannot divide a Number by Zero', e)
except ValueError:
    print('Invalid Input')
except Exception as e:
    print('Something went Wrong...')
finally:
    print('resource Closed')
