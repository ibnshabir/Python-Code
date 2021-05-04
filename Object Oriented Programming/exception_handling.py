while True:
    x= int(input('enter x: '))
    y= int(input('enter y: '))
    try:
        print(x/y)
    except Exception:
        print('cant divide by zero')