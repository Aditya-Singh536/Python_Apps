def secretcode():
  actualstring = input('The words to convert to secret code:')
  print(' ')
  reversedstring = actualstring[::-1]
  print(f'Your secret code is: {reversedstring}')

if __name__ == '__main__':
  secretcode()
