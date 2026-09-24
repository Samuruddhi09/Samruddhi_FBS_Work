gender = input ('Enter gender(F/M): ')
age = int (input('Enter age:'))

if (gender == 'M'):
    if (age >= 21):
        print ('Boy is eligible for marriage.')
    else :
        print('Pehele kama lo')

else:
    if (age >= 18):
        print ('Girl is eligible for marriage.')
    else:
        print ('Phele padhai kar lo')