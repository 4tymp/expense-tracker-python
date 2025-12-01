import datetime,itertools

class Expenses_list:

    id_iter = itertools.count() #auto iteracja

    def __init__(self,desc,amount):
        self.date = datetime.datetime.now()
        self.desc = desc
        self.amount = amount
        self.id = next(Expenses_list.id_iter)