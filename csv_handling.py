import csv

# funkcja wczytujaca dane z pliku csv
def load_from_csv():
    filename = "my_expenses.csv"

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