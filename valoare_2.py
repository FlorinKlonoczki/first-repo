"""
Learning IF Statement
"""
run_complex_if = True
if run_complex_if:
    expected_user = 'Florin'
    expected_pwd = '0000'
    expected_email = 'gigel@yahoo.com'
    actual_user, actual_pwd, actual_email = input('Enter the user:'), input('Enter the password:'), input(
        'Enter email:')
    number_of_if = 0
    if actual_user.lower() == expected_user.lower():
        print('Username is correct')
        number_of_if += 1
        if actual_pwd == expected_pwd:
            print('Correct password')
            number_of_if += 1
            if len(expected_pwd) < 7:
                print('Schimba parola cu una mai puternica')
            if actual_email.lower() == expected_email:
                print('Correct email')
                print('Logare reusita')
                number_of_if += 1
            else:
                print('Wrong email!Please try again')
                new_email = input('Enter email again')
                if new_email == expected_email:
                    print('Now is a good email')
                    number_of_if += 1
                else:
                    print('Your email is wrong')
        else:
            print('Wrong password!')
    else:
        print('Wrong username.Please try again')
        print(f'Ai utiliza IF de {number_of_if}')
else:
    print('String slicing')
    figura = 'dreptunghi'
    print(figura[-1])
    print(figura[1:])
    print([len(figura) - 1])
    print(figura[0:-1:2])
    print(figura[::2])

# todo contorizare pt fiecare else;
# todo extra check ca parola are si litere si cifre
# todo sa inlociuasca leterele neafisate din dreptunghi cu *
# todo parola introdusa de user sa fie afisate de * in numar egal cu numarul caracterelor din pass
