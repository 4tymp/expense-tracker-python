import csv

from classes import Expenses_list
from csv_handling import saving_to_csv

#funkcja dodajaca nasze expenses
def add(args, expenses):
    if args.description is not None and args.amount is not None and args.amount > 0:
        new_expense = Expenses_list(args.description, args.amount)

        expenses.append(new_expense)

        saving_to_csv(expenses)

        print("successfully added new expense")
    else:
        print("proper use of add: add --description 'description' --amount 10")