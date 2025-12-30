

import argparse 

def clc_age():
    import datetime
    import re
    yearORage = input('enter your age or year of birth : ')
    # remove all non-digit characters
    text = (''.join(re.findall(r'\d+', str(yearORage))))
    if len(text) > 4:
        print('pleas enter valid number ...!')
        return
    # convert to intger 
    i = int(text)
    # check if the input is year or age
    if type(i) == int :
        print(f'you age is : {datetime.datetime.now().year - i}'.strip().capitalize() if len(str(i)) >= 4
            else f'you born in : {datetime.datetime.now().year - i}'.strip().capitalize() )
    else:
        print('pleas enter valid number ...!')
parser = argparse.ArgumentParser(description='..... Welcome to alr3doi110 tools for 2023 ....'.title())
print('*'*50) 
print('..... Welcome to alr3doi110 tools for 2023 ....\n'.title())
print('*'*50)
arg  = parser.add_argument('command', choices=['age'], help='A list of integers')
arg = parser.parse_args()
if arg.command == 'age':
    clc_age()
else:
    print('unknown command ...!')