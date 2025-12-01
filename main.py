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
parser.add_argument("command", help="starts add sequence")
parser.add_argument("--description", help="sets expense description")
parser.add_argument("--amount", help="sets expense amount", type=int)
args = parser.parse_args()

if args.command == "add":
    if args.description is not None and args.amount is not None and args.amount > 0:
        new_expense = Expenses(args.description, args.amount)
        expenses.append(new_expense)

        print("successfully added new expense")
    else:
        print("proper use of add: add --description 'description' --amount 10")
elif args.command == "list":
    print("# ID  Date       Description  Amount")

    for i in expenses:
        print(f"# {i.id}  {i.date}       {i.description}  {i.amount}")
        
