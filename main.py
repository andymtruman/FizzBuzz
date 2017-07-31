x = 1
isFizz = None
isBuzz = None
msg = ""

while x <= 20:
    if x % 3 == 0:
        isFizz = True
    if x % 5 == 0:
        isBuzz = True

    if isFizz and isBuzz:
        msg = 'FizzBuzz'
        isFizz = False
        isBuzz = False
    elif isFizz:
        msg = 'Fizz'
        isFizz = False
    elif isBuzz:
        msg = 'Buzz'
        isBuzz = False
    else:
        msg = x
    print msg

    x += 1
