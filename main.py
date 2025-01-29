import sys

print('\t\tWelcome to Mk Library')

# Global variables initialization
sciFil = []
romancel = []
moneyl = []
log = {}

# ID pass function
def login():
    global log
    name = input('Enter your name: ')
    passw = input('Enter password: ')
    log = {name: passw}
    print('Login successful')

# Category selection function
def cat():
    global sciFil, romancel, moneyl
    while True:
        print('\nList of books category available')
        category = int(input('1.Sci-Fi\n2.Romance\n3.Money(recommended)\n4.Exit\n'))
        if category == 4:
            break
            
        if category == 1:
            l = int(input('How many books do you want in Sci-Fi?: '))
            for _ in range(l):
                book = input('Enter which book do you want: ')
                sciFil.append(book)
                print(f'{book} book added to the bill\n')
                
        elif category == 2:
            l = int(input('How many books do you want in romance?: '))
            for _ in range(l):
                book = input('Enter which book do you want: ')
                romancel.append(book)
                print(f'{book} book added to the bill\n')
                
        elif category == 3:
            l = int(input('How many books do you want in money oriented?: '))
            for _ in range(l):
                book = input('Enter which book do you want: ')
                moneyl.append(book)
                print(f'{book} book added to the bill\n')

# Billing function
def timme():
    global sciFil, romancel, moneyl
    while True:
        timee = int(input('\nPress 1 for purchase\n2 for rent: '))
        total_books = len(sciFil) + len(romancel) + len(moneyl)
        
        if timee == 1:
            if total_books == 0:
                print("You haven't selected any books!")
                continue
                
            if total_books <= 2:
                bill = total_books * 300
            elif total_books <= 4:
                bill = total_books * 250
            else:
                bill = total_books * 220
            print(f'Your total Purchase Bill: {bill} Rs.')
            break
            
        elif timee == 2:
            if total_books == 0:
                print("You haven't selected any books!")
                continue
                
            if total_books <= 2:
                bill = total_books * 100
            elif total_books <= 4:
                bill = total_books * 75
            else:
                bill = total_books * 50
            print('\nPenalty Charges: 100 Rs. per day')
            print(f'Your Rental Bill: {bill} Rs.')
            break
            
        else:
            print('Invalid Number! Try Again!')

# Farewell message
def goodbye():
    print('\nThank you for visiting Mk Library!')
    print('Please come back again!')

# Main program flow
login()
cat()
timme()
goodbye()