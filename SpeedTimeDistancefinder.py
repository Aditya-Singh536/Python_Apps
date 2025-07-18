print('If don\'t know the number give 0.')

def STDfinder():
    a = int(input('Enter the distance in km:'))
    b = int(input('Enter the time in h:'))
    c = int(input('Enter the speed in km/h:'))
    s = 's'
    t = 't'
    d = 'd'

    print('What to find?\n')
    
    y = input('If distance:d,time:t,speed:s:')

    if y == s:
        print(a/b,'km/h is your speed.')
    elif y == t:
        print(a/c,'h is your time.')
    elif y == d:
        print(b*c,'km is your distance.')

print('If don\'t known value give it "0"\n')

if __name__ == '__main__':
    STDfinder()

