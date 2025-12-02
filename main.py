from classes import Expenses_list
from parse import listening
from adding import add
from csv_handling import load_from_csv

expenses = load_from_csv()

args = listening() #wrzuca do zmiennej args

if args.command == "add":
    add(args, expenses)
elif args.command == "list":
    print("# ID  Date                    Description        Amount")

    for i in expenses:
        print(f"# {i.id}  {i.date}       {i.desc}                 {i.amount}")

elif args.command == "summary":
    summ = 0
    for i in expenses:
        summ += i.amount
    
    print(f"Total Expenses: {summ}")