from classes import Expenses
from parse import listening
from adding import add

expenses = []

parser = listening() # slucha parsera
args = listening.parse_args() #wrzuca do zmiennej args

if args.command == "add":
    add(args, expenses)
elif args.command == "list":
    print("# ID  Date       Description  Amount")

    for i in expenses:
        print(f"# {i.id}  {i.date}       {i.description}  {i.amount}")
        
