import pandas as pd
import os

# check if our csv exists or not

def check_status_and_get_new_balance(prevBalance=0):
    print('Enter gain or spent')
    ch = input().strip()
    if ch.lower() == 'gain':
        prevBalance += float(input('Enter amount: '))
    elif ch.lower() == 'spent':
        prevBalance -= float(input('Enter amount: '))

    return prevBalance



if os.path.exists('./Expense.csv'):
    #exits then read last row from file
    expFile = pd.read_csv('Expense.csv')

    #get the last line from the balance file
    prevBalance = expFile.tail(1).Balance

    prevBalance = check_status_and_get_new_balance(prevBalance)
    date = pd.datetime.now()

    # now we make a new dataframe to insert in our Expense.csv file

    df = pd.DataFrame({'Date': date, 'Balance': prevBalance})
    df.to_csv('Expense.csv', mode='a', header=False)

else:
    #file does not exist so we have to create a new Expense.csv file
    prevBalance = check_status_and_get_new_balance(0)
    date = pd.datetime.now()

    # now we make a new dataframe to insert in our Expense.csv file

    df = pd.DataFrame({'Date': [date], 'Balance': [prevBalance]})
    df.to_csv('Expense.csv')