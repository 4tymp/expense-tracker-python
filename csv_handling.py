import csv,datetime,itertools

from classes import Expenses_list

# funkcja wczytujaca dane z pliku csv
def load_from_csv():
    filename = "my_expenses.csv"
    
    expenses = []

    with open(filename, "r") as f: # otwiera plik
        csvreader = csv.DictReader(f) #jako dict reader
        for row in csvreader:
            e = Expenses_list( # i wrzuca sobie to co zapisane w pliku dzieki konstruktorowi
                row["Description"],
                float(row["Amount"])
            )
            e.id = int(row["ID"]) # a to manualnie, bo nie ma w konstruktorze
            e.date = datetime.datetime.fromisoformat(row["Date"])
            expenses.append(e)

    # ustaw iterator ID na kolejny numer
    if expenses:
        Expenses_list.id_iter = itertools.count(expenses[-1].id + 1) # no i wrzuca do naszej listy po ktorej sie odwolujemy

    return expenses

# funkcja zpaisujaca wpisane dane do pliku csv
def saving_to_csv(expenses):
    fields = ["ID", "Date", "Description", "Amount"] # najpierw wypelniasz sobie rzeczy ktore bedziesz potrzebowal
    rows = [ #potem petla od tylu wypielniasz sobie rzedy
        [i.id, i.date, i.desc, i.amount]
        for i in expenses
    ]
    #i potem otwierasz plik w trybie w - write i wypisujesz to co miales wczesniej
    filename = "my_expenses.csv"
    with open(filename, "w") as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(fields)
        csvwriter.writerows(rows) # !!! writerows bo jest ich wiecej!