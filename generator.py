import string
import random
import sys


def create():
    while True:
        lowercase_letter = string.ascii_lowercase
        uppercase_letter = string.ascii_uppercase
        numbers = string.digits
        symbols = string.punctuation

        combination = uppercase_letter + lowercase_letter + numbers + symbols

        while True:
            try:
                response = input(
                    'Would you like to generate a fresh, strong password for enhanced security? [Y/N]: ').lower()

                if response == 'n':
                    print('Exiting...')
                    sys.exit()

                elif response != 'y' and response != 'n':
                    print('Enter [Y or N]')
                    break

                size = int(input('Please specify the desired password length, choosing a value between 8 and 80 characters: '))
                if (size < 8 or size > 80):
                    print('Kindly input a value within the specified range of 8 to 80 characters.')
                else:
                    password = "".join(random.sample(combination, size))
                    print('Password:', password)
                    break
            except ValueError:
                print('Please enter a valid number.')


if(__name__ == '__main__'):
    create()
