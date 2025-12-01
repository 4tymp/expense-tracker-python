import argparse,itertools,datetime

class Expenses:

    id_iter = itertools.count() #auto iteracja

    def __init__(self,desc,amount):
        self.date = datetime.datetime.now()
        self.desc = desc
        self.amount = amount
        self.id = next(Expenses.id_iter)

expenses = []

parser = argparse.ArgumentParser()
parser.add_argument("--description", help="sets expense description")
parser.add_argument("--amount", help="sets expense amount", type=int)
args = parser.parse_args()

if len(args.description) > 0 and args.amount > 0:
    new_expense = Expenses(args.description, args.amount)
    expenses.append(new_expense)

    print(expenses[0].id, expenses[0].desc, expenses[0].amount, expenses[0].date)