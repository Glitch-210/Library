import sys

''' 
    features
        1. id pass
        2. category
        3. time slot
        4. fees 
        5. penalty
        6. bill
        7. bye bye come back msg
''' 

print('\t\tWelcome to Mk Library')


#id pass function
def login():
    global log
    name = input('Enter your name: ')
    passw = input('Enter password: ')
    log={name:passw}
    print('Login successfull')

#category
def cat():
    while True:
        print('List of books category available')
        category = int(input('1.Sci-Fi\n2.Romance\n3.Money(recommended)\n4.Exit\n'))
        match category:
            case 1:
                global sciFil
                sciFil = []
                l = int(input('How many books do you want in Sci-Fi?: '))
                for i in range(l):
                    sciFi = input('Enter which book do you want: ')
                    sciFil.append(sciFi)
                    print(f'{sciFi} book added to the bill\n')
            case 2:
                global romancel
                romancel = []
                l = int(input('How many books do you want in romance?: '))
                for i in range(l):
                    romance = input('Enter which book do you want: ')
                    romancel.append(romance)
                    print(f'{romance} book added to the bill\n')
            case 3:
                global moneyl
                moneyl = []
                l = int(input('How many books do you want in money oriented?: '))
                for i in range(l):
                    money = input('Enter which book do you want: ')
                    moneyl.append(money)
                    print(f'{money} book added to the bill\n')
            case 4:
                break


#time
def timme():
    while True:
        timee = int(input('Press 1 for purchase\n2 for rent: '))
        if timee == 1:
            sciFil = [0]
            romancel = [0]
            moneyl = [0]
            books = (len(moneyl) + len(romancel) + len(sciFil))-3
            if books > 0 and books <= 2:
                bill = books*300
            elif  books > 2 and books <= 4:
                bill = books*250
            else:
                bill = books*220
            print(f'Your total Bill {bill}Rs.')
        elif timee == 2:
            books = (len(moneyl) + len(romancel) + len(sciFil))-3
            if books > 0 and books <= 2:
                bill = books*100
            elif  books > 2 and books <= 4:
                bill = books*75
            else:
                bill = books*50
            print('Penalty Charges: 100Rs. per day')
            print(f'Your rental Bill {bill}Rs.')
        else:
            print('Invalid Number Try Again!')

login()
cat()
timme()