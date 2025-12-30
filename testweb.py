import requests 
from  rich  import print
# urls = ['https://www.alqusor.com.sa/' , 'https://www.google.com/' , 'https://www.github.com/']
urls = 'https://www.google.com/'

def get_headers():
    try:
        urls = input('enter url or urls (comma separated) : ')
        if type(urls) == list:
            for u in urls:
                res = requests.get(u)
                if res.status_code == 200:
                    for k, v in res.headers.items():
                        print(f'{k}: {v}')
                    print('success')
                    print('*' * 30)
        elif urls: 
            res = requests.get(urls)
            if res.status_code == 200:
                for k, v in res.headers.items():
                    print(f'[yellow] {k}/ : [green] {v}/  ')
            print('success')
            print('*' * 30)
        else:
            print('please provide a valid url ...!')
    except Exception as e:  
        print(f'error occured: {e}')

# get_headers(urls)

import argparse 

parser = argparse.ArgumentParser(description='..... Welcome to alr3doi110 tools for 2023 ....'.title())
print('*'*50)
print('..... Welcome to alr3doi110 tools for 2023 ....\n'.title())
print('*'*50)
parser.add_argument('command', choices=['info_headers'], help='A list of integers')
arg = parser.parse_args()
if arg.command == 'info_headers':
    get_headers()
else:
    print('unknown command ...!')