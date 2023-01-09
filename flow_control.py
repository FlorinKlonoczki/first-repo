nota = 5
nota_curenta = int(input('Introduceti nota dvs '))
if nota_curenta > nota:
    print(f'Congrats! you pass the exam')
elif nota_curenta < nota:
    print(f'You failed!')
else:
    print(f'Ai trecut la limita')