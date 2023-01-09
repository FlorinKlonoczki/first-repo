# TODO -a se completa spatiile libere literelor din dreptunghi neafisate inlocuite cu *
figura = 'dreptunghi'
fig = figura[0] + '*' + figura[2] + '*' + figura[4] + '*' + figura[6] + '*' + figura[8] + '*'
print(fig)

# TODO - a se verifica lungimea parolei introdusa si sa o afiseze cu steluta *
user = input('Introduceti userul dvs: ')
parola = input('Introduceti parola dvs: ')
parola = len(parola) * '*'
print(f' Userul dvs este {user} si parola dvs este {parola} si are {int(len(parola))} caractere.')
import re

# TODO - sa numaram cate else sunt- sa contorizam.
# TODO -sa adaugam un extra check ca parola are si litere si cifre
expected_user = 'Cristina'
expected_psw = '0000'
expected_email = 'cristina_comsha@gmail.com'
actual_user, actual_psw, actual_email = input('Enter user: '), input('Enter password: '), input('Enter email: ')
nr_of_if = 0
nr_of_else = 0
if actual_user.lower() == expected_user.lower():
    print('username valid!')
    if actual_psw == expected_psw:
        print('The psw is valid!')
        nr_of_if += 1
        if len(expected_psw) < 7:
            print('Psw not strong enough!')
            nr_of_if += 1
        if not re.search('[A-Z]', actual_psw):
            print('Psw must contain upper case!')
            nr_of_if += 1
        if not re.search('[0-9]', actual_psw):
            print('Psw must contain digits!')
            nr_of_if += 1
        if actual_email.lower() == expected_email.lower():
            print('Succesfull login!')
            nr_of_if += 1
        else:
            print('Wrong email! Please try again!')
            nr_of_else += 1
            new_email = input('Enter email again: ')
            if new_email.lower() == expected_email.lower():
                print('Now its ok! Succesfull login!')
                nr_of_if += 1
            else:
                print('Wrong email! Your account its blocked!')
                nr_of_else += 1
    else:
        print('Wrong psw! Please try again!')
        nr_of_else += 1
else:
    print('Wrong username! Please try again!')
    nr_of_else += 1
print(f'Ai utilizat {nr_of_if} de if!')
print(f'Ai utilizat {nr_of_else} de else!')

