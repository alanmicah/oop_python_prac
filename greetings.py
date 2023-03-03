# def main():
#     print('Hello World!')

def main():
  print('This line is printed directly from the main function of the program')
  secondary_function()

def secondary_function():
  print('This line is printed from a secondary function call within the main function')


def greet_someone():
    name = input('What is your name?')
    hometown = input('And where are you from?')
    print('Very nice to meet you, {}!'.format(name), f'from {hometown}!')

greet_someone()

if __name__ == '__main__':
    main()