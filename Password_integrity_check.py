import re

# password must contain atleast 1 digit , small and caps letter
# and a special character and minimum length of 10 characters

def check(text):
    if re.search(r'([0-9a-zA-Z!@#&%$]){20,}', text):
        print('Strong')
    elif re.search(r'([0-9a-zA-Z!@#$%&]){8,19}', text):
        print('Good')
    else:
        print('Weak')

if __name__ == '__main__':
    check(input())